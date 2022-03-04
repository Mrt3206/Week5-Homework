
class Customer():
    """ Customer information"""
    customer_list=[]
    
    def __init__(self,name,last_name,id):
        self.id=id
        self.name=name
        self.last_name=last_name
        Customer.customer_list.append({"name":self.name,"last_name":self.last_name,"customer id:":self.id})
    
    def __str__(self):
       print(self.customer_list)
    @classmethod
    def get_cust_info(cls):
        print(cls.customer_list)
           
    
class Items():
    """Shopping Items"""
    def __init__(self,name,price,qty):
        """Initialize items as price,quantity """
        self.name=name
        self.price=price
        self.qty=qty
        self.discount=0
        self.price_tobe_paid=0
        self.item_number=0
        self.item={self.name:(self.price,self.qty)}
        self.shopping_cart()
        
        
    def __str__():
        pass
    def calculate_discount(self):
        """Calculate discount"""
        self.total_price=self.price*self.qty
        if self.total_price>=4000:
            self.discount=0.25*self.total_price
        elif 2000<=self.total_price<4000:
            self.discount=0.15*self.total_price
        else:
            self.discount=0.10*self.total_price
            
        self.price_tobe_paid=self.total_price-self.discount
   
        
    def shopping_cart(self):
        
        self.item_list.append(self.item)
        for i in self.item_list:
            self.total_price+=self.price
        
        
        
        
    def get_total_amount():
        pass
    



