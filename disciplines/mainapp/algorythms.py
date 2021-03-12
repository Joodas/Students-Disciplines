from statistics import median


class Average:
    def calculate_avg(self, array):
        raise NotImplementedError()


class Arithmetic(Average):
    def calculate_avg(self, array):
        length = len(array)
        summary = sum(array)
        avg = summary / length
        return avg


class Median(Average):
    def calculate_avg(self, array):
        avg = float(median(array))
        return avg


class Query:
    @staticmethod
    def get_query(array, strategy):
        global algorithm
        if strategy == 'Arithmetic':
            algorithm = Arithmetic()
        elif strategy == 'Median':
            algorithm = Median()
        result = algorithm.calculate_avg(array)
        return result
