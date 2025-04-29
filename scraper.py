from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time

def get_reviews(url, max_reviews=20):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)

    driver.get(url)
    time.sleep(3)

    reviews = []
    while len(reviews) < max_reviews:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        review_elements = soup.find_all('div', class_='t-ZTKy')
        for elem in review_elements:
            reviews.append(elem.get_text(strip=True))
            if len(reviews) >= max_reviews:
                break
        try:
            next_btn = driver.find_element("xpath", "//span[text()='Next']")
            next_btn.click()
            time.sleep(2)
        except:
            break
    driver.quit()
    return reviews
