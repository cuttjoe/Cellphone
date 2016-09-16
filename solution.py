cellc=[]
cellctotal=0
vodacom=[]
vodacomtotal=0
mtn=[]
mtntotal=0
for i in range (0,10):
	number=input("enter a phone number")
	if len(number)!=10:
		print("the number is invalid please enter a new number with 10 digits")
		number=input("enter a new number that has 10 digits")
	if number[:3]=="072" or number[:3]=="076" or number[:3]=="079" or number=="082":
		print("---------------------")
		print("This number is available and has been added to the database")
		print("---------------------")
		vodacom.append(number)
		vodacomtotal=vodacomtotal+1
	elif number[:3]=="073" or number[:3]=="075" or number[:3]=="077" or number=="078" or number=="083":
		print("---------------------")
		print("This number is available and has been added to the database")
		print("---------------------")
		mtn.append(number)
		mtntotal=mtntotal+1
	elif number[:3]=="084" or number[:3]=="062":
		print("---------------------")
		print("This number is available and has been added to the database")
		print("---------------------")
		cellc.append(number)
		cellctotal=cellctotal+1
	else:
		print("---------------------")
		print("unavailable number")
		print("---------------------")
print("the total number of vodacom numbers is", vodacomtotal, "the vodacom numbers are", vodacom)
print("the total number of mtn numbers is", mtntotal, "the mtn numbers are", mtn)
print("the total number of cellc numbers is", cellctotal, "the cellc numbers are", cellc)
	
