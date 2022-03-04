class Society():
    """Creating a Society with name, house_of_no_mem, flat and income"""
    def __init__(self,society_name="", house_no_of_mem=""):
        self.society_name=society_name
        self.house_no_of_mem=house_no_of_mem
        self.flat=""
        self.income=0
    
    def input_data(self):
        """Reading information from member, enter income"""
        
        self.society_name=input("Enter society name : ")
        self.house_no_of_mem=input("Enter house_no_of_mem:")
        self.income=int(input("Enter income :"))
    
    def allocate_flat(self):
        """Allocate flat according to income """
        if self.income>=25000:
            self.flat="A Type"
            print(f"Flat is {self.flat}")
        elif 20000 <= self.income< 25000:
            self.flat="B Type"
            print(f"Flat is {self.flat}")
        elif 15000 <= self.income< 20000:
            self.flat="C Type"
            print(f"Flat is {self.flat}")
        else:
            self.flat="D Type"
            print(f"Flat is {self.flat}")
    
    def show_data(self):
        print(f"Society Name: {self.society_name}, house_no_of_mem: {self.house_no_of_mem}, income : {self.income}, flat:{self.flat}")
         
            
        
                
        
            
        