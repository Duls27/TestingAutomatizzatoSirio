import pandas as pd
import os

#This function use Panda library for extract info from excel file
#INPUT: path to excel file
#OUTPUT: data frames with data for each excell sheet
def get_excel_info (path_file_login):
    # Load the xlsx file

    df_users = pd.read_excel(path_file_login,sheet_name='users_info')
    df_config = pd.read_excel(path_file_login, sheet_name='config_info')
    df_carica_esame = pd.read_excel(path_file_login, sheet_name='carica_esame')

    return df_config, df_users, df_carica_esame

def get_exam_info (exam_folder_path):
    exams_dict = {}
    exam_list=os.listdir(path=exam_folder_path)
    for is_it_exam in exam_list:
        if is_it_exam.__contains__("."):
            extension=is_it_exam.split(sep=".")[1]
            exams_dict[extension]=exam_folder_path + '/' + is_it_exam

        else:
            exams_dict[is_it_exam]= [(exam_folder_path + '/' + is_it_exam + '/') + s for s in os.listdir(path=exam_folder_path + '/' + is_it_exam)] #appending exam_folder path to every element in list of element in folder

    df=pd.DataFrame(data=exams_dict)
    return df

