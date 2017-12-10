class Animal(object):
  
  def __init__(self):
    print('Animal Created')

  def whoAmI(self):
    print('Animal')

a = Animal()
print(a)
a.whoAmI()


class Dog(Animal):

  def __init__(self,name):
    Animal.__init__(self)
    self.name = name
    print('Dog Created')

  def __str__(self):
    return "%s" %(self.name)

  def whoAmI(self):
    print('Dog')

  def bark(self):
    print('woof')

b = Dog(name = 'Bob')
print(b)
b.whoAmI()
b.bark()    
print(b.name)
