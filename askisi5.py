import string


def stringchange(line):
    for character in string.punctuation:
        line = line.replace(character, " ")
    return line


word_count = {}
twoletters_count = {}
threeletters_count = {}

def sortword(dictionary):
    sorted_values = []
    for key in dictionary:
        sorted_values.append((dictionary[key], key))
    sorted_values = sorted(sorted_values)
    sorted_values = sorted_values[::-1]
    return sorted_values




with open("two_cities_ascii.txt", 'r') as fi:
    for line in fi:
        line = stringchange(line)
        words = line.split()

        for word in words:
            word = word.lower()
            twochars = word[0:2]
            if (len(word)>2):
              threechars = word[0:3]

            if twochars in twoletters_count:
                twoletters_count[twochars] += 1
            else:
                twoletters_count[twochars] = 0

            if threechars in threeletters_count:
                threeletters_count[threechars] += 1
            else:
                threeletters_count[threechars] = 0


            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 0


top_words = sortword(word_count)[:10]
top_two = sortword(twoletters_count)[:3]
top_three = sortword(threeletters_count)[:3]

print("The ten most used words are:")
for tuple_freq in top_words:
    count, word = tuple_freq
    print("{0:15}{1:8d}".format(word, count))

print("The three most used first two letters are:")
for tuple_freq in top_two:
    count, twochars = tuple_freq
    print("{0:15}{1:8d}".format(twochars, count))

print("The three most used first three letters are:")
for tuple_freq in top_three:
    count, threechars = tuple_freq
    print("{0:15}{1:8d}".format(threechars, count))






