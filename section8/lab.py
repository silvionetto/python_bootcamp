class Sample(object):
  pass

class Dog(object):

  species = 'mammal'

  def __init__(self,breed,name):
    self.breed = breed
    self.name = name

sam = Dog(breed = 'Huskie', name = 'Sammy')

print(sam)

print(type(sam))

print(sam.breed)
print(sam.species)
print(sam.name)

x = Sample()

print(type(x))
