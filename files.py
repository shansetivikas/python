# a -> append text
# w -> overwrite
# r -> read
f = open('demo.txt','a')
f.write('hello')
f.close()

f = open("demo.txt",'r')
read_file = f.read()
# print(read_file)
f.seek(0)
read_file = f.read()
print(read_file)

print(f.readline())

with open('demo.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)

with open('demo.txt',mode='a') as my_new_file:
    contents = my_new_file.write("hi")

with open('demo.txt', mode='r') as my_new_file:
    contents = my_new_file.read()

print(contents)



