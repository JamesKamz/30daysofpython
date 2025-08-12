#day 19 of 30 days with Python
def count_lines_and_words(file):
    with open(file, 'r') as f:
        txt=f.read()
    lines= txt.splitlines()
    num_lines=len(lines)
    words=txt.split()
    num_words=len(words)
    response = print(f"The file {file} has Number of lines: {num_lines}, Number of words: {num_words}")
    return response

count_lines_and_words("./data/data/obama_speech.txt")
count_lines_and_words("./data/data/michelle_obama_speech.txt")
count_lines_and_words("./data/data/donald_speech.txt")
count_lines_and_words("./data/data/melina_trump_speech.txt")