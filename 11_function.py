#TODO:設計函式印出該寶可夢的詳細資訊
def print_pokemon_info(pokemon_name, pokedex):
    #TODO...

pokemon_dictionary = {
    "皮卡丘": {"屬性": "電", "等級": 25, "招式": ["電擊", "十萬伏特"]},
    "妙蛙種子": {"屬性": "草", "等級": 16, "招式": ["藤鞭", "種子機關槍"]},
    "小火龍": {"屬性": "火", "等級": 18, "招式": ["噴射火焰", "火花"]},
    "傑尼龜": {"屬性": "水", "等級": 20, "招式": ["水槍", "泡沫"]},
}

input_pokemon = input("歡迎來到寶可夢圖鑑，請輸入寶可夢名稱：")
print_pokemon_info(input_pokemon, pokemon_dictionary)