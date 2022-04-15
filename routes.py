import flask
import dataclasses
import os
import pytwitter  # upm package(python-twitter-v2)



def get_twitter_api():# -> pytwitter.Api:
    print(dir(pytwitter))
    return pytwitter.Api(
      bearer_token=os.environ["TWITTER_BEARER_TOKEN"])


@dataclasses.dataclass
class Filter:
    name: str
    text: str


@dataclasses.dataclass
class User:
    screen_name: str
    user_name: str
    user_id: str


def _get_filters():
    return {
        'content_filters': [
            Filter(name='eth_address', text='Reply contains Eth address'),
            Filter(name='only_image',
                   text='Reply contains no text other than an image.'),
            Filter(name='only_quote',
                   text='Reply contains no text other than a quote tweet.')
        ],
        'account_filters': [
            Filter(name='default_account',
                   text='Username matches default account format.')
        ]
    }


def _get_most_recent_tweet(api, user: User):
    tweets = api.get_timelines(
      user_id=user.user_id,
      # We can't set a value smaller than 5.
      max_results=5,
      exclude=['retweets', 'replies']).data
    # TODO(finbarr): Figure out if this is the most recent or
    # not.
    return tweets[0]

#def _get_replies(tweet):


def _get_user(name: str, api) -> User:
    user = api.get_users(usernames=[name]).data[0]
    print(f'{user}')
    return User(screen_name=user.name,
                user_name=user.username,
                user_id=user.id)


def add_routes_to_app(app: flask.Flask, config):
    api = get_twitter_api()
    user = _get_user(config['name'], api)

    @app.route('/')
    def hello_world():
        most_recent_tweet = _get_most_recent_tweet(api, user)
        return flask.render_template('config.html',
                                     filters=_get_filters(),
                                     tweet=most_recent_tweet,
                                     user=user)

    @app.route('/about')
    def about():
        return flask.render_template('about.html')
