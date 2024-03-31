from typing import Union
from fastapi import FastAPI,Request, APIRouter, HTTPException, Response
from model import UserModel
from pydantic import EmailStr
from typing import  Dict, Any
import smtplib
from db import collection_name
from email.message import EmailMessage
from sqlalchemy.orm import Session
from pydantic import  EmailStr 

class UserRepository:

    def create_user(self,signup:UserModel):
         try:
             collection_name.insert_one(dict(signup))
             #self.sess.commit()
             print("created")
         except:
             return False
         return True
 
    def get_user(self):
       return  collection_name.find_one()
    
    def get_user_by_email(self,email:EmailStr):
        return collection_name.find_one({"email": email})
    
    def get_user_by_username(self,username:str):
        return collection_name.find_one({"username": username})
    
    
        
    
    def update_user(self,id:int,details:Dict[str,Any]) -> bool:
        collection_name.find_one_and_update({"_id":id},{
         "$set":dict(UserModel)
         })
    
 
class SendEmailVerify:
 
  def sendVerify(token,email):
    email_address = "tanmud754@gmail.com" # type Email
    email_password = "tlbkqffcprmfjbya" # If you do not have a gmail apps password, create a new app with using generate password. Check your apps and passwords https://myaccount.google.com/apppasswords
 
    # create email
    msg = EmailMessage()
    msg['Subject'] = "Verify Token"
    msg['From'] = email_address
    msg['To'] =email 
    msg.set_content(
       f"""\
    verify account        
     http://localhost:8080:8080/{token}
    """,
         
    )
    # send email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)