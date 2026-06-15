# Python 文件读写教学代码

# 1. 写入文件
with open('example.txt', 'w', encoding='utf-8') as f:
    f.write('Hello, World!\n')
    f.write('This is a test file.\n')

# 2. 读取整个文件
with open('example.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print("整个文件内容:")
    print(content)

# 3. 逐行读取
with open('example.txt', 'r', encoding='utf-8') as f:
    print("\n逐行读取:")
    for line in f:
        print(line.strip())

# 4. 读取所有行到列表
with open('example.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("\n行列表:", lines)

# 5. 追加内容
with open('example.txt', 'a', encoding='utf-8') as f:
    f.write('Appended line.\n')

# 6. 读写二进制文件
with open('example.bin', 'wb') as f:
    f.write(b'\x00\x01\x02\x03')

with open('example.bin', 'rb') as f:
    binary_data = f.read()
    print("\n二进制数据:", binary_data)