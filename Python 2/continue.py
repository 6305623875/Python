cart=[10,20,600,40,50]
for item in cart:
    if item>500:
	   print("We cannot process this item :",item)
	   continue
	print(item)	