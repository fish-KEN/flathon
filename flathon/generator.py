import openpyxl
from flathon.fbs_const import ROOT_HIERARCHY_NAME
from util import excel_util

def generate(file_path):

    # Check file is excel
    if excel_util.is_excel_file(file_path) == False:
        print('Not excel file ' + file_path)
        return

    
    #  Laod excel
    workbook = openpyxl.load_workbook(file_path)
    