from poe_api_wrapper import PoeApi


tokens = {
    'b': 'YVNKZKBGPbWgKMAW1Xn17g%3D%3D',
    'lat': 'qf2oLEe0K1aw4G2NxfvwsaN9b9no9%2BsjrhlXsDWqHA%3D%3D'
}

client = PoeApi(cookie=tokens)

bot = "5ademni_bot"

print(client.get_available_knowledge(botName=bot, count=6))

# {'Job_List': [2064315]}
