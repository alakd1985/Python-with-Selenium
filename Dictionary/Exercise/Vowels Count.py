word = input('Enter any word::')
vowel = {'a', 'e', 'i', 'o', 'u'}
d = {}
for ch in word:
    if ch in vowel:
        d[ch] = d.get(ch, 0) + 1
        # if vowel found in the word then it will start counting from 0 and increases by one.
        # increased number replaces the old value
print(d)
for k, v in d.items():
    print(k, 'occurs', v, 'times')
