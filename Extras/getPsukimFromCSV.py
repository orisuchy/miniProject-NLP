import pandas as pd

df = pd.read_csv("Ach.csv", names=['path', 'text'])


# genesis = df[df['path'].str.contains("בראשית")]
text_file = open("sample.txt", "w", encoding='utf-8')
for line in df['text']:
    # print(line)
    line = line.replace('*', '')
    line = line.replace('[', '')
    line = line.replace(']', '')
    line = line.replace('(', '')
    line = line.replace(')', '')
    text_file.write(line + " ")
text_file.close()

words_seen = set()
with open("sample.txt", "r+", encoding='utf-8') as f:
    d = f.readlines()
    for line in d:
        for word in line.split():
            # word.replace('*', '')
            if word not in words_seen:
                f.write(word)
                words_seen.add(word)
    # d = f.readlines()
    # f.seek(0)
    # for i in d:
    #     if i not in lines_seen:
    #         f.write(i)
    #         lines_seen.add(i)
    # f.truncate()
f.close()
print(words_seen)
with open("sample_sorted.txt", "w", encoding='utf-8') as s:
    for i, w in enumerate(sorted(words_seen)):
        s.write(str(i) + "\t" +w+'\n')
s.close()
