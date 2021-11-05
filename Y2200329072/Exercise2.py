def is_email(sign):
    if "." and "@" in sign:
        return True
    else:
        return False
    
email=str(input("enter your email "))
if is_email(email) == True:
    print(email + "valid e-mail")
else:
    print(email + "not a valid e-mail")
    