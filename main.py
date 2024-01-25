from tools import *
import pickle, os

bot = initbot()
meldungen = initsoup("https://www.erfurter-bahn.de/")
already_send_tweets = []

if(os.path.isfile("twets.pkl")):
    with open('twets.pkl', 'rb') as handle:
        already_send_tweets = pickle.load(handle)

for i in meldungen:
    meldung = tweetify(i.text)

    if(meldung not in already_send_tweets):
        print(len(meldung))
        print(meldung)
        already_send_tweets.append(meldung)
        print()

    else:
        print("schon gesendet!")


    bot.send_tweet(tweetify(i.text))

set(already_send_tweets)
with open('twets.pkl', 'wb') as handle:
    pickle.dump(already_send_tweets, handle, )


pickle.dump(bot.bot.get_cookies(), open("cookies.pkl", "wb"))
bot.touch_grass()
