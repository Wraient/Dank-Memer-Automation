import requests
import time
import threading

url = "https://discord.com/api/v9/interactions" #api

channel = "963481563633434684" #channel
guild_id = "961594529927020594" #idk it works for everyone
session_id = "e643b430d26b058c8b504d13ebe29c63" #anything just a non empty string
application_id = "270904126974590976" #dank memer

key = "" # your discord authorization key

fish = ["1022917002878259287", "1011560371078832206", "fish"] # version, id, name
hunt = ["1022917002932793367", "1011560371171102760", "hunt"] # version, id, name
dig = ["1022917002878259285", "1011560371078832204", "dig"] # version, id, name
beg = ["1022917002878259280", "1011560371041095699", "beg"] # version, id, name


def send_cmd(the_list, key):
    json = {
        "type": 2, 
        "application_id": application_id, 
        "guild_id": guild_id, 
        "channel_id": channel, 
        "session_id": session_id, 
        "data": {
            "version": f"{the_list[0]}", 
            "id": f"{the_list[1]}", 
            "name": f"{the_list[2]}", 
            "application_command": {
                "id": f"{the_list[1]}", 
            }, 
        }
    }
    headers = {
    "Authorization": key
    }
    r = requests.post(url, headers=headers, json=json)
    if r.status_code==204:
        print("Command send!")
    else:
        print("Command not send, error code : ", r.status_code, "sucks to be you lol")

command = [dig, hunt, fish]
while True: 
    x = threading.Thread(target = send_cmd, args = (dig,sudh,))
    x.start()
    send_cmd(dig)
    send_cmd(hunt)
    send_cmd(fish)
    time.sleep(10)
    send_cmd(beg)
    time.sleep(35)