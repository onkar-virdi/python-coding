age = input("what is your age")

age = int(age)
print("user has entered", age)
my_age = 2022-age
print("my age is ", my_age)

number = True
book = False

if number:
    print("Have a good day")

elif book:
    print("have a wonderful day")

else:
    print("go home")

hello = 30

if hello > 30:
    print("its a warm day")

elif hello == 30:
    print("temperature is 30")

else:
    print("its a cold day")

park_time= 4

if park_time >= 4:
    cost = 4*3 + 2*1
    print("cost", cost)

else:
    print("no charges")

park_time = input("how many hours")
print("user has entered hours", park_time)

if park_time == 4:
    cost = 4*3 + 2*1
    print("cost", cost)

elif park_time <= 4:
    cost = 5*3 + 3*1
    print("cost", cost)

else:
    print("good, as gold")

