
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time, os
from bs4 import BeautifulSoup
import urllib.request
import pickle
import secret

 
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

    def send_tweet(self, text):
        bot = self.bot

        bot.get("https://twitter.com/compose/tweet")

        time.sleep(1)

        composebox = bot.switch_to.active_element
        composebox.send_keys(text)

        post_button = bot.find_element('xpath', '//div[@data-testid="tweetButton"]')
        post_button.click()

        time.sleep(1)

    def touch_grass(self):
        self.bot.quit()


def initbot():
    bot = Twitterbot()


    if(os.path.isfile('cookies.pkl')):
        bot.bot.get("https://twitter.com")
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            bot.bot.add_cookie(cookie)
        
        bot.bot.get("https://twitter.com")
    else:
        credentials = secret.get_credentials()
        bot.logon(credentials['email'], credentials['password'])
        pickle.dump(bot.bot.get_cookies(), open("cookies.pkl", "wb"))

    return bot

def initsoup(text):
    f = urllib.request.urlopen(text)
    content = f.read()

    meldungen = []

    soup = BeautifulSoup(content, 'html.parser')

    search_term = 'stoerungsmeldungen'
    stoerungsdiv = soup.select_one(f'div[class*="{search_term}"]')

    if stoerungsdiv:
        messages = stoerungsdiv.find_all('div', class_="message")
        for msg in messages:
            message = msg.select_one(".text")
            meldungen.append(message)
    else:
        print(":(")

    return meldungen

def tweetify(text):
    replacers = {
        'Gera': '#Gera',
        'Weimar': '#Weimar',
        'Gewerkschaft der Lokführer (GDL)': '#GDL',
        'Streik': '#Streik',
        "Sehr geehrte Fahrgäste, ": '',
        "Ihre Erfurter Bahn": '',
        "Montag": "Mo",
        "Dienstag" : "Di",
        "Mittwoch" : "Mi",
        "Donnerstag" : "Do",
        "Freitag" : "Fr",
        "Samstag" : "Sa",
        "Sonntag" : "So",
        ".2024": '',
        " Uhr": '',
        "Erfurter Bahn": 'EB',
        "ihre Mitglieder ": '',
        "Dennoch kann es ": 'Es kann ',
        "Wir bitten um Ihr Verständnis.": "Wir bitten um Verständnis.",
        "vereinzelten ": ''
        }

    returner = text

    for key, value in replacers.items():
        returner = returner.replace(key, value)
        returner = returner[0].upper() + returner[1:]

    return returner