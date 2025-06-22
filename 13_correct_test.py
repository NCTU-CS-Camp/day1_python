import json
file1 = open('right_pokedex.json', 'r', encoding='utf-8')
file2 = open('answer_pokedex.json', 'r', encoding='utf-8')
data1 = json.load(file1)
data2 = json.load(file2)
if data1 == data2:
    print('恭喜你，答案正確！')
else:
    print('答案錯誤，請再檢查一次！')