import requests
from bs4 import BeautifulSoup
import pandas as pd
import sqlite3

conn = sqlite3.connect('books.db')

# Cursor object to interact with the database
cursor = conn.cursor()

# Create the books table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        link TEXT NOT NULL,
        price REAL NOT NULL,
        stock TEXT NOT NULL
    )
''')
conn.commit() # Save the changes

current_page = 1
data = []
proceed = True

while proceed:
    print("Currently scraping page: "+str(current_page))
    
    url = "https://books.toscrape.com/catalogue/page-"+str(current_page)+".html"
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    # Check if we have reached a non-existing page (end of catalog)
    if soup.title.text == "404 Not Found":
        proceed = False
    else:
        all_books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

        for book in all_books:
            item = {}
            item['Title'] = book.find("img").attrs["alt"]
            item['Link'] = "https://books.toscrape.com/catalogue/"+book.find("a").attrs["href"]
            item['Price'] = book.find("p", class_="price_color").text[2:]
            item['Stock'] = book.find("p", class_="instock availability").text.strip()

            data.append(item)

            # Insert the data into the database
            cursor.execute('''
                INSERT INTO books (title, link, price, stock) 
                VALUES (?, ?, ?, ?)
            ''', (item['Title'], item['Link'], item['Price'], item['Stock']))
        conn.commit()  # Save changes to the database

    current_page += 1

# Store data in Excel and CSV formats as well
df = pd.DataFrame(data)
df.to_excel('books.xls', sheet_name='Sheet1', index=False, engine='xlsxwriter')
df.to_csv("books.csv")

# Query the database to ensure data is stored correctly
cursor.execute('SELECT * FROM books')
rows = cursor.fetchall()

print("\nSample Data from Database:")
for row in rows[:10]:  # Print the first 10 records
    print(row)

# Close the database connection
conn.close()