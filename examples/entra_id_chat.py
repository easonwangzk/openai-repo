import os
import subprocess
import sys
from urllib.parse import urlparse

from dotenv import load_dotenv

try:
    import requests
    from azure.core.exceptions import ClientAuthenticationError
    from azure.identity import (
        AzureCliCredential,
        CredentialUnavailableError,
        DefaultAzureCredential,
    )
except ImportError as exc:
    raise SystemExit(
        "Missing Azure dependencies. Install them with: "
        "pip install requests azure-identity"
    ) from exc


def _normalize_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if not endpoint.startswith("https://"):
        raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT must start with 'https://'.")

    parsed = urlparse(endpoint)
    if not parsed.netloc:
        raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT is not a valid URL.")

    # Accept full endpoint forms like .../openai/v1/responses and normalize to host root.
    return f"{parsed.scheme}://{parsed.netloc}/"


def _build_responses_url(endpoint: str) -> str:
    parsed = urlparse(endpoint)
    path = (parsed.path or "").rstrip("/").lower()

    # If user provides OpenAI endpoint root directly, keep it.
    if path.endswith("/openai/v1"):
        return endpoint.rstrip("/") + "/responses"

    # If user provides a full responses URL, keep it as-is.
    if path.endswith("/openai/v1/responses"):
        return endpoint

    # If user provides project endpoint or resource root, convert to OpenAI responses path.
    return _normalize_endpoint(endpoint) + "openai/v1/responses"


def _get_access_token() -> str:
    scope = "https://cognitiveservices.azure.com/.default"

    # 1) Try explicit Azure CLI paths first (common on Windows when PATH is stale).
    az_candidates = [
        "az",
        "C:/Program Files/Microsoft SDKs/Azure/CLI2/wbin/az.cmd",
        "C:/Program Files (x86)/Microsoft SDKs/Azure/CLI2/wbin/az.cmd",
    ]
    for az_cmd in az_candidates:
        try:
            result = subprocess.run(
                [
                    az_cmd,
                    "account",
                    "get-access-token",
                    "--resource",
                    "https://cognitiveservices.azure.com",
                    "--query",
                    "accessToken",
                    "-o",
                    "tsv",
                ],
                check=True,
                capture_output=True,
                text=True,
            )
            token = result.stdout.strip()
            if token:
                return token
        except Exception:
            pass

    # 2) Try AzureCliCredential if az is discoverable via environment.
    try:
        return AzureCliCredential().get_token(scope).token
    except Exception:
        pass

    # 3) Final fallback for other environments.
    return DefaultAzureCredential(exclude_interactive_browser_credential=False).get_token(scope).token


def main() -> int:
    load_dotenv()

    endpoint = os.getenv("AZURE_AI_FOUNDRY_ENDPOINT", "").strip()
    model = os.getenv("AZURE_AI_MODEL", "gpt-4o-mini").strip()

    if not endpoint:
        print(
            "Missing AZURE_AI_FOUNDRY_ENDPOINT. Add it to your .env file, for example:\n"
            "AZURE_AI_FOUNDRY_ENDPOINT=https://your-resource.services.ai.azure.com/"
        )
        return 1

    if not model:
        print("Missing AZURE_AI_MODEL. Example: AZURE_AI_MODEL=gpt-4o-mini")
        return 1

    try:
        responses_url = _build_responses_url(endpoint)

        access_token = _get_access_token()

        response = requests.post(
            responses_url,
            headers={
                "Authorization": f"Bearer {access_token}",
                "Content-Type": "application/json",
            },
            json={
                "model": model,
                "input": "Use one sentence to explain what RAG is.",
                "instructions": "You are a concise assistant.",
                "max_output_tokens": 120,
            },
            timeout=60,
        )
        response.raise_for_status()
        payload = response.json()
        output = payload.get("output", [])

        output_text = ""
        if output:
            message = output[0]
            content = message.get("content", [])
            if content:
                output_text = content[0].get("text", "")

        print("Model response:\n")
        print(output_text or "(No text output returned)")
        return 0

    except ValueError as exc:
        print(f"Configuration error: {exc}")
        return 1
    except CredentialUnavailableError as exc:
        print(
            "No Azure credential was found. Run 'az login' first, or provide a supported\n"
            "credential source for DefaultAzureCredential."
        )
        print(f"Details: {exc}")
        return 1
    except ClientAuthenticationError as exc:
        print(
            "Authentication failed. Make sure your signed-in identity has access to this\n"
            "Foundry resource and model deployment."
        )
        print(f"Details: {exc}")
        return 1
    except requests.HTTPError as exc:
        status_code = exc.response.status_code if exc.response is not None else None
        response_text = exc.response.text if exc.response is not None else ""

        if status_code in (401, 403):
            print(
                "Permission denied (401/403). Ensure your identity has access to this\n"
                "resource and deployment in Azure AI Foundry."
            )
        elif status_code == 404:
            print(
                "Resource or model not found (404). Check AZURE_AI_FOUNDRY_ENDPOINT and\n"
                "AZURE_AI_MODEL (deployment name) in .env."
            )
        else:
            print("Request failed while calling Azure OpenAI Responses API.")

        print(f"Status: {status_code}")
        if response_text:
            print(f"Details: {response_text}")
        return 1
    except requests.RequestException as exc:
        print(
            "Network/client error while calling Azure OpenAI Responses API."
        )
        print(f"Details: {exc}")
        return 1
    except Exception as exc:  # Keep final fallback for unexpected runtime issues.
        print("Unexpected error while running the sample.")
        print(f"Details: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
