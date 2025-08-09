# Day 18 of 30 days with python
import re
from collections import Counter

paragraph = '''I love teaching. If you do not love teaching
what else can you love. I love Python if you do not love
something which can give you all the capabilities to develop
an application what else can you love.'''


# Extract words
words = re.findall(r'\b\w+\b', paragraph)
# Count frequency
word_counts = Counter(words)
# Sort by frequency (desc) then alphabetically
sorted_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
print(sorted_counts)

text = """The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 
in the negative direction, 0 at origin, 4 and 8 in the positive direction."""

# Extract numbers (with optional minus sign)
points = re.findall(r'-?\d+', text)
points = list(map(int, points))
# Sort
sorted_points = sorted(points)
# Distance
distance = sorted_points[-1] - sorted_points[0]
print("Points:", points)
print("Sorted:", sorted_points)
print("Distance:", distance)


def is_valid_variable(name):
    return bool(re.match(r'^[A-Za-z_]\w*$', name))

print(is_valid_variable('first_name'))  # True
print(is_valid_variable('first-name'))  # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname'))   # True


def clean_text(text):
    # Remove all non-alphanumeric except spaces
    return re.sub(r'[^\w\s]', '', text)

def most_frequent_words(text):
    words = re.findall(r'\b\w+\b', text)
    counts = Counter(words)
    return counts.most_common(3)

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve
%tea@ching%;. There $is nothing; &as& mo@re rewarding as
educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching
m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s
mo@tivate yo@u to be a tea@cher!?'''

cleaned_text = clean_text(sentence)
print(cleaned_text)
print(most_frequent_words(cleaned_text))