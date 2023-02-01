import module_Customer
import module_Product

class CartIterator:
    def __init__(self, products):
        self.products = products
        self.index = 0

    def __next__(self):
        if self.index < len(self.products):
            self.index += 1
            return self.products[self.index - 1]
        raise StopIteration

class Cart:
    MAX_LIMIT = 40

    def __init__(self, customer: module_Customer.Customer):
        self.customer = customer
        self.products = []
        self.__quantities = []

    def __getitem__(self, item):
        return self.products[item]

    def __len__(self):
        return len(self.products)

    def get_weight(self):
        return sum(self.__quantities)

    def add_product(self, product: module_Product.Product, quantity: int | float = 1):
        if self.get_weight() + quantity <= Cart.MAX_LIMIT:
            self.products.append(product)
            self.__quantities.append(quantity)

    def total(self):
        result = 0
        for product, quantity in zip(self.products, self.__quantities):
            result += product.price * quantity

        return result

    def __str__(self):
        result = f'{self.customer}\n'
        result += '\n'.join(map(lambda item: f'{item[0]} x {item[1]} = {item[0].price * item[1]} UAH',
                                zip(self.products, self.__quantities)))
        result += f'\nTotal: {self.total()} UAH'
        return result

