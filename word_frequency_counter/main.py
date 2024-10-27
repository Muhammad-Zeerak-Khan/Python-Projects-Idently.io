import re
import os
import PyPDF2
import logging

from collections import Counter
from dataclasses import dataclass

@dataclass
class WordFrequencyCounter:
    input_file_path: str 

    def get_frequency(self, text: str) -> list[tuple[str, int]]:
        lowered_text: str = text.lower()
        words : list[str] = re.findall(r'\b\w+\b', lowered_text)
        word_count: Counter = Counter(words)

        return word_count.most_common()

    def read_directly_from_user_string(self) -> None:
        input_text: str = input("Enter your text: ").strip() # Removes leading and trailing whitespaces

        word_frequencies: list[tuple[str, int]] = self.get_frequency(input_text)
        print(word_frequencies)
        for word, count in word_frequencies:
            print(f" {word} : {count}")


    def read_from_text_file(self) -> None:
        input_string: str = ""
        with open(self.input_file_path, 'r') as file:
            input_string += file.read()
            input_string = input_string.replace("\n", " ")
            input_string = input_string.strip()
            #word_count = self.get_frequency(input_string)
        
        return input_string

    def read_from_pdf_file(self) -> None:
        # Creating a pdf reader object
        reader = PyPDF2.PdfReader(self.input_file_path)

        # Looping through the page
        total_text: str = ""
        for page in range(len(reader.pages)):
            total_text += reader.pages[page].extract_text()
        return total_text    




if __name__ == "__main__":
    input_file: str = input("Please enter the text file path: ")
    word_frequency_counter: WordFrequencyCounter = WordFrequencyCounter(input_file)
    file_type = os.path.basename(input_file)

    if file_type.endswith(".pdf"):
        text_input = word_frequency_counter.read_from_pdf_file()
    elif file_type.endswith(".txt"):
        text_input = word_frequency_counter.read_from_text_file()
    total_word_count: int = len(text_input)    
    most_common_words = word_frequency_counter.get_frequency(text_input)
    print(f"The total number of words in the document is : {total_word_count}\n")
    print(most_common_words)


"""
Create a function that allows the user to read a file directly (such as text)
so that the user doesnot have to copy and paste text
"""