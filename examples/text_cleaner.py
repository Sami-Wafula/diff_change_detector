import string
import re

def clean_text_data(raw_text):
    """
    Standardizes a block of text for natural language processing.
    """
    # 1. Handle empty input
    if not raw_text or not isinstance(raw_text, str):
        return ""

    # 2. Convert to lowercase for consistency
    text = raw_text.lower()

    # 3. Remove punctuation using a translation table
    # string.punctuation contains characters like !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # 4. Remove digits using regular expressions
    text = re.sub(r'\d+', '', text)

    # 5. Remove extra whitespaces and newlines
    # split() without arguments handles all types of whitespace
    words = text.split()
    
    # 6. Join words back into a single string with one space between them
    cleaned_text = " ".join(words)

    # 7. Basic validation: check if the result is still useful
    if len(cleaned_text) < 1:
        return "Warning: Text was cleared during cleaning."

    return cleaned_text

# Example Usage:
messy_input = "  Hello! This is an EXAMPLE... It has 123 numbers and !!! punctuation.   "
print(f"Cleaned: '{clean_text_data(messy_input)}'")
