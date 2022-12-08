import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def get_app_reviews(url: str) -> list:
    '''
        Get reviews for specified app from App Store
        :param url: URL to the app reviews page
        :return: list of reviews

        Note: Use selenium to mimic real browser to be able to access reviews page
    '''
    review_list = []
    ### Algorithm:
    # 1. Open browser using selenium
    driver = webdriver.Chrome(executable_path="/home/amara/Desktop/reviewscraper/driver/chromedriver")

    # 2. Navigate to the reviews page which is passed as the url parameter
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # 3. Make the driver wait to not be detected and click the review arrow button
    review_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF")))

    # arrow_button = driver.find_element(By.CLASS_NAME, "VfPpkd-Bz112c-LgbsSe yHy1rc eT1oJ QDwDD mN1ivc VxpoF")
    review_button.click()

    #4 . Navigate through the new reviews page 
    soup = BeautifulSoup(driver.page_source, "html.parser")
    reviews = soup.find_all("div", class_="h3YV2d")
    
    # 5. Iterate through the reviews and extract the review text and other relevant information
    for review in reviews:

    # 6. Add the review text and other relevant information to a list
        review_list.append(review.text)

    # 7. Return the list
    print(review_list)

    #8. Close the browser window
    driver.close()
    pass

def clean_data() -> None:
    '''Clean data from previous runs'''
    pass