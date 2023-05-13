from typing import Optional
from boto3 import client

from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseSettings

from models.admin import Admin
from models.event import Event


class Settings(BaseSettings):
    # database configurations
    DATABASE_URL: Optional[str] = None

    # AWS S3 configurations
    AWS_ACCESS_KEY_ID: Optional[str] = None
    AWS_SECRET_ACCESS_KEY: Optional[str] = None
    AWS_S3_CUSTOM_DOMAIN: Optional[str] = None
    AWS_BUCKET_NAME: Optional[str] = None

    # JWT
    secret_key: str
    algorithm: str = "HS256"

    class Config:
        env_file = ".env"
        orm_mode = True


async def initiate_database():
    client = AsyncIOMotorClient(Settings().DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[Admin, Event])
