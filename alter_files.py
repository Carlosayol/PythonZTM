path = '.../dbfiles'
for filename in os.listdir(path):
for i in os.listdir(path):
    if i.endswith(".txt"):
        with open(i, 'r') as f_in:
            for line in f_in:
               line=tweet_to_words(line).encode('utf-8')
               open(i, 'w').write(line)