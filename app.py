from flask import Flask
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

app = Flask(__name__)

@app.route('/')
def scrape():
    options = Options()
    options.add_argument('start-maximized')
    options.add_argument('disable-infobars')
    # options.add_argument('headless')

    driver = webdriver.Chrome(chrome_options=options)

    driver.get('https://www.youtube.com/@Houseofhighlights/videos')

    for _ in range(20):
        driver.execute_script("window.scrollTo(0,1080)")
        time.sleep(0.5)

    content = driver.page_source.encode('utf-8').strip()
    soup = BeautifulSoup(content, 'lxml')

    img_tags = soup.find_all('img', class_='yt-core-image--fill-parent-height yt-core-image--fill-parent-width yt-core-image yt-core-image--content-mode-scale-aspect-fill yt-core-image--loaded',limit=20)
    image_sources = [ tag['src'] for tag in img_tags ]
    driver.close()

    return { 'image_sources': image_sources }
