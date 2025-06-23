import json
#TODO: 用load讀取錯誤的資料，並修改字典內容，再用dump轉成正確的json格式存成檔案
jsonFile = open('wrong_pokedex.json','r', encoding='utf-8')
data = json.__(1)__(jsonFile)
data['寶可夢資料']['妙蛙種子'][__(2)__] = __(2)__
data['寶可夢資料']['小火龍'][__(3)__] = __(3)__
data['寶可夢資料']['傑尼龜'][__(4)__] = __(4)__

new_jsonFile = open('right_pokedex.json','w', encoding='utf-8')
json.__(5)__(data, new_jsonFile, ensure_ascii=False, indent=2)