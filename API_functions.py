import requests
import json
from datetime import datetime, timezone, timedelta

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
        "btc": format(get_index_price('btc_usd')['result']['index_price'], ".2f"),
        "eth": format(get_index_price('eth_usd')['result']['index_price'], ".2f"),
        "sol": format(get_index_price('sol_usd')['result']['index_price'], ".2f")
    }
    return index_prices

def timestamp_to_hkt_datetime(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone(timedelta(hours=8)))

def timestamp_to_hkt_date(timestamp):
    return datetime.fromtimestamp(timestamp / 1000, tz=timezone(timedelta(hours=8))).date()

def get_prev_week_prices():
    prev_week_btc = get_funding_chart_data('BTC_USDC-PERPETUAL', '1m')['result']['data']
    prev_week_eth = get_funding_chart_data('ETH_USDC-PERPETUAL', '1m')['result']['data']
    prev_week_sol = get_funding_chart_data('SOL_USDC-PERPETUAL', '1m')['result']['data']

    filtered_btc = [entry for entry in prev_week_btc if timestamp_to_hkt_datetime(entry['timestamp']).hour == 16]
    sorted_btc = sorted(filtered_btc, key=lambda x: x['timestamp'], reverse=True)

    filtered_eth = [entry for entry in prev_week_eth if timestamp_to_hkt_datetime(entry['timestamp']).hour == 16]
    sorted_eth = sorted(filtered_eth, key=lambda x: x['timestamp'], reverse=True)

    filtered_sol = [entry for entry in prev_week_sol if timestamp_to_hkt_datetime(entry['timestamp']).hour == 16]
    sorted_sol = sorted(filtered_sol, key=lambda x: x['timestamp'], reverse=True)

    last_7_entries_at_4pm_hkt_btc = sorted_btc[:7]
    last_7_entries_at_4pm_hkt_eth = sorted_eth[:7]
    last_7_entries_at_4pm_hkt_sol = sorted_sol[:7]

    compiled_entries = { 'timestamp':[], 'btc':[], 'eth':[], 'sol':[]}
    for (btc_entry, eth_entry, sol_entry) in zip(last_7_entries_at_4pm_hkt_btc, last_7_entries_at_4pm_hkt_eth, last_7_entries_at_4pm_hkt_sol):
        compiled_entries['timestamp'].append(timestamp_to_hkt_datetime(btc_entry['timestamp']))
        compiled_entries['btc'].append(btc_entry['index_price'])
        compiled_entries['eth'].append(eth_entry['index_price'])
        compiled_entries['sol'].append(sol_entry['index_price'])

    return compiled_entries

def datetime_serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()