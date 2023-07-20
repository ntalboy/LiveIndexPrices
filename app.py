from flask import Flask, render_template
import json
import API_functions

'''
Try to build the exact data being shown here but you need to 
create three column (One for BTC, ETH and SOL), live index price 
of them as well as showing last 7 days index price @ 4pm HKT
'''

app = Flask(__name__)



@app.route('/')
def index():
    data = API_functions.get_prev_week_prices()
    formatted_data = {
        'timestamp': [ts.isoformat() for ts in data['timestamp']],
        'btc': data['btc'],
        'eth': data['eth'],
        'sol': data['sol']
    }
    return render_template('index.html', index_prices = API_functions.get_index_prices(), compiled_prices =json.dumps(formatted_data))

@app.route('/update_prices')
def update_prices():
    return json.dumps(API_functions.get_index_prices())

if __name__ == '__main__':
    app.run(debug=True)