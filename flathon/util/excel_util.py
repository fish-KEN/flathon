def is_excel_file(file_name):
    if '$' in file_name or '.meta' in file_name:
        print('[flathon] Not exceel file ' + file_name)
        return False
        
    return file_name.endswith('.xlsx')
