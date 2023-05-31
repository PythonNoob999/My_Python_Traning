# the requests lib to get html data

# the site API Docs used in this example https://www.weatherapi.com/docs/

import requests

# the vanilla website link to add our wanted destnitions in it

vanilla_link = ("http://api.weatherapi.com/v1/")

#API key

api = "YOUR API KEY"

def weather(location):

    # the vanilla link + our wanted section of the web+ api key+extra parameter(location)

    url = f"{vanilla_link}current.json?key={api}&q={location}"

    # getting the data from the new URL that we made

    melon = requests.get(url)

    # printing only the wanted data

    print(melon.json()['current']['temp_c'])

weather("Egypt")
