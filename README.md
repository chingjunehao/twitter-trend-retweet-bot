# Twitter bot using Python & Tweepy to retweet/favorite/follow users
A Python-built with Tweepy bot to retweet/favorite specified keywords or keywords from trend in specified area. Handle multiple hashtags and keywords as well.

# Requirements
[Python3](https://www.python.org/) - Python version 3.6
[Tweepy](http://www.tweepy.org/) - Python library to access Twitter API

# Instruction
- Understand [Twitter's Rules on Automation](https://help.twitter.com/en/rules-and-policies/twitter-automation) to prevent getting banned by Twitter.
- Create a new Twitter [App](https://apps.twitter.com/app/new).
- Get consumer_key, consumer_secret, access_token and access_token_secret from the App.
- Replace your key, secret and token in the code.
- Replace the woeid for the location that you want to get the trends from. May get the woeid [here](https://codebeautify.org/jsonviewer/f83352)
- Or replace the specific keywords to retweet things you want to.
- The keywords = "machine learning%20OR%20%23computer science" will search for machine learning and #computer science.
- Run tweety.py to start retweeting/favoriting/following!

# Additional Information
- May consider hosting your code on a Raspberry Pi to run daily.
- Set schedule on [pythonanywhere](https://www.pythonanywhere.com) to make the code runs daily.
- Use sleep() to set time between each retweet so that you will not getting banned by Twitter.
