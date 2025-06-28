#TODO: 完成建立類別，並且創建新的寶可夢
class Pokemon:
    def __init__(self, pokemon_name, pokemon_type, pokemon_weak):
        self.pokemon_name = pokemon_name
        self.pokemon_type = __(1)__
        self.pokemon_weak = __(2)__ 

    def introduction(self):
        print(f"__(3)__")
    
    def move(self, move_name):
        print(f"__(4)__")

# 建立新的寶可夢
pikachu = Pokemon(__(5)__)
pikachu.introduction()
pikachu.move("耍憨")

'''
範例輸出:
皮卡丘的屬性是電, 弱點是地面。
皮卡丘使用了「耍憨」招式！
'''