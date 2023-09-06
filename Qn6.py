# # built - in

# def remove_dupliacte_and_sort(words):
#     unique_words = list(set(words))
#     unique_words.sort()
#     return unique_words


# ipstr = input('Enter a sentence: ')
# word_list = ipstr.split()
# result = remove_dupliacte_and_sort(word_list)
# print("ans:", " ".join(result))

# user-defined

def remove_dupl(words):
    unique = []
    for w in words:
        if w not in unique:
            unique.append(w)
    return unique


def sort_it(words):
    n = len(words)
    for i in range(n):
        for j in range(i+1, n):
            if words[i] > words[j]:
                words[i], words[j] = words[j], words[i]
    return words


ipstr = input("enter a sentence: ")
word_list = ipstr.split()
unique_words = remove_dupl(word_list)
sorted_words = sort_it(unique_words)
print("ans: ", " ".join(sorted_words))
