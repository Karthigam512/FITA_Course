import xlrd


def get_workbook_handle(workbook_name):
    workbook_handle = xlrd.open_workbook(workbook_name)
    return workbook_handle


def get_sheet_handle(workbook_handle, sheet_name):
    sheet_handle = workbook_handle.sheet_by_name(sheet_name)
    return sheet_handle


def get_row_count(sheet_handle):
    row_count = sheet_handle.nrows
    return row_count


def get_column_count(sheet_handle):
    column_count = sheet_handle.ncols
    return column_count


def read_userdata(workbook_name, sheet_name):
    data = []
    wb_handle = get_workbook_handle(workbook_name)
    s_handle = get_sheet_handle(wb_handle, sheet_name)
    count = get_row_count(s_handle)
    for row in range(1, count):
        data.append(s_handle.row_values(row))
    return data


#print(read_userdata("userdata.xls", "Login"))

