#Zaahid'sCode
CellC=[]
cellctotal=0
Vodacom=[]
vodacomtotal=0
MTN=[]
mtntotal=0
for i in range(0,10):
	n=input("Enter your number Please")
	if len(n)!=10:
		print("This is an invalid number")
	if n[:3]=="082" or n[:3]=="076":
		Vodacom.append(n)
		vodacomtotal=vodacomtotal+1
	elif n[:3]=="083":
		MTN.append(n)
		mtntotal=mtntotal+1
	elif n[:3]=="084" or n[:3]=="062":
		CellC.append(n)
		cellctotal=cellctotal+1
	else:
		print("Not available")
print("The number of CellC numbers amounted to ", cellctotal, "The numbers entered is ", CellC)
print("The number of Vodacom numbers amounted to ",vodacomtotal, "The numbers entered is ", Vodacom)
print("The number of mtn numbers amounted to ",mtntotal, "The numbers entered is ", MTN)ode here
