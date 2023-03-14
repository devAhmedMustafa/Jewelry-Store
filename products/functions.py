from .models import Product

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
