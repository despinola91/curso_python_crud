import uuid

class Client:

    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #Si no tenemos un uuid entonces generamos uno


    def to_dict(self):
        return vars(self)

    
    @staticmethod #metodos que se pueden ejecutar sin instancia de clase
    def schema():
        return ['name', 'company', 'email', 'position', 'uid']
