x = [1,2,3]
y = [4,5,6]

result = zip(x,y)
print result

print map(lambda pair: max(pair),zip(x,y))