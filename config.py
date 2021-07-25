import yaml

with open('config.yaml', 'r') as stream:
    configs = yaml.safe_load(stream)

api_key = configs['API_KEY']
api_secret = configs['API_SECRET']
