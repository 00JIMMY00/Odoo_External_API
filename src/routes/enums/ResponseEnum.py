from enum import Enum

class ResponseSignal(Enum):
    DATA_INSERTION_SUCCESS = "Your data inserted successfully to your database "
    DATA_INSERTION_FAILED  = "Your data failed to insert"