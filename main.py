import tools as tb
import secret, os
import pickle

bot = tb.Twitterbot()

if(os.path.isfile('cookies.pkl')):
    bot.bot.get("https://twitter.com")
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        bot.bot.add_cookie(cookie)
else:
    credentials = secret.get_credentials()
    bot.logon(credentials['email'], credentials['password'])
    pickle.dump(bot.bot.get_cookies(), open("cookies.pkl", "wb"))

bot.send_tweet()

pickle.dump(bot.bot.get_cookies(), open("cookies.pkl", "wb"))
bot.touch_grass()

