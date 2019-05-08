class Filter:
    @staticmethod
    def integer(value):
        if value is None:
            return None
        try:
            return int(value)
        except ValueError:
            return value

    @staticmethod
    def string(value):
        if value is None:
            return None
        try:
            return str(value)
        except ValueError:
            return value
