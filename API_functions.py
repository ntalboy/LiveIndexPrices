import requests
import json

def get_funding_chart_data(instrument_name, length):
    '''
    instrument_name 
        required = true
        type = string (ex: BTC_USDC-PERPETUAL, ETH_USDC-PERPETUAL, SOL_USDC-PERPETUAL, ...)
    length
        required = true
        type = string
        enum = 8h, 24h, 1m
    '''
    r = requests.get(f'https://test.deribit.com/api/v2/public/get_funding_chart_data?instrument_name={instrument_name}&length={length}')
    return json.loads(r.text)

# def get_instruments(currency, kind=None, expired=None):
def get_instruments(currency, **kwargs):

    '''
    currency
        required = true
        type = string
        enum = BTC, ETH, USDC
    kind
        required = false
        type = string
        enum = future, option, spot, future_combo, option_combo
    expired
        required = false
        type = boolean
    '''
    url = f'https://test.deribit.com/api/v2/public/get_instruments?currency={currency}'
    for parameter, value in kwargs.items():
        url += f'&{parameter}={value}'
    r = requests.get(url)
    return json.loads(r.text)

def get_index_price(index_name):
    '''
    index_name
        required = true
        type = string
        enum = btc_usd, eth_usd, sol_usd, ...
    '''
    r = requests.get(f'https://test.deribit.com/api/v2/public/get_index_price?index_name={index_name}')
    return json.loads(r.text)

def get_index_prices():
    index_prices = {
        'btc': get_index_price('btc_usd')['result']['index_price'],
        'eth': get_index_price('eth_usd')['result']['index_price'],
        'sol': get_index_price('sol_usd')['result']['index_price']
    }
    return index_prices

