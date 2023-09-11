cart=[10,20,600,40,50]
for item in cart:
    if item>500:
	   print("We cannot process this item")
	   continue
	print(item)	
else:
    print("congrats all items processed succesfully")