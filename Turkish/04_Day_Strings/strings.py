# 4. Gün - Metinler (Advanced Practice)

# 1. String Formatting & Escape Sequences
name = "Myrat"
age = 17
print(f"Name:\t{name}\nAge:\t{age}")

# 2. String Slicing & Reversing
language = "Python"
print("First char:", language[0])
print("First 3 chars:", language[0:3])
print("Reversed:", language[::-1])

# 3. String Methods
text = "  python programming language  "
clean_text = text.strip().title()
print("Cleaned & Titled:", clean_text)

# 4. Replace & Split
sentence = "Coding For All"
print("Replaced:", sentence.replace("Coding", "Python"))
print("Split to list:", sentence.split())

# 5. String Membership & Alignment
word = "Turkmenistan"
print("Is 'men' in word?:", "men" in word)
print("Centered:", word.center(20, "*"))
