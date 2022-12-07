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
    driver.get(url)
    driver.implicitly_wait(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    soup = BeautifulSoup(driver.page_source, "html.parser")
    reviews = soup.find_all(class_="EGFGHd")
    
    review_list = []
 
    # 3. Iterate through the reviews and extract the review text and other relevant information
    for review in reviews:
        review_list.append(review.text)
    # 4. Add the review text and other relevant information to a list

    # 5. Return the list
    print(review_list)
    driver.close()
    pass

def clean_data() -> None:
    '''Clean data from previous runs'''
    pass