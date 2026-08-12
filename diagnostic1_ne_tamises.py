def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 20
    elif shipping_speed == "overnight":
        shipping = 35
    elif shipping_speed == "standard" and cart_total >= 100:
        shipping = 0
    elif shipping_speed == "standard":
        shipping = 10
    else:
        print("No")
        shipping = 0

    total = cart_total + shipping
    return total

print(calculate_checkout(100, "express"))
