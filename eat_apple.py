import requests

channel_id = "" # discord channel
key = "" # your discord autorization key

api_interact = "https://discord.com/api/v9/interactions"
def eat_apple(key):
    json = {
        "type":2,
        "application_id":"270904126974590976",
        "guild_id":"961594529927020594",
        "channel_id":channel_id,
        "session_id":"1817bb3307a397038aea275794bc0820",
        "data":{
            "version":"1022917002987315258",
            "id":"1011560371267579941",
            "name":"use",
            "type":1,
            "options":[
                {
                    "type":3,
                    "name":"item",
                    "value":"Apple"
                }
            ],
            "application_command":{
                "id":"1011560371267579941"
            },

        },
    }

    headers = {
        "Authorization": key
    }
    r = requests.post(api_interact, headers=headers, json=json)
    if r.status_code==204:
        # print("Command send!")
        pass
    else:
        print("Command not send, error code :", r.status_code, "sucks to be you lol")
    
eat_apple(key)