# TODO1: 創建寶可夢圖鑑
pokemons = __(1)__

'''
圖鑑內容：
皮卡丘: Lv.25
傑尼龜: Lv.18
小火龍: Lv.22
妙蛙種子: Lv.20
格式：{"寶可夢名稱", 等級}
等級只需用數字創建就好，不需包含Lv.
'''

# 印出目前的寶可夢圖鑑
print("===寶可夢圖鑑管理系統===")
for pokemon, level in pokemons.items():
    print(f"{pokemon}: Lv.{level}")

# 寶可夢升級 （修改字典）
print("\n--- 寶可夢升級 ---")
upgrade_pokemon = input("請輸入要升級的寶可夢名稱：")
if upgrade_pokemon in pokemons:
    new_level = int(input("請輸入新的的等級："))
    # TODO2: 修改寶可夢等級
    pokemons__(2)__ = __(3)__
    print(f"{upgrade_pokemon} 升級到 Lv.{new_level} 了！")

# 釋放寶可夢 （刪除字典）
print("\n--- 釋放寶可夢 ---")
release_pokemon = input("請輸入要釋放的寶可夢名稱：")
if release_pokemon in pokemons:
    # TODO3: 刪除寶可夢
    __(4)__
    print(f"{release_pokemon} 已被釋放到野外！")

# 印出修改後的寶可夢圖鑑
print("\n===更新後的圖鑑===")
for pokemon, level in pokemons.items():
    print(f"{pokemon}: Lv.{level}")