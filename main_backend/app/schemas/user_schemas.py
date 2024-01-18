from pydantic import BaseModel

class LoginUser(BaseModel):
    first_name: str
    last_name: str
    report: str
    password: str
