import csv


class CsvRead:
    def __init__(self, path):
        self.path = path

    def read_data(self):
        data = []
        with open(self.path, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        return data
