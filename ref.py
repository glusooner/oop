class Ref:
    def __init__(self,name):
        self.name = name
        print(name)
    def pull(self):
        print('load ref data from db')
    def push(self):
        print('push ref data to db')
    conn = 'dev'

class Ref_port(Ref):
    def pull(self):
        print('here is proc to pull port hierarchy')
    def push(self):
        print('here is proc to push port hierarchy')
    conn ='prod'

class Ref_prod(Ref):
    def pull(self):
        print('here is proc to pull prod hierarchy')
    def push(self):
        print('here is proc to push prod hierarchy')


r0 = Ref('parent')
r1 = Ref_port('port')
r2 = Ref_prod('prod')

rl =[r0,r1,r2]

[r.pull() for r in rl]
