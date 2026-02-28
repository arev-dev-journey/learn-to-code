from functools import lru_cache
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = 'Partner Inventory Sync System'
    environment: str = Field(default='local', alias='ENVIRONMENT')
    api_key: str = Field(default='dev-partner-key', alias='PARTNER_API_KEY')

    database_url: str = Field(
        default='postgresql+psycopg://postgres:postgres@localhost:5432/inventory',
        alias='DATABASE_URL',
    )

    queue_backend: str = Field(default='db', alias='QUEUE_BACKEND')
    sqs_queue_url: str | None = Field(default=None, alias='SQS_QUEUE_URL')
    aws_region: str = Field(default='us-east-1', alias='AWS_REGION')

    llm_base_url: str | None = Field(default=None, alias='LLM_BASE_URL')
    llm_api_key: str | None = Field(default=None, alias='LLM_API_KEY')
    llm_model: str = Field(default='gpt-4o-mini', alias='LLM_MODEL')


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
