import sqlite3


class Concert:
    def __init__(self, id, band_id, venue_id, date) -> None:
        self.id = id
        self.band_id = band_id
        self.venue_id = venue_id
        self.date = date
        pass
    @classmethod
    def create_table(cls):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS concerts(
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       band_id INTEGER,
                       venue_id INTEGER,
                       date TEXT,
                       FOREIGN KEY(band_id) REFERENCES bands(id)
                       FOREIGN KEY(venue_id) REFERENCES venues(id)
                       )
                       ''')
        connection.commit()
        connection.close()
    @classmethod
    def insert_into_concerts(cls, band_id, venue_id, date):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('INSERT INTO concerts(band_id, venue_id, date) VALUES (?,?)', (band_id, venue_id, date))
        connection.commit()
        connection.close()

    def band(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM bands WHERE id = ?', (self.band_id,))
        band = cursor.fetchone()
        connection.close()
        return band
    def venue(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM venues WHERE id = ?', (self.venue_id,))
        venue = cursor.fetchone()
        return venue
    def hometown_show(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
           SELECT bands.hometown, venues.city
                       FROM concerts
                       JOIN bands ON concerts.band_id = bands.id
                       JOIN venues ON concerts.venue_id = venues.id
                       WHERE concerts.id = ?
                    ''',(self.id,))
        result = cursor.fetchone()
        connection.close()
        return result[0] == result[1]
    def introduction(self):
        connection = sqlite3.connect("mydb.db")
        cursor = connection.cursor()
        cursor.execute('''
            SELECT bands.name, bands.hometown, venues.city
            FROM concerts
            JOIN bands ON  concerts.band_id = bands.id
            JOIN venues ON concerts.venue_id = venues.id
            WHERE concerts.id = ?
        ''', (self.id,))
        result = cursor.fetchone()
        connection.close()
        return f"Hello {result[2]}!!!!! We are {result[0]} and we're from {result[1]}"




    pass