class Customer:
    all_customers = [ ]
    count_all_customers = 0

    def __init__(self,given_name,family_name):
     
        self.given_name= given_name
        self.family_name= family_name
        Customer.count_all_customers +=1
        Customer.all_customers.append(self)



    def get_given_name(self):
        return self.given_name
    def set_given_name(self,new_name):
        self.given_name= new_name
    def get_family_name(self):
        return self.family_name
    def set_family_name(self,new_family_name):
        self.family_name= new_family_name

    def full_name(self):
        return f'{self.given_name} {self.family_name}' 
    
    @classmethod
    def get_all_customers(cls):
        return cls.all_customers

   


c1 = Customer('IAn','Gich')
c2 = Customer('John','Doe')

all_customers = Customer.get_all_customers()
# print(Customer.count_all_customers)
print([i.full_name() for i in all_customers])
