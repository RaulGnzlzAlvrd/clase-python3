import string

# Variables usadas para determinar el inicio y fin de los headers
start_header = 'END OF THIS PROJECT GUTENBERG EBOOK'
end_header = 'START OF THIS PROJECT GUTENBERG EBOOK'

def process_file(filename):
    """
    """
    hist = dict()
    fin = open(filename)
    skip_gutenberg_header(fin)
    for line in fin:
        if start_header in line:
            break
        process_line(line, hist)
    return hist

def skip_gutenberg_header(fin):
    """
    """
    for line in fin:
        if end_header in line:
            break

def process_line(line, hist):
    """
    """
    line = line.replace('-', ' ')
    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

def total_words(hist):
    """
    """
    return sum(hist.values())

def different_words(hist):
    """
    """
    return len(hist)

def most_common(hist):
    """
    """
    t = []
    for key, value in hist.items():
        t.append((value, key))
    t.sort(reverse=True)
    return t

def substract(d1, d2):
    """
    """
    res = dict()
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

def main():
    hist = process_file('book.txt')

    books = ["book1.txt", "book2.txt", "book3.txt"]
    for book in books:
        hist = process_file(book)
        print('Total number of words:', total_words(hist))
        print('Number of different words:', different_words(hist))

    t = most_common(hist)
    print('The 10 most common words are:')
    for freq, word in t[:10]:
        print(word, freq, sep='\t')

    words = process_file("words.txt")
    diff = substract(hist, words)
    print("Words in the book that aren't in the word list:")
    for word in diff:
        print(word, end=' ')

if __name__ == '__main__':
    main()
