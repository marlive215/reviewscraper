import requests
from bs4 import BeautifulSoup

def get_app_reviews(url: str) -> list:
    '''
        Get reviews for specified app from App Store
        :param url: URL to the app reviews page
        :return: list of reviews

        Note: Use selenium to mimic real browser to be able to access reviews page
    '''
    response = requests.get(url)
    pass

def clean_data() -> None:
    '''Clean data from previous runs'''
    pass