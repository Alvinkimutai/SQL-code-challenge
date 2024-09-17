import sqlite3

class Venue:
    def __init__(self, id, title, city) -> None:
        self.id = id
        self.title = title
        self.city = city
        # pass
    @ classmethod
    def create_table(cls):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS venues(i
                       id INTEGER PRIMARY KEY AUTOINCREAMENT,
                       title TEXT,
                       city TEXT
                       )
                       '''
        )
        connection.commit()
        connection.close()

    @ classmethod
    def insertdata(cls, title, city):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute(''' 
        INSERT INTO venues (title, city) VALUES(?,?)''',(title,city))
        connection.commit()
        connection.close()

    def concerts(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute(' SELECT * FROM concerts WHERE venue_id = ?', (self.id))
        concerts = cursor.fetchall()
        connection.close()
        return concerts
    
    def bands(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT DISTINCT bands. *FROM bands
            JOIN concerts ON concerts.band_id = band.id
            WHERE concerts.venue_id = ?
            ''', (self.id,))
        bands = cursor.fetchall()
        connection.close()
        return bands
    def concert_on(self, date):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM concerts WHERE venue_id = ? AND date = ?', (self.id, date))
        concert = cursor.fetchone()
        connection.close()
        return concert
    def most_frequent_band(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT band_id, COUNT(*) as performance_count
            FROM concerts
            WHERE venue_id = ?
            GROUP BY band_id
            ORDER BY performance_count DESC
            LIMIT 1
        ''', (self.id,))
        most_frequent_band = cursor.fetchone()
        connection.close()
        return most_frequent_band

    

    # pass