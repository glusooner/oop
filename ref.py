class Ref:
    def __init__(self,name):
        self.name = name
        print(name)
    def load(self):
        print('load ref data')

    conn = 'dev'

class Ref_port(Ref):
    def load(self):
        print('here is proc to load port hierararchy')
    
    conn ='prod'

class Ref_prod(Ref):
    def load(self):
        print('here is proc to load prod hierarchy')

r0 = Ref('parent')
r0.load()
print(r0.conn)
r1 = Ref_port('port')
r1.load()
print(r1.conn)
r2 = Ref_prod('prod')
r2.conn
r2.load()
print(r2.conn)

