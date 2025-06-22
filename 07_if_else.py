print("=== 寶可夢治療 ===")

# 輸入資料
name = input("寶可夢名稱：")
hp = int(input("HP值："))

print(f"\n{name} 的HP是 {hp}")

# 判斷寶可夢所需治療
if hp == 0: # 如果hp為0
    print("昏厥了！需要治療")
    
elif hp < 50: # 如果hp<50
    print("受傷了，要休息")
    
else: # 其它
    print("很健康！")