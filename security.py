from passlib.context import  CryptContext 
from fastapi.security import OAuth2PasswordBearer
from jose import jwt 
from fastapi import Depends, Request
from fastapi import HTTPException
from model import UserModel
 
JWT_SECRET="Final%#*#@Year*&^%Project"
ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=5
 
pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto") 
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="user/signin")
COOKIE_NAME="Authorization"
 
# create Token
def create_access_token(user):
    try:
        payload={
            "email":user['email'], 
            "username":user['username'],
            "is_active":user['is_active']
        }
        return  jwt.encode(payload,key=JWT_SECRET,algorithm=ALGORITHM)
    except Exception as ex:
        print(str(ex))
        raise ex
 
# create verify Token
def verify_token(token):
    try:
        payload=jwt.decode(token,key=JWT_SECRET,algorithms=[ALGORITHM])
        print("hey")
        return payload
    except Exception as e:
        print(str(e))
        raise e
 
# password hash
def  get_pass_hash(password):
    return pwd_context.hash(password)
 
# password verify
def verify_pass(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
 
def get_current_user_from_token(token:str=Depends(oauth2_scheme)):
    user= verify_token(token)
    return user
 
def get_current_user_from_cookie(request:Request) -> UserModel:
    token=request.cookies.get(COOKIE_NAME)
    if token:
        user = verify_token(token)
        return user