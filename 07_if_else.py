print("=== 寶可夢治療 ===")

# 輸入資料
name = input("寶可夢名稱：")
hp = int(input("HP值："))

print(f"\n{name} 的HP是 {hp}")

# 判斷寶可夢所需治療
__(1)__ # 如果hp<=0
    print("昏厥了！需要治療")
    
__(2)__ # 如果hp<50
    print("受傷了，要休息")
    
__(3)__ # 其它
    print("很健康！")