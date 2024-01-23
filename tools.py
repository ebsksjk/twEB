
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time, os
 
class Twitterbot:
 
    def __init__(self):
        options = webdriver.FirefoxOptions() 
        options.headless = True
        self.bot = webdriver.Firefox(options=options) 
 
    def logon(self, email, password):
        bot = self.bot

        self.email = email
        self.password = password
        bot.get('https://twitter.com/login')
        time.sleep(1)
 
        email = bot.find_element('xpath', '//input[@autocomplete="username"]')
        email.send_keys(self.email)
        email.send_keys(Keys.RETURN)
        time.sleep(2)

        password = bot.find_element('xpath', '//input[@autocomplete="current-password"]')
        password.send_keys(self.password)
        password.send_keys(Keys.RETURN)
        time.sleep(2)

    def send_tweet(self):
        bot = self.bot

        bot.get("https://twitter.com/compose/tweet")

        time.sleep(1)

        composebox = bot.switch_to.active_element
        composebox.send_keys('uwu')

        post_button = bot.find_element('xpath', '//div[@data-testid="tweetButton"]')
        post_button.click()

        time.sleep(1)

    def touch_grass(self):
        self.bot.quit()
