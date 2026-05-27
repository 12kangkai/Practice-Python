print('list是Python内置的一种数据类型，list是一种有序的集合，可以随时添加和删除其中的元素。' )
classmates = ['张三', '李四', '王五']
print(classmates)
print(len(classmates))

print('访问list元素可以使用索引顺序访问，索引从0开始，依次增加1，以此类推。' );
print(classmates)
print(classmates[0])
print(classmates[1])
print(classmates[2])
# classmates[3] # IndexError: list index out of range

print('访问list元素可以使用索引倒序访问，最后一个元素的索引是-1，倒数第二个元素的索引是-2，以此类推。' );
print(classmates)
print(classmates[-0])
print(classmates[-1])
print(classmates[-2])
#classmates[-3] # IndexError: list index out of range

print('追加元素到list末尾可以使用append()方法' );
classmates.append('赵六')
print(classmates)

print('插入元素到指定位置可以使用insert(index, element)方法' );
classmates.insert(1, '钱七')
print(classmates)

print('删除list末尾的元素可以使用pop()方法' );
print(classmates.pop())
print(classmates)

print('删除指定位置的元素也可以使用pop(index)方法' );

print(classmates.pop(1))
print(classmates)

print('修改list元素可以直接通过索引赋值' );
classmates[1] = '孙八'
print(classmates)

print('list元素可以是不同类型的，list本身也可以包含另一个list')
L = ['Apple', 123, True]
s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s[0])
print(s[2])
print(s[2][0]) # 访问方式类似二维数组

print("----------------")

print('tuple是Python内置的一种数据类型，tuple与list类似，但是tuple一旦创建完成后就不能再修改。' );

print('创建tuple使用()，但是要注意只有一个元素的tuple必须在元素后面加上逗号，否则Python会把括号当成普通的括号来处理。' );
t = (1, 2)
print(t)
t = ()
print(t)
t = (1,)
print(t)

print('访问tuple元素可以使用索引顺序访问，索引从0开始，依次增加1，以此类推。' );
t = ('a', 'b', 'c')
print(t)
print(t[0])
print(t[1])
print(t[2])

print('访问tuple元素可以使用索引倒序访问，最后一个元素的索引是-1，倒数第二个元素的索引是-2，以此类推。' );
t = ('a', 'b', 'c')
print(t)
print(t[-1])
print(t[-2])
print(t[-3])

print('tuple一旦创建完成后就不能再修改，所以没有append()、insert()这样的方法，但是可以通过重新赋值来实现类似的效果。' );
t = ('a', 'b', 'c')
print(t)
t = ('d',) + t[1:]
print(t)

print('虽然tuple的元素不能修改，但是如果tuple中包含的是可变对象，比如list，那么这个list是可以修改的。' );
t = ('a', 'b', ['A', 'B'])
print(t)
t[2][0] = 'X'
t[2][1] = 'Y'
print(t)








