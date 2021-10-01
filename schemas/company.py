# Schema helps to serialize and convert mongodb format to the UI required fields.

def companyEntity(db_item) -> dict:
    """Converting raw data to Json and returning one company Enitity"""
    return {
        "id": str(db_item["_id"]),
        "cname": db_item["company_name"],
        "uen": db_item["company_uen"],
        "name": db_item["company_personName"],
        "address": db_item["company_personAddress"],
        "nationality": db_item["company_personNationality"]
    }

def listOfCompanyEntity(db_item_list) -> list:
    """Function: APPEND Converted JSON entity onto list_company_entity Array. 
    Return: Array output"""
    list_company_entity = []
    for item in db_item_list:
        list_company_entity.append(companyEntity(item))
    return list_company_entity