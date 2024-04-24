# Currency Conversion Chatbot :- CoinVert
### Deployment
- Live Link:- https://telegram.me/coinvert69_bot
- wait for some time as backend loading takes time.

## Overview

The Currency Conversion Chatbot API is a Flask-based web service that allows users to perform currency conversions through a conversational interface. Users can interact with the chatbot by providing input in natural language, specifying the source currency, target currency, and amount to be converted. The chatbot then utilizes an external currency conversion API to fetch the latest exchange rates and calculate the converted amount.

## Features

- **Conversational Interface**: Users can interact with the chatbot by sending requests in natural language, making the currency conversion process intuitive and user-friendly.
- **Currency Conversion**: The chatbot supports conversion between various currencies, allowing users to specify the source and target currencies along with the amount to be converted.
- **Real-Time Exchange Rates**: The chatbot fetches real-time exchange rates from an external API, ensuring accurate and up-to-date conversions.
- **JSON Response Format**: The API returns responses in JSON format, making it easy for developers to integrate with other applications and services.

## Usage

1. **Send Request**: Send a POST or GET request to the API endpoint ("/") with the required parameters:
   - **source_currency**: The currency code of the source currency (e.g., USD, EUR).
   - **amount**: The amount of money to be converted.
   - **target_currency**: The currency code of the target currency.
2. **Receive Response**: Receive a JSON response containing the converted amount and fulfillment text, indicating the result of the conversion.

## Technologies Used
Flask: A lightweight web framework for building web applications in Python.
Requests: A Python library for making HTTP requests to external APIs.
JSON: A lightweight data-interchange format for exchanging data between a server and a client.
Dialogflow: It is used for training of the chatbot

## External APIs
ExchangeRate-API: The chatbot utilizes the ExchangeRate-API to fetch real-time exchange rates and perform currency conversions. The API provides accurate and reliable data for various currency pairs.
