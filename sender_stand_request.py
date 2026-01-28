import config
import requests
import data
""""
    Solicitudes GET
"""

def get_docs():

    return requests.get(config.URL_SERVICE + config.DOC_PATH)

# print(get_docs().status_code) # Salida: 200

def get_logs():

    return requests.get(config.URL_SERVICE + config.LOG_MAIN_PATH, params={"count": 20})

# print(get_logs().status_code)

# print(get_logs().headers)

def get_users_table():

    return requests.get(config.URL_SERVICE + config.USERS_TABLE_PATH)

# print(get_users_table().status_code)

"""
    Solicitudes POST
"""

def post_new_user(body):

    return requests.post(config.URL_SERVICE + config.CREATE_USER_PATH, json=body, headers=data.headers)

# result = post_new_user(data.user_body)

# print(result.status_code)

# print(result.json())

def post_products_kits(body):

    return requests.post(config.URL_SERVICE + config.PRODUCTS_KITS_PATH, json=body, headers=data.headers)

# result = post_products_kits(data.product_ids)

# print(result.status_code)

# print(result.json())