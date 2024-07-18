import json
with open('config.json') as f:
    config = json.load(f)
client_id = config['client_id']
client_secret = config['client_secret']
