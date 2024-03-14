from poe_api_wrapper import PoeApi


with open('know_base/job_offers.txt', 'r', encoding='utf-8') as f:
    data = f.read()

client = PoeApi("CmpguqkTtuqLZh5w1XeRGw%3D%3D")

bot = "5ademni_bot"
message = "say hi!"


client.edit_knowledge(knowledgeSourceId=1428020, title='Job offers',
                      content=data)


print(client.get_available_knowledge(botName=bot))
