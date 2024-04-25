from poe_api_wrapper import PoeApi


with open('harvest/know_base/txt/tanit_jobs.txt', 'r', encoding='utf-8') as f:
    data = f.read()

tokens = {
    'b': 'YVNKZKBGPbWgKMAW1Xn17g%3D%3D',
    'lat': 'qf2oLEe0K1aw4G2NxfvwsaN9b9no9%2BsjrhlXsDWqHA%3D%3D'
}

client = PoeApi(cookie=tokens)

bot = "5ademni_bot"
message = "say hi!"


client.edit_knowledge(knowledgeSourceId=1428020, title='Job offers',
                      content=data)
