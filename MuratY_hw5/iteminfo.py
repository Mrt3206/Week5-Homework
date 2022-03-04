from asyncio.windows_events import NULL


class ItemInfo():
    """Define a Item with a Code, name, price, quatity, discount rate and net price"""
    def __init__(self):
        self.item_code=0
        self.item=NULL
        self.price=NULL
        self.qty=NULL
        self.discount=NULL
        self.netprice=0
    
    def calculate_discount(self):
        """Calculate discount by quantity"""
        if self.qty<=10:
            self.discount=0
        elif 11 <= self.qty<20:
            self.discount=15
        elif self.discount>=20:
            self.discount=20
    
    def buy(self):
        """User enter values for item, price and quantity"""
        self.item_code=int(input("Enter item code: "))
        self.item=input("Enter item name: ")
        self.price=float(input("Enter item price: "))
        self.qty=int(input("Enter item quantity: "))
        
        self.calculate_discount()
        self.netprice=self.price*self.qty-self.discount
    
    def show_all(self):
        """View the content of all the data members."""
        print(f"item name: {self.item}, item code: {self.item_code}")
        print(f"item price: {self.price}, item quantity: {self.qty}")
        print(f"item discount: {self.discount}, item net price: {self.netprice}")
        
        