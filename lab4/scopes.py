name = "Silvio"

def func():
  name = "Netto"
  
  def hello():
    print(name)

  hello()

func()

print(name)

def funcGlobal():
  global name
  print(name)
  name = "Global"

funcGlobal()
print(name)
