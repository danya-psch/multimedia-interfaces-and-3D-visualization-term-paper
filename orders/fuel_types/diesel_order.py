from orders.fuel_order import FuelOrderInterface


class DieselOrder(FuelOrderInterface):
    additional_words = ["пальне","плюс"]
    main_words = ["дт", "дт+", "дизель", "диз", "дизеля", "дизелю", "дизел", "дизельне"]

    def __init__(self):
        pass

    def log(self):
        pass

    def load_data(self):
        pass

    def process(self):
        pass

