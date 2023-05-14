from fastapi import Body, APIRouter, HTTPException
from passlib.context import CryptContext

from auth.jwt_handler import sign_jwt
from database.database import add_admin
from models.admin import Admin, AdminSignIn

router = APIRouter()

hash_helper = CryptContext(schemes=["bcrypt"])


@router.post("/login")
async def admin_login(admin_credentials: AdminSignIn = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin_credentials.username)
    if admin_exists:
        correct_password = hash_helper.verify(
            admin_credentials.password, admin_exists.password)
        if correct_password:
            admin = await Admin.find_one(Admin.email == admin_credentials.username)
            token = sign_jwt(admin_credentials.username)
            del admin.password

            return {
                "status_code": 202,
                "response_type": "success",
                "description": "Login successfully",
                "token": token.get('access_token'),
                "admin": admin
            }

        raise HTTPException(
            status_code=403,
            detail="Incorrect email or password"
        )

    raise HTTPException(
        status_code=403,
        detail="Incorrect email or password"
    )


@router.post("/register")
async def admin_signup(admin: Admin = Body(...)):
    admin_exists = await Admin.find_one(Admin.email == admin.email)
    if admin_exists:
        raise HTTPException(
            status_code=409,
            detail="Admin with email supplied already exists"
        )

    admin.password = hash_helper.encrypt(admin.password)
    new_admin = await add_admin(admin)
    return {
        "status_code": 201,
        "response_type": "success",
        "description": "Admin registered successfully",
        "admin": new_admin
    }
