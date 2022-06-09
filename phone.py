from item import Item

# child class - Inheritance class
class Phone(Item):

    def __init__(self, item_name:str, item_price: float, item_quatity = 0, broken_phone = 0):
        super().__init__(item_name,item_price,item_quatity)
        
        # # run vlidations
        assert broken_phone >= 0, "broken phone quantity must be positive integer"

        # assign
        self.broken_phone = broken_phone
