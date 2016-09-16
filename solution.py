CellC=str("084")
MTN=str("082")
Voda=str("076")
CellCT=0
MTNT=0
VodaT=0
for i in range (10):
	A=input("pls Enter a number")
	if len(A)<10 and len(A)>10:
		print("error")
	else:
		if A[:3]==CellC:
			CellCT=CellCT+1
		elif A[:3]==MTN:
			MTNT=MTNT+1
		elif A[:3]==Voda:
			VodaT=VodaT+1
print ("Voda",VodaT)
print ("MTN",MTNT)
print ("CellC",CellCT)
