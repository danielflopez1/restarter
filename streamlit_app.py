import streamlit as st

# Set the title of the app
st.title("Word Highlighter")

# Input field for the word
highlight_word = st.text_input("Enter a word to highlight:")

# The text where we'll highlight the word
text = "The quick brown fox jumps over the lazy dog. The dog was not impressed by the fox's agility."
text = highlight_word
# Function to highlight the word
def highlight(text, word):
    if word:
        return text
    return text

# Display the text with the highlighted word
st.markdown(highlight(text, highlight_word))
