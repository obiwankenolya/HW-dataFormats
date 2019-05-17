import json
with open ('newsafr.json') as datafile:
    json_data = json.load(datafile)
    newsstand = json_data['rss']['channel']['items']
    long_words_list = []
    unique_words_dict = {}
    top10_dict = {}
    for news in newsstand:
        words_list = news['description'].split()
        for word in words_list:
            if len(word) >= 6:
                long_words_list.append(word.capitalize())

    def get_top_10():
        for word in long_words_list:
            if word not in unique_words_dict.keys():
                unique_words_dict[word] = long_words_list.count(word)
        unique_words_count_list = sorted(unique_words_dict.values(), reverse=True)
        del(unique_words_count_list[10:])
        for value in unique_words_count_list:
            for word in unique_words_dict:
                if unique_words_dict[word] == value:
                    top10_dict[word] = value
                    break
        print(top10_dict)

    get_top_10()


import xml.etree.ElementTree as ET
tree = ET.parse('newsafr.xml')
newsstand = tree.findall('channel/item/description')
long_words_list = []
unique_words_dict = {}
top10_dict = {}
for news in newsstand:
    words_list = news.text.split()
    for word in words_list:
        if len(word) >= 6:
            long_words_list.append(word.capitalize())
get_top_10()
