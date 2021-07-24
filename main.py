'fun begins here'
class User:
    def log(self):
        print('i am a customer')

class Teacher(User):
    def log(self):
        print('i am a teacher')

class Customer(User):
    def __init__(self,name,membership_type):
        self.name = name
        self.membership_type = membership_type
        
    def __str__(self):
       return self.name + ":" + self.membership_type

    def __eq__(self,other):
        if self.name == other.name:
            return True
        return False

    def upgrade(self,new_membership):
        self.membership_type = new_membership

    def print_all(customers):
        for customer in customers:
            print(customer)


    __repr__=__str__

users =[Customer('caleb','gold'),
        Customer('george','platinum'),
        Teacher()]




for user in users:
    user.log()