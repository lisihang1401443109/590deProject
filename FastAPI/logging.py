from utils import get_db
import json

db_handler = get_db('logging')



def log_request(request_body, user):
    serialized_body = json.dumps(request_body)
    with db_handler.connect() as conn:
        try:
            conn.execute("INSERT INTO logs (request_body, user) VALUES (:request_body, :user)",
                         {"request_body": serialized_body, "user": user})
        except Exception as e:
            print(e)
            return False
    return True
    
    