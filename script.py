##############################################################
#       Whatsapp tool for message bomb  #
#       Author : Parth Panchal          #
#       DON'T COPY THIS CODE WITHOUT GIVE ME THE CREDITS 
###########################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import csv,os,time

driver = webdriver.Chrome('chromedriver.exe'
driver.get('https://web.whatsapp.com/')

def main():
    print("""
         _   _ _ _       _       _   _ _      _
        | | | (_) |_ ___| |__   | | | (_) ___| | _____ _ __
        | |_| | | __/ __| '_ \  | |_| | |/ __| |/ / _ \ '__|
        |  _  | | || (__| | | | |  _  | | (__|   <  __/ |
        |_| |_|_|\__\___|_| |_| |_| |_|_|\___|_|\_\___|_|   """)

    print("""
  =========================Whatsapp Message Sender===================""")

    print("""   Author : Parth Panchal""")

    print("""  ===================================================================

        
        1. Send to single user.
        
        2. Send to multiple user.

        3. Send to group.
        
        4. Exit.""")

    print("\n\t Please scan QR Code...")
    while True:
        try:
            choice = int(input("\n\tPlease Enter Your Choice [1-4] : "))
            break
        except:
            continue
    
    if(choice==1):   
        while True:
            try:
                number = input("\n\tEnter mobile number : ")
                break
            except:
                continue

        while True:
            try:
                msg = input("\n\tEnter Message : ")
                break
            except:
                continue

        while True:
            try:
                count = int(input("\n\tEnter number of counts : "))
                break
            except:
                continue

        search = driver.find_element_by_class_name('selectable-text')
        search.send_keys(number)
        search.send_keys(Keys.ENTER)

        msg_box = driver.find_element_by_class_name('_1Plpp')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()

    elif(choice==2):
        print("\n\tPlease add contact numbers in names.csv file...")
        while True:
            try:
                msg = input("\n\tEnter Message : ")
                break
            except:
                continue

        while True:
            try:
                count = int(input("\n\tEnter number of counts : "))
                break
            except:
                continue

        with open('names.csv','r') as names:
            reader = csv.reader(names)
            for row in reader:
                name = str(row[0])
                search = driver.find_element_by_class_name('_2S1VP')
                search.send_keys(name)
                search.send_keys(Keys.ENTER)
                msg_box = driver.find_element_by_class_name('_1Plpp')

                for i in range(count):
                    msg_box.send_keys(msg)
                    button = driver.find_element_by_class_name('_35EW6')
                    button.click()
        
    elif(choice==3):
        while True:
            try:
                number = input("\n\tEnter Group Name : ")
                break
            except:
                continue

        while True:
            try:
                msg = input("\n\tEnter Message : ")
                break
            except:
                continue

        while True:
            try:
                count = int(input("\n\tEnter number of counts : "))
                break
            except:
                continue        

        search = driver.find_element_by_class_name('selectable-text')
        search.send_keys(number)
        search.send_keys(Keys.ENTER)

        msg_box = driver.find_element_by_class_name('_1Plpp')

        for i in range(count):
            msg_box.send_keys(msg)
            button = driver.find_element_by_class_name('_35EW6')
            button.click()

    elif(choice==4):
        try:
            driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[3]').click()
            time.sleep(1)
            driver.find_element_by_xpath('//*[@title="Log out"]').click()
        except:
            pass
        print("\n\tBye Bye! :)")
        exit()

    else:
        print("\n\tYou Entered wronge choice..")

    restart = input("\n\tDO YOU WANT TO START AGAIN (y or n) : ")

    yes = ["yes","y","Y","YES"]
    if restart in yes:
        os.system('clear')
        main()
    else:
        print("\n\tBye Bye! :)")
        exit()
main()