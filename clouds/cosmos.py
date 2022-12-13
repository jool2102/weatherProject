import requests,json
from azure.cosmos import CosmosClient
import time
i = 1
while True:
    i = i+1

    api_key = "02535417df1956f146800cc5c3292f45"
    openweather_api = "http://api.openweathermap.org/data/2.5/weather?"
    cityName = "Stockholm"

    complete_url = openweather_api + "appid=" + api_key + "&q=" + cityName
    response = requests.get(complete_url)

    x = response.json()
    ## DIN cosmos info
    client = CosmosClient(
        "cosmosDB url",

        "Api key for cosmosdb"
    )

    data = x
    x["id"] = "Api_id" + str(i)
    print(x)
    print(type(x))

    database = client.get_database_client("ToDoList")
    
    container = database.get_container_client("Items")
    container.create_item(data)
    
    time.sleep(5)
