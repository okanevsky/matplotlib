from datetime import datetime

format = '%Y-%m-%d'

current_date = datetime.strptime("2014-7-1", format)
print(current_date)