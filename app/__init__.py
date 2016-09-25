from flask import Flask, render_template, jsonify, redirect
from app.helpers.helper import get_all_data

public = 'public'

app = Flask(__name__, template_folder=public, static_folder=public)


@app.route('/repayment')
@app.route('/')
def index():
  return render_template('index.html')

# @app.route('/repayment')
# def redirect_index():
#   return redirect('/')

@app.route('/visual')
def visual():
  return render_template('visual.html')


# Oh god...
@app.route('/api/transactions')
def test():
  data = get_all_data()
  times = {}
  for entry in data:
    try:
      a = times[entry['date']]
      a['total'] += entry['amount']
      a['transactions'] = a['transactions'] + 1
    except:
      times[entry['date']] = {
        'total': entry['amount'],
        'date': entry['date'],
        'transactions': 1
      }
  return jsonify(times)
