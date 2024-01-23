from tools import *
import pickle

bot = initbot()
meldungen = initsoup("https://www.erfurter-bahn.de/")

for i in meldungen:
    print(len(tweetify(i.text)))
    print(tweetify(i.text))
    print()

    bot.send_tweet(tweetify(i.text))

pickle.dump(bot.bot.get_cookies(), open("cookies.pkl", "wb"))
bot.touch_grass()