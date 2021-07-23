class Customer:
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type
        print('customer created')


c = Customer('caleb','gold')
print(c.name, c.membership_type)