# TODO: Import Statements [FASTApI, company_routes]
from fastapi import FastAPI
from routes.company import company_router

# TODO: Create App from FastApi
app = FastAPI()

# TODO: Register the router
app.include_router(company_router)