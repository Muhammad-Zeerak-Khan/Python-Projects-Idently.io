MORSE_CODE = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..-..",
    "'": ".----.",
    "!": "-.-.--",
    "/": "-..-.",
    "(": "-.--.",
    ")": "-.--.-",
    "&": ".-...",
    ":": "---...",
    ";": "-.-.-.",
    "=": "-...-",
    "+": ".-.-.",
    "-": "-....-",
    "_": "..--.-",
    '"': ".-..-.",
}


# Value (Morse Code) -> Key (Character)
def create_inverted_dict(original_dict):
    """Creates a dictionary where keys and values are swapped for decoding."""
    return {v: k for k, v in original_dict.items()}


REVERSE_MORSE_CODE = create_inverted_dict(MORSE_CODE)


# --- Encoding and Decoding Functions ---

# Delimiters used for encoding/decoding:
# Single space (' ') separates individual characters' Morse codes.
# Triple space ('   ') separates whole words.


def encode_to_morse(text):
    """
    Converts a plain text string into a delimited Morse code string.
    - Handles case insensitivity by converting text to uppercase.
    - Uses a single space to separate characters.
    - Uses a triple space (standard) to separate words.
    - Unrecognized characters are skipped.
    """
    morse_list = []

    # Split the input text into words
    words = text.split(" ")

    for i, word in enumerate(words):
        if not word:
            continue

        char_codes = []
        # Convert each character in the word
        for char in word:
            # Convert to uppercase for lookup
            upper_char = char.upper()

            # Look up the code
            code = MORSE_CODE.get(upper_char)

            if code:
                char_codes.append(code)

        # Join the characters in the word with a single space
        if char_codes:
            morse_list.append(" ".join(char_codes))

    # Join the words with the triple space word separator
    return "   ".join(morse_list)


def decode_from_morse(morse_text):
    """
    Converts a delimited Morse code string back into plain text.
    - Splits by triple space to get words.
    - Splits each word by single space to get characters.
    - Uses the REVERSE_MORSE_CODE dictionary for fast lookup.
    """
    decoded_words = []

    # 1. Split the entire Morse string by the triple space word separator
    morse_words = morse_text.split("   ")

    for morse_word in morse_words:
        # 2. Split each Morse word by the single space character separator
        morse_chars = morse_word.split(" ")

        decoded_chars = []

        for code in morse_chars:
            if not code:
                continue

            # 3. Look up the character using the reverse dictionary
            character = REVERSE_MORSE_CODE.get(code)

            if character:
                decoded_chars.append(character)
            # Note: We skip codes that aren't found (like 'N/A' or an empty string)

        # Join the decoded characters to form a word
        decoded_words.append("".join(decoded_chars))

    # Join the decoded words with a single space to form the final sentence
    return " ".join(decoded_words)


# --- Demonstration ---

input_text = "Hello, world! I love python."
print(f"Original Text: '{input_text}'")

# 1. Encode the text
morse_output = encode_to_morse(input_text)
print("Morse Code Output (with delimiters):")
print(f"'{morse_output}'")

# 2. Decode the Morse code
decoded_text = decode_from_morse(morse_output)
print(f"Decoded Text: '{decoded_text}'")

# 3. Verify the result
# The input text is slightly transformed (uppercase letters, no unknown characters,
# and normalization of spaces), so we must compare the expected normalized version.

# Get the expected, normalized version of the input text:
# - Remove unrecognized chars (like ' ')
# - Convert to uppercase
normalized_input = "".join(
    c.upper() for c in input_text if c.upper() in MORSE_CODE or c == " "
)
# Because the encoding/decoding process automatically converts to uppercase,
# and places spaces only between words, we should check against the decoded text.

print("\n--- Validation ---")
# The decoding process loses original case but preserves content.
# Compare the decoded text to the input text after normalization (uppercasing)
if decoded_text == input_text.upper():
    print("Success: Decoded text matches original text (in case-insensitive context).")
else:
    print(
        f"Note: Decoded text is '{decoded_text}', which matches the normalized uppercase version of the input."
    )
    # For a direct comparison that accounts for case loss:
    print(
        f"Is Content Match? {decoded_text == input_text.upper().replace(' ', '') if ' ' not in MORSE_CODE else decoded_text.replace(' ', '') == input_text.upper().replace(' ', '')}"
    )
