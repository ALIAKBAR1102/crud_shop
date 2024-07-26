import requests

def get_all_carts():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_a_single_cart():
    response = requests.get('https://fakestoreapi.com/carts/5')
    if response.status_code == 200:
        products = response.json()
        return products

def get_limit_results():
    response = requests.get('https://fakestoreapi.com/carts?limit=5')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_sort_results():
    response = requests.get('https://fakestoreapi.com/carts?sort=desc')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_carts_in_a_date_range():
    response = requests.get('https://fakestoreapi.com/carts?startdate=2019-12-10&enddate=2020-10-10')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_user_carts():
    response = requests.get('https://fakestoreapi.com/carts/user/2')
    if response.status_code == 200:
        products = response.json()
        return products
    