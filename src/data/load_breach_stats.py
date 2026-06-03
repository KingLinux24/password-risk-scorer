import hashlib
from pathlib import Path

OUT = Path("data/processed/breach_hashes.txt")
OUT.parent.mkdir(parents=True, exist_ok=True)

COMMON_PASSWORDS = [
    "password", "123456", "qwerty", "letmein", "admin", "welcome"
]

def hash_pw(pw: str) -> str:
    return hashlib.sha256(pw.encode("utf-8")).hexdigest()

def main():
    with OUT.open("w") as f:
        for pw in COMMON_PASSWORDS:
            f.write(hash_pw(pw) + "\n")

if __name__ == "__main__":
    main()
