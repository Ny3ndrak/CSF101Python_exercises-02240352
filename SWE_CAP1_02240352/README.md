
This project aims to clean and spell-check a given dictionary text file. It includes scripts to convert `.docx` files to `.txt` format, remove unwanted noise, and check the spellings.

## Features

- **Convert `.docx` to `.txt`**: Using the `python-docx` library, i converted dictionary document to a text file.
- **Clean Text**: Removed unwanted characters, numbers, and extra whitespace from text files.
- **Spell Checker**: Extract unique words and identify potential misspellings by comparing two text files.

# 1. Read the input file
# Import the necessary library.
# Define the URL of the file to download.
# Make the GET request to the URL.
# Open (or create) the target file in write-binary mode.
# Write the content of the response to the file.
# Print a confirmation message.

# Step 1: Import the requests Library
First, ensure you’ve imported the requests library, which is essential for making HTTP requests.

import requests
# Step 2: Define the URL
Specify the URL from which you want to download the file.
url = 'https://csf101-server-cap1.onrender.com/get/input/352'

# Step 3: Make the HTTP GET Request
Use the requests.get() method to make a GET request to the specified URL. This method returns a response object that contains the server's response to the request.
txt_file = requests.get(url)

# Step 4: Open the Output File
Open a new file (or overwrite an existing one) in binary write mode ('wb'). This is where the content from the URL will be saved.
with open('352.txt', 'wb') as file:

# Step 5: Write the Content to the File
Write the content of the response object to the file using the write method.
    data = file.write(txt_file.content)

# Step 6: Confirm the Download
Print a message to confirm that the file has been successfully downloaded.
print('Downloaded 352.txt')


# 2. clean the dictionary
# Define a function to clean text by extracting the first word of each line.
# Open the input file and read each line.
# Extract the first word of each line and store it in a list.\
# Open the output file and write the cleaned words to it.
# Call the function with the specified input and output file names.

# Step 1: Define the Function
First, you define a function named clean_text which will take two arguments: input_file and output_file.
def clean_text(input_file, output_file):
    cleaned_words = []
Function Definition: The function is defined to accept two parameters: input_file (the file to read from) and output_file (the file to write to).

Initialize List: cleaned_words is an empty list that will store the cleaned words.

# Step 2: Open the Input File
You then open the input file to read its content.
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            words = line.split()
            if words:
                dzongkha_word = words[0]
                cleaned_words.append(dzongkha_word)
Open File: with open(input_file, 'r', encoding='utf-8') as file: opens the file in read mode with UTF-8 encoding.
Iterate Lines: for line in file: iterates through each line in the file.
Split Line: words = line.split() splits the line into individual words.
Check Words: if words: checks if the line has any words.
Extract First Word: dzongkha_word = words[0] takes the first word from the line.
Append to List: cleaned_words.append(dzongkha_word) adds the extracted word to the cleaned_words list.

# Step 3: Open the Output File
Next, you open the output file to write the cleaned words.
    with open(output_file, 'w', encoding="utf-8") as file:
        for words in cleaned_words:
            file.write(words + "\n")
        print(f"cleaned words saved to {output_file}")
Open File: with open(output_file, 'w', encoding="utf-8") as file: opens the file in write mode with UTF-8 encoding.
Write Words: for words in cleaned_words: iterates through the cleaned words list.
Write to File: file.write(words + "\n") writes each word to the output file, followed by a newline.
Print Confirmation: print(f"cleaned words saved to {output_file}") prints a message indicating that the cleaned words have been saved to the output file.

# Step 4: Define File Paths
You specify the input and output file names.
input_file = "dzo.txt"
output_file = "clean.txt"
Input File: input_file is set to "dzo.txt".
Output File: output_file is set to "clean.txt".

# Step 5: Call the Function
Finally, you call the clean_text function with the specified file names.
clean_text(input_file, output_file)
Function Call: clean_text(input_file, output_file) executes the function, passing the input and output file names as arguments.

# Read cleaned_dictionary.txt into python
# Import the re module for regular expressions.
# Define a function to extract unique Dzongkha words.
# Read and process 352.txt to extract words.
# Read and process cleaneddict.txt to extract words.
# Find words unique to 352.txt.
# Print the unique words indicating they are incorrect.

# 3.Step 1: Import the re Library
First, you import the regular expressions module to work with text patterns.
import re

# Step 2: Define the extract_words Function
This function extracts words from the provided text using a specific Unicode range (for Dzongkha script).
def extract_words(text):
    words = re.findall(r'[\u0F00-\u0FFF]+', text)
    return set(words)
Function Name: extract_words
Parameter: text (the input string to process)
Regex Pattern: r'[\u0F00-\u0FFF]+' matches Dzongkha characters.
Return Set: Converts the list of matched words to a set to ensure uniqueness.

# Step 3: Read the First File (352.txt)
You open the first file, read its content, and extract words using the defined function.

with open("352.txt", encoding="utf-8") as file:
    content1 = file.read()
    word1 = extract_words(content1)
Open File: with open("352.txt", encoding="utf-8") as file: opens 352.txt in read mode.
Read Content: content1 = file.read() reads the entire content of the file into a variable.
Extract Words: word1 = extract_words(content1) extracts unique Dzongkha words from the file content.

# Step 4: Read the Second File (cleaneddict.txt)
Similarly, you open the second file, read its content, and extract words.
with open("cleaneddict.txt", encoding="utf-8") as file:
    content2 = file.read()
    word2 = extract_words(content2)
Open File: with open("cleaneddict.txt", encoding="utf-8") as file: opens cleaneddict.txt in read mode.
Read Content: content2 = file.read() reads the entire content of the file into a variable.
Extract Words: word2 = extract_words(content2) extracts unique Dzongkha words from the file content.

# Step 5: Find Words Unique to the First File
You compare the sets of words extracted from both files to find words that are only in the first file.
unique_to_file1 = word1.difference(word2)
Set Difference: unique_to_file1 = word1.difference(word2) finds words that are in word1 but not in word2.

# Step 6: Print the Unique Words
Finally, you print each word that is unique to the first file, indicating it is incorrect.
 for word in unique_to_file1:
    print(f"The word '{word}' is incorrect.")
Iterate and Print: for word in unique_to_file1: loops through the unique words.
Print Statement: print(f"The word '{word}' is incorrect.") prints each unique word with a message.