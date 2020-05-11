import sys, os
from matplotlib import pyplot as plt

# USAGE:
# python plotppl.py [train log file] [save file] [model name]

assert len(sys.argv) == 4, "need 3 arguments"
update_list = []
ppl_list = []

def strip_clean(word):
    return word.strip("\n").strip("{").strip("}").strip(" ").strip(":").strip(",").strip('"')

def get_ppl(word_list):
    found = False
    for word in word_list:

        if found:
            return float(strip_clean(word))

        if strip_clean(word) == "valid_ppl":
            found = True

    return None

def get_update(word_list):
    found = False
    for word in word_list:

        if found:
            return int(strip_clean(word))

        if strip_clean(word) == "valid_num_updates":
            found = True

    return None

with open(sys.argv[1], "r") as readfile:
    for line in readfile:
        words = line.split(" ")
        if "INFO" in words and "valid" in words:
            update_list.append(get_update(words))
            ppl_list.append(get_ppl(words))

fig, ax = plt.subplots()
ax.plot(update_list, ppl_list)

ax.set(xlabel='After Update (updates)', ylabel='Perplexity',
       title=sys.argv[3] + " perplexity history")
ax.grid()

fig.savefig(sys.argv[2], format="jpg")
plt.show()