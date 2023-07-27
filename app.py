from flask import Flask, render_template
import json
import API_functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                            index_prices = API_functions.get_index_prices(),
                            compiled_prices =json.dumps(API_functions.get_prev_week_prices_at_4()),
                            DVOL_data = json.dumps(API_functions.get_prev_week_volatility())
                            )

@app.route('/update_prices')
def update_prices():
    return json.dumps(API_functions.get_index_prices())

if __name__ == '__main__':
    app.run(debug=True)