from .BaseModel import BaseModel


class ContactModel(BaseModel):
    def __init__(self, db_client):
        super().__init__(db_client)

    
    @classmethod
    async def insert_contact(cls, db_client: object, myData: dict):
        row = cls(db_client)
        await row.insert(myData)
        print("row inserted succefully !!")
        # print("my dict is :", myData)
        return row 


    async def insert(self, myData: dict):
        
        id = self.db_client.execute_kw(self.settings.DB_NAME, 2, 
                                       self.settings.ODOO_API_KEY, 'res.partner', 
                                       'create', [myData])
