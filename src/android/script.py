from bs4 import BeautifulSoup
from selenium import webdriver


def get_app_reviews(url: str) -> list:
    '''
        Get reviews for specified app from App Store
        :param url: URL to the app reviews page
        :return: list of reviews

        Note: Use selenium to mimic real browser to be able to access reviews page
    '''
    ### Algorithm:
    # 1. Open browser using selenium
    driver = webdriver.Chrome(executable_path='/home/amara/Desktop/reviewscraper/driver/chromedriver')
    # 2. Navigate to the reviews page which is passed as the url parameter
    page = driver.get(url)
    review = BeautifulSoup(page.text , 'lxml')
    #
    review_name = review.find_all("div", class_="X5PpBb").text
    print(review_name)
    # 3. Iterate through the reviews and extract the review text and other relevant information

    # 4. Add the review text and other relevant information to a list
    # 5. Return the list
    pass

def clean_data() -> None:
    '''Clean data from previous runs'''
    pass