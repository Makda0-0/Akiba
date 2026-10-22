import string

def clean(text):
   
   
    for p in string.punctuation:
        text = text.replace(p, "")
    # Return lowercase version
    return text.lower()


def count_words(text):
    return len(clean(text).split())


def count_characters(text):
  
    return len(clean(text).replace(" ", ""))


def count_vowels_consonants(text):
    vowels = 0
    consonants = 0
    for ch in clean(text):
        if ch.isalpha():
            if ch in "aeiou":
                vowels += 1
            else:
                consonants += 1
    return vowels, consonants


def longest_word(text):
    longest = ""
    for word in clean(text).split():
        if len(word) > len(longest):
            longest = word
    return longest


def word_frequency(text):
    freq = {}
    for word in clean(text).split():
        if word in freq:
            freq[word] = freq[word] + 1
        else:
            freq[word] = 1
    return freq


def repeated_words(text):
    freq = word_frequency(text)
    repeated = []
    for word in freq:
        if freq[word] > 1:
            repeated.append(word)
    return repeated


def top_five_words(text):
    freq = word_frequency(text)
 
    pairs = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return pairs[:5]



paragraph = "Python is useful and Python is powerful."

print("Words:", count_words(paragraph))
print("Characters (no spaces):", count_characters(paragraph))

v, c = count_vowels_consonants(paragraph)
print("Vowels:", v, "| Consonants:", c)

print("Longest word:", longest_word(paragraph))
print("Repeated words:", repeated_words(paragraph))
print("Word frequency:", word_frequency(paragraph))
print("Top 5 words:", top_five_words(paragraph))