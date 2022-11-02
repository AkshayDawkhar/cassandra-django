import random 
import string 

def userName():
    return ''.join(random.sample(string.ascii_letters ,12))
