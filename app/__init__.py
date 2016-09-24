from flask import Flask, render_template, jsonify
from faker import Factory
from datetime import datetime
import random
import operator

public = 'public'

app = Flask(__name__, template_folder=public, static_folder=public)

faker = Factory.create()


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/api/transactions')
def get_all_data():
  entries = []

  rent = {
    'time': datetime(
      year=2016,
      month=9,
      day=1
    ),
    'name': 'Toronto Leasing',
    'notes': 'Business Rent',
    'amount': float(-3000.00),
    'type': 'C'
  }
  entries.append(rent)

  for num in range(0, 6):
    salaries = {
      'time': datetime(
        year=2016,
        month=9,
        day=1
      ),
      'name': 'Interac e-Transfer',
      'notes': 'Employee Salary',
      'amount': float(-2080.00),
      'type': 'C'
    }
    entries.append(salaries)

  for num in range(0, 50):
    year = 2016
    month = 9
    day = random.randint(1, 30)
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    date = datetime(
      year=year,
      month=month,
      day=day,
      hour=hour,
      minute=minute,
      second=second
    )

    income = float("{0:.2f}".format(random.uniform(-500, 1000)))
    data = {
      'time': date,
      'name': faker.company(),
      'notes': '--',
      'amount': income,
      'type': 'D' if income > 0 else 'C'
    }
    entries.append(data)
  entries.sort(key=operator.itemgetter('time'))

  total = 0
  for entry in entries:
    total += entry['amount']


  return jsonify({
    'total': total,
    'data': entries}
  )
