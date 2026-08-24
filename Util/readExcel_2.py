import openpyxl


def get_workbook_handle(workbook_name):
    workbook_handle = openpyxl.load_workbook(workbook_name)
    return workbook_handle


def get_sheet_handle(workbook_handle, sheet_name):
    sheet_handle = workbook_handle[sheet_name]
    return sheet_handle


def read_userdata(workbook_name, sheet_name):
    data = []
    wb_handle = get_workbook_handle(workbook_name)
    s_handle = get_sheet_handle(wb_handle, sheet_name)
    for row in s_handle.iter_rows(min_row=2, values_only=True):
        data.append(row)
    return data

