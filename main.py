from fastapi import FastAPI
from routes import user 
from model import UserModel
import db
from typing import Union  
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI,Request,Depends, APIRouter, HTTPException, Response, responses
#from config import Base, engine, sess_db
from sqlalchemy.orm import Session
from security import get_pass_hash, verify_pass, create_access_token,verify_token, COOKIE_NAME
from pydantic import  EmailStr 
from userrepo import UserRepository, SendEmailVerify


app = FastAPI()
app.include_router(user)

@app.get('/')
def home():
    return{'message': 'Home page'}

# @app.post("/signup")
# def signup_user(username: str ,email:EmailStr ,password:str):
#     userRepository=UserRepository()
#     db_user= userRepository.get_user_by_username(username)
#     if db_user:
#          return "username is not valid"
 
#     signup=UserModel(email=email,username=username,password=get_pass_hash(password))
#     success=userRepository.create_user(signup)
#     token=create_access_token(signup)
#     SendEmailVerify.sendVerify(token,email)
#     if success:
#         enter_details()
    
#     else:
#         raise HTTPException(
#             status_code=401, detail="Credentials not correct"
#         )

# @app.post("/signinuser")
# def signin_user(username : str ,password:str):
#     userRepository = UserRepository()
#     db_user = userRepository.get_user_by_username(username)
#     if not db_user:
#         return "username or password is not valid"
 
#     if verify_pass(password,db_user['password']):
#         token=create_access_token(db_user)
#         return {COOKIE_NAME:token,"token_type":"project"}

# @app.post("/registerData")
# def enter_details():
#     name=str
#     age=int
#     adress=str
#     pincode=str

# @app.get("/{token}")
# def verify_user(token):
#     userRepository=UserRepository()
#     payload=verify_token(token)
#     username=payload.get("username")
#     db_user=userRepository.get_user_by_username(username)
 
#     if not username:
#         raise  HTTPException(
#             status_code=401, detail="Credentials not correct"
#         )
#     if db_user['is_active']==True:
#         return "your account  has been allreay activeed"
 
#     db_user['is_active']=True

# @app.get("/items/{item_id}", response_model=UserModel)
# async def read_item(item_id: str):
#     item = await collection_name.find_one({"_id": item_id})
#     if item:
#         return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.put("/items/{item_id}", response_model=UserModel)
# async def update_item(item_id: str, item: Item):
#     updated_item = await collection_name.find_one_and_update(
#         {"_id": item_id}, {"$set": item.dict()}
#     )
#     if updated_item:
#         return item
#     raise HTTPException(status_code=404, detail="Item not found")

# @app.delete("/items/{item_id}", response_model=UserModel)
# async def delete_item(item_id: str):
#     deleted_item = await collection_name.find_one_and_delete({"_id": item_id})
#     if deleted_item:
#         return deleted_item
#     raise HTTPException(status_code=404, detail="Item not found")