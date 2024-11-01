from person import Person, Manager, Department
from classtools import AttrDisplay
import shelve
import glob

bob = Person('Bob Smith')
sue = Person('Sue Jones', 'Dev', 100000)
tom = Manager('Tom Jones', 'Mgr', 50000)

db = shelve.open('persondb')
for obj in (bob, sue, tom):
    db[obj.name] = obj
db.close()

glob.glob('person*')