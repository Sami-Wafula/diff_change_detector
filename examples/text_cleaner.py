import string
import re

def process_and_clean_text(input_string):
    """
    A robust text-cleaning function designed for NLP preprocessing.
    
    Operations performed:
    - Type checking and error handling.
    - Lowercasing (Case normalization).
    - Punctuation removal via translation tables.
    - Numeric digit removal via Regular Expressions.
    - Whitespace normalization (stripping and collapsing).
    """

    # 1. VALIDATION: Ensure we are working with a string to avoid crashes.
    # If the input is None or another type, we cast it or return empty.
    if input_string is None:
        return ""
    
    raw_data = str(input_string)

    # 2. NORMALIZATION: Convert everything to lowercase.
    # This ensures that 'Apple' and 'apple' are treated as the same word.
    lowered_text = raw_data.lower()

    # 3. PUNCTUATION: Create a translation table to strip symbols.
    # string.punctuation includes: !"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~
    # The third argument in maketrans specifies characters to be mapped to None.
    punctuation_table = str.maketrans('', '', string.punctuation)
    no_punc_text = lowered_text.translate(punctuation_table)

    # 4. DIGITS: Use Regex to find and remove all numbers (0-9).
    # '\d+' matches one or more consecutive digits.
    # We replace them with an empty string.
    no_numbers_text = re.sub(r'\d+', '', no_punc_text)

    # 5. WHITESPACE: Clean up messy spacing and newlines.
    # .split() splits by any whitespace (space, tab, newline).
    # This effectively removes leading/trailing spaces and internal doubles.
    words_list = no_numbers_text.split()

    # 6. RECONSTRUCTION: Join the cleaned words back into a sentence.
    # We use a single space as the delimiter.
    final_cleaned_string = " ".join(words_list)

    # 7. FINAL CHECK: Provide feedback if the text is now empty.
    # This can happen if the input was only numbers and symbols.
    if not final_cleaned_string.strip():
        return "Process Warning: Resulting string is empty."

    # Return the finalized, clean version of the text.
    return final_cleaned_string
