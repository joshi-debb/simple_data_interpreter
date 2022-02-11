class Producto:
    
    def __init__(self, name, price, sold):
        self.name = name
        self.price = price
        self.sold = sold

    def setName (self, name):
        self.name = name
    
    def setPrice (self, price):
        self.price = price
    
    def setSold (self, sold):
        self.sold = sold
    
    def getName (self):
        return self.name
    
    def getPrice (self):
        return self.price
    
    def getSold (self):
        return self.sold