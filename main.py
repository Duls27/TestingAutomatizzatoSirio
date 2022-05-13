import file_manager, test_manager
import os
from selenium import webdriver

#get data from excell file
path_desktop= os.path.normpath(os.path.expanduser("~/Desktop"))

try:
    df_config, df_users, df_carica_esame=file_manager.get_excel_info(path_file_login= path_desktop+"/SirioUI/bootstrap.xlsx")
except IOError:
    print("Reading Excel file ERROR !")

df_config["path_folder_screenshot"]=path_desktop + "/SirioUI/Screenshot/"
if not os.path.exists(df_config.iloc[0]["path_folder_screenshot"]):
    os.mkdir(df_config.iloc[0]["path_folder_screenshot"])

try:
    df_exams_path= file_manager.get_exam_info(path_desktop+"/SirioUI/EsamiTest")
except IOError:
    print("Reading files for test ERROR !")

try:
    #chrome_options = webdriver.ChromeOptions()
    #chrome_options.add_argument("--incognito")
    #private_driver = webdriver.Chrome(df_config.iloc[0]['path_chrome_driver'], options=chrome_options) #opening WebBrowser
    driver=webdriver.Chrome(df_config.iloc[0]['path_chrome_driver'])

except IOError:
    print("Error opening Chrome, check your ChromeWebDriver installation. For package see https://chromedriver.chromium.org/")


driver.get(df_config.iloc[0]['link_piattaforma']) #Open Page to platform
test_manager.oper_test(driver, df_users, df_exams_path, df_carica_esame,df_config)
