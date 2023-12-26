import statistics
import random
import matplotlib.pyplot as plt

BOOK_LENGTH = 10
PAGE_LENGTH = 10
TYPO_ODDS = "1 in 10"
PRUE_CATCH_RATE = 0.8
FRIDA_CATCH_RATE = 0.8

'''
Helper functions for book and proofreading logic
'''

# Generate the book, with good words 'g' and typos 't'
def generate_book():
    book = []
    choice_list = []
    typos, cleans = TYPO_ODDS.split(" in ")
    typos = int(typos)
    cleans = int(cleans)
    for _ in range(typos):
        choice_list.append("t")
    for _ in range(cleans):
        choice_list.append("g")
    for page in range(BOOK_LENGTH):
        temp = []
        for word in range(PAGE_LENGTH):
            temp.append(random.choice(choice_list))
        book.append(temp)
    return book

# Determine the percentage of pages with no typos
def pct_clean_pages(book):
    clean_pages = 0
    for page in book:
        clean_flag = True
        for word in page:
            if word == "t":
                clean_flag = False
        if clean_flag:
            clean_pages += 1

    pct_clean = round(clean_pages / BOOK_LENGTH * 100, 1)
    return pct_clean

# Determine the percentage of words that are typos
def pct_typo_words(book):
    typos = 0
    for page in book:
        for word in page:
            if word == "t":
                typos += 1

    pct_typos = round(typos / (BOOK_LENGTH * PAGE_LENGTH) * 100, 2)
    return pct_typos

# Simulate proofreader Prue 'cleaning' the book
def prue_clean(book):
    i = 0
    for page in book:
        j = 0
        for word in page:
            if word == "t":
                choice = random.choices(
                    population=["fix", "miss"], 
                    weights=[PRUE_CATCH_RATE, 1 - PRUE_CATCH_RATE],
                    k=1
                    )
                if choice[0] == "fix":
                    book[i][j] = "g"
            j += 1
        i += 1

    return book

# Simulate proofreader Frida 'cleaning' the book
def frida_clean(book):
    i = 0
    for page in book:
        j = 0
        for word in page:
            if word == "t":
                choice = random.choices(
                    population=["fix", "miss"], 
                    weights=[FRIDA_CATCH_RATE, 1 - FRIDA_CATCH_RATE],
                    k=1
                    )
                if choice[0] == "fix":
                    book[i][j] = "g"
            j += 1
        i += 1

    return book


'''
Called functions for larger operations
'''

# Get a random book, Prue cleans it once
# Returns: (original book, Prue-cleaned book)
def book_then_prue_clean():
    book = generate_book()
    cleaned_book = prue_clean(book)
    return book, cleaned_book

# Get a random book, Frida cleans it once
# Returns: (original book, Frida-cleaned book)
def book_then_frida_clean():
    book = generate_book()
    cleaned_book = frida_clean(book)
    return book, cleaned_book

# Get a random book, Prue cleans it, then Frida
# Returns: (original book, P-then-F-cleaned book)
def book_cleaned_pf():
    book = generate_book()
    prue_cleaned = prue_clean(book)
    pf_cleaned = frida_clean(prue_cleaned)
    return book, pf_cleaned

# Same as above, except Frida then Prue
# Returns: (original book, F-then-P-cleaned book)
def book_cleaned_fp():
    book = generate_book()
    frida_cleaned = frida_clean(book)
    fp_cleaned = prue_clean(book)
    return book, fp_cleaned


if __name__ == "__main__":
    book = generate_book()
    print(f"{pct_clean_pages(book)}% clean pages, {pct_typo_words(book)}% typos")
    
    cleaned_book = prue_clean(book)
    print()
    print(f"after cleaning, {pct_clean_pages(cleaned_book)}% clean pages, {pct_typo_words(cleaned_book)}% typos")
