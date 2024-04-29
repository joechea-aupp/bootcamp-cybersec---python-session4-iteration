# file mode:
# r: read
# w: write
# a: append

with open('password.txt', 'r') as file:
    print(file.read())


# with open('password.txt', 'r') as file:
#     print(file.readline())
#     print(file.readline())


# with open('password.txt', 'r') as file:
#     print(file.readlines())


# with open('capture_password.txt', 'w') as file:
#     file.write('123456')
#     print('password saved')
