


def check_name(first_name):
    for i in first_name:
        try:
            int(i)
            return False
        except:
            continue
    return True


def check_number(phone_number):
    str_number = str(phone_number)
    for i in str_number:
        try:
            int(i)
            continue 
        except:
            return False    
        
def check_if_phone_exists():
    pass            
