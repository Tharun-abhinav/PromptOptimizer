import re
from symspellpy import SymSpell, Verbosity

# Initialize SymSpell
sym_spell = SymSpell()
# Load default dictionary
sym_spell.load_dictionary()

def preprocess_text(text):
    # Remove unnecessary spaces, including newlines and multiple spaces
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def spell_correct(text):
    words = text.split()
    corrected_words = []
    for word in words:
        # Get suggestions for the word
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions:
            # Use the first suggestion (most likely correction)
            corrected_words.append(suggestions[0].term)
        else:
            # If no suggestions found, keep the original word
            corrected_words.append(word)
    return " ".join(corrected_words)

def optimize_prompt(prompt):
    # First, remove unnecessary spaces
    processed_prompt = preprocess_text(prompt)
    # Then, apply spell correction
    corrected_prompt = spell_correct(processed_prompt)
    return corrected_prompt 