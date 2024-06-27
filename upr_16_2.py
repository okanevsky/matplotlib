import csv
from matplotlib import pyplot as plt
from datetime import datetime
# Чтение дат и температурных максимумов   и минимумов из файла.
def read_csv(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        dates, highs = [], []
        for row in reader:
            try:
                current_date = datetime.strptime(row[0], '%Y-%m-%d')
                high = int(row[1])
            except ValueError:
                continue
            else:
                dates.append(current_date)
                highs.append((high-32) * 5/9)
    return dates, highs

filename1 = 'data\death_valley_2014.csv'
filename2 = 'data\sitka_weather_2014.csv'

dates1, highs1 = read_csv(filename1)
dates2, highs2 = read_csv(filename2)

# Нанесение данных на диаграмму.
fig = plt.figure(dpi=128, figsize=(11, 7))
plt.plot(dates1, highs1, c='red', alpha = 0.5)
plt.plot(dates2, highs2, c= 'blue', alpha = 0.5)
# Форматирование диаграммы.
plt.title("Максимальные температуры на аляске и в долине смерти", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Температура (С)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
plt.show()