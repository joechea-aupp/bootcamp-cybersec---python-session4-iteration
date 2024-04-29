password_pools = ['123456', 'password', '123456789', '12345678', '12345', '1234567', '1234567890', 'qwerty', 'abc123']

victim_password = 'qwerty'

for password in password_pools:
    print(f'Checking password: {password}')
    if password == victim_password:
        print(f'Password found!, password is: {password}')
        break


