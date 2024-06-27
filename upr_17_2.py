import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

def visualisation(name, dict, name_file):
    # Построение визуализации.
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Популярные статьи'
    chart.x_labels = name
    chart.add('', dict)
    chart.render_to_file(name_file)


# Создание вызова API и сохранение ответа.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Обработка информации о каждой статье.
submission_ids = r.json()
submission_dicts, names = [], []
for submission_id in submission_ids[:30]:
    # Создание отдельного вызова API для каждой статьи.
    url = ('https://hacker-news.firebaseio.com/v0/item/' + str(submission_id) + '.json')
    submission_r = requests.get(url)
    response_dict = submission_r.json()
    submission_dict = {
        'title': response_dict['title'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        'value': response_dict.get('descendants', 0)
        }
    names.append(submission_dict['title'])
    submission_dicts.append(submission_dict)

    submission_dicts = sorted(submission_dicts, key=itemgetter('value'), reverse=True)

visualisation(names, submission_dicts, 'upr_17_2.svg')