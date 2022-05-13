import support_functions, test_list
import pandas as pd
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def oper_test (chrdriver: webdriver.Chrome, df_users: pd.DataFrame, df_exams_path: pd.DataFrame, df_carica_esame: pd.DataFrame, df_config: pd.DataFrame):

    chrdriver=support_functions.get_access(chrdriver, df_users.iloc[0]['oper'], df_users.iloc[1]['oper'])
    chrdriver.find_element_by_link_text("Carica").click()
    chrdriver.find_element_by_link_text("Esame").click()

   # for n_rows in df_carica_esame.index:
    #    print(n_rows, type(n_rows))
    test_list.test_send_exam(chrdriver, df_carica_esame,0, df_exams_path, df_config)

    chrdriver.find_element_by_link_text("Carica").click()
    chrdriver.find_element_by_link_text("Esame").click()



