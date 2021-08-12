'''
from selenium import webdriver
import time

driver = webdriver.Google()

driver.get("https://unisysmt.service-now.com/nav_to.do?uri=%2Fsys_report_template.do%3Fjvar_report_id%3Dced8f78b1b06e8102426c5d96e4bcb39%26jvar_selected_tab%3DmyReports%26jvar_list_order_by%3D%26jvar_list_sort_direction%3D%26sysparm_reportquery%3Dz%26jvar_search_created_by%3D%26jvar_search_table%3D%26jvar_search_report_sys_id%3D%26jvar_report_home_query%3D")
while True:
    time.sleep(20)
    driver.refresh()
    driver.quit()
'''

