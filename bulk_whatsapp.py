from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from urllib import parse
from selenium.webdriver.chrome.options import Options
import os
import sys

try:
    import autoit
except:
    pass
import time

numbers_to_skip = ["9900705226","8746826014","7299665542","9331966979","9176673232","9989801801","8884413788","9535644355","9933586005","7842464290","9535644355","9538225954","9902223733","9804856807","8861513233"]

# chrome_options = Options()
# chrome_options.add_argument("user-data-dir=" + os.path.dirname(sys.argv[0]))
# driver = webdriver.Chrome(chrome_options=chrome_options)
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
    message = (message + "\n#sleeptight \n\n"
                + "Click on link in the previous message to place your order.")

    try:
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
        # for ch in order_link:
        #     if ch == "\n":
        #         ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
        #     else:
        #         input_box.send_keys(ch)
        time.sleep(3)
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
            modified_link = link.split('=')[:-1]
            modified_link = (',').join(modified_link)
            if any(number in modified_link for number in numbers_to_skip):
                continue
            browser.get(modified_link)
            element = wait.until(EC.presence_of_element_located((By.ID, 'action-button')))
            element.click()
            print("Sending message to", link)
            query_params = dict(parse.parse_qsl(parse.urlsplit(link).query))
            message = query_params['text']
            # order_link = query_params['order_link'] + "&mobile_number?" + query_params['mobile_number'] + "&time_slot=" + query_params["time_slot"].replace(" ", "%20")
            # make sure text message is last part of link
            # send_unsaved_contact_message(message, order_link)
            send_unsaved_contact_message(message)
            time.sleep(2)

if __name__ == "__main__":

    print("Web Page Open")

    # Append more contact as input to send messages
    # input_contacts()
    # Enter the message you want to send
    # input_message()

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()
    time.sleep(30)
    # if(isSchedule=="yes"):
    #     schedule.every().day.at(jobtime).do(sender)
    # else:
    #     sender()

    send_using_csv()

    # First time message sending Task Complete
    print("Task Completed")

    browser.quit()
