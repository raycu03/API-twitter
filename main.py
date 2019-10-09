from flask import Flask, render_template
from flask import request
from flask_bootstrap import Bootstrap
import tweepy

consumer_key=""
consumer_secret=""
access_token=""
access_token_secret=""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)
app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/hola',methods=['GET', 'POST'])	
def hola():
  respuesta1 = request.args.get('respuesta1')
  user = api.get_user(id=respuesta1)

  public_tweets = api.user_timeline(id=respuesta1)
  return render_template('index.html', m = request.method, r = user.screen_name,f=user.followers_count,t=public_tweets)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")