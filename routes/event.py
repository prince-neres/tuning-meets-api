from fastapi import APIRouter, Body

from database.database import *
from models.event import *

router = APIRouter()


@router.get("/", response_description="Events retrieved", response_model=Response)
async def get_events():
    events = await retrieve_events()
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Events data retrieved successfully",
        "data": events
    }


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


@router.post("/", response_description="Event data added into the database", response_model=Response)
async def add_event_data(event: Event = Body(...)):
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


@router.put("/{id}", response_model=Response)
async def update_event(id: PydanticObjectId, req: UpdateEventModel = Body(...)):
    updated_event = await update_event_data(id, req.dict())
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
