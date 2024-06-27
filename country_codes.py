from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Возвращает для заданной страны ее код Pygal, состоящий из 2 букв."""
    for code, name in COUNTRIES.items():
        if name == 'American Samoa':
            return 'as'
        elif name == 'Antigua and Barbuda':
            return 'ag'
        elif name == 'Aruba':
            return 'aw'
        elif name == 'Bahamas, The':
            return 'bs'
        elif name == 'Barbados':
            return 'bb'
        elif name == 'Bermuda':
            return 'bm'
        elif name == 'Bolivia':
            return 'bo'
        elif name == 'Cayman Islands':
            return 'ky'
        elif name == 'Comoros':
            return 'km'
        elif name == 'Congo, Dem. Rep.':
            return 'cd'
        elif name == 'Congo, Rep.':
            return 'kg'
        elif name == 'Dominica':
            return 'dm'
        elif name == 'Egypt, Arab Rep.':
            return 'eg'
        elif name == 'Fiji':
            return 'fj'
        elif name == 'French Polynesia':
            return 'pf'
        elif name == 'Gambia, The':
            return 'gm'
        elif name == 'Gibraltar':
            return 'gi'
        elif name == 'Grenada':
            return 'gd'
        elif name == 'Hong Kong SAR, China':
            return 'hk'
        elif name == 'Iran, Islamic Rep.':
            return 'ir'
        elif name == 'Kiribati':
            return 'ki'
        elif name == 'Korea, Dem. Rep.':
            return 'kp'
        elif name == 'Korea, Rep.':
            return 'kr'
        elif name == 'Kyrgyz Republic':
            return 'kg'
        elif name == 'Lao PDR':
            return 'la'
        elif name == 'Libya':
            return 'ly'
        elif name == 'Macao SAR, China':
            return 'mo'
        elif name == 'Macedonia, FYR':
            return 'mk'
        elif name == 'Marshall Islands':
            return 'mh'
        elif name == 'Micronesia, Fed. Sts.':
            return 'fm'
        elif name == 'Moldova':
            return 'md'
        elif name == 'New Caledonia':
            return 'nc'
        elif name == 'Northern Mariana Islands':
            return 'mp'
        elif name == 'Palau':
            return 'pw'
        elif name == 'Qatar':
            return 'qa'
        elif name == 'Samoa':
            return 'as'
        elif name == 'Sint Maarten (Dutch part)':
            return 'bq'
        elif name == 'Slovak Republic':
            return 'sk'
        elif name == 'Solomon Islands':
            return 'sb'
        elif name == 'St. Lucia':
            return 'lc'
        elif name == 'St. Martin (French part)':
            return 'mq'
        elif name == 'Tanzania':
            return 'tz'
        elif name == 'Tonga':
            return 'to'
        elif name == 'Trinidad and Tobago':
            return 'tt'
        elif name == 'Turks and Caicos Islands':
            return 'tc'
        elif name == 'Tuvalu':
            return 'tv'
        elif name == 'Vanuatu':
            return 'vu'
        elif name == 'Venezuela, RB':
            return 've'
        elif name == 'Virgin Islands':
            return 'vi'
        elif name == 'Yemen, Rep.':
            return 'ye'
        elif name == country_name:
            return code
        
    # Если страна не найдена, вернуть None.
    return None
