import module_neg_price_error, module_Product, module_Customer, module_Cart


try:
    x_1 = module_Product.Product('banana', -10)
except module_neg_price_error.NegativePriceError as error:
    print(error)

try:
    x_2 = module_Product.Product('apple', 25)
except module_neg_price_error.NegativePriceError as error:
    print(error)

try:
    x_3 = module_Product.Product('orange', 35)
except module_neg_price_error.NegativePriceError as error:
    print(error)

customer_1 = module_Customer.Customer('Ivanov', 'Ivan', '123456789')
customer_2 = module_Customer.Customer('Ivanov', 'Petro', '123456799')

order_1 = module_Cart.Cart(customer_1)

try:
    order_1.add_product(x_1)
except NameError:
    print(f'You can not add another products until you change the price for this product!')

try:
    order_1.add_product(x_2, 2)
except NameError:
    print(f'You can not add another products until you change the price for this product!')

try:
    order_1.add_product(x_3, 35)
except NameError:
    print(f'You can not add another products until you change the price for this product!')

print(order_1)

order_2 = module_Cart.Cart(customer_2)
order_2.add_product(x_2, 10)
print(order_2)
