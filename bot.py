from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
drive = webdriver.Chrome('./chromedriver')
drive.get('https://fs4.formsite.com/JNepAX/zhf6iqbfsn/index.html')
drive.find_element_by_id('RESULT_TextField-2').send_keys('Maya')
drive.find_element_by_id('RESULT_TextField-3').send_keys('Lekhi')
time.sleep(2)
drive.find_element_by_id('FSsubmit').click()
time.sleep(2)
symptons = Select(drive.find_element_by_id('RESULT_RadioButton-6'))
symptons.select_by_visible_text('No')
household = Select(drive.find_element_by_id('RESULT_RadioButton-7'))
household.select_by_visible_text('No')
lastDays = Select(drive.find_element_by_id('RESULT_RadioButton-8'))
lastDays.select_by_visible_text('No')
travel = Select(drive.find_element_by_id('RESULT_RadioButton-9'))
travel.select_by_visible_text('No')
child = Select(drive.find_element_by_id('RESULT_RadioButton-10'))
child.select_by_visible_text('No')
time.sleep(2)
# submit form button
# drive.find_element_by_id('FSsubmit').click()
drive.quit()