class Client:
    def __init__(self, name: str, age: int, email: str):
        if self.validate_email(name):
            self._name = name
            self._age = age
            self._email = email
        else:
            print("Email invalid. Doesn't have")
    
    def to_string(self):
        return "Name: " + str(self._name) + "\nAge: " + str(self._age) + "\nEmail: " + str(self._email)
 
    def __validate_email(self, name: str):
        if name.find('@') < 0:
            return False
        else:
            return True

