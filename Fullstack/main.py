import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('dishes.db')

# Create a cursor object to execute SQL commands
cursor = conn.cursor()

# Create the dishes table
cursor.execute('''
CREATE TABLE IF NOT EXISTS dishes (
    dishId INTEGER PRIMARY KEY,
    dishName TEXT NOT NULL,
    imageUrl TEXT NOT NULL,
    isPublished BOOLEAN NOT NULL
)
''')

# Insert the JSON data into the table
dishes = [
    {"dishName": "Jeera Rice", "dishId": 1, "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/jeera-rice.jpg", "isPublished": True},
    {"dishName": "Paneer Tikka", "dishId": 2, "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/paneer-tikka.jpg", "isPublished": True},
    {"dishName": "Rabdi", "dishId": 3, "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/rabdi.jpg", "isPublished": True},
    {"dishName": "Chicken Biryani", "dishId": 4, "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/chicken-biryani.jpg", "isPublished": True},
    {"dishName": "Alfredo Pasta", "dishId": 5, "imageUrl": "https://nosh-assignment.s3.ap-south-1.amazonaws.com/alfredo-pasta.jpg", "isPublished": True}
]

for dish in dishes:
    cursor.execute('''
    INSERT INTO dishes (dishId, dishName, imageUrl, isPublished)
    VALUES (?, ?, ?, ?)
    ''', (dish['dishId'], dish['dishName'], dish['imageUrl'], dish['isPublished']))

# Commit the changes and close the connection
conn.commit()
conn.close()
