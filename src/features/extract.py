import math
import re
from collections import Counter

def entropy(password: str) -> float:
    counts = Counter(password)
    length = len(password)
    return -sum((c/length) * math.log2(c/length) for c in counts.values())

def has_dictionary_word(password: str) -> bool:
    dictionary = ["password", "admin", "welcome", "login"]
    p = password.lower()
    return any(word in p for word in dictionary)

def char_classes(password: str) -> int:
    classes = 0
    classes += bool(re.search(r"[a-z]", password))
    classes += bool(re.search(r"[A-Z]", password))
    classes += bool(re.search(r"[0-9]", password))
    classes += bool(re.search(r"[^a-zA-Z0-9]", password))
    return classes

def extract_features(password: str) -> dict:
    return {
        "length": len(password),
        "entropy": entropy(password),
        "char_classes": char_classes(password),
        "has_dictionary_word": int(has_dictionary_word(password)),
        "has_repetition": int(bool(re.search(r"(.)\1{2,}", password))),
    }
