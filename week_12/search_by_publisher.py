import sqlite3;

def get_games_by_genre(genre_name):
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Game.releaseYear, Genre.name
            FROM Game
            JOIN GenreInGame ON Game.id = GenreInGame.gameId
            JOIN Genre ON Genre.id = GenreInGame.genreId
            WHERE LOWER(Genre.name) = LOWER(?)
            ORDER BY Game.name;
        """, (genre_name,))

        return cursor.fetchall()

def get_games_by_publisher(publisher_name):
    with sqlite3.connect("db/TopGamesDB.db") as connection:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT Game.name, Publisher.name
            FROM Game
            JOIN GamePublisher ON Game.id = GamePublisher.gameId
            JOIN Publisher ON Publisher.id = GamePublisher.publisherId
            WHERE LOWER(Publisher.name) = LOWER(?)
            ORDER BY Game.name;
        """, (publisher_name,))

        return cursor.fetchall()

print(get_games_by_publisher("Nintendo"))