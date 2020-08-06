import json

Product = '{ "id":"A_120", "name":"Leche", "value": 10.00, "discount":0.10, "stock":5}'


def validate_name(name):
    if (type(name) == str) and (len(name) < 55):
        print("valid name")
    else:
        return "invalid product name"


def validate_value(value):
    if (type(value) == float) and (0 < value < 99999.9):
        print("valid value")
    else:
        return "invalid value"


def validate_discount_value(descount, value):
    if (type(descount) == float) and (descount < value):
        print("valid discount")
    else:
        return "Invalid discount value"


def validate_stock(stock):
    if (type(stock) == int) and (stock > -1):
        print("valid stock")
    else:
        return "Invalid stock value"


def validate_product(object):
    product = json.loads(object)
    error_name = validate_name(product["name"])
    error_value = validate_value(product["value"])
    error_discount = validate_discount_value(product["discount"], product["value"])
    error_stock = validate_stock(product["stock"])
    error = []
    if error_name:
        error.append(error_name)
    if error_value:
        error.append(error_value)
    if error_discount:
        error.append(error_discount)
    if error_stock:
        error.append(error_stock)
    return error


# error = validate_product(Product)
# print(error)
def validate_fields(products):
    fields_to_validate = ["id", "name", "value", "discount", "stock"]
    error_counter = 0
    for p in products:
        keys = p.keys()
        check = all(item in keys for item in fields_to_validate)
        if check == False:
            error_counter += 1
    return error_counter

