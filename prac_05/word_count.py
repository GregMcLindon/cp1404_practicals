"""CP1404 Practicals week5 - print the frequency of given words in a given sentance"""

text_dict = {}
text_input = input("Text: ")
max_word_length = 0
for word in text_input.split():
    if len(word) > max_word_length:
        max_word_length = len(word)
    try:
        text_dict[word] += 1
    except:
        text_dict[word] = 1
for word, word_count in sorted(text_dict.items()):
    print("{:{}} : {}".format(word, max_word_length, word_count))
