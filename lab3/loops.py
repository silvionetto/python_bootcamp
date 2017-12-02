x = (1,2,3,4,5)
for i in x:
  print(i)

for i in x:
  if i < 5:
    print("menor")
  else:
    print("maior")

x = [(1,2),(3,4),(5,6)]
for (i1,i2) in x:
  print(i1)

x = {'k1':1,'k2':2}
for k,v in x.items():
  print(v)
