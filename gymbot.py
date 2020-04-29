import requests
import random
import hashlib
import datetime

exercises = {
    "upper": {
        "Push Ups": [20, "reps"],
        "Burpees": [20, "reps"],
        "Shoulder Taps": [20, "reps"],
        "Inch Worms": [10, "reps"],
        "Bear Crawls": [30, "seconds"],
        "Tricep Dips": [20, "reps"],
        "Close-Grip Push Ups": [10, "reps"],
        "Kick Throughs": [20, "reps"]
    },
    "legs": {
        "Squats": [20, "reps"],
        "Lunges": [20, "reps"],
        "High Knees": [30, "seconds"],
        "Mountain Climbers": [30, "seconds"],
        "Squat Jumps": [20, "reps"],
        "Side Lunges": [20, "reps"],
        "Reverse Lunges": [20, "reps"]
    },
    "core": {
        "Sit Ups": [20, "reps"],
        "Planks": [30, "seconds"],
        "Side Planks": [30, "seconds"],
        "Supermans": [20, "reps"],
        "Leg Raises": [20, "reps"],
        "Bicycle Crunches": [20, "reps"]
    }
}

today_md5 = hashlib.md5(str(datetime.date.today()).encode('utf-8')).hexdigest()
today_md5_str = str(int(today_md5, base=32))
today_md5_str_mid = int(len(today_md5_str)/2)

class safelist(list):
    def get(self, index, default=None):
        try:
            return self.__getitem__(index)
        except IndexError:
            return default

upper_keys = safelist(list(exercises['upper'].keys()))
legs_keys = safelist(list(exercises['legs'].keys()))
core_keys = safelist(list(exercises['core'].keys()))

def get_key(keys, _list):
    for i in _list:
        key = keys.get(int(i))
        if key != None:
            break
    return key

upper_key = get_key(upper_keys, today_md5_str[0:])
legs_key = get_key(legs_keys, today_md5_str[::-1])
core_key = get_key(core_keys, today_md5_str[today_md5_str_mid:])

upper_val = exercises['upper'][upper_key]
legs_val = exercises['legs'][legs_key]
core_val = exercises['core'][core_key]

text = ""

if datetime.datetime.now().hour == 8:
    text += "Good morning sunshine! \n Now "
elif datetime.datetime.now().hour == 10:
    text += "Just before you have that cookie... "
elif datetime.datetime.now().hour == 12:
    text += "Lunch is going to taste so much better if you "
elif datetime.datetime.now().hour == 13:
    text += "You should be ashamed of yourself for eating all that... \n Now "
elif datetime.datetime.now().hour == 16:
    text += "You're almost there big boy... \n Now"
elif datetime.datetime.now().hour == 17:
    text += "If you've made it this far, you might as well go all the way... "
else:
    text += "Just "

text = "drop and give me: \n *Upper body* \n {} ({} {}) \n *Legs* \n {} ({} {}) \n *Core* \n {} ({} {}) \n".format(
    upper_key, upper_val[0], upper_val[1],
    legs_key, legs_val[0], legs_val[1],
    core_key, core_val[0], core_val[1],
)

icon_emoji = "man-cartwheeling"
channel = "#workout"
username = "GymBot"
url = 'https://hooks.slack.com/services/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'

requests.post(url, json={'text': text, 'icon_emoji': icon_emoji, 'channel': channel, 'username': username})