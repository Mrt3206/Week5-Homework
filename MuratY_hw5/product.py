class Product():
    """"""
    def __init__(self,product_id="",product_name="",product_purchase_price=0,product_sale_price=0):
        """Initialize Product class with product_id, product_name,product_purchase_price
        product_sale_price"""
        self.product_id=product_id
        self.product_name=product_name
        self.product_purchase_price=product_purchase_price
        self.product_sale_price=product_sale_price
        self.remarks=""
    
    def set_remarks(self):
        """Assigns price margin and sets Remark as Loss or Profit"""
        if self.product_sale_price-self.product_purchase_price>0:
            self.remarks="Profit"
        elif self.product_sale_price-self.product_purchase_price<0:
            self.remarks="Loss" 
        else:
            print("No profit no Loss")   
    
    def set_details(self):
        """Accept values for product_id, product_name, product_purchase_price
        product_sale_price and invokes SetRemarks()"""   
        self.product_id=int(input("Enter product id: "))
        self.product_name=input("Enter product name: ")
        self.product_purchase_price=float(input("Enter product purchase price: "))
        self.product_sale_price=float(input("Enter product sale price: "))
        
        self.set_remarks()
    
    def get_details(self):
        """Display all data members"""
        print(f"Product id: {self.product_id}, Product name: {self.product_name}")
        print(f"Product Purchase Price: {self.product_purchase_price}, Product Sale Price: {self.product_sale_price} ")
        print(f"Product Remarks: {self.remarks}")
    
        
        
    