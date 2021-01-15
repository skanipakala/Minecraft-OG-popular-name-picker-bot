## MINECRAFT NAME SNIPER VERSION 1.0

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from pyvirtualdisplay import Display


driver = webdriver.Chrome('C:/chromedriver.exe')
print('Driver successfully imported...Starting Program')



display = Display(visible=1, size=(1600, 902))
display.start()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--profile-directory=Default')
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-plugins-discovery");
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.delete_all_cookies()
driver.set_window_size(800,800)
driver.set_window_position(0,0)

input('hello>>>>')
## Go to minecraft login page
driver.get('https://www.minecraft.net/en-us/login')
sleep(1.25)

login_button = driver.find_element_by_xpath('//*[@id="AccountNavMenu"]/a[1]')
login_button.click()
print('[!] Small Login Button Clicked')
sleep(2)
email_text_box =  driver.find_element_by_id('email')
email_text_box.send_keys('YOUR EMAIL')
sleep(3)
print('[!] email successfully sent')

pswd_text_box =  driver.find_element_by_id('password')
pswd_text_box.send_keys('[YOUR PASSWORD]')
sleep(3)
print('[!] password successfully sent')

green_login_button = driver.find_element_by_xpath('//*[@id="CoreAppsApp"]/main/div/div/div/div/div[1]/form/button')
green_login_button.click()
print('[!] Logged into minecraft account successfully')

print('-------------------------[ALERT]-------------------------')

#isReady = input('Type anything and press enter if you completed the Re-Captcha !!!')
#print('[!] Recapta Security Bypassed')


change_profile_name_button = driver.find_element_by_xpath('//button[@aria-label = "{}"]'.format('Change profile name'))
change_profile_name_button.click()
print('[!] Change profile button clicked')

sleep(1.5)

while(True):
    
    new_name_text_box =  driver.find_element_by_id('newName')
    print('got the new name textBox')

    driver.execute_script("arguments[0].setAttribute('aria-invalid','true')", new_name_text_box)
    print('edit success')

    new_name_text_box.click()
    print('yay clicked textbox for username')
    new_name_text_box.send_keys('COOL NAME')##< ---- Enter the NAME YOU WANT HERE
    print('[!] New USER NAME sent')

    verify_pswd_text_box = driver.find_element_by_xpath('//*[@id="newNamePassword"]')
    print('got the password verifier textbox')
    verify_pswd_text_box.send_keys('[YOUR PASSWORD')
    print('[!] Password verification sent')


    CHANGE_NAME_BUTTON = driver.find_element_by_xpath('//button[@data-testid = "{}"]'.format('ChangeNameButton'))
    print('[!] Change Name button FOUND!')

    driver.execute_script("arguments[0].setAttribute('class','btn btn-enabled')", CHANGE_NAME_BUTTON)
    print('[!] Change Name button ACTIVATED....ABOUT TO SPAM IT!!!')

    
    CHANGE_NAME_BUTTON.click()
    print('[+] button clicked')
    driver.refresh()
    sleep(0.25)
