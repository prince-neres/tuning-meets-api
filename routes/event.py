from fastapi import APIRouter, Body, Depends, UploadFile, File
from auth.jwt_bearer import JWTBearer
from database.database import *
from models.event import *
from services import s3_image_upload

token_listener = JWTBearer()
router = APIRouter()


@router.get("/", response_description="Events retrieved", response_model=List[Event])
async def get_events(q: str = ""):
    events = await retrieve_events(q)
    return events


@router.get("/{id}", response_description="Event data retrieved", response_model=Response)
async def get_event_data(id: PydanticObjectId):
    event = await retrieve_event(id)
    if event:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Event data retrieved successfully",
            "data": event
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Event doesn't exist",
    }


@router.post("/", response_description="Event data added into the database", response_model=Response, dependencies=[Depends(token_listener)])
async def add_event_data(event: Event = Body(...), image: UploadFile = File(...)):
    if image.filename:
        url = s3_image_upload(image)
        event.image = url

    new_event = await add_event(event)

    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Event created successfully",
        "data": new_event
    }


@router.delete("/{id}", response_description="Event data deleted from the database")
async def delete_event_data(id: PydanticObjectId):
    deleted_event = await delete_event(id)
    if deleted_event:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Event with ID: {} removed".format(id),
            "data": deleted_event
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Event with id {0} doesn't exist".format(id),
        "data": False
    }


@router.put("/{id}", response_model=Response, dependencies=[Depends(token_listener)])
async def update_event(id: PydanticObjectId, event: UpdateEventModel = Body(...), image: UploadFile = File(...)):
    if image.filename:
        url = s3_image_upload(image)
        event.image = url

    updated_event = await update_event_data(id, event.dict())
    if updated_event:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Event with ID: {} updated".format(id),
            "data": updated_event
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "An error occurred. Event with ID: {} not found".format(id),
        "data": False
    }
