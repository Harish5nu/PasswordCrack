import hashlib

def generate_md5(password):
    return hashlib.md5(password.encode()).hexdigest()

def crack_hash(md5_hash, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='latin-1') as file:
            for word in file:
                word = word.strip()
                if generate_md5(word) == md5_hash:
                    return word
        return None
    except FileNotFoundError:
        print(f"Error: The wordlist file at '{wordlist_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def main():
    print("Welcome to MD5 Hash Generator and Cracker!")
    print("1. Generate MD5 Hash for a Password")
    print("2. Crack An MD5 Hash using a Wordlist")

    option = input("Choose an option (1 or 2): ")

    if option == '1':
        password = input("Enter the password to generate it's MD5 hash: ")
        hashed_password = generate_md5(password)
        print(f"MD5 Hash of '{password}': {hashed_password}")

    elif option == '2':
        md5_hash = input("Enter the MD5 hash to crack: ")
        wordlist_path = input("Enter the path to the wordlist file (e.g., 'rockyou.txt'): ")
        
        result = crack_hash(md5_hash, wordlist_path)
        
        if result:
            print(f"Password found: {result}")
        else:
            print("Password not found.")
    
    else:
        print("Invalid option! Please choose either 1 or 2.")

if __name__ == "__main__":
    main()
