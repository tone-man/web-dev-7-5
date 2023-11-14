import csv
import sqlite3

# Function to parse CSV and extract book titles and authors
def parse_csv(csv_file_path):
    book_data = []

    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            title = row['Book-Title']
            author = row['Book-Author']
            
            book_data.append({'title': title, 'author': author})

    return book_data

# Function to check if author exists
def check_and_add_author(conn, author):
    cursor = conn.cursor()

    # Check if author exists
    cursor.execute("SELECT * FROM author WHERE author=?", (author,))
    existing_author = cursor.fetchone()

    if not existing_author:
        # Author doesn't exist, add them to the database
        cursor.execute("INSERT INTO author (author) VALUES (?)", (author,))
        conn.commit()

        # Return the ID of the newly added author
        return cursor.lastrowid
    else:
        # Return the ID of the existing author
        return existing_author[0]
    
# Function to check if a book exists in the SQLite database and add if not
def check_and_add_book(conn, title):
    cursor = conn.cursor()

    # Check if the book already exists
    cursor.execute("SELECT * FROM books WHERE title=?", (title,))
    existing_book = cursor.fetchone()

    if not existing_book:
        # Book doesn't exist, add it to the database
        cursor.execute("INSERT INTO books (title) VALUES (?)", (title,))
        conn.commit()

        return cursor.lastrowid
    else:
        #return id of the existing_book
        return existing_book[0]

# Function to check if book-author mapping exists and add if not
def check_and_add_mapping(conn, book_id, author_id):
    cursor = conn.cursor()

    # Check if the mapping already exists
    cursor.execute("SELECT * FROM BooksAuthorMapping WHERE book_id=? AND author_id=?", (book_id, author_id,))
    existing_mapping = cursor.fetchone()

    if not existing_mapping:
        # Mapping doesn't exist, add it to the database
        cursor.execute("INSERT INTO BooksAuthorMapping (book_id, author_id) VALUES (?, ?)", (book_id, author_id,))
        conn.commit()
    
    
# Main Section
csv_file_path = 'books.csv'
books = parse_csv(csv_file_path)

# SQLite database setup
db_file_path = 'library.db'
conn = sqlite3.connect(db_file_path)

# Iterate through books, check and add authors to the database
for book in books:
    author = book['author']
    title = book['title']
    author_id = check_and_add_author(conn=conn, author=author)
    book_id = check_and_add_book(conn=conn, title=title)
    check_and_add_mapping(conn=conn, book_id=book_id, author_id=author_id)

    

# Close the database connection
conn.close()

