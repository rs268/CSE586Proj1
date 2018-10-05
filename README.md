# Waypoints Application
## How to run
To setup your system to run this application the first step is to make sure you have any version of python above 3.3, and make sure that python is added to the PATH environment variable. Next Django 2.1 needs to be installed. Use pip to install django:
```
pip install django
```

This project is using a CDN in order to use Bootstrap and its dependencies, so it is not necessary to download it.
Next this project uses the Google Maps Python Client, so use pip to install that as well, in the following way:
```
pip install googlemaps
```

Next the necessary API keys need to be placed in their necessary locations. These are the API keys for Google Maps API and OpenWeather API. Edit these in the settings.py file in the following way:

Once this is all set up we need to initialize the database. This needs to be done for each phase. Navigate into the folder of the phase that you want to run and use the following commands:
```
python manage.py makemigrations
```
and then
```
python manage.py migrate
```

this will initialize the models in the database. Next we need to initialze the cache:
```
python manage.py createcachetable
```

Remember to do this in both phases.
Now you're ready to run the application. In the command prompt type:
```
python manage.py runserver
```
And in a web browser navigate to 127.0.0.1:8000, you should see this instruction in your command prompt. To exit the server use CTRL+C.

## Using the Application
Usage of the application is very simple. In the origin input box type where the route will start using any format that Google Maps accepts.
Then type the destination of the route in the destination input box. Then click the Get Route button. On the map you can click on a marker and a window will pop up with the weather at that location.

Enjoy!