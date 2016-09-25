from flask import Flask, render_template, jsonify
from app.helpers.helper import get_all_data

public = 'public'

app = Flask(__name__, template_folder=public, static_folder=public)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/visual')
def visual():
  return render_template('visual.html')

@app.route('/sGraph')
def sGraph():
  return render_template('sGraph.html')

# Oh god...
@app.route('/api/transactions/test')
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


@app.route('/api/transactions')
def a():
    data = get_all_data();
    return jsonify({'data': data})
