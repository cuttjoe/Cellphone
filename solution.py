CellC=[]
Vodacom=[]
MTN=[]
CellCT=0
MTNT=0
VodacomT=0
for i in range(0,9):
	a=input("enter your number please")
	if len(a)!=10:
		print("Invalid Number")
	elif a[:3]=="082" or a[:3]=="076":
		Vodacom.append(a)
		VodacomT=VodacomT+1
	elif a[:3]=="083":
		MTN.append(a)
		MTNT=MTNT+1
	elif a[:3]=="084" or a[:3]=="062":
		CellC.append(a)
		CellCT=CellCT+1
print("CellC Numbers", CellC, "Total," CellCT)
print("MTN Numbers", MTN, "Total", MTNT)
print("Vodacom Numbers", Vodacom, "Total", VodacomT)

    	
