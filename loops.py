# if elif and else
loc = "Bank"

if loc == "Hello Bank":
    print(False)
elif loc == "Bank":
    print(True)
elif loc == "Store":
    print("Hello")
else:
    print("Wrong")

# for loop
my_iterable = [1,2,3]
for item_name in my_iterable:
    print(item_name)

for num in my_iterable:
    if num%2==0:
        print(num)
    else:
        print(None)

word = "letter"
for letter in word:
    print(letter)

tup = (1,2,3)
for item in tup:
    print(item)

my_list = [(1,2),(3,4),(5,6)]
for item in my_list:
    print(item)

for (a,b) in my_list:
    print(a)
    print(b)

d = {'k1':1,'k2':2}
for item in d.items():
    print(item)

for item in d:
    print(item)

for (key,value) in d.items():
    print(key)
    print(value)

# while loops execute when ome condition is true

x=0

while x<5:
    print(f'the current value of x is {x}')
    x += 1
else:
    print("x is not less than 5")

# break, continue, pass
# pass - does nothing at all

my_string = "Vikas"

for item in my_string:
    if item=="V":
        continue
    print(item)

for item in my_string:
    if item == "i":
        break
    print(item)
