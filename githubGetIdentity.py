import requests

# Replace with your own values
client_id = '64cb5c3fd396c9d10318'
redirect_uri = 'http://localhost'
login = 'shared1s'
scope = 'repo'
state = 'your-unguessable-random-string'
allow_signup = 'true'  # or 'false'

# Set up the API request parameters
params = {
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'login': login,
    'scope': scope,
    'state': state,
    
    'allow_signup': allow_signup,
}

# Make the API request to request a user's GitHub identity
response = requests.get('https://github.com/login/oauth/authorize', params=params)

    