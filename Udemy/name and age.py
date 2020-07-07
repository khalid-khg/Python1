x = "is"
y = "my"
z = "name"
c = y + " " + z + " " + x
print(c)
x = " my name is "
z = "Khalid"
y = "my name is {}".format(z)
print(y)

x = 33
y = "Khalid"
z = "my name is {} and my age is {}".format(y , x)
print(z)

f = "my name is {1} and my age is {0}".format(x , y)
print(f)

x = "Khalid"
y = f"my name is {x}" #لابد وضع f لكي يظهر الاسم (f) تعني  formst
print(y)

x = "Khalid"
y = "33"
z = f"my name is {x} and my age is  {y}"
print(z)

x = ["Khalid" , "sports" , "33"]
z = f"my name is {x[0]} and my hobbie is  playing {x[1]} and my age is {x[2]}"
print(z)