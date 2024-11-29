from .BaseModel import BaseModel


class ContactModel(BaseModel):
    def __init__(self, db_client):
        super().__init__(db_client)

    
    @classmethod
    async def insert_contact(cls, db_client: object):
        row = cls(db_client)
        await row.insert()
        print("row inserted succefully !!")
        return row 
    
    async def insert(self):
        vals = {
        'name': 'saed'
        }
        id = self.db_client.execute_kw(self.settings.DB_NAME, 2, 
                                       self.settings.ODOO_API_KEY, 'res.partner', 
                                       'create', [vals])
