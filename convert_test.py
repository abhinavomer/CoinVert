import requests
def fetch_conversion_factor(src,trg):
    url=f'https://v6.exchangerate-api.com/v6/fa2187e6cd409b1e9ee3afb6/latest/{src}'
    response=requests.get(url)
    response=response.json()
    cf=response['conversion_rates'][trg]
    print(cf)
fetch_conversion_factor("USD","GBP")
