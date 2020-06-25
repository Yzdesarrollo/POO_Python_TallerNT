class Account:

    quantity = 0.0

    def __init__(self, document, name, date, quantity=None):
        self.document = document
        self.name = name
        self.date = date
        if not (quantity is None):
          self.quantity = quantity

    #getter
    def get_document(self):
        return self._document
    def get_name(self):
        return self._name
    def get_date(self):
        return self._date
    def get_quantity(self):
        return self._quantity

    #setter
    def set_document(self , document):
        self.document = document
    def set_name(self , name):
        self.name = name
    def set_date(self, date):
        self.date = date
    def set_date(self, quantity):
        self.quantity = quantity

    def __repr__(self):
        return str(self.__dict__)

    def ingresar(self, quantity):
        if quantity >= 0:
            self.quantity = quantity

    def retirar(self, quantity):
        if quantity <= self.quantity:
            self.quantity = self.quantity - quantity
        else:
          self.quantity = 0.0
          print("Se pudo retirar ", self.quantity)


account = Account(89234567, "Yeison Zaraza", "21/06/2020", 5000)
print(account)

