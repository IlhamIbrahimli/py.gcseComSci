def validate_pwd(pwd,minlen):
    if len(pwd) < minlen:
        return False
    else:
        return True
    
print(validate_pwd("thisisahardpassword",8))
print(validate_pwd("abc",8))

