import os
import sys

from dotenv import load_dotenv

try:
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.exceptions import ClientAuthenticationError, HttpResponseError
    from azure.identity import CredentialUnavailableError, DefaultAzureCredential
except ImportError as exc:
    raise SystemExit(
        "Missing Azure dependencies. Install them with: "
        "pip install azure-ai-inference azure-identity"
    ) from exc


def _normalize_endpoint(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if not endpoint.startswith("https://"):
        raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT must start with 'https://'.")
    return endpoint if endpoint.endswith("/") else endpoint + "/"


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
        endpoint = _normalize_endpoint(endpoint)

        credential = DefaultAzureCredential(exclude_interactive_browser_credential=False)
        client = ChatCompletionsClient(endpoint=endpoint, credential=credential)

        response = client.complete(
            model=model,
            messages=[
                SystemMessage("You are a concise assistant."),
                UserMessage("Use one sentence to explain what RAG is."),
            ],
            temperature=0.2,
            max_tokens=120,
        )

        print("Model response:\n")
        print(response.choices[0].message.content)
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
    except HttpResponseError as exc:
        status_code = getattr(exc, "status_code", None)
        if status_code in (401, 403):
            print(
                "Authorization error (401/403). Confirm RBAC permissions for your user or\n"
                "service principal on this resource."
            )
        elif status_code == 404:
            print(
                "Resource or model not found (404). Check endpoint and model name in .env."
            )
        else:
            print("Request failed while calling Azure AI Foundry.")
        print(f"Status: {status_code}")
        print(f"Details: {exc}")
        return 1
    except Exception as exc:  # Keep final fallback for unexpected runtime issues.
        print("Unexpected error while running the sample.")
        print(f"Details: {exc}")
        return 1


if __name__ == "__main__":
    sys.exit(main())
