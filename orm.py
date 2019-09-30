import json

data = json.loads('''{"schemaName": "MicroShop",
"entities": [
    {"Customer": {
        "name": "String",
        "orders": "*Order"}},
    {"Order": {
        "date": "String",
        "total": "Number",
        "customer": "Customer",
        "lines": "*OrderLine"}},
    {"OrderLine": {
        "order": "Order",
        "product": "Product",
        "count": "Number",
        "total": "Number"}},
    {"Product": {
        "name": "String",
        "price": "Number"}}
]
}''')


def generate_schema(schema):
    file_name = schema['schemaName'] + '.sql'
    rs = ''

    rs += f'''
DROP SCHEMA IF EXISTS {schema['schemaName']};
CREATE SCHEMA {schema['schemaName']};
USE {schema['schemaName']};'''

    for entity in schema['entities']:
        for (k, v) in entity.items():
            rs += \
                f'''

DROP TABLE IF EXISTS `{k}`;
CREATE TABLE `{k}`
(
    `id` INT (11) NOT NULL AUTO_INCREMENT PRIMARY KEY'''
            for (field_name, field_type) in v.items():
                field_info = generate_field(field_name, field_type)
                if field_type[0] == '*':
                    continue

                rs += \
                    f''',
    `{field_info.get('field_name')}` {field_info.get('field_type')}({field_info.get('length')})'''

            rs += \
                '''
);'''

    try:
        f = open(file_name, "w+")
        f.write(rs)
        f.close()

        print(f'Schema file {file_name} created successfully!')
    except (OSError, IOError) as e:
        print('Something went wrong!', e)


def generate_entity_file(entities):
    for entity in entities:
        rs = ''
        setters_getters = ''
        for (k, v) in entity.items():
            file_name = f'{k}.java'
            rs += \
                f'''public class {k} {{'''
            for (field_name, field_type) in v.items():
                field_info = generate_field(field_name, field_type, out="java")
                rs += \
                    f'''
    private {field_info.get('field_type')} {field_info.get('field_name')};'''

                setters_getters += \
                    f'''
                
    public void set{field_info.get('field_name').capitalize()}({field_info.get('field_type')} {field_info.get('field_name')}) {{
        this.{field_info.get('field_name')} = {field_info.get('field_name')}; 
    }}

    public {field_info.get('field_type')} get{field_info.get('field_name').capitalize()}() {{
        return {field_info.get('field_name')}; 
    }}'''

            rs += setters_getters
            rs += \
                '''
}'''

        try:
            f = open(file_name, "w+")
            f.write(rs)
            f.close()

            print(f'Entity file {file_name} created successfully!')
        except (OSError, IOError) as e:
            print('Something went wrong!', e)
    return rs


def generate_field(field_name, field_type, out='sql'):
    if out == 'sql':
        string_type = 'VARCHAR'
        number_type = 'INT'

    if out == 'java':
        string_type = 'String'
        number_type = 'int'

    if field_type == 'String':
        return {'field_name': field_name, 'field_type': string_type, 'length': '255'}
        # return f'`' \
        #        f'{field_name}` VARCHAR(255)'

    if field_type == 'Number':
        return {'field_name': field_name, 'field_type': number_type, 'length': '11'}
        # return f'`' \
        #        f'{field_name}` INT(11)'

    if field_type[0] == '*':
        return {'field_name': field_name, 'field_type': f'List<{field_type[1:]}>'}

    return {'field_name': field_name.lower() + '_id', 'field_type': number_type, 'length': '11'}
    # return f'`' \
    #        f'{field_name.lower()}_id` INT(11)'


generate_schema(data)
generate_entity_file(data['entities'])
# print(generate_schema(data))
