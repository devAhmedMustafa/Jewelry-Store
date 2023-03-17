from .models import Product, Buying
import random
import string

def isBlank(field):
    if field and field.strip():
        return True
    else:
        return False
    

def check_left():

    products = Product.objects.all()

    for x in products:

        if x.left != 0:
            x.on_stock = True
            x.save()

        else:
            x.on_stock = False
            x.save()

def generate_serial_key():

    lowercase = list(string.ascii_lowercase)
    nums = list(string.digits)

    serial_key = []

    random.shuffle(lowercase)
    random.shuffle(nums)

    for i in range(4):
        serial_key.append(lowercase[i])
        serial_key.append(nums[i])

    random.shuffle(serial_key)

    serial_key = "".join(serial_key[0:])
    return serial_key

def add_serial_key():

    serial_key = generate_serial_key()

    for x in Buying.objects.all():

        if serial_key == x.serial_key:
            add_serial_key()

        else:
            continue

    return serial_key
