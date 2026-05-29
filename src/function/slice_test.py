# Python slice 特性 教学代码

text = 'Python slicing example'
nums = list(range(10))

print('原始字符串:', text)
print('原始列表  :', nums)

# 基本切片: [start:stop]
print("text[0:6] =>", text[0:6])
print("nums[2:5] =>", nums[2:5])

# 省略 start 或 stop
print("text[:6] =>", text[:6])
print("text[7:] =>", text[7:])
print("nums[:4] =>", nums[:4])
print("nums[5:] =>", nums[5:])

# 负数索引
print("text[-7:-1] =>", text[-7:-1])
print("nums[-4:-1] =>", nums[-4:-1])

# 步长 step
print("text[0:18:3] =>", text[0:18:3])
print("nums[::2] =>", nums[::2])
print("nums[1::2] =>", nums[1::2])

# 反向切片
print("text[::-1] =>", text[::-1])
print("nums[::-1] =>", nums[::-1])

# 切片不会改变原始对象
slice_example = nums[3:7]
print('nums[3:7] =>', slice_example)
print('原始 nums 未改变 =>', nums)

# 切片也可用于字符串和元组（不可变序列）
tuple_data = tuple(nums)
print('tuple_data[2:6] =>', tuple_data[2:6])

# 赋值给列表切片
nums[2:5] = [20, 21, 22]
print('修改后 nums =>', nums)
