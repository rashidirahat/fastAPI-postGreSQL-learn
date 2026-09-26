from fastapi import APIRouter, Depends, HTTPException, status
from schemas.user import UserCreate, UserDetails
from dependencies import admin_name

router = APIRouter(
    prefix="/users",
)

@router.get("")
async def get_users(admin_name: str = Depends(admin_name)):
    return {"users": UserDetails(id=1, name="John Doe", email="john.doe@example.com", is_active=True), "admin_name": admin_name}