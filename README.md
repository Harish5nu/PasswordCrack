# MD5 Hash Generator & Cracker

This Python program allows you to **generate MD5 hashes** and **crack MD5 hashes** using a wordlist.

## Features

1. **Generate MD5 Hash**: You can input a password, and the program will generate its MD5 hash.
2. **Crack MD5 Hash**: You can input an MD5 hash and a wordlist to attempt cracking the hash.

## Requirements

- Python 3.x installed
- A **wordlist file** (e.g., `rockyou.txt`) for cracking hashes.

## How to Use

1. Run the script:

2. Choose an option:

    Option 1: Generate MD5 hash for a password.

    Option 2: Crack an MD5 hash using a wordlist.

    Generate MD5 Hash (Option 1):

3. Enter a password, and the program will show you its MD5 hash.

    Enter the password: hello123

    MD5 Hash: e99a18c428cb38d5f260853678922e03

    Crack MD5 Hash (Option 2):

4. Enter an MD5 hash and the path to the wordlist file.

    The program will try to find the password.

    Enter MD5 hash: e99a18c428cb38d5f260853678922e03

5. Enter the wordlist file: /path/to/rockyou.txt

    Results:

If the password is found, it will display it.

If not, it will say "Password not found."
