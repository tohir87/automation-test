import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import time


fxProfile = webdriver.FirefoxProfile();

fxProfile.set_preference("browser.download.folderList", 2);
fxProfile.set_preference("browser.download.manager.showWhenStarting", False);
fxProfile.set_preference("browser.download.dir", os.getcwd() + "/downloads/");
fxProfile.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv/pdf/*/*.*");

browser = webdriver.Firefox(fxProfile)

# Variables
visa_reference_number = '1209500020173'
applicant_dob = '18 Feb 2000'
document_number = 'AK0171465'
country = 'KEN'

#go to immigration website
browser.get("https://online.immi.gov.au/evo/firstParty?actionType=query")

# wait for it to load
time.sleep(10)

document_type = Select(browser.find_element_by_id('_2a0a2a0a2a0a1a_input'))

# select document type of passport
document_type.select_by_value('01')

#wait for 3 secs
time.sleep(4)

reference_type = Select(browser.find_element_by_id('_2a0a2a0a2c1a0b_input'))
# select Visa grant number
reference_type.select_by_value('4')

time.sleep(3)

# key in the visa grant number
browser.find_element_by_id('_2a0a2a0a2c1b1b0_input').send_keys(visa_reference_number)
print('Visa Reference number:' + visa_reference_number)

time.sleep(2)

# key in the date of birth
browser.find_element_by_id('_2a0a2a0a2e0a1a_input').send_keys(applicant_dob)
print('Date of birth:' + applicant_dob)

time.sleep(2)

# passport number
browser.find_element_by_id('_2a0a2a0a2e0b1a_input').send_keys(document_number)
print('Passport number:' + document_number)

time.sleep(2)

# country
Select(browser.find_element_by_id('_2a0a2a0a2e0c1a_input')).select_by_value(country)
print('Set country:' + country)

time.sleep(2)

# agree to terms and conditions
browser.find_element_by_id('_2a0a2a0a2f1b0_input').click()
print('Terms and conditions')

time.sleep(2)

browser.find_element_by_id('_2a0a2a0a3b0a').click()

time.sleep(3)

# take screenshots of page
print('Taking screenshot')
browser.get_screenshot_as_file('screenshots/vivo_' + visa_reference_number +  '.png')

# download pdf
browser.find_element_by_id('_2a2a2a0a2a1a0a').click()
print('Downloading PDF')

time.sleep(5)

browser.quit()
