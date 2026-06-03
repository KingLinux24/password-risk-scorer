import hashlib
from pathlib import Path

BREACH_HASHES = Path("data/processed/breach_hashes.txt")

def sha256(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def breached(password: str) -> bool:
    h = sha256(password)
    with BREACH_HASHES.open("r") as f:
        return h in {line.strip() for line in f}
