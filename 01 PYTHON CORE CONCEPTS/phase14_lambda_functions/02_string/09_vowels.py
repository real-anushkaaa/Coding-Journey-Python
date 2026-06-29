# ----------------------------------------
# Create lambda function to count vowels.
# ----------------------------------------

count_vowel = lambda text: sum(1 for ch in text if ch.lower() in "aeiou")

print(count_vowel("anushka"))