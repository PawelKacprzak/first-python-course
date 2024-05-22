password = 'My_password_123'

if len(password) > 8:
    print('Your password contain 8 or more letters.')
    if any(str.isdigit(c) for c in password):
        print('Your password contain min. 1 digit.')
        if any(str.isupper(b) for b in password):
            print('Your password contain min. 1 uppercase letter.')
            if any(str.islower(a) for a in password):
                print('Your password contain min. 1 lowercase letter.')
                print('The password is complex enough.')
            else:
                print('The password must contain at least one lowercase letter.')
        else:
            print('The password must contain at least one uppercase letter.')
    else:
        print('The password must contain at least one digit.')
else:
    print('The password is too short.')
        
    