def word_counter(a_string):
    words = a_string.split()
    word_count = len(words)
    return word_count

#Testing
some_text = "Hello World, its me."
print(word_counter(some_text))
