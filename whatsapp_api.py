from selenium import webdriver
import time

driver = webdriver.Chrome("c:\\data\\chromedriver.exe")
driver.maximize_window()
driver.get('https://web.whatsapp.com')
driver.maximize_window()
lis = []




def login_status():
    try:
        driver.finde_element_by_class_name('landing-main')
        return False
    except:
        return True


def notification():
    try:
        driver.find_element_by_class_name('_1pJ9J')
        return True
    except:
        return False


class Conversation:
    type = 'Whatsapp'
    id = ''
    incident_type = ''
    active_state = True
    prompt = False
    topic_mem = ''
    replied = False
    sentiment = ''


    def send_message(self, x):
        chat_list = driver.find_elements_by_class_name('_3m_Xw')
        for w in chat_list:
            if w.text.split('\n')[0] == self.id:
                w.click()
                text_box = driver.find_element_by_css_selector("div[title='Type a message']")
                text_box.send_keys(x)
                driver.find_element_by_css_selector("button[class='_4sWnG']").click()
                menu = driver.find_elements_by_class_name('_26lC3')[4]
                menu.click()
                close = driver.find_element_by_css_selector('div[aria-label="Close chat"]')
                close.click()



def scan():
    lis.clear()
    if login_status() is True and notification() is True:

        notif = driver.find_elements_by_class_name('_1pJ9J')
        for x in notif:
            x.click()
            new = Conversation()
            new.id = driver.find_element_by_class_name('_21nHd').text
            new.latest_message = driver.find_elements_by_class_name('copyable-text')[-2].text
            lis.append(new)
            menu = driver.find_elements_by_class_name('_26lC3')[4]
            menu.click()
            close = driver.find_element_by_css_selector('div[aria-label="Close chat"]')
            time.sleep(0.3)
            close.click()
    return lis









