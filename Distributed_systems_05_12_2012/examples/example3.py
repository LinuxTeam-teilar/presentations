
# P= C * V * V * F

C = 0.1 #Capacity
V = 35  #Voltage
F = 1600 #Frequency
FC = 0 #Frequency Counter
P = 0  #P

while (True):
	P= C*V*V*F
	FC = FC + 100
	F = F + 100
	if (FC % 400 == 0):
		V += 0.1
	print "Gia V "+ str(V) +" kai F "+str(F)+ " exoume P= "+ str(P)
	if (F> (1600*2)):
		break