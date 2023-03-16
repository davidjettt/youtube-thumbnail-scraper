from flask import Flask, render_template
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from config import Config
from channel_form import ChannelForm
import os
# from selenium.webdriver.common.by import By

app = Flask(__name__)
app.config.from_object(Config)

# function that scrapes for thumbnail images of a channel
def scrape_youtube_channel(url):
    image_sources = []

    options = Options()
    options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    options.add_argument('headless')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    # options.add_argument('start-maximized')
    # options.add_argument('disable-infobars')

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=options)
    driver.get(url)

    last_height = driver.execute_script("return document.documentElement.scrollHeight")
    target_count = 20
    while target_count > len(image_sources):
        driver.execute_script('window.scrollTo(0, document.documentElement.scrollHeight);')
        time.sleep(1)
        new_height = driver.execute_script("return document.documentElement.scrollHeight")

        if new_height == last_height:
            break

        last_height = new_height
        content = driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        img_tags = soup.find_all('img', class_='yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded')

        for tag in img_tags:
            if len(image_sources) == 20:
                break
            image_sources.append(tag['src'])

    driver.close()
    return image_sources

@app.route('/', methods=['GET', 'POST'])
def index():
    form = ChannelForm()
    image_sources = []
    if form.validate_on_submit():
        url = form.data['channel_url']

        image_sources = scrape_youtube_channel(url)

    return render_template('index.html', form=form, image_sources=image_sources)


# Testing route
@app.route('/scrape')
def scrape(url):
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    # options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)

    driver.get(url)

    for _ in range(20):
        driver.execute_script("window.scrollTo(0,1080)")
        time.sleep(0.5)

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

    img_tags = soup.find_all('img', class_='yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded',limit=20)
    image_sources = [ tag['src'] for tag in img_tags ]
    driver.close()

    return { 'image_sources': image_sources }
