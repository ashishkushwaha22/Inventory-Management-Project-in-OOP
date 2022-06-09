import csv

class Item:

    # defining class variables
    pay_rate = 0.8
    all = []

    # initialising class
    def __init__(self, item_name:str, item_price: float, item_quatity = 0):

        # run vlidations of the inputs
        assert item_price >= 0, "price must be positive integer"
        assert item_quatity >= 0, "price must be positive integer"
        
        # assign to self
        self.__name = item_name
        self.__price = item_price
        self.quantity = item_quatity

        # action
        Item.all.append(self)

    # readonly attribute - Encapsulation
    @property
    def name(self):
        return self.__name

    # setters
    @name.setter
    def name(self, value):
        if len(value) > 25:
            print("___Name length must be less then 25 characters___")
        else:
            self.__name = value

    #Encapsulating the price
    @property  
    def price(self): 
        return self.__price

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value


    def calculate_total_price(self):
        return self.__price * self.quantity

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    # defing the **class method** for getting the data from the csv file and creating instances(objects)
    @classmethod
    def ins_from_csv(cls):
        with open("oop project\data.csv") as data_file:
            reader = csv.DictReader(data_file)
            i = list(reader)
            
            for item in i:
                Item(
                    item_name=item.get('name'),
                    item_price=float(item.get('price')),
                    item_quatity=int(item.get('quantity'))
                )

    # defining the **static method** to check if the inputs are integer or not.
    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    # it is a bulitin function to represent the objects as an string
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

    # abstracting the method
    def __info(self):
        return Item.all

    def send_mail(self):
        print(f"Send mail to someone with detiails {self.__info()}")