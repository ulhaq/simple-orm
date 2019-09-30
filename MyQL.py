import mysql.connector
import re

db = mysql.connector.connect(host="localhost", user="root", passwd="", database='microshop')

cursor = db.cursor()

def my_query(stmt):
    if stmt[0].isalpha():
        if '.' in stmt:
            stmt = stmt.split('.')
            cursor.execute(f"SELECT {stmt[1]} FROM {stmt[0]}")
        else:
            cursor.execute(f"SELECT * FROM {stmt}")

    if stmt[0] == '(':
        reg = re.match(r"\((.*)\|(.*)\)(\.(.*))?", stmt)

        if '.' not in stmt:
            cursor.execute(f"SELECT * FROM {reg.group(1)} WHERE {reg.group(2)}")
        else:
            after_dot = reg.group(4).split('.')

            if len(after_dot) < 2:
                cursor.execute(f"SELECT `{reg.group(4)}`.* FROM `{reg.group(1)}` INNER JOIN `{reg.group(4)}` ON `{reg.group(1)}`.`id`=`{reg.group(4)}`.`{reg.group(1)}_id` WHERE {reg.group(1)}.{reg.group(2)}")
            else:
                if after_dot[1][0].islower():
                    cursor.execute(f"SELECT DISTINCT `{after_dot[0]}`.{after_dot[1]} FROM `{reg.group(1)}` INNER JOIN `{after_dot[0]}` ON {reg.group(1)}.{after_dot[0]}_id={after_dot[0]}.id WHERE {reg.group(1)}.{reg.group(2)}")
                else:
                    cursor.execute(f"SELECT `{after_dot[2]}`.* FROM `{reg.group(1)}` INNER JOIN `{after_dot[0]}` ON `{reg.group(1)}`.`id`=`{after_dot[0]}`.`{reg.group(1)}_id` INNER JOIN `{after_dot[1]}` ON `{after_dot[0]}`.`id`=`{after_dot[1]}`.`{after_dot[0]}_id` INNER JOIN `{after_dot[2]}` ON `{after_dot[2]}`.`id`=`{after_dot[1]}`.`{after_dot[2]}_id` WHERE {reg.group(1)}.{reg.group(2)}")

    rs = []
    for row in cursor.fetchall():
        row_dict = {}
        for field, f_name in zip(row, cursor.column_names):
            row_dict.update({f_name: field})
        rs.append(row_dict)

    return rs;


print(my_query("Customer"))
print(my_query("Customer.name"))
print(my_query("(Customer|name='Joe')"))
print(my_query("(Customer|name='Doe').Order"))
print(my_query("(Customer|name='Doe').Order.Orderline.Product"))
print(my_query("(Order|total > 200).Customer.name"))