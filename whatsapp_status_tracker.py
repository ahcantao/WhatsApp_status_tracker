#!/usr/bin/env python3
#pip install -U selenium
from time import sleep
from selenium import webdriver

def connect(): 
    logged_in      = False
    counting_tries = 0
    max_tries      = 5
    browser        = webdriver.Chrome()
    print('Open WhatsApp on your phone and scan the QR code on the new chorme window.')
    browser.get('https://web.whatsapp.com')
    while logged_in is False:
        sleep(5)
        try:
            info = browser.find_element_by_class_name('Qk8nZ')
            if info.text == 'Keep your phone connected':
                logged_in = True
                print('You\'re on!')
                return True, browser
        except:
            #exit timing
            counting_tries += 1
            if counting_tries == 4:
                break
            else:
                print('be fast to connect: Try '+str(counting_tries)+' of '+str(max_tries))
            pass
    return True, browser

def setup_contact_window(browser, stalked_contact_name):
    search = browser.find_element_by_class_name('_2zCfw.copyable-text.selectable-text')
    #search.text
    search.clear()
    search.send_keys(stalked_contact_name)
    #browser.save_screenshot('screenshot.png')
    sleep(3)
    contacts = browser.find_elements_by_class_name('X7YrQ')  #_1H6CJ
    for contact in contacts:
        if stalked_contact_name+"\n" in contact.text:
            contact.click()
            search.clear()
            print('Do NOT use the WhatsApp web while stalking.\n')
            print('Do NOT click/open other chats while stalking.\n')
            print('Use your phone to do so.\n')
            return True
    if not contacts:
        print('Contact not found!! Check if \''+stalked_contact_name+'\' is written exactely the same as in your agenda.')
        return False

def stalk(browser, stalked_contact_name, informed_contact_name,check_frequency_sec,message_to_be_sent):
    print('You\'re already stalking!')
    status = ''
    while status != 'online':
        try: 
            status = browser.find_element_by_class_name('_315-i._F7Vk').text #_315-i _F7Vk
        except:
            pass
        sleep(check_frequency_sec)
    search = browser.find_element_by_class_name('_2zCfw.copyable-text.selectable-text')
    search.send_keys(informed_contact_name)
    sleep(5)
    chats = browser.find_elements_by_class_name('X7YrQ')
    for chat in chats:
        #name = chat.get_attribute('title')
        if informed_contact_name+'\n' in chat.text:
            chat.click()
            break
    send = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    send.send_keys(message_to_be_sent)
    sendbutton = browser.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    
if __name__== "__main__":
    stalked_contact_name  = '' #insert the name exactely like in your agenda
    informed_contact_name = '' #insert the name exactely like in your agenda
    check_frequency_sec   = 6  #check the status every _ seconds
    message_to_be_sent    = stalked_contact_name + ' is online'

    connected, browser    = connect()
    while True:
        sleep(5)
        setup = setup_contact_window(browser, stalked_contact_name)
        sleep(5)
        stalk(browser, stalked_contact_name, informed_contact_name,check_frequency_sec, message_to_be_sent)