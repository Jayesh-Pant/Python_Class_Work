'''a=1
b=1
c=a+b
print(c)
if(a>10):
    print("a is greater than 10")
else:
    print("a is less than or equal to 10")

for i in range(0,10):
    print(i*"*")'''

'''''a=1.0
b=1'''
'''c=a+b
d=c-b
print(type(a))
print(id(a),id(b),id(c),id(d))
'''
'''print(a is b, a==b)

message = "Hello Python"
message = message.upper()
print(message)'''

'''for letter in message:
    print(letter)
'''
'''for i in range(0,len(message)+1):
    letter = message[0:i]
    print(letter)'''''


def add(a,b):
    c=a+b
    return c
a=5
b=6
print(add(a,b))