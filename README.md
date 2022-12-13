### Background: 


My initial idea was spiked from the idea, that I have always felt that the weather report on your app in wintertime always read alot colder than how it really felt for me leaving my apartment. 

And I very much think this is the truth. And there is probably endless facts online that gives me the answer directly, but for me it would be interesting to see and learn how much it actually differs on a cold day, compared to a place a bit more rural but still in the Stockholm area

### Components:

Initially I was going to use a physical Raspberry Pi with a temperature sensor to read temperature at my place, but I could not get a hand on one so I will use an emulator instead. This will ofcourse make the temperature comparison useless but the projet will still function as intended.

From the other point of view I am going to use the openweather API since I've heard good things about that service, that it is easier to work with rather than SMHI for example.

With this two starting points I chose the Azure platform to handle and process all the data, Utilizing their features such as IOT-hub to connect my device to cloud, Stream analytics for a quick and easy pipeline to visualization, Cosmosdb for storage and visualization with PowerBI.

Below we see my initial idea of how this project would look with the help of a flowchart.
![bild](https://user-images.githubusercontent.com/91683500/207085572-59ba1aeb-cb95-4287-b446-5e4c2a6a725d.png)

After looking at the flowchart for just a short while, It does not seem right to process the API data through the IOT hub but that will be corrected if necessary onwards. 

An updated flowchart will be made when things are in its place.

### Goal:


My goal with this project is to get more comfortable with everything revolving the Azure Cloud Services but also a funny bonus in knowing the temperature differences from a little more rural area in Stockholm compared to the innercity.

### Method:

I first began by setting up a IOT-hub and configuring it with my emulator through Azure, this was a simple task and I could directly see that I had messages pouring in to my hub. 

For me a valid next step was to visualize this data in some way just to see. I ended up picking a stream since it looked simple to work with and that it could directly pump it out to Power Bi. It was not that simple for me personally from the getgo since I firstly used Embedded Power Bi on the platform which drained my credits overnight :)

After some extra work I managed to connect the raspberry to PowerBi visualization through a stream. Wish I saved a screenshot of it, but did not, and have since then removed that stream after trying new stuff.

Next step was to somehow store all this incoming data, and for that CosmosDB sounded like the most interesting alternative. Here I was stuck for a while since the data did not seem to enter the DB even though I saw requests, after some research it became clear that message routing from the IOT hub was the best way and scrap the stream. 

Now the messages are appearing and being stored in the container. Now just one easy step left, pushing the data to Power BI for visualization. Or so I thought. I'm currently stuck at this part since my temperature data is being encoded in base64 and have not been able to resolve this as of yet.
(I have added some screenshots in a folder that shows my progress)

Moving on to the API point of view a simple python application is used to fetch data from openweather API to the same cosmosDB that stores my raspberry data.
This was a more straight forward task since the database was set up from working with the raspberry and no base64 in the way.

Below is an updated flowchart:
![bild](https://user-images.githubusercontent.com/91683500/207371100-c0b7fcd4-c012-40c7-84b8-05101ac4cd7c.png)

