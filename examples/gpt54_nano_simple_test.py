import os
import subprocess
import sys
from urllib.parse import urlparse

import requests
from dotenv import load_dotenv
from azure.identity import AzureCliCredential, DefaultAzureCredential


def build_responses_url(endpoint: str) -> str:
    endpoint = endpoint.strip()
    if not endpoint:
        raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT is required.")
    if not endpoint.startswith("https://"):
        raise ValueError("AZURE_AI_FOUNDRY_ENDPOINT must start with https://")

    parsed = urlparse(endpoint)
    path = (parsed.path or "").rstrip("/").lower()

    if path.endswith("/openai/v1/responses"):
        return endpoint
    if path.endswith("/openai/v1"):
        return endpoint.rstrip("/") + "/responses"
    return f"{parsed.scheme}://{parsed.netloc}/openai/v1/responses"


def get_access_token() -> str:
    scope = "https://cognitiveservices.azure.com/.default"

    for az_cmd in [
        "az",
        "C:/Program Files/Microsoft SDKs/Azure/CLI2/wbin/az.cmd",
        "C:/Program Files (x86)/Microsoft SDKs/Azure/CLI2/wbin/az.cmd",
    ]:
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

    try:
        return AzureCliCredential().get_token(scope).token
    except Exception:
        return DefaultAzureCredential(exclude_interactive_browser_credential=False).get_token(scope).token


def main() -> int:
    load_dotenv()

    endpoint = os.getenv(
        "AZURE_AI_FOUNDRY_ENDPOINT",
        "https://zikaiwang-5test-resource.services.ai.azure.com/openai/v1/responses",
    )
    model = os.getenv("AZURE_AI_MODEL", "gpt-5.4-nano")

    question = " ".join(sys.argv[1:]).strip()
    if not question:
        question = input("请输入你的问题: ").strip()
    if not question:
        print("问题不能为空。")
        return 1

    try:
        url = build_responses_url(endpoint)
        token = get_access_token()

        resp = requests.post(
            url,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json",
            },
            json={"model": model, "input": question},
            timeout=60,
        )
        resp.raise_for_status()
        data = resp.json()

        output_text = ""
        for item in data.get("output", []):
            if item.get("type") == "message":
                for c in item.get("content", []):
                    if c.get("type") == "output_text":
                        output_text += c.get("text", "")

        print("\n回答:\n")
        print(output_text or "(模型没有返回文本)")
        return 0
    except requests.HTTPError as exc:
        body = exc.response.text if exc.response is not None else ""
        print(f"HTTP错误: {exc}")
        if body:
            print(body)
        return 1
    except Exception as exc:
        print(f"运行失败: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
