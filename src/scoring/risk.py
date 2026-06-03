from src.features.extract import extract_features
from src.scoring.exposure import breached

def score(password: str) -> dict:
    f = extract_features(password)
    risk = 0.0
    reasons = []

    if f["length"] < 12:
        risk += 0.25
        reasons.append("Password is shorter than recommended length")

    if f["char_classes"] < 3:
        risk += 0.2
        reasons.append("Limited character diversity")

    if f["has_dictionary_word"]:
        risk += 0.2
        reasons.append("Contains common dictionary words")

    if f["has_repetition"]:
        risk += 0.15
        reasons.append("Repeated character patterns detected")

    if breached(password):
        risk += 0.4
        reasons.append("Password appears in known breach datasets")

    risk = min(risk, 1.0)

    if risk < 0.3:
        level = "low"
    elif risk < 0.6:
        level = "medium"
    else:
        level = "high"

    return {
        "risk_score": round(risk, 2),
        "risk_level": level,
        "reasons": reasons
    }
