# 🔐 Random Password Generator (Python)

This is a simple password generator script I wrote in Python. It creates a secure, random password with a mix of uppercase letters, lowercase letters, digits, and special characters — based on the total length you choose.

## 🧠 Why I Made This

I made this project to practice using the `string` and `random` modules in Python, and to get more comfortable with:
- Working with lists and character sets
- Taking and validating user input
- Writing logic to meet specific conditions (like % splits)
- Shuffling data and creating randomized output

Plus, I wanted a quick way to generate secure passwords!

## 💡 How It Works

1. The script imports all character types using the `string` module.
2. It asks the user for the desired password length.
3. It makes sure the length is at least 8 characters (recommended minimum).
4. It randomly shuffles character sets (letters, digits, punctuation).
5. It builds the password with:
   - **60% letters** (30% lowercase + 30% uppercase)
   - **40% digits and symbols** (20% each)
6. It shuffles the final result and prints out the generated password.
