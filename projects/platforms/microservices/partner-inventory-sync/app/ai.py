import json
import os


def build_low_stock_recommendation(low_stock_items: list[dict]) -> tuple[str, str]:
    if not low_stock_items:
        return "No low-stock SKUs detected. Current inventory levels are healthy.", "rules"

    model_id = os.getenv("BEDROCK_MODEL_ID")
    if model_id:
        try:
            import boto3

            client = boto3.client("bedrock-runtime", region_name=os.getenv("AWS_REGION", "us-east-1"))
            prompt = (
                "You are an inventory operations copilot. Given low-stock records, provide "
                "three concise actions to reduce stockout risk.\n"
                f"Low-stock records: {json.dumps(low_stock_items)}"
            )
            body = json.dumps(
                {
                    "inputText": prompt,
                    "textGenerationConfig": {
                        "maxTokenCount": 300,
                        "temperature": 0.2,
                    },
                }
            )
            response = client.invoke_model(modelId=model_id, body=body)
            payload = json.loads(response["body"].read())
            text = payload.get("results", [{}])[0].get("outputText", "")
            if text:
                return text.strip(), f"bedrock:{model_id}"
        except Exception:
            pass

    top = ", ".join(f"{item['sku']} ({item['total_quantity']})" for item in low_stock_items[:3])
    summary = (
        f"Prioritize replenishment for {top}. Set partner-level reorder alerts and increase sync cadence "
        "to every 5 minutes for these SKUs until safety stock is restored."
    )
    return summary, "rules"
