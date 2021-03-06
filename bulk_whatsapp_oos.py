import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from urllib import parse

try:
    import autoit
except:
    pass
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
Link = "https://web.whatsapp.com/"

def whatsapp_login():
    global wait,browser,Link
    # chromedriver = "/path/to/chromedriver/folder"
    browser.get(Link)
    # browser.maximize_window()
    print("QR scanned")


def send_unsaved_contact_message(message):
    try:
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
        time.sleep(4)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")
    except NoSuchElementException:
        print("Failed to send message")
        return

def send_using_csv():
    text_file = open("./test_data", "r")
    links = text_file.read().split('\n')
    if len(links)>0:
        for link in links:
            # driver  = webdriver.Chrome()
            message = link.split('=')[-1]
            modified_link = link.split('=')[0]
            # modified_link = (',').join(modified_link)
            browser.get(modified_link)
            element = wait.until(EC.presence_of_element_located((By.ID, 'action-button')))
            element.click()
            print("Sending message to", link)
            query_params = dict(parse.parse_qsl(parse.urlsplit(link).query))
            message = query_params['text']
            # make sure text message is last part of link
            send_unsaved_contact_message(message)
            time.sleep(4)

if __name__ == "__main__":

    print("Web Page Open")

    # Append more contact as input to send messages
    # input_contacts()
    # Enter the message you want to send
    # input_message()

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()
    time.sleep(10)
    # if(isSchedule=="yes"):
    #     schedule.every().day.at(jobtime).do(sender)
    # else:
    #     sender()

    send_using_csv()

    # First time message sending Task Complete
    print("Task Completed")

    browser.quit()
