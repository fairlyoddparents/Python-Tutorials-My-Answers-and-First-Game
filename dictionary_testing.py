data = {'texto': 'UVA',
        'autor': 'Pirolo',
        'ano1': '1985',
        'ano2': '     ',
        'titulo': 'El libro de las dietas',
        'medio': '',
        'pais': 'ARGENTINA',
        'tema': '501.- Gastronomía'
        }

def check_field_not_empty(value):
    if value.strip() != "" and value.strip().lower() != "menu":
        return True

def testing_dictionary_use(data):
    empty_list = []
    for field, value in data.items():
        if check_field_not_empty(value):
            field = f"This is the field name {field}"
            value = f"This is the value {value}"
            empty_list.append((field, value))
    print(empty_list)

testing_dictionary_use(data)

#print(data['texto'].strip().lower() != "")
