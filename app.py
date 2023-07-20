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
    return render_template('index.html', index_prices = API_functions.get_index_prices(), compiled_prices = json.dumps(API_functions.get_prev_week_prices(), default=API_functions.datetime_serializer))

@app.route('/update_prices')
def update_prices():
    return json.dumps(API_functions.get_index_prices())

if __name__ == '__main__':
    app.run(debug=True)