from pydantic import BaseModel


# user query
class RequestModel(BaseModel):
   user_input: str

# bot response
class ResponseModel(BaseModel):
   response: str