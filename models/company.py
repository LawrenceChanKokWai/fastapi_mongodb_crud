# TODO: Import Statement
from pydantic import BaseModel

class Company(BaseModel):
    company_uen: str
    company_name: str
    company_personName: str
    company_personAddress: str
    company_personNationality: str