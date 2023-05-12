from beanie import Document
from typing import Optional
from fastapi.security import HTTPBasicCredentials
from pydantic import BaseModel, EmailStr


class Admin(Document):
    fullname: str
    email:  EmailStr
    password: str
    date_created: Optional[str]
    date_updated: Optional[str]

    class Collection:
        name = "admin"

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@youngest.dev",
                "password": "3xt3m#",
                "date_created": "2023-05-11T21:32:16.349849",
                "date_updated": "2023-05-11T21:32:16.349849",
            }
        }


class AdminSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "abdul@youngest.dev",
                "password": "3xt3m#"
            }
        }


class AdminData(BaseModel):
    fullname: str
    email: EmailStr
    date_created: str
    date_updated: str

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdul@youngest.dev",
                "date_created": "2023-05-11T21:32:16.349849",
                "date_updated": "2023-05-11T21:32:16.349849",
            }
        }
