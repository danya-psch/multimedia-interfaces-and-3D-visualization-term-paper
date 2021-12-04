from orders.fuel_order import FuelOrderInterface


class PetrolOrder(FuelOrderInterface):
    additional_words = ["плюс"]
    main_words = ["92", "95", "95+", "98", "98+", "100", "сотий", "п'ятий", "восьмий"]

    def __init__(self):
        pass

    def log(self):
        pass

    def load_data(self):
        pass

    def process(self):
        pass

