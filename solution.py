import time
CellC=[]
Voda=[]
MTN=[]
for i in range(0,10):
	CellPhone=input("Enter a CellPhone")
	if len(CellPhone)!=10:
		print ("____")
		print ("NOT A NUMBER")
		print ("____")
		time.sleep(5)
		for i in range(0,100):
			print ("")
	if (CellPhone[:3])==("084") and len(CellPhone)==10:
		print ("____")
		print ("Cell C")
		print ("____")
		time.sleep(5)
		CellC.append(CellPhone)
		for i in range(0,100):
			print ("")
	if (CellPhone[:3])==("076") and len(CellPhone)==10:
		print ("____")
		print ("Voda")
		print ("____")
		time.sleep(5)
		Voda.append(CellPhone)
		for i in range(0,100):
			print ("")
	if (CellPhone[:3])==("083") and len(CellPhone)==10:
		print ("____")
		print ("MTN")
		print ("____")
		time.sleep(5)
		MTN.append(CellPhone)
		for i in range(0,100):
			print ("")
print ("Cell C Numbers:",CellC,"")
print ("Voda Numbers:",Voda,"")
print ("MTB Numbers:",MTN,"")
		
		
