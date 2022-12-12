
Background: 
----------------------------------------------------------------------------------------------------------------------------------------------------------------
My initial idea was spiked from the idea, that I have always felt that the weather report on your app in wintertime always read alot colder than how it really felt for me leaving my apartment. And I very much think this is the truth and there is probably endless facts online that gives me the answer directly, but for me it would be interesting to see and learn how much it actually differs on a cold day compared to a place closeby but not in the city centre.
----------------------------------------------------------------------------------------------------------------------------------------------------------------
Components:
Initially I was going to use a physical Raspberry Pi with a temperature sensor to read temperature at my place, I could not get a hand on one so I will use a emulator instead. This will ofcourse make the temperature comparison useless but the projet will still function as intended.

From the other point of I am going to use openweather API since I have heard good things about that service, that it is easier to work with rather than SMHI for example.

With this two starting points I chose the Azure platform to handle and process all the data, Utilizing their features such as IOT-hub, Cosmosdb and visualization with PowerBI.

Below we see my initial idea of how this project would look with the help of a flowchart.
![bild](https://user-images.githubusercontent.com/91683500/207085572-59ba1aeb-cb95-4287-b446-5e4c2a6a725d.png)

After looking at the flowchart for just a short while, It does not seem right to process the API data through the IOT hub but that will be corrected if necessary onwards. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------
An updated flowchart will be made when things are in its place.
