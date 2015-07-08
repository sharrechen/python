__author__ = 'sharon'

def censor(text, word):
    text = text.split()
    for index, item in enumerate(text):
        if item == word:
            text[index] = "*" * len(item)
    return " ".join(text)

 # practice to write item count in list; similar to list.count()
def count(sequence, item):
    found = 0
    for i in sequence:
        if i == item:
            found += 1
    return found

def purify(num_list):
    even_num = []
    for i in num_list:
        if (i & 1) == 0:
            even_num.append(i)
    return even_num

def product(num_list):
    multiply = 1
    for i in num_list:
        multiply *= i
    return multiply

def remove_duplicates(item_list):
    return list(set(item_list))

def median(num_list):
    sorted_num = sorted(num_list)
    num_len = len(sorted_num)
    if num_len & 1:
        return sorted_num[num_len/2]
    else:
        index = int(num_len/2)
        return (sorted_num[index] + sorted_num[index-1]) / 2.0

def get_middles(sequence):
    first, *middles, last = sequence  # python3
    return middles

if __name__ == "__main__":
    text = "this hack is wack hack"
    word = "hack"
    string = censor(text, word)
    print(string)
    print(median([4, 5, 5, 4]))
    print(get_middles([1, 2, 3, 4, 5, 6, 7]))