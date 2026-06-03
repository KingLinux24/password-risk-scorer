import getpass
from src.scoring.risk import score

def main():
    pw = getpass.getpass("Enter password (input hidden): ")
    result = score(pw)
    print(result)

if __name__ == "__main__":
    main()
