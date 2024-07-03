import requests
import time

key = "" # your discord authorization key
channel_id = "" # your channel id

api_interact = "https://discord.com/api/v9/interactions"
api_history = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=" # LIMIT NOT SET


headers = {
"Authorization": key
}

quantity = 1
item = "Zig's Capybara"

json = {
    "type":2,
    "application_id":"270904126974590976",
    "guild_id":"961594529927020594",
    "channel_id":channel_id,
    "session_id":"3ac459b76f802c1124e708def97114ca",
    "data":{
        "version":"1034827622112309248",
        "id":"1011560371078832207",
        "name":"friends",
        "type":1,
        "options":[
            {
                "type":2,
                "name":"share",
                "options":[
                    {
                        "type":1,
                        "name":"items",
                        "options":[
                            {
                                "type":6,
                                "name":"user",
                                "value":"270904126974590976"
                            },
                            {
                                "type":3,
                                "name":"quantity",
                                "value":quantity
                            },
                            {
                                "type":3,
                                "name":"item",
                                "value":item
                            }
                        ]
                    }
                ]
            }
        ],
        "application_command":{
            "id":"1011560371078832207",
        },
    },
}


def click_button(last_message:str):
    custom_id = last_message[0]["components"][0]["components"][1]["custom_id"]
    sendThis = json
    sendedThis = requests.post(api_interact, headers=headers, json = sendThis)
    print(custom_id)
    if sendedThis.status_code==204:
        print("Click Status code : 204, lucky mf")
    else:
        print("Click Status code : ", sendedThis.status_code, "sucks to be you lol")

r = requests.post(api_interact, headers=headers, json=json)
if r.status_code==204:
    print("Command send!")
else:
    print("Command not send, error code :", r.status_code, "sucks to be you lol")

got = requests.get(api_history+"1", headers = headers)
message = got.json()
time.sleep(2)
# print(message)
click_button(message)

