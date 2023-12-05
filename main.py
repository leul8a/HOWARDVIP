# import requests
# from bs4 import BeautifulSoup
# from collections import Counter
# from string import punctuation
# import nltk
# import time
# from datetime import datetime
# import csv
#
# nltk.download('stopwords')
# from nltk.corpus import stopwords
#
# # Load the list of stopwords
# stopwords_set = set(stopwords.words('english'))
#
# # Function to clean and split text into words
# def get_clean_words(text):
#     return (x.rstrip(punctuation).title() for x in text.split() if x.rstrip(punctuation).lower() not in stopwords_set)
#
# # Function to count words in a BeautifulSoup tag collection
# def count_words(tags):
#     # Using 'string' instead of 'text' to avoid deprecation warning
#     text = (' '.join(s.findAll(string=True)) for s in tags)
#     return Counter(get_clean_words(' '.join(text)))
#
# # Functions for new functionality
# def read_max_counts(filename):
#     try:
#         with open(filename, mode='r') as infile:
#             reader = csv.reader(infile)
#             return {rows[0]: int(rows[1]) for rows in reader}
#     except FileNotFoundError:
#         return {}
#
# def update_max_counts(current_counts, max_counts):
#     deltas = {}
#     for word, count in current_counts.items():
#         previous_max = max_counts.get(word, 0)
#         deltas[word] = count - previous_max
#         if count > previous_max:
#             max_counts[word] = count
#     return deltas
#
# def save_max_counts(max_counts, filename):
#     with open(filename, mode='w') as outfile:
#         writer = csv.writer(outfile)
#         for word, count in max_counts.items():
#             writer.writerow([word, count])
#
# def save_daily_deltas(deltas, filename):
#     with open(filename, mode='a') as outfile:
#         outfile.write(f"Timestamp: {datetime.now()}\n")
#         for word, delta in deltas.items():
#             outfile.write(f"{word}: {delta}\n")
#         outfile.write("\n")
#
# # Main loop for automation
# while True:
#     # Get the url content
#     r = requests.get("http://localhost:8000/sample_website.html")  # Update with your local or actual URL
#     soup = BeautifulSoup(r.content, "html.parser")
#
#     # Count words in the full page to avoid double-counting
#     full_text = soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
#     total_counts = count_words(full_text)
#
#     # Read previous max counts
#     max_counts = read_max_counts("word_counts.txt")
#
#     # Compare and calculate deltas
#     deltas = update_max_counts(total_counts, max_counts)
#
#     # Save updated max counts
#     save_max_counts(max_counts, "word_counts.txt")
#
#     # Save daily deltas
#     save_daily_deltas(deltas, "daily_deltas.txt")
#     break
#     # Wait for a shorter period for testing purposes
#     # Change this to time.sleep(86400) for a 24-hour interval in production
#     time.sleep(10)
#
#     # Break the loop after one run for testing; remove this line for the actual use case
#
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
