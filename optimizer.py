import re

def rule_based_optimizer(prompt: str) -> str:
    optimized = prompt

    # Rule 1: Remove extra spaces/newlines
    optimized = re.sub(r'\s+', ' ', optimized).strip()

    # Rule 2: Replace passive voice (basic example)
    optimized = re.sub(r'\bis being\b', 'is', optimized)

    # Rule 3: Remove filler words (example)
    filler_words = ["actually", "basically", "in order to", "very", "really", "just", "simply"]
    for word in filler_words:
        optimized = re.sub(rf'\b{word}\b', '', optimized, flags=re.IGNORECASE)

    # Rule 4: Shorten phrases
    replacements = {
        "due to the fact that": "because",
        "in the event that": "if",
        "at this point in time": "now",
        "a large number of": "many",
        "has the ability to": "can"
    }

    for long, short in replacements.items():
        optimized = re.sub(long, short, optimized, flags=re.IGNORECASE)

    return optimized.strip()
