numcase = input()
answer = ""

for i in range(numcase):
    line = raw_input()
    line = line.split()
    word1 = line[0]
    word2 = line[1]

    no = word1 + " & " + word2 + " are NOT anagrams."
    yes = word1 + " & " + word2 + " are anagrams."
    if i < numcase -1:
        no = no + "\n"
        yes = yes + "\n"

    word1 = list(word1)
    word2 = list(word2)
    length1 = len(word1)
    length2 = len(word2)

    if length1 != length2:
        answer = answer + no
        continue
    for j in range(length1):
        subj = word1[j]
        found = 0
        k = 0
        while k < length2:
            if subj == word2[k]:
                found = 1
                del word2[k]
                length2 = length2 - 1
                break
            k = k + 1
        if found == 0:
            answer = answer + no
            break
    if found == 1:
        answer = answer +  yes

print answer
