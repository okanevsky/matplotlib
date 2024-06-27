from die import Die
import pygal
# Создание кубика D6.
die = Die()

# Моделирование серии бросков с сохранением результатов в списке.

results = [die.roll() for roll_num in range(1000)]
#for roll_num in range(1000):
#    result = die.roll()
#    results.append(result)

# Анализ результатов.
frequencies = [results.count(value) for value in range(1, die.num_sides+1)]
#for value in range(1, die.num_sides+1):
#    frequency = results.count(value)
#    frequencies.append(frequency)
#print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = [value for value in range(1, 7)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')