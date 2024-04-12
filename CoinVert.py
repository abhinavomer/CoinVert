from flask import Flask,request,jsonify
import requests
app=Flask(__name__)

@app.route('/',methods=["POST","GET"])
def index():
    data=request.get_json()
    source_currency=data['queryResult']['parameters']['unit-currency'][0]['currency']
    amount=data['queryResult']['parameters']['unit-currency'][0]['amount']
    target_currency=data['queryResult']['parameters']['currency-name']
    cf=fetch_conversion_factor(source_currency,target_currency)
    final_amount=amount*cf
    response={
        'fulfillmentText':"{} {} is {} {}".format(amount,source_currency,final_amount,target_currency)
    }
    print (jsonify(response))
    return jsonify(response)

def fetch_conversion_factor(src,trg):
    url=f'https://v6.exchangerate-api.com/v6/fa2187e6cd409b1e9ee3afb6/latest/{src}'
    response=requests.get(url)
    response=response.json()
    cf=response['conversion_rates'][trg]
    return cf

