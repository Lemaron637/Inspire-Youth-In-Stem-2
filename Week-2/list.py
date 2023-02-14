names=["John","Peter","Mary","Leo"]
#accessing items in a list
print("names")
print(names[0:-1])
print(names[-3])
print(names[2])
fruits=["banana","orange","guava","kiwi","lime"]
print(fruits[0:-1])
print(fruits[3])
#Adding two list
vegetables=["cabbages","carrots","onions","cucumber","tomato"]
stationery=["pens","ink","paper","erasers","books"]
shoppings=vegetables+stationery
print(shoppings)
for vegetable in vegetables:
    print(vegetable)
for shopping in shoppings:
    print(shopping)
print("My name is " + names[0]+ " and my favourite fruit is " + fruits[2])