from tkinter import *
from tkinter import Label, Text, messagebox, simpledialog
import json
import os

window = Tk()

# Defining variables
Book_title = StringVar()
Book_author = StringVar()
Publication_year = StringVar()
Search_title = StringVar()

window.geometry("1200x500")
window.title("Book Management System")

BOOKS_FILE = "books.json"

# Load books from file
def load_books():
    if os.path.exists(BOOKS_FILE):
        try:
            with open(BOOKS_FILE, 'r', encoding='utf-8') as file:
                return json.load(file)
        except:
            return []
    return []

# Save books to file
def save_books(books):
    with open(BOOKS_FILE, 'w', encoding='utf-8') as file:
        json.dump(books, file, indent=4, ensure_ascii=False)

# Register a new book
def register_book():
    title = Book_title.get().strip()
    author = Book_author.get().strip()
    year = Publication_year.get().strip()
    
    if not title or not author or not year:
        messagebox.showerror('Error', 'Please fill in all fields')
        return
    
    try:
        year_int = int(year)
        if year_int < 0 or year_int > 2100:
            messagebox.showerror('Error', 'Publication year must be between 0 and 2100')
            return
    except ValueError:
        messagebox.showerror('Error', 'Publication year must be a number')
        return
    
    books = load_books()
    books.append({
        'title': title,
        'author': author,
        'year': year_int
    })
    save_books(books)
    
    Book_title.set('')
    Book_author.set('')
    Publication_year.set('')
    messagebox.showinfo('Success', f'Book "{title}" registered successfully!')
    refresh_display()

# Show all books
def show_all_books():
    display.config(state=NORMAL)
    display.delete(1.0, END)
    
    books = load_books()
    
    if not books:
        display.insert(END, "No books registered yet.\n")
    else:
        display.insert(END, "=" * 80 + "\n")
        display.insert(END, f"{'TITLE':<30} {'AUTHOR':<25} {'YEAR':<10}\n")
        display.insert(END, "=" * 80 + "\n")
        for book in books:
            title = book['title'][:29]
            author = book['author'][:24]
            year = str(book['year'])
            display.insert(END, f"{title:<30} {author:<25} {year:<10}\n")
    
    display.config(state=DISABLED)

# Search book by title
def search_book():
    search_term = Search_title.get().strip().lower()
    
    if not search_term:
        messagebox.showwarning('Warning', 'Please enter a title to search')
        return
    
    books = load_books()
    results = [book for book in books if search_term in book['title'].lower()]
    
    display.config(state=NORMAL)
    display.delete(1.0, END)
    
    if results:
        display.insert(END, "=" * 80 + "\n")
        display.insert(END, "SEARCH RESULTS\n")
        display.insert(END, "=" * 80 + "\n")
        display.insert(END, f"{'TITLE':<30} {'AUTHOR':<25} {'YEAR':<10}\n")
        display.insert(END, "-" * 80 + "\n")
        for book in results:
            title = book['title'][:29]
            author = book['author'][:24]
            year = str(book['year'])
            display.insert(END, f"{title:<30} {author:<25} {year:<10}\n")
    else:
        display.insert(END, f"No books found matching '{search_term}'")
    
    display.config(state=DISABLED)

# Delete a book
def delete_book():
    search_term = simpledialog.askstring("Delete Book", "Enter the book title to delete:")
    
    if search_term is None:
        return
    
    search_term = search_term.strip().lower()
    books = load_books()
    original_count = len(books)
    books = [book for book in books if book['title'].lower() != search_term]
    
    if len(books) < original_count:
        save_books(books)
        messagebox.showinfo('Success', 'Book deleted successfully!')
        refresh_display()
    else:
        messagebox.showwarning('Not Found', f'No book found with title "{search_term}"')

# Refresh display with all books
def refresh_display():
    show_all_books()

# Exit program
def exit_program():
    if messagebox.askyesno('Exit', 'Are you sure you want to exit?'):
        window.quit()

# Main labels
title_label = Label(master=window, text="Book Management System", fg="white", bg="#1a5276", relief=RAISED, font=("Arial", 14, "bold"))
title_label.place(x=0, y=0, width=1200, height=40)

# Left panel - Input fields
input_frame = Label(master=window, text="Register New Book", fg="white", bg="#2c3e50", relief=RAISED, font=("Arial", 11, "bold"))
input_frame.place(x=0, y=40, width=280, height=460)

title_label = Label(master=window, text="Title:", fg="white", bg="#34495e", relief=FLAT, font=("Arial", 9))
title_label.place(x=10, y=60)
title_entry = Entry(window, textvar=Book_title, width=33)
title_entry.place(x=10, y=85)

author_label = Label(master=window, text="Author:", fg="white", bg="#34495e", relief=FLAT, font=("Arial", 9))
author_label.place(x=10, y=115)
author_entry = Entry(window, textvar=Book_author, width=33)
author_entry.place(x=10, y=140)

year_label = Label(master=window, text="Publication Year:", fg="white", bg="#34495e", relief=FLAT, font=("Arial", 9))
year_label.place(x=10, y=170)
year_entry = Entry(window, textvar=Publication_year, width=33)
year_entry.place(x=10, y=195)

# Buttons in left panel
register_btn = Button(window, relief=RAISED, text='Register Book', width=25, bg="#27ae60", fg="white", font=("Arial", 9, "bold"), command=register_book)
register_btn.place(x=10, y=235)

show_btn = Button(window, relief=RAISED, text="Show All Books", width=25, bg="#2980b9", fg="white", font=("Arial", 9, "bold"), command=show_all_books)
show_btn.place(x=10, y=275)

# Search section
search_label = Label(master=window, text="Search Book:", fg="white", bg="#34495e", relief=FLAT, font=("Arial", 9))
search_label.place(x=10, y=320)
search_entry = Entry(window, textvar=Search_title, width=33)
search_entry.place(x=10, y=345)

search_btn = Button(window, relief=RAISED, text="Search by Title", width=25, bg="#e67e22", fg="white", font=("Arial", 9, "bold"), command=search_book)
search_btn.place(x=10, y=375)

delete_btn = Button(window, relief=RAISED, text="Delete Book", width=25, bg="#c0392b", fg="white", font=("Arial", 9, "bold"), command=delete_book)
delete_btn.place(x=10, y=415)

exit_btn = Button(window, relief=RAISED, text="Exit", width=25, bg="#7f8c8d", fg="white", font=("Arial", 9, "bold"), command=exit_program)
exit_btn.place(x=10, y=455)

# Right panel - Display
display = Text(window, width=95, height=27, bg='#ecf0f1', fg='#2c3e50', font=("Courier", 9))
display.place(x=300, y=50)
display.config(state=DISABLED)

# Load and display initial books
show_all_books()

window.mainloop()


