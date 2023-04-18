# file = open('data.txt',"w")
# file.write("AA")
# file.close()

# file = open('data.txt','r+')
#
# try:
#     file.write("hello")
# finally:
#     file.close()

# with open('data.txt','w') as file:
#     file.write('hello')

# with open('data.txt','r') as file:
#     for line in file.readlines():
#         print(line)

# with open('data.txt', 'r') as file:
#     print(list(file))
#     for line in list(file):
#         print(line)

with open('data.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        print(line)