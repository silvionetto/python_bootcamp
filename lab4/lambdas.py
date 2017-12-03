def square(num):
  result = num**2
  return result

def square2(num):
  return num**2

def square3(num): return num**2

print(square(2))
print(square2(2))
print(square3(2))

square4 = lambda num: num**2

print(square4(2))

even = lambda num: num%2 == 0

print(even(2))
