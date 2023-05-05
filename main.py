import sqlite3

def db_setup(db_name):
  conn = sqlite3.connect("DataBases/"+db_name)
  cur = conn.cursor()
  #create class/race and sub(class/race) tables
  cur.execute('''CREATE TABLE IF NOT EXISTS class_table(id INTEGER PRIMARY KEY,class_name STRING,flavour_text STRING,subclass_level INTEGER)''')
  cur.execute('''CREATE TABLE IF NOT EXISTS race_table(id INTEGER PRIMARY KEY,race_name STRING,flavor_text STRING)''')
  cur.execute('''CREATE TABLE IF NOT EXISTS sub_class_table(id INTEGER PRIMARY KEY,subclass_name STRING,flavor_text STRING)''')
  cur.execute('''CREATE TABLE IF NOT EXISTS sub_race_table(id INTEGER PRIMARY KEY,subrace_name STRING,flavour_text STRING''')

  #create features table
  

if __name__ == "__main__":
  db_setup("DnD-data.db")
  