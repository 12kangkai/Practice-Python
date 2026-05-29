# Python iterable teaching code

# Built-in iterables
sequence = [1, 2, 3]
text = "hello"

print("Sequence is iterable:", hasattr(sequence, '__iter__'))
print("Text is iterable:", hasattr(text, '__iter__'))

# Using a for loop over an iterable
print("For loop over list:")
for item in sequence:
    print(item)

print("For loop over string:")
for ch in text:
    print(ch)

# Creating an iterator explicitly
iterator = iter(sequence)
print("Iterator created from list:", iterator)
print("Next values from iterator:")
print(next(iterator))
print(next(iterator))
print(next(iterator))

# StopIteration is raised when iterator is exhausted
try:
    print(next(iterator))
except StopIteration:
    print("Iterator exhausted")

# Generator as iterable and iterator

def squares(n):
    for i in range(n):
        yield i * i

print("Squares generator:")
for value in squares(5):
    print(value)

# Custom iterable class
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

print("Countdown custom iterable:")
for number in Countdown(5):
    print(number)
