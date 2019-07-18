import json

with open('papers.json', encoding='utf-8') as file:
    j = json.load(file)

    out = open('titles.txt', 'w', encoding='utf-8')
    for item in j.values():
        if item['type'] == 'paper':
            out.write(item['title'])
            out.write('\n')

    out.close()