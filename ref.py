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
r0.pull()
r0.push()
print(r0.conn)
print(r0.name)

r1 = Ref_port('port')
r1.pull()
r1.push()
print(r1.conn)
print(r1.name)
r2 = Ref_prod('prod')
r2.conn
r2.pull()
r2.push()
print(r2.conn)
print(r2.name)
