from utils.hesh_password import hash_psw

class Label:
    def __init__(self, password: str, email: str):
        self.password = password
        self.email = email

    def not_found(self):
        print(f"User {self.email},\n pasword {self.password}\n and his hesh passwod {hash_psw(self.password)}\n not found")
        return {"message": "Ok"}