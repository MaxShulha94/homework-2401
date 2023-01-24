import module11

class Product:

    def __init__(self, title: str, price: int | float):
        self.title = title
        self.price = price
        if self.price <= 0:
            raise module11.NegativePriceError(f'Price for {self.title} can not be zero or less!')

    def __str__(self):
        return f'{self.title}: {self.price} UAH'