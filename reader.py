import json

messages = json.load(open("channel_messages.json", "r"))

last_messages = messages[:2]
json.dump(last_messages, open("last_messages.json", "w"))