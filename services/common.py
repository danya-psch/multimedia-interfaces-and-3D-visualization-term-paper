class Common(object):

    @staticmethod
    def has_numbers(text):
        return any(char.isdigit() for char in text)