lst = [47,11,42,13]
result = reduce(lambda x,y: x+y, lst)

print result

result = reduce(lambda x,y: x if (x>y) else y, lst)

print result