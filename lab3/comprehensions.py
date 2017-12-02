l = [letter for letter in 'word']
print(l)

l = [number for number in range(11) if number % 2 == 0]
print(l)

celsius = [0,10,20,30,40]
fahrenheit = [ (temp * (9/5.0) + 32) for temp in celsius]
print(fahrenheit)

# final result is x**4 for num in range(11)
l = [x**2 for x in [x**2 for x in range(11)]]
print(l)
