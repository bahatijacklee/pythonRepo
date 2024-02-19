# creating a key
module1= {
    'name':"alpha",
    'version':2.34,
     'type':"alphaGroup",
    'creator':"Jacklee",
    'binary':True,
}
print(module1)
print(module1.keys())
print(module1.values())
print(module1.items())
# accessing items
#x=module1('name')
#print(x)

for x in module1:
    print(module1[x])

for x,y in module1.items():
    print(x,y)

for x in module1.values():
    print(x)

for x in module1.keys():
    print(x)

