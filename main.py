import requests
from bs4 import BeautifulSoup
from collections import Counter
from string import punctuation
import nltk
import csv

nltk.download('stopwords')
from nltk.corpus import stopwords

# Load the list of stopwords
stopwords_set = set(stopwords.words('english'))

# Function to clean and split text into words
def get_clean_words(text):
    return (x.rstrip(punctuation).title() for x in text.split() if x.rstrip(punctuation).lower() not in stopwords_set)

# Function to count words in text
def count_words(text):
    return Counter(get_clean_words(text))

# Function to get unique text from the HTML
def get_unique_text(soup):
    texts = set(soup.stripped_strings)  # Use a set to avoid duplicates
    return ' '.join(texts)

# Function to save word counts to file
def save_word_counts(word_counts, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        for word, count in word_counts.items():
            writer.writerow([word, count])

# Main script execution
# Replace `while True:` with a loop for a single iteration for testing
for _ in range(1):
    # Get the url content
    r = requests.get("http://localhost:8000/sample_website.html")  # Update with your local or actual URL
    soup = BeautifulSoup(r.content, "html.parser")

    # Get unique text from the HTML content
    unique_text = get_unique_text(soup)

    # Count words in the unique text
    word_counts = count_words(unique_text)

    # Save word counts
    save_word_counts(word_counts, "word_counts.txt")

    # No need to sleep since this is a single iteration for testing
    # time.sleep(10)

# Print message to indicate the script has finished running
print("Script completed and word counts have been saved.")
