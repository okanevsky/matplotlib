from die import Die
import pygal
# Создание кубика D6.
# Создание двух кубиков D6.
die_1 = Die(8)
die_2 = Die(8)
die_3 = Die(8)

# Моделирование серии бросков с сохранением результатов в списке.
results = [die_1.roll() + die_2.roll() + die_3.roll() for roll_num in range(50000)]


# Анализ результатов.
min_result = 3
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
frequencies = [results.count(value) for value in range(min_result, max_result+1)]

hist = pygal.Bar()

hist.title = "Results of rolling a D" + str(die_1.num_sides) + ", D" + str(die_2.num_sides) + " and a D" + str(die_3.num_sides) + " 50,000 times."
hist.x_labels = [value for value in range(min_result, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D' + str(die_1.num_sides) + ', D' + str(die_2.num_sides) + ' and a D' + str(die_3.num_sides), frequencies)
hist.render_to_file('die_visual.svg')