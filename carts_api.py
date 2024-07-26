import requests

def get_all_carts():
    response = requests.get('https://fakestoreapi.com/carts')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_single_cart(cart_id):
    response = requests.get(f'https://fakestoreapi.com/carts/{cart_id}')
    if response.status_code == 200:
        products = response.json()
        return products

def get_limit_results(limit):
    response = requests.get(f'https://fakestoreapi.com/carts?limit={limit}')
    if response.status_code == 200:
        products = response.json()
        return products
    
def get_sort_results(sort_type):
    response = requests.get(f'https://fakestoreapi.com/carts?sort={sort_type}')
    if response.status_code == 200:
        products = response.json()
        return products
    
