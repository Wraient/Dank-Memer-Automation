import requests
import time 
import random

channel_id = "" # discord channel
key = "" # your discord autorization key

highlow_id = ["1022917002748235843", "1011560370911072258", "highlow"] # version, id, label
api_history = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=" # LIMIT NOT SET
api_interact = "https://discord.com/api/v9/interactions"


headers={"Authorization": key}

def send_cmd(the_list):
    json = {
        "type": 2, 
        "application_id": "270904126974590976", 
        "guild_id": "961594529927020594", 
        "channel_id": channel_id, 
        "session_id": "d66b76e1cd6b9ab1488b9bed89c4f8c8", 
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
    r = requests.post(api_interact, headers=headers, json=json)
    if r.status_code==204:
        print("Command send!")
    else:
        print("Command not send, error code :", r.status_code, "sucks to be you lol")

def click_json(custom_id, message_id, channel_id):
    sendThis = {
    "application_id":"270904126974590976",
    "channel_id":channel_id,
    "data":{
        "component_type": 2, 
        "custom_id": custom_id
    },
    "component_type": 2,
    "custom_id": custom_id,
    "guild_id":"961594529927020594",
    "message_flags":0,
    "message_id":message_id,
    # "nonce":"1061171593855631360",
    "session_id":"55eb3605fad3b549922fddd3e33ad733",
    "type":3,
    }
    return sendThis

def high_low_click():
    got = requests.get(api_history+"1", headers = headers)
    messages = got.json()
    for m in range(len(messages)):
        if messages[m]["embeds"][0]["description"]:
            try:
                high_low_guess_number_hint = int(messages[m]["embeds"][0]["description"][-5:-3])
                if high_low_guess_number_hint>50:
                    high_low_click = 0 #lower
                elif high_low_guess_number_hint<50:
                    high_low_click=2 #higher
                else:
                    high_low_click = 1 #jackpot
            except:
                print("high-low got me high (why.)")
                break
            print(high_low_click)
        if len(messages[m]["components"])==0:
            print("Not the correct message, ig")
            continue
        else:
            components = messages[m]["components"][0]["components"]
            
        message_id = messages[m]["id"]
        lable_id = []
        for index in range(len(components)):
            lable_id.append([components[index]["label"], components[index]["custom_id"]])
        
        lable = lable_id[high_low_click][0]
        custom_id = lable_id[high_low_click][1]
        break
        # return [click, id, message_id]
    sendThis = click_json(custom_id, message_id, channel_id)
    sendedThis = requests.post(api_interact, headers=headers, json = sendThis)
    print(sendedThis.status_code)

send_cmd(highlow_id)
time.sleep(2)
high_low_click()