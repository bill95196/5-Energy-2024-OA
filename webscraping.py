from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from datetime import datetime
import time

def main():

    # Define the date range for data collection
    data_from = '03/16/2024'
    today_date = datetime.now()
    data_to = today_date.strftime('%m/%d/%Y')

    url = 'http://oasis.caiso.com/mrioasis/default.do?tiny=izbRTw'
    cb = webdriver.Chrome()

    cb.get(url)
    time.sleep(2)  # Wait for the page to load

    # Navigate to "SYSTEM DEMAND" 
    sys_page = cb.find_element(by=By.XPATH, value='.//*[@data-copy-text="SYSTEM DEMAND"]')
    ActionChains(cb).move_to_element(sys_page).perform()
    time.sleep(0.5)

    # Select "Wind and Solar Forecast" 
    wind_page = cb.find_element(by=By.XPATH, value='.//*[@data-copy-text="Wind and Solar Forecast"]')
    ActionChains(cb).move_to_element(wind_page).perform()
    wind_page.click()
    time.sleep(1)


    data_to_input = cb.find_element(by=By.XPATH, value='//input[contains(@onchange, "PFC_date_to")]')
    ActionChains(cb).move_to_element(data_to_input).perform()
    data_to_input.send_keys(Keys.END + Keys.BACK_SPACE * 10)
    time.sleep(0.5)
    data_to_input.send_keys(data_to)
    time.sleep(0.5)

    data_from_input = cb.find_element(by=By.XPATH, value='//input[contains(@onchange, "PFC_date_from")]')
    ActionChains(cb).move_to_element(data_from_input).perform()
    data_from_input.send_keys(Keys.END + Keys.BACK_SPACE * 10)
    time.sleep(0.5)
    data_from_input.send_keys(data_from)
    time.sleep(0.5)


    # Click the "Apply" button to submit the date range and retrieve data
    apply_button =  cb.find_element(by=By.XPATH, value='//button[@title="Apply"]')
    ActionChains(cb).move_to_element(apply_button).perform()
    apply_button.click()
    time.sleep(22)

    # Click the "Download CSV" button to download the data
    download_button =  cb.find_element(by=By.XPATH, value='//button[@title="Download CSV"]')
    ActionChains(cb).move_to_element(download_button).perform()
    download_button.click()
    time.sleep(30)
    cb.quit()

if __name__ == '__main__':
    main()
    