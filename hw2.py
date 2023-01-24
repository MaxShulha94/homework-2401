import module11, module12, module13, module14
from module12 import Product

try:
    x_1 = Product('banana', -10)
except module11.NegativePriceError as error:
    print(error)

try:
    x_2 = Product('apple', 25)
except module11.NegativePriceError as error:
    print(error)

try:
    x_3 = Product('orange', 35)
except module11.NegativePriceError as error:
    print(error)

customer_1 = module13.Customer('Ivanov', 'Ivan', '123456789')
customer_2 = module13.Customer('Ivanov', 'Petro', '123456799')

order_1 = module14.Cart(customer_1)

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

order_2 = module14.Cart(customer_2)
order_2.add_product(x_2, 10)
print(order_2)
