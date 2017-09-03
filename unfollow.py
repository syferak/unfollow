from selenium import webdriver
import time
#open firefox
browser = webdriver.Firefox() 
#enter site url here that is instagram
browser.get('https://www.instagram.com/accounts/login/') 
#wait till it loads
browser.implicitly_wait(10) 
#find username and password textbox
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
 #Enter your username here
username.send_keys('enter username')
 #Enter your password here
password.send_keys('enter password')
login = browser.find_element_by_tag_name('button')
login.submit()
browser.implicitly_wait(10)
#navigate to profile
profile = browser.find_element_by_link_text('Profile')
profile.click()
browser.implicitly_wait(10)
#find the following tab  using xpath
following = browser.find_element_by_xpath("//a[@href='/username/following/']")
following.click()
browser.implicitly_wait(20)
#run a loop that clicks unfollow button and simultaneously scrolls
for i in range(1,100):
    browser.execute_script('var b = document.getElementsByClassName("_4gt3b"); b[0].scrollTop += 100;')
    unfollow = browser.find_element_by_xpath('//button[@class="_ah57t _6y2ah _i46jh _rmr7s"]').click()
    time.sleep(2)




