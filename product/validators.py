import json

Product = '{ "id":"A_120", "name":"Leche", "value": 10.00, "discount":0.10, "stock":5}'


def validate_name(name):
    if (type(name) != str) or (len(name) > 55):
        return "Invalid product name"


def validate_value(value):
    if (type(value) != float) or not (0 < value < 99999.9):
        return "Invalid value"


def validate_discount_value(descount, value):
    if (type(descount) != float) or (descount > value):
        return "Invalid discount value"


def validate_stock(stock):
    if (type(stock) != int) or (stock < -1):
        return "Invalid stock value"


def _validate_product(product):
    error_name = validate_name(product.get("name"))
    error_value = validate_value(product.get("value"))
    error_discount = validate_discount_value(
        product.get("discount"), product.get("value")
    )
    error_stock = validate_stock(product.get("stock"))
    error = []
    if error_name:
        error.append(error_name)
    if error_value:
        error.append(error_value)
    if error_discount:
        error.append(error_discount)
    if error_stock:
        error.append(error_stock)
    return product["id"], error


def validate_products(products):
    products_report = []
    for p in products:
        id, errors = _validate_product(p)
        if errors:
            report = {"product_id": id, "errors": errors}
            products_report.append(report)
    return products_report


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

