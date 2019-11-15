data = """
park 800804-1003040
kim 802923-1231111
"""

result = []
for line in data.split("\n"):
    word_result = []
    for word in line.split(" "):
        if len(word) == 14 and word[:6].isdigit() and word[7:].isdigit():
            word = word[:6] + "-"  + "*******"
        word_result.append(word)
    result.append(" ".join(word_result))

print("\n".join(result))