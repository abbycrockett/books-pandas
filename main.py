import pandas as pd
from tabulate import tabulate

# DataFrame object
df = pd.read_csv('amazon_top50_books.csv')

# Shows the Top 5 Books
print("\nTop 5 Books (9/25/2025):")
print(tabulate(df.head(), headers='keys', tablefmt='pretty', showindex=False))

# Shows book price statistics as a table
price_stats = [
    ["Avg", f"${df['Price'].mean():.2f}"],
    ["Min", f"${df['Price'].min():.2f}"],
    ["Max", f"${df['Price'].max():.2f}"]
]
print("\nBook Price Statistics:")
print(tabulate(price_stats, tablefmt='pretty', showindex=False))

# Shows the shape (rows, columns) of the DataFrame
# Note: If you just print df.shape, it will return (50, 5)
print(f"\nShape: {df.shape[0]} rows and {df.shape[1]} columns...")

# Shows the column names
print(f" {list(df.columns)}")

# Shows the summary statistics, and rounds the values to 2 decimal places
print("\nSummary Statistics:")
summary_stats = df.describe().round(2)
print(tabulate(summary_stats, headers='keys', tablefmt='pretty'))

# Counts the number of books per author
author_counts = df['Author'].value_counts().reset_index()
author_counts.columns = ['Author', 'Count']
print("\nBooks per Author:")
print(tabulate(author_counts, headers='keys', tablefmt='pretty', showindex=False))