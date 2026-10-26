# prompt the user for the title of a book, and the number of days late to return the book, and print the output
def main():
    book_title = input("What is the book title: ")
    formatted_title = format_title(book_title)
    try:
        days_late = int(input("How many days late to return the book: "))
        fine_category = get_fine_category(days_late)
        if fine_category is not None:
            fine = calculate_fine(days_late, fine_category)
            print(
                f"{formatted_title} is {fine_category}, with a fine of KSH {fine:.2f}."
            )
        else:
            return None
    except ValueError:
        pass


# return the title of a book in title case
def format_title(t):
    t = t.title().strip()
    return t


# return the fine category based on the number of days late to return a book
def get_fine_category(d):
    if d == 0:
        return "No Fine"
    elif 0 < d <= 3:
        return "Minor"
    elif 3 < d <= 7:
        return "Moderate"
    elif d > 7:
        return "Severe"
    else:
        return None


# return the fine based on the number of days late to return a book and the fine category
def calculate_fine(d, c):
    if c == "No Fine":
        return 0.0
    elif c == "Minor":
        return 10 * d
    elif c == "Moderate":
        return 20 * d
    else:
        return 50 * d


if __name__ == "__main__":
    main()
