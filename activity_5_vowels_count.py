#for a word, count the number of vowels
def count_vowels(word):
    vowels = "aeiou"
    count = 0
    for alpha in word:
        if alpha in vowels:
            count += 1

    return count
        
print(count_vowels("umbrella"))