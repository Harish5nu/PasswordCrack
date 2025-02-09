import hashlib

def crack_hash(hash_to_crack, wordlist):
    """Attempt to crack an MD5 hash using a wordlist."""
    try:
        with open(wordlist, "r", encoding="latin-1") as file:  # FIXED Encoding Issue
            for word in file:
                word = word.strip()
                hashed_word = hashlib.md5(word.encode()).hexdigest()
                if hashed_word == hash_to_crack:
                    return f"[+] Password found: {word}"
    except FileNotFoundError:
        return "[-] Wordlist file not found."
    
    return "[-] Password not found in wordlist."

if __name__ == "__main__":
    hash_input = input("Enter the MD5 hash to crack: ")
    wordlist_path = input("Enter the path to the wordlist file: ")
    result = crack_hash(hash_input, wordlist_path)
    print(result)
