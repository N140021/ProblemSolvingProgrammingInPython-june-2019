# Function to validate a phone number
import re
def phonenumberValidation(num):
    pattern='^[6-9][0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
    if re.match(pattern,str(num)):
        #print("Valid number")
        return True
    else:
        #print("Invalid number")
        return False
    return
def emailValidation(email):
    pattern='^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,18}[.][a-z]{2,4}$'
    if re.match(pattern,email):
        return True
    return False