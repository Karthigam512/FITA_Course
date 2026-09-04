import csv
import openpyxl


class CSVDataRead:
    def __init__(self, filepath):
        self.filepath = filepath

    def read_userdata(self):
        data = []
        with open(self.filepath, newline='') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None)
            for row in csv_reader:
                data.append(row)
        return data


class XLDataRead:
    def __init__(self, filepath):
        self.filepath = filepath

    @staticmethod
    def get_workbook_handle(workbook_name):
        workbook_handle = openpyxl.load_workbook(workbook_name)
        return workbook_handle

    @staticmethod
    def get_sheet_handle(workbook_handle, sheet_name):
        sheet_handle = workbook_handle[sheet_name]
        return sheet_handle

    def read_userdata(self):
        data = []
        wb_handle = self.get_workbook_handle(self.filepath)
        s_handle = wb_handle.active
        for row in s_handle.iter_rows(min_row=2, values_only=True):
            data.append(row)
        return data


def get_reader(filepath: str):
    if filepath.endswith('.csv'):
        return CSVDataRead(filepath)
    elif filepath.endswith('.xlsx'):
        return XLDataRead(filepath)
    else:
        raise ValueError("Unsupported file format")


class GetCred:

    def __init__(self, filepath):
        self.filepath = filepath

    def get_data_count(self):
        userdata = get_reader(self.filepath).read_userdata()
        return len(userdata)

    def get_credentials(self, index):
        userdata = get_reader(self.filepath).read_userdata()
        username = userdata[index][0]
        password = userdata[index][1]
        return username, password
