from mysql import connector
conn = connector.connect(host='localhost', port=3306, user = 'root', password='', database='test')
conn.autocommit = True
cursor = conn.cursor()

# insert data into db
'''
sqltext = 'insert into users (name,address,email) values ("chris","ma","licheng019@gmail.com")'
cursor.execute(sqltext)
cursor.close()
conn.close()
'''
# read data from db
'''
sqltext = 'select * from users'
cursor.execute(sqltext)
for row in cursor:
    print (row)
cursor.close()
conn.close()
'''

#insert more than one record
'''
from faker import Factory
userfaker = Factory.create()
userInfo = [(userfaker.name(),userfaker.address(),userfaker.email()) for i in range(10)]
sql_template = 'insert into users (name,address,email) values (%s, %s, %s)'
cursor.executemany(sql_template,userInfo)
cursor.close()
conn.close()
'''
