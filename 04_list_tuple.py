name1 = "大比鳥"
height1 = 1.5
weight1 = 39.5
# 創建大比鳥的資訊元組(tuple)，順序：name, height, weight
information_tuple = ???


name2 = "妙蛙草"
height2 = 1.0
weight2 = 13.0
# 創建妙蛙草的資訊串列(list)，順序：name, height, weight
information_list = ???

assert isinstance(information_tuple, tuple), "information_tuple 不是 tuple"
assert isinstance(information_list, list), "information_list 不是 list"

print(f"-----大比鳥-----")
print(f"姓名：{information_tuple[0]}")
print(f"身高：{information_tuple[1]}")
print(f"體重：{information_tuple[2]}")

print(f"------妙蛙草-----")
print(f"姓名：{information_list[0]}")
print(f"身高：{information_list[1]}")
print(f"體重：{information_list[2]}")