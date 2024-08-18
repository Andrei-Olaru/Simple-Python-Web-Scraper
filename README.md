# Python Web Scraper with SQLite Database Integration

This project is a simple Python web scraper that extracts book data from an online bookstore, stores it in an SQLite database, and also exports the data to Excel and CSV files.

## Explanation of the Code

### Database Connection and Table Creation

- The script connects to an SQLite database (`books.db`). If the database doesn't exist, it is created automatically.
- It creates a table called `books` with the following fields:
  - `id`: An auto-incremented primary key.
  - `title`: The title of the book.
  - `link`: The URL link to the book's page.
  - `price`: The price of the book.
  - `stock`: The availability status of the book (In Stock or Out of Stock).

### Web Scraping

- The script scrapes book data from the website in a loop, iterating over multiple pages until it encounters a "404 Not Found" page, which indicates the end of the catalog.

### Data Insertion

- For each book, the script inserts the data directly into the SQLite database using `INSERT INTO` statements.
- Additionally, the scraped data is stored in a `pandas` DataFrame, which is later exported to both Excel (`books.xls`) and CSV (`books.csv`) files.

### Data Verification

- After scraping and inserting the data, the script queries the first 10 records from the `books` table to verify that the data was correctly inserted.

### Closing the Connection

- The database connection is closed at the end of the script to free up resources.

## Running the Code

To run the script:

1. Make sure you have Python installed on your system.
2. Install the required packages using the following command:

   ```bash
   pip install requests beautifulsoup4 pandas
    ```
3. Run the script in your environment. The script will create a `books.db` SQLite database file with the scraped data.

## Visualizing Data

To visualize and explore the data, you can use the following tools:

- **SQLite Browser (DB Browser for SQLite)**: A free, open-source tool that allows you to browse, edit, and query SQLite databases.
- **Pandas**: You can load and explore the database contents using Pandas in Python.

Feel free to explore and delete the .csv, .xls and .db files in order to test the code on your own!