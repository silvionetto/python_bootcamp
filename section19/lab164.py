def fahrenheit(T):
	return (9.0/5)*T + 32

temps = [0,22.5,40,100]

results = map(fahrenheit,temps)

print results