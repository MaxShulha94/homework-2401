class NegativePriceError(Exception):
    def __int__(self, message):
        self.message = message