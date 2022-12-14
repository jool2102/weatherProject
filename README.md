### Background: 


My initial idea was spiked from the idea, that I have always felt that the weather report on your app in wintertime always read alot colder than how it really felt for me leaving my apartment. 

And I very much think this is the truth. There is probably endless sources online that explains why and how, but for me it would be interesting to see and learn how much it actually differs on a cold day, compared to a place more rural but still in the Stockholm area.

### Components:

Initially I was going to use a physical Raspberry Pi with a temperature sensor to read temperature at my place, but I could not get a hand on one, so I will use an emulator instead. This will ofcourse make the temperature comparison useless but the project will still function as intended.

From the other point of view I am going to use the openweather API since I've heard good things about that service, that it is easier to work with rather than SMHI for example.

With this two starting points I chose the Azure platform to handle and process all the data, Utilizing their features such as IOT-hub to connect my device to cloud, Stream analytics for a quick and easy pipeline to visualization, Cosmosdb for storage and visualization with PowerBI.

Below we see my initial idea of how this project would look with the help of a flowchart.
![bild](https://user-images.githubusercontent.com/91683500/207085572-59ba1aeb-cb95-4287-b446-5e4c2a6a725d.png)

After looking at the flowchart for just a short while, It does not seem right to process the API data through the IOT hub but that will be corrected if necessary onwards. 

An updated flowchart will be made when things are in its place.

### Goal:


My goal with this project is to get more comfortable with everything revolving the Azure Cloud Services but also a funny bonus in knowing the temperature differences from a little more rural area in Stockholm compared to the city centre.

### Method:

I first began by setting up a IOT-hub and configuring it with my emulator through Azure, this was a simple task and I could directly see that I had messages pouring in to my hub. 

For me a valid next step was to visualize this data in some way just to see. I ended up picking a stream since it looked simple to work with and that it could directly pump it out to Power Bi. It was not that simple for me personally from the getgo since I firstly used Embedded Power Bi on the platform which drained my credits overnight :)

After some extra work I managed to connect the raspberry to PowerBi visualization through a stream. Wish I saved a screenshot of it, but did not, and have since then removed that stream after trying new stuff.

Next step was to somehow store all this incoming data, and for that CosmosDB sounded like the most interesting alternative. Here I was stuck for a while since the data did not seem to enter the DB even though I saw requests, after some research it became clear that message routing from the IOT hub was the best way and scrap the stream. 

Now the messages are appearing and being stored in the container. Now just one easy step left, pushing the data to Power BI for visualization. Or so I thought. I'm currently stuck at this part since my temperature data is being encoded in base64 and have not been able to resolve this as of yet.
(I have added some screenshots in a folder that shows my progress)

Moving on to the API point of view a simple python application is used to fetch data from openweather API to the same cosmosDB that stores my raspberry data.
This was a more straight forward task since the database was set up from working with the raspberry and no base64 in the way.

I wish that I would of cracked this, and be able to visualize live data from two directions but I unfortunately could not. I will instead do something that i'm familiar with, so I handpicked values from the API-fetch and did some formatting and now there is a simple visualization. Pictures of it can be found in the print folder.

### Security suggestions:

In hindsight I surely did not take enough security procautions, which is something that is not good enough if you would use this commercially, Security is a very big aspect to  to take in to account if you are working with this commercially. I would read and study every step I took more throughly, regarding what and how everything operates(etc how Iot hub really works, general weaknesses etc.)

Using updated protocols and stronger passwords in general would help alot. Also researching the API you are going to use is a very good habit to have, there is a risk that the API is not updated to standards or have general security flaws. Iot units like the Raspberry pie is also prone to weaknesses since often the person working with it(in this case me) do not have the best knowledge in security within Iot units. After reading more about this I would take the necessary procautions accordingly.

Thank you for reading, I had fun, mostly. Atleast when things was working :)

Below is an updated flowchart of what it was supposed to look like:
![bild](https://user-images.githubusercontent.com/91683500/207371462-3fc571f7-5408-4275-9881-1658f3dcdf73.png)


