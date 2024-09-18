import sqlite3
class Band:
    def __init__(self, id, name, hometown ) -> None:
       self.id = id
       self.name = name
       self.hometown = hometown
       pass
    
    @ classmethod
    def create_table(cls):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''CREATE TABLE IF NOT EXISTS bands
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      name TEXT, 
                      hometown TEXT)''')
       connection.commit()
       connection.close

    @classmethod
    def drop_table(cls):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''
         DROP TABLE IF EXISTS bands;
                      ''')
       connection.commit()
       connection.close()


    @ classmethod
    def create(cls, name, hometown):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute("insert into bands (name, hometown) values(?,?)", (name, hometown))
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


    def play_in_venue(self, venue, date):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('INSERT INTO concerts(band_id, venue_id, date) VALUES(?,?,?)', (self.id, venue.id, date))
       connection.commit()
       connection.close


    @classmethod
    def all_introductions(cls):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''SELECT concert.date, venue.city, bands.name, bands.hometown
                      FROM concerts
                      JOIN venues on concerts.venue id = venues.id
                      JOIN bands on concert.band id = bands.id'''
                      )
       intro = cursor.fetchall()
       connection.close
       return [f"Hello {city}!!!!! We are {name} and we're from {hometown}" for city, name, hometown in intro]
    
    @classmethod
    def most_performances(cls):
       connection = sqlite3.connect("mydb.db")
       cursor = connection.cursor()
       cursor.execute('''SELECT band id, COUNT(*) as performance_count
                      FROM concerts
                      GROUP BY band_id
                      ORDER BY performance_count DESC
                      LIMIT 1''')
       result = cursor.fetchone()
       connection.close()
       return result[0] if result else None
       
       
    
    
    
    # cursor.executemany("insert into band values(?,?)", bands)

    # for row in cursor.execute("select * from band"):
      
    #   print(row)
    
    # print("*************************")

    # cursor.execute("select * from band where hometown=:h",{"h":"Tanzania"})

    # band_search = cursor.fetchall()

    # print(band_search)

    


    pass


















# bands = [("Ammbasodors of christ", "Tanzania"), 
    #      ("Zabron singers", "Tanzania"),
    #      ("Alarm Ministries Rwanda", "Rwanda"),
    #      ("Healing Worship Team", "Kenya")
    #      ]