from datetime import datetime
import random
import operator
from faker import Factory

def get_all_data():
  faker = Factory.create()

  entries = []

  rent = {
    'date': datetime(
      year=2016,
      month=9,
      day=1
    ),
    'name': 'Toronto Leasing',
    'notes': 'Business Rent',
    # 'amount': float(-3000.00),
    'amount': -3000,
    'type': 'C'
  }
  entries.append(rent)

  for num in range(1, 4):
    salaries = {
      'date': datetime(
        year=2016,
        month=9,
        day=1
      ),
      'name': 'Interac e-Transfer',
      'notes': 'Employee Salary',
      'amount': -2080,
      'type': 'C'
    }
    entries.append(salaries)

  for num in range(0, 610):
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

    income = random.randint(-500, 500)
    data = {
      'date': date,
      'name': faker.company(),
      'notes': 'Purchase' if income > 0 else 'Expense',
      'amount': income,
      'type': 'D' if income > 0 else 'C'
    }
    entries.append(data)
  entries.sort(key=operator.itemgetter('date'))

  total = 0
  for entry in entries:
    entry['date'] = entry['date'].strftime("%d-%m-%y")
    total += entry['amount']

  return entries
