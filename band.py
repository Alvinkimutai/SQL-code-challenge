import sqlite3




class Band:
    def __init__(self, id, name, hometown ) -> None:
       self.id = id
       self.name = name
       self.hometown = hometown
       pass
    # bands = [("Ammbasodors of christ", "Tanzania"), 
    #      ("Zabron singers", "Tanzania"),
    #      ("Alarm Ministries Rwanda", "Rwanda"),
    #      ("Healing Worship Team", "Kenya")
    #      ]

    @ classmethod
    def create_table(cls):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''CREATE TABLE IF NOT EXIST band 
                      (id INTEGER PRIMARY KEY AUTOINCREAMENT,
                      name TEXT, 
                      hometown TEXT)''')
       connection.commit()
       connection.close
    @ classmethod
    def create(cls, name, hometown):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute("insert into band (name, hometown) values(?,?)", (name, hometown))
       connection.commit()
       connection.close
    
    def concerts(self):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('SELECT * FROM concerts WHERE band id = ?', (self.id,))
       connection.commit()
       connection.close
    
    def venues(self):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''SELECT DISTINCT venues.*FROM venues
                      JOIN concerts on concerts.venue_id = venues.id
                      WHERE concerts.band_id = ?''', (self.id,)).fetchall()
       connection.commit()
       connection.close
    
    
    
    # cursor.executemany("insert into band values(?,?)", bands)

    # for row in cursor.execute("select * from band"):
      
    #   print(row)
    
    # print("*************************")

    # cursor.execute("select * from band where hometown=:h",{"h":"Tanzania"})

    # band_search = cursor.fetchall()

    # print(band_search)

    


    pass
