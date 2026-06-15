from io import StringIO, BytesIO

# ===== StringIO: 处理文本数据 =====
print("=== StringIO 示例 ===")

# 创建 StringIO 对象
sio = StringIO()

# 写入字符串
sio.write("Hello, World!\n")
sio.write("Python StringIO\n")

# 获取所有内容
content = sio.getvalue()
print("内容:", content)

# 重置指针位置
sio.seek(0)

# 读取内容
print("读取:", sio.readline())

# ===== BytesIO: 处理二进制数据 =====
print("\n=== BytesIO 示例 ===")

# 创建 BytesIO 对象
bio = BytesIO()

# 写入字节
bio.write(b"Binary data")
bio.write(b"\nBytes IO")

# 获取所有内容
binary_content = bio.getvalue()
print("内容:", binary_content)

# 重置指针
bio.seek(0)

# 读取字节
print("读取:", bio.read(6))

# ===== 实用场景 =====
print("\n=== 实用场景 =====")

# StringIO 用于文本处理
text_buffer = StringIO()
for i in range(3):
    text_buffer.write(f"Line {i}\n")
print("文本缓冲:", text_buffer.getvalue())

# BytesIO 用于二进制处理
bytes_buffer = BytesIO()
bytes_buffer.write(b"\x00\x01\x02")
bytes_buffer.write(b"\x03\x04\x05")
print("二进制缓冲:", bytes_buffer.getvalue().hex())