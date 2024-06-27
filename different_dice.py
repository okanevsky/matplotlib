from die import Die
import pygal
# Создание кубика D6.
# Создание двух кубиков D6.
die_1 = Die()
die_2 = Die(10)

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() + die_2.roll() for roll_num in range(50000)]
#for roll_num in range(50000):
#    result = die_1.roll() + die_2.roll()
#    results.append(result)

# Анализ результатов.
min_result = 2
max_result = die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(2, max_result+1)]
#for value in range(2, max_result+1):
#    frequency = results.count(value)
#    frequencies.append(frequency)
#print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling a D6 and a D10 50,000 times."
hist.x_labels = [value for value in range(min_result, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('die_visual.svg')