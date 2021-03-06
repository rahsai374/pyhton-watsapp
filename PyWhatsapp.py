import schedule
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
try:
    import autoit
except:
    pass
import time
import datetime
import os

browser = None
Contact = None
message = None
Link = "https://web.whatsapp.com/"
wait = None
choice = None
docChoice = None
doc_filename = None
unsaved_Contacts = None

def input_contacts():
    global Contact,unsaved_Contacts
    # List of Contacts
    Contact = []
    unsaved_Contacts = []
    while True:
        inp = str(input("Enter unsaved contact numbers with country code(interger):\n\nValid input: 91943xxxxx12\nInvalid input: +91943xxxxx12\n\n"))
        print (inp)
        inp = inp.split(',')
        unsaved_Contacts = unsaved_Contacts + inp
        break

    if len(Contact) != 0:
        print("\nSaved contacts entered list->",Contact)
    if len(unsaved_Contacts) != 0:
        print("Unsaved numbers entered list->",unsaved_Contacts)
    input("\nPress ENTER to continue...")

def input_message():
    global message
    # Enter your Good Morning Msg
    print()
    print("Enter the message and use the symbol '~' to end the message:\nFor example: Hi, this is a test message~\n\nYour message: ")
    message = []
    temp = ""
    done = False

    while not done:
      temp = input()
      if len(temp)!=0 and temp[-1] == "~":
        done = True
        message.append(temp[:-1])
      else:
        message.append(temp)
    message = "\n".join(message)
    print()
    print(message)

def whatsapp_login():
    global wait,browser,Link
    # chromedriver = "/path/to/chromedriver/folder"
    browser = webdriver.Chrome()
    wait = WebDriverWait(browser, 600)
    browser.get(Link)
    # browser.maximize_window()
    print("QR scanned")


def send_unsaved_contact_message():
    global message
    try:
        time.sleep(7)
        input_box = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        for ch in message:
            if ch == "\n":
                ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.BACKSPACE).perform()
            else:
                input_box.send_keys(ch)
        input_box.send_keys(Keys.ENTER)
        print("Message sent successfuly")
    except NoSuchElementException:
        print("Failed to send message")
        return

def sender():
    global Contact,choice, docChoice, unsaved_Contacts
    for i in Contact:
        send_message(i)
        print("Message sent to ",i)
    time.sleep(5)
    if len(unsaved_Contacts)>0:
        for i in unsaved_Contacts:
            link = "https://wa.me/"+i
            #driver  = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="action-button"]').click()
            time.sleep(4)
            print("Sending message to", i)
            send_unsaved_contact_message()
            time.sleep(7)

def send_using_csv():
    text_file = open("./test_data", "r")
    links = text_file.read().split('\n')
    if len(links)>0:
        for link in links:
            # driver  = webdriver.Chrome()
            browser.get(link)
            time.sleep(1)
            browser.find_element_by_xpath('//*[@id="action-button"]').click()
            time.sleep(4)
            print("Sending message to", link)
            send_unsaved_contact_message()
            time.sleep(7)

if __name__ == "__main__":

    print("Web Page Open")

    # Append more contact as input to send messages
    # input_contacts()
    # Enter the message you want to send
    # input_message()

    # Let us login and Scan
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB")
    whatsapp_login()

    # if(isSchedule=="yes"):
    #     schedule.every().day.at(jobtime).do(sender)
    # else:
    #     sender()

    send_using_csv()

    # First time message sending Task Complete
    print("Task Completed")

    # browser.quit()