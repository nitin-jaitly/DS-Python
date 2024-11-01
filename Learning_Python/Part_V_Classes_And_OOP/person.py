from classtools import AttrDisplay
class Person(AttrDisplay):
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def __del__(self):
        print('Deleting %s' % self.name)

    def last_name(self):
        return self.name.split()[-1]

    def give_raise(self, percent):
        self.pay = int(self.pay * (1 + percent))

    def __repr__(self):
        return '[Person: %s, %s, %s]' % (self.name, self.job, self.pay)


class Manager(Person):
    def __init__(self, name, job, pay):
        Person.__init__(self, name, 'Mgr', pay)

    def give_raise(self, percent, bonus=.10):
        Person.give_raise(self, percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)


class Department:
    def __init__(self, *args):
        self.members = list(args)

    def add_member(self, person: Person):
        self.members.append(person)

    def add_manager(self, manager: Manager):
        self.members.append(manager)

    def give_raises(self, percent):
        for person in self.members:
            person.give_raise(percent)

    def showAll(self):
        for person in self.members:
            print(person)


def main():
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', 'Dev', 100000)
    tom = Manager('Tom Jones', 'Mgr', 50000)

    print(bob)
    print(sue)
    print(bob.last_name(), sue.last_name())
    sue.give_raise(.10)
    print(sue)
    tom = Manager('Tom Jones', 'Mgr', 50000)
    tom.give_raise(.10)
    print(tom.last_name())

    print(tom)

    development = Department(bob, sue)
    development.add_manager(tom)
    development.give_raises(0.10)
    development.showAll()
    #
    # print(bob.last_name(), sue.last_name())
    # sue.give_raise(.10)
    # print(sue)
    #
    # tom.give_raise(.10)
    # print(tom.last_name())
    # print(tom)
    #
    # print('--All three--')
    # for obj in (bob, sue, tom):
    #     obj.give_raise(.10)
    #     print(obj)
    #

if __name__ == "__main__":
    main()