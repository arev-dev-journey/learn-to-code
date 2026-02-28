# Partner Inventory Sync Backend (AWS-ready)

A production-style backend example that:

- ingests partner inventory snapshots
- processes operational events
- synchronizes canonical inventory state
- exposes HTTP APIs
- uses AI tooling for low-stock recommendations (Bedrock when configured)
- deploys on AWS ECS Fargate via CloudFormation

## Architecture

1. **Ingestion API** (`POST /v1/partners/{partner_id}/inventory`) stores partner inventory.
2. **Event API** (`POST /v1/events`) queues business events.
3. **Sync API** (`POST /v1/sync/run`) processes pending events and materializes canonical inventory.
4. **Read APIs** expose partner and canonical state.
5. **AI API** (`GET /v1/ai/recommendations/low-stock`) summarizes low-stock actions using:
   - Amazon Bedrock (`BEDROCK_MODEL_ID` configured), or
   - deterministic fallback rules.

## Local Run

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

Test:

```bash
pytest
```

## API quickstart

```bash
curl -X POST http://localhost:8000/v1/partners/acme/inventory \
  -H 'content-type: application/json' \
  -d '{"items":[{"sku":"SKU-1","quantity":5},{"sku":"SKU-2","quantity":18}]}'

curl -X POST http://localhost:8000/v1/sync/run

curl http://localhost:8000/v1/inventory/SKU-1

curl 'http://localhost:8000/v1/ai/recommendations/low-stock?threshold=10'
```

## AWS deployment (ECS Fargate)

Build and push container:

```bash
docker build -t partner-inventory-sync .
# tag and push to ECR ...
```

Deploy stack:

```bash
aws cloudformation deploy \
  --template-file infra/aws/ecs-fargate.yaml \
  --stack-name partner-inventory-sync \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
      VpcId=vpc-xxxxxxxx \
      PublicSubnets='subnet-aaa,subnet-bbb' \
      ContainerImage=123456789012.dkr.ecr.us-east-1.amazonaws.com/partner-inventory-sync:latest
```

### Optional Bedrock setup

Set environment variables on the ECS task definition:

- `AWS_REGION=us-east-1`
- `BEDROCK_MODEL_ID=amazon.titan-text-express-v1` (or another enabled model)

Also grant `bedrock:InvokeModel` permission to the task role.
