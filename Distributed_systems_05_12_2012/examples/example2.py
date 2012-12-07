# Amdahl's law => S(N)= 1 / ( ( 1 - P ) + P / N ) 

P = 0
result = 0
CPUS = 64

while (P <= 1):
	result = 1 / ( ( 1 - P ) + P / CPUS )
	print result
	P = P + 0.01

