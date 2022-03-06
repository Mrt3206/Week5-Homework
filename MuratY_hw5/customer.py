
class Customer():
    """ Customer information"""
    customer_list = []

    def __init__(self, name, last_name, id):
        self.id = id
        self.name = name
        self.last_name = last_name
        Customer.customer_list.append({"name": self.name, "last_name": self.last_name, "customer id:": self.id})
        self.shopping = Items()

    def __str__(self):
        return f"[customer_id:{self.id}, items:{self.shopping.shopping_cart()}, \
        total price: {self.shopping.get_total_amount()} \
         Price to be paid: {self.shopping.calculate_discount()}, discount: {self.shopping.discount}]"
    @classmethod
    def get_cust_info(cls):
        print(cls.customer_list)

class Items():

    """Shopping Items"""
    shopping_cart_list = {}
    total_price = 0
    discount=0
    def __init__(self, name="", price=0, qty=0):
        """Initialize items as price,quantity """
        self.name = name
        self.price = price
        self.qty = qty
        self.price_tobe_paid = 0

    def __str__():
        pass
    
    @classmethod
    def calculate_discount(cls):
        """Calculate discount"""
        if cls.total_price >= 4000:
            cls.discount = 0.25 * cls.total_price
        elif 2000 <= cls.total_price < 4000:
            cls.discount = 0.15 * cls.total_price
        else:
            cls.discount = 0.10 * cls.total_price
        return (cls.total_price - cls.discount)

    def shopping_cart(self):
        """Enter items,price and quantity"""
        flag = "Y"
        while flag == "y" or flag=="Y":
            self.name = input("Enter item name: ")
            self.price = float(input("Enter item price: "))
            self.qty = int(input("Enter item quantity: "))
            Items.shopping_cart_list[self.name] = (self.price, self.qty)
            flag = input("For enter item name : Y for quit:q ")
        return Items.shopping_cart_list.keys()
    
    @classmethod
    def get_total_amount(cls):
        """Calculate Total Price"""
        for key in cls.shopping_cart_list:
            cls.total_price += cls.shopping_cart_list[key][0] * cls.shopping_cart_list[key][1]
        return cls.total_price

"""Test"""
customer1 = Customer("Murat", "yel", 123)
print(customer1)







    



