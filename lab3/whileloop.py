x = 0

while x < 10:
  print(x)
  x += 1 

  if x == 3:
    continue
    print("3")
  elif x == 6:
    break
else:
 print("All done")
