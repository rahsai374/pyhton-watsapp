from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from urllib import parse
from random import randint
import random

from datetime import datetime
startTime = datetime.now()

try:
    import autoit
except:
    pass
import time

browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
Link = "https://web.whatsapp.com/"


freinds_number = ['918051053816', '919986017572', '919901683322', '917259238014', '917506134639', '917899740690', '919535507833']
global TOTAL_MESSAGE_SENT
TOTAL_MESSAGE_SENT = 0

print('TOTAL_MESSAGE_SENT', TOTAL_MESSAGE_SENT)

def whatsapp_login():
    global wait,browser,Link
    # chromedriver = "/path/to/chromedriver/folder"
    browser.get(Link)
    # browser.maximize_window()
    print("QR scanned")


def send_unsaved_contact_message(message):
    try:
        time.sleep(randint(1,2))
        input_box = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')))
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
        input_box.send_keys(Keys.ENTER)
        time.sleep(randint(1,2))
        print("Message sent successfuly")
    except:
        print("Failed to send message")
        return

def send_using_csv():
    text_file = open("./test_data", "r")
    links = text_file.read().split('\n')
    if len(links)>0:
        for link in links:
            # driver  = webdriver.Chrome()
            # message = link.split('=')[-1]
            message = """ *Hey! I am Droppt*, 
The most convenient and affordable Breakfast Delivery Service in town. 

We have partnered with top restaurants such as *Chai Point, Kota Kachori, Madurai Idli Shop, Vasudev Adigas* and more to sort your breakfast. And yeah, it is available at unbeatable price. *Starting just @ Rs. 49*.
 
Check us out now : *https://www.droppt.co*

Pls: Send us *No* if you are not interested
            """
            # modified_link = link.split('=')[0]
            # modified_link = (',').join(modified_link)
            time.sleep(randint(3,5))
            browser.get(link)
            # element = wait.until(EC.presence_of_element_located((By.ID, 'action-button')))
            # element.click()
            print("Sending message to", link)
            # query_params = dict(parse.parse_qsl(parse.urlsplit(link).query))
            # message = query_params['text']
            # make sure text message is last part of link
            global TOTAL_MESSAGE_SENT
            TOTAL_MESSAGE_SENT = TOTAL_MESSAGE_SENT + 1
            time.sleep(randint(3,5))
            try:
                popup_element = browser.find_element_by_xpath('//div[@class="_3lLzD"]').click()
                continue
                print("Failed to send message")
            except NoSuchElementException:
                print("yo")
                
            element = wait.until(EC.presence_of_element_located((By.ID, 'action-button')))
            element.click()
            
            send_unsaved_contact_message(message)
            if(TOTAL_MESSAGE_SENT%20==0):
                freinds_message = "Hey Dude I am droppt how are you"
                random.shuffle(freinds_number)
                for number in freinds_number[0:2]:
                    update_link = 'https://wa.me/{0}?text='.format(number)
                    browser.get(update_link)
                    time.sleep(1)
                    element = wait.until(EC.presence_of_element_located((By.ID, 'action-button')))
                    element.click()
                    send_unsaved_contact_message(freinds_message)
                    time.sleep(randint(3,5))
            time.sleep(randint(2,4))

if __name__ == "__main__":

    print("Web Page Open")

    # Append more contact as input to send messages
    # input_contacts()
    # Enter the message you want to send
    # input_message()

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()
    time.sleep(25)
    # if(isSchedule=="yes"):
    #     schedule.every().day.at(jobtime).do(sender)
    # else:
    #     sender()

    send_using_csv()
    print('TOTAL_MESSAGE_SENT', TOTAL_MESSAGE_SENT)    
    # First time message sending Task Complete
    print("Task Completed")

    print("Total time taken", datetime.now() - startTime)


    browser.quit()
