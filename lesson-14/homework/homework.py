# Homework
# Task: JSON Parsing
# write a Python script that reads the students.jon JSON file and prints details of each student.
import json 

with open('students.json') as f:
    x = json.load(f)
    print(x)
# # Task: Weather API
# # Use this url : https://openweathermap.org/
# # Use the requests library to fetch weather data for a specific city(ex. your hometown: Tashkent) and print relevant information (temperature, humidity, etc.).
import requests
import json
payload = {'q': 'London', 'appid': 'appid'}
lat = int(input('Enter value of lat: '))
lon = int(input('Enter value of lon: '))
r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=41&lon=69&appid=b26686294c2685b07920cf5686795429')
data = r.text
print(data)

# Task: JSON Modification
# Write a program that allows users to add new books, update existing book information, and delete books from the books.json JSON file.
import json

class BookManager:
    def __init__(self, filename='books.json'):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_books(self):
        with open(self.filename, 'w') as f:
            json.dump(self.books, f, indent = 4)

    def add_book(self, title, author, year):
        if any(book['title'].lower() == title.lower() for book in self.books):
            print('Book already exists.')
            return
        self.books.append({'title': title, 'author': author, 'year': year})
        self.save_books()
        print('Book added successfully')

    def update_book(self, title):
        for book in self.books:
            if book['title'].lower() == title.lower():
                new_author = input(f'Enter new author (current: {book['author']}): ').strip()
                new_year = input(f'Enter new year (current: {book['year']}): ').strip()
                if new_author:
                    book['author'] = new_author
                if new_year:
                    book['year'] = new_year
                self.save_books()
                print('Book updated successfully!')
                return
        print('Book not found.')

    def delete_book(self, title):
        original_count = len(self.books)
        self.books = [book for book in self.books if book['title'].lower() != title.lower()]
        if len(self.books) == original_count:
            print('Book not found.')
        else:
            self.save_books()
            print('Book deleted successfully!')

    def list_books(self): 
        if not self.books:
            print('No books available')
        else:
            for i, book in enumerate(self.books, 1):
                print(f'{i}. {book['title']} by {book['author']} ({book['year']})')

def main():
    manager = BookManager()

    while True:
        print("\n=== Book Manager ===")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            title = input('Enter book title: ').strip()
            author = input('Enter author name: ').strip()
            year = input('Enter publication year: ').strip()
            manager.add_book(title, author, year)
        elif choice == '2':
            title = input('Ennter the title of the book to update: ').strip()
            manager.update_book(title)
        elif choice == '3':
            title = input('Enter the title of the book to delete: ').strip()
            manager.delete_book()
        elif choice == '4':
            manager.list_books()
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main() 

# Task: Movie Recommendation System
# Use this url http://www.omdbapi.com/ to fetch information about movies.
# Create a program that asks users for a movie genre and recommends a random movie from that genre.
import requests
import random

API_KEY = "f9319cf8"
BASE_URL = "https://www.omdbapi.com/"

def get_movies_by_genre(genre):
    movies = []
    for page in range(1, 100):
        params = {
            "apikey": API_KEY,
            "s": genre,
            "type": "movie",
            "page": page
        }
        response = requests.get(BASE_URL, params = params)
        data = response.json()
        if data.get("Search"):
            movies.extend(data["Search"])
    return movies

def recommend_movie(genre):
    movies = get_movies_by_genre(genre)
    if not movies:
        print('No movies found for this genre. Try another one!\n')
        return
    movie = random.choice(movies)
    print(f"Recommended Movie: {movie['Title']} ({movie['Year']})")
    print(f"More details: https;//www.imdb.com/title/{movie['imdbID']}\n")

def main():
    genre = input('Enter a movie genre (e.g., Action, Comedy, Horror): ').strip()
    recommend_movie(genre)

if __name__ == "__main__":
    main()




