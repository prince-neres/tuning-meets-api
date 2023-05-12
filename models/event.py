from typing import Optional, Any
from beanie import Document
from pydantic import BaseModel


class Adress(BaseModel):
    number: int
    complement: str
    neighborhood: str
    city: str
    uf: str
    cep: int

    class Config:
        schema_extra = {
            "example": {
                "street": "L2 Norte",
                "number": 1000,
                "complement": "Quadra 10, Lote 10",
                "neighborhood": "Asa Sul",
                "city": "Brasília",
                "uf": "DF",
                "cep": "72750600"
            }
        }


class Event(Document):
    title: str
    description: str
    image: str
    adress: Adress
    latitude: float
    longitude: float
    date_created: str
    date_updated: str
    date_expected: str

    class Collection:
        name = "events"

    class Config:
        schema_extra = {
            "example": {
                "title": "fgsdfgsdfgsdfgsdf",
                "description": "sfdgdf gsdfg sdfgsdfgsdfgsdf",
                "image": "https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.mentecoletiva.com.br%2Ftop-10-carros-japoneses-jdm-cars%2F&psig=AOvVaw1SGGe7mag6PoI-YEb2HRuY&ust=1683938198782000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCKiCo-PE7v4CFQAAAAAdAAAAABAE",
                "adress": {
                    "street": "L2 Norte",
                    "number": 1000,
                    "complement": "Quadra 10, Lote 10",
                    "neighborhood": "Asa Sul",
                    "city": "Brasília",
                    "uf": "DF",
                    "cep": "72750600"
                },
                "latitude": -15.7942287,
                "longitude": -47.8821658,
                "date_created": "2023-05-11T21:32:16.349849",
                "date_updated": "2023-05-11T21:32:16.349849",
                "date_expected": "2023-05-11T21:32:16.349849",
            }
        }


class UpdateEventModel(BaseModel):
    title: Optional[str]
    description: Optional[str]
    image: Optional[str]
    adress: Optional[Adress]
    latitude: Optional[float]
    longitude: Optional[float]
    date_created: Optional[str]
    date_updated: Optional[str]
    date_expected: Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "title": "fgsdfgsdfgsdfgsdf",
                "description": "sfdgdf gsdfg sdfgsdfgsdfgsdf",
                "image": "https://www.google.com/url?sa=i&url=http%3A%2F%2Fwww.mentecoletiva.com.br%2Ftop-10-carros-japoneses-jdm-cars%2F&psig=AOvVaw1SGGe7mag6PoI-YEb2HRuY&ust=1683938198782000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCKiCo-PE7v4CFQAAAAAdAAAAABAE",
                "adress": {
                    "street": "L2 Norte",
                    "number": 1000,
                    "complement": "Quadra 10, Lote 10",
                    "neighborhood": "Asa Sul",
                    "city": "Brasília",
                    "uf": "DF",
                    "cep": "72750600"
                },
                "latitude": -15.7942287,
                "longitude": -47.8821658,
                "date_created": "2023-05-11T21:32:16.349849",
                "date_updated": "2023-05-11T21:32:16.349849",
                "date_expected": "2023-05-11T21:32:16.349849",
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data"
            }
        }
