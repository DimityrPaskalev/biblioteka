import streamlit as st
books = [
    "The Hobbit",
    "1984",
    "Pride and Prejudice",
    "To Kill a Mockingbird",
    "The Great Gatsby"
]
st.title(" Book Checker App")
new_book = st.text_input("Enter a book to add")
if st.button("Add Book"):
    if new_book.strip() == "":
        st.warning("Please enter a book title.")
    else:
        books.append(new_book)   
        st.success(f'"{new_book}" added to the list!')
check_book = st.text_input("Enter a book to check")
if st.button("Check Book"):
    if check_book in books:
        st.success("The book exists in the database!")
    else:
        st.error("The book is NOT in the database!")
if st.button("Show All Books"):
    st.write(books)
