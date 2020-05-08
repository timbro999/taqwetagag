import random

sentence_list = []


def noun_gen(lang_ft):
    ran_num = random.randint(0, 9)
    i = ran_num
    lang_ft = open("{}.txt".format(lang_ft))
    list_1 = lang_ft.read().split(";")

    sentence_list.append(list_1[i])


def start_gen():
    list.clear(sentence_list)
    x = 0

    while x < 100:

        type_word = random.randint(0, 2)
        if type_word == 0:
            noun_gen("adjectives")
        if type_word == 1:
            noun_gen("nouns")
        if type_word == 2:
            noun_gen("verbs")
        x += 1
        if x == 100:
            print(sentence_list)
