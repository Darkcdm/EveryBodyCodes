input = "ACCBBACCBBCACBBAABCABBBCBBBACBCAABACABCABBACCBAABCAABCBBBCACBCAAACBABCACCBABBAABCCBBBABABBACBBBBCBAACACAABCABBBBCAAABBABCCBACCACACBCCACAAACCAAABACCBAAAACCCCACCABBCBCACAABBCCBCCBABCACCACACABACCCBBBCBABBBBAAAAAABBABBCBACBCAABABCBCBBBBBACAAAABCCABBAABBBBBCBABCBCCCCCABCAAAABACBAAABBBCABCCCAACABCAAACCBCBBAABABCAAABBBACBACBCBCCABABCBBCAAACACBCACCACAACCBCACCBABAAACBBABBCCBABAABBCCCAAABAABAABCABBACABAAACBACCAAABBAACCBCBCBCCBAABABBCBAAAABBACABBABCAAABABAAAABACBBAABBBACABCBABBCCCABCBAABCBAABCBCCBBCAACCBCCABBBCAABCACCBBABBBACCCAABACAAAACCCBBBACCABACBAAACABCACCCBCCBBBCACACBABBCCABCAABBCBCCBBABCCCBBCACABBCCBCBAAABCBBCAAACCCACCAAACBCCCAAAACCCCACCCBCABBABACCBABABCCBABBBBBBACBABBBCABABACAABCCACCBBAAABAAAAACCAAABCCAABABACCCABCABAABACBBCACACABAABCABABCCCBCCCCABBCCCBAACBCBCCBBCAAABBBBBCBBABABBBCABBCABCBBBCCACBBCACABBBABBCBBABAAACCCCCCABACCCABAAABABBACCCABABCAAACCCBBACBABCAAABAAAACACCBBBBAACBBBCCBABACACBBACCBBCBACABABBCCBBBCCAABBBAACCBBCCCCAABABAAACACBBACACBBCBBAACCABCABBBBCABABBBACACCCCCCAABACABAABABCABA"
testInput = "ABBAC"
def getHealthPotions(input:str):
    sum = 0
    for char in input:
        if char == "A":
            sum += 0
            continue

        if char == "B":
            sum += 1
            continue

        if char == "C":
            sum += 3
            continue 

    return sum



print(getHealthPotions(testInput))
print(getHealthPotions(input))