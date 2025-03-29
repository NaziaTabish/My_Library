import streamlit as st
st.title("Personal Library Manager")
if 'library' not in st.session_state:
    st.session_state.library = []
def display_books():
    if len(st.session_state.library) == 0:
        st.write("No books in the library.")
    else:
        st.write("Your Library:")
        for i, book in enumerate(st.session_state.library, 1):
            st.write(f"{i}. {book['title']} by {book['author']}")
def add_book(title, author):
    st.session_state.library.append({"title": title, "author": author})
    st.success(f"Book '{title}' by {author} added successfully!")
def delete_book(book_index):
    if 0 <= book_index < len(st.session_state.library):
        removed_book = st.session_state.library.pop(book_index)
        st.success(f"Book '{removed_book['title']}' deleted successfully!")
    else:
        st.error("Invalid book selection.")
with st.form(key="add_book_form"):
    st.subheader("Add a New Book")
    title = st.text_input("Book Title")
    author = st.text_input("Author Name")
    submit_button = st.form_submit_button("Add Book")

    if submit_button and title and author:
        add_book(title, author)
st.subheader("Delete a Book")
book_to_delete = st.selectbox("Select a book to delete", [f"{book['title']} by {book['author']}" for book in st.session_state.library] + ["Select a book to delete"])
if book_to_delete != "Select a book to delete":
    delete_button = st.button("Delete Selected Book")
    if delete_button:
        book_index = [f"{book['title']} by {book['author']}" for book in st.session_state.library].index(book_to_delete)
        delete_book(book_index)
display_books()
