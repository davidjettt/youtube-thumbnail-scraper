# Youtube Thumbnail Image Scrapper

This is a project that scrapes a YouTube channel for most recent video thumbnail images.

## Technologies Used
* Flask
* Beautiful Soup
* Selenium

## Project Start Guide
1. Clone this repo
2. Open cloned project in a code editor/IDE
3. Add an environment variable to the  ```.flaskenv``` file. Shown below
```Javascript
SECRET_KEY=<YOUR SECRET KEY>
```
4. In your terminal, ```cd``` into the root of the project directory (same level as the ```Pipfile``` file) and run ```pipenv install``` to create your virtual enviornment and install all dependencies in that environment.
5. **Optional:** Run ```pipenv shell``` to go into your virtual environment.
6. Start the server by running ```pipenv run flask run``` if you are not in your virtual environment or run ```flask run``` if you are in your virtual environment.
7. Go to ```http://localhost:5000/``` in a ```Google Chrome``` browser to see project.
