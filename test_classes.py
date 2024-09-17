import sqlite3
from band import Band
from venue import Venue
from concert import Concert

"""Create tables and populate the database before running tests."""
Band.create_table()
Venue.create_table()
Concert.create_table()

    # Create some sample data
band1 =Band.create("Ammbasodors of Christ", "Tanzania")
band2 = Band.create("Zabron Singers", "Tanzania")
venue1 = Venue.insertdata("Venue One", "City A")
venue2 = Venue.insertdata("Venue Two", "City B")

print(band1)











# if __name__ == '__main__':
#     print(setup_database())
#     # unittest.main()





# from band import Band
# from concert import Concert
# from venue import Venue

# bands = [("Ammbasodors of christ", "Tanzania"), 
#          ("Zabron singers", "Tanzania"),
#          ("Alarm Ministries Rwanda", "Rwanda"),
#          ("Healing Worship Team", "Kenya")
#          ]

# band1 = Band()

# print(band1.create_table())
# # print(band1.create())