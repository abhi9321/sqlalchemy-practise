from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///college.db', echo=True)
connection = engine.connect()

sql = """
SELECT * FROM students
where id >= :x
"""

t = text(sql)
result = connection.execute(t, x=2).fetchall()
for row in result:
    print(row)

