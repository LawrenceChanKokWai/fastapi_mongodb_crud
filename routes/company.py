# TODO: import statements
from bson.objectid import ObjectId
from fastapi import APIRouter
from models.company import Company
from config.database import connection
from schemas.company import companyEntity, listOfCompanyEntity

# TODO: Creating and define APIRouter
company_router = APIRouter()
"""Defined FastApi Router"""

@company_router.get('/companies')
async def find_all_companies():
    """GET: Getting all companies
    RETURN: All company entity in the database."""
    return listOfCompanyEntity(connection.local.company.find())

@company_router.get('/companies/{companyId}')
async def find_company_by_id(companyId):
    """GET: Getting one company by companyId.
    RETURN: one company from the database by companyId"""
    return companyEntity(connection.local.company.find_one({"_id": ObjectId(companyId)}))

@company_router.post('/companies')
async def create_company(company: Company):
    """POST: Inserting one company to the database dictionary.
    RETURN: All company entity in the database."""
    connection.local.company.insert_one(dict(company))
    return listOfCompanyEntity(connection.local.company.find())

@company_router.put('/companies/{companyId}')
async def update_company(companyId, company: Company):
    """PUT: Find the company and update with the new company data.
    RETURN: Company Entity that had found ObjectId of id"""
    connection.local.company.find_one_and_update(
        {"_id": ObjectId(companyId)},
        {"$set": dict(company)}
    )
    return companyEntity(connection.local.company.find_one({"_id": ObjectId(companyId)}))

@company_router.delete('/companies/{companyId}')
async def delete_company(companyId):
    """DELETE: Finds the company, deletes it.
    RETURN: The same company object."""
    return companyEntity(connection.local.company.find_one_and_delete({"_id": ObjectId(companyId)})) 
