from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from .database import users_collection
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
 email: str
 password: str

@router.post("/login")
async def login(user: User):
 db_user = await users_collection.find_one({"email": user.email})
 print(user.password)
 print(db_user['password'])
 if not db_user or not pwd_context.verify(user.password, db_user["password"]):
  raise HTTPException(status_code=401, detail="Invalid credentials")
 return {"message": "Login successful"}
   
@router.post("/signup")
async def signup(user_data: User):
    email = user_data.email
    password = pwd_context.hash(user_data.password)

    # Check if user already exists (use await)
    existing_user = await users_collection.find_one({"email": email})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    # Insert user into MongoDB
    user_data = {
        "email": email,
        "password": password
    }
    result = await users_collection.insert_one(user_data)

    if result.inserted_id:
        return {"message": "User created successfully"}
    else:
        raise HTTPException(status_code=500, detail="Error creating user")
