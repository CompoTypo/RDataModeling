import io
import re


csv = open('./adult.data', 'r+')
out = open('./adult_prepped.csv', 'w+')

for line in csv:
    words = line.split(', ')
    words[-1] = words[-1].strip('\n')
    words[-1] = words[-1].replace('.','')

    for word in words:
        try:
            int(word[0])
            out.write(word + ',')
        except:
            if word == '?':
                out.write('NA,')
            else:
                out.write('\"' + word + '\",')

    out.write('\n')
