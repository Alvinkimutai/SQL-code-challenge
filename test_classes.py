import sqlite3
from band import Band
from venue import Venue
from concert import Concert

"""Create tables and populate the database before running tests."""
Band.drop_table()
Band.create_table()
Venue.drop_table()
Venue.create_table()
Concert.drop_table()
Concert.create_table()




    # Create some sample data

band1 =Band.create("Ammbasodors of Christ", "Tanzania")
band2 = Band.create("Zabron Singers", "Tanzania")
venue1 = Venue.insertdata("Venue One", "City A")
venue2 = Venue.insertdata("Venue Two", "City B")


# print(band1)


# Fetch and print all bands
print("All Bands:")
for band in Band.all_introductions():
    print(band)

# Fetch and print all venues
print("\nAll Venues:")
with sqlite3.connect("mydb.db") as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM venues')
    venues = cursor.fetchall()
    for venue in venues:
        print(venue)

# Create concerts
Concert.insert_into_concerts(1, 1, "2024-01-01")  # Band 1 at Venue 1
Concert.insert_into_concerts(2, 2, "2024-02-01")  # Band 2 at Venue 2

# Test Concert data retrieval
print("\nConcerts:")
with sqlite3.connect("mydb.db") as connection:
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM concerts')
    concerts = cursor.fetchall()
    for concert in concerts:
        print(concert)

# Test relationships
print("\nConcerts for Ammbasodors of Christ:")
band1 = Band(1, "Ammbasodors of Christ", "Tanzania")
for concert in band1.concerts():
    print(concert)

print("\nVenues for Zabron Singers:")
band2 = Band(2, "Zabron Singers", "Tanzania")
for venue in band2.venues():
    print(venue)

# Check if the concerts have the correct bands and venues
print("\nChecking concert details:")
for concert in concerts:
    concert_instance = Concert(concert[0], concert[1], concert[2], concert[3])
    band = concert_instance.band()
    venue = concert_instance.venue()
    print(f"Concert ID: {concert[0]}, Band: {band[1]}, Venue: {venue[1]}, Date: {concert[3]}")

# Check hometown shows
print("\nHometown Shows:")
for concert in concerts:
    concert_instance = Concert(concert[0], concert[1], concert[2], concert[3])
    if concert_instance.hometown_show():
        print(f"Concert ID: {concert[0]} is a hometown show for {band[1]}.")

# Test the most frequent band
most_frequent_band = Band.most_performances()
print(f"\nMost Frequent Band ID: {most_frequent_band}")

# Test for concert introductions
print("\nConcert Introductions:")
for concert in concerts:
    concert_instance = Concert(concert[0], concert[1], concert[2], concert[3])
    print(concert_instance.introduction())









