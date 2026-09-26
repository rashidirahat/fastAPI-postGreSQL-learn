from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    id: int = Field(..., description="The ID of the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email of the user")

class UserDetails(BaseModel):
    id: int = Field(..., description="The ID of the user")
    name: str = Field(..., description="The name of the user")
    email: str = Field(..., description="The email of the user")
    is_active: bool = Field(..., description="Indicates if the user is active") 
    