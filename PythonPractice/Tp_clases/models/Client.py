class Client:
    def __init__(self, name: str, age: int, email: str):
        if self.validate_email():
            self._name = name
            self._age = age
            self._email = email
        else:
            print("Email invalid. Doesn't have")

    
    def to_string(self):
        return "Name: " + str(self._name) + "\nAge: " + str(self._age) + "\nEmail: " + str(self._email)
 
    def validate_email(self):
        if self._name.find('@') < 0:
            return False
        else:
            return True

