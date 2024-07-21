import psycopg2
import pandas as pd
import os

# Connect to the PostgreSQL database
conn = psycopg2.connect("host=localhost dbname=Sparkify user=postgres password=2Ndofficial#")
cur = conn.cursor()

# Create the tables
cur.execute("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id TEXT PRIMARY KEY,
        title TEXT,
        artist_id TEXT,
        year INT,
        duration FLOAT
    )
""")

cur.execute("""
        CREATE TABLE IF NOT EXISTS artists (
        artist_id TEXT PRIMARY KEY,
        name TEXT,
        location TEXT,
        latitude FLOAT,
        longitude FLOAT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS time (
        start_time TIMESTAMP PRIMARY KEY,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        gender TEXT,
        level TEXT
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS songplays (
        songplay_id SERIAL PRIMARY KEY,
        start_time TIMESTAMP REFERENCES time(start_time),
        user_id INT REFERENCES users(user_id),
        level TEXT,
        song_id TEXT REFERENCES songs(song_id),
        artist_id TEXT REFERENCES artists(artist_id),
        session_id INT,
        location TEXT,
        user_agent TEXT
    )
""")

conn.commit()

# Sample Indian artists and songs
indian_artists = [
    {'artist_id': 'AR001', 'name': 'A.R. Rahman', 'location': 'Chennai, India', 'latitude': 13.0827, 'longitude': 80.2707},
    {'artist_id': 'AR002', 'name': 'Shreya Ghoshal', 'location': 'Murshidabad, India', 'latitude': 24.1839, 'longitude': 88.2449},
    {'artist_id': 'AR003', 'name': 'Arijit Singh', 'location': 'Jiaganj, India', 'latitude': 24.4567, 'longitude': 88.1234}
]

indian_songs = [
    {'song_id': 'S001', 'title': 'Jai Ho', 'artist_id': 'AR001', 'year': 2008, 'duration': 279.47},
    {'song_id': 'S002', 'title': 'Tujhe Kitna Chahein Aur', 'artist_id': 'AR003', 'year': 2019, 'duration': 230.93},
    {'song_id': 'S003', 'title': 'Jalte Dil', 'artist_id': 'AR002', 'year': 2012, 'duration': 312.56}
]

# Insert sample data into the database
for artist in indian_artists:
    cur.execute("INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)",
                (artist['artist_id'], artist['name'], artist['location'], artist['latitude'], artist['longitude']))

for song in indian_songs:
    cur.execute("INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)",
                (song['song_id'], song['title'], song['artist_id'], song['year'], song['duration']))

conn.commit()

# Close the connection
conn.close()

print("Tables created and sample data inserted successfully.")

import psycopg2

# Connect to the PostgreSQL database
conn = psycopg2.connect("host=localhost dbname=Sparkify user=postgres password=2Ndofficial#")
cur = conn.cursor()

# Retrieve all songs from the database
cur.execute("SELECT * FROM songs")
songs = cur.fetchall()

# Print the songs
for song in songs:
    print(song)

# Close the connection
conn.close()

