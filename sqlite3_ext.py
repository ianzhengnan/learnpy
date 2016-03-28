
import os, sqlite3

db_file = os.path.join(os.path.dirname(__file__), 'test.db')

if os.path.isfile(db_file):
    os.remove(db_file)

conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute(r'create table user(id varchar(20) primary key, name varchar(20), score int)')
cursor.execute(r"insert into user values ('A-001', 'Adam', 95)")
cursor.execute(r"insert into user values ('A-002', 'Eric', 62)")
cursor.execute(r"insert into user values ('A-003', 'Doris', 78)")
cursor.close()
conn.commit()
conn.close()

def get_score_in(low, height):

    try:
        conn = sqlite3.connect(db_file)
        cursor = conn.cursor()
        values = []
        cursor.execute('select name from user where score >=? and score <=?', (low, height))
        return [n[0] for n in cursor.fetchall()]

    finally:
        cursor.close()
        conn.close()
#Test
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Eric', 'Doris'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Adam', 'Eric', 'Doris'], get_score_in(60, 100)

print('Pass')



