import json
import pygal
from pygal.style import RotateStyle, LightColorizedStyle
from country_codes import get_country_code

# Список заполняется данными.
filename = 'data\population_data.json'

with open(filename) as f:
    pop_data = json.load(f)

# Построение словаря с данными численности населения.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        coutry_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_code(coutry_name)
        if code == None:
            with open('data\country_none.txt','a') as f:
                f.write(coutry_name + '\n')

        if code:
            cc_populations[code] = population
            # Группировка стран по 3 уровням населения.
            cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
            for cc, pop in cc_populations.items():
                if pop < 10000000:
                    cc_pops_1[cc] = pop
                elif pop < 1000000000:
                    cc_pops_2[cc] = pop
                else:
                    cc_pops_3[cc] = pop
            # Проверка количества стран на каждом уровне.
            wm_style = RotateStyle('#336699', base_style=LightColorizedStyle)
            wm = pygal.maps.world.World(style = wm_style)
            wm.title = 'World Population in 2010, by Country'
            wm.add('0-10m', cc_pops_1)
            wm.add('10m-1bn', cc_pops_2)
            wm.add('>1bn', cc_pops_3)

            wm.render_to_file('world_population.svg')