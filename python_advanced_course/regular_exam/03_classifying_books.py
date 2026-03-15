def classify_books(*args, **kwargs):
    fiction = {}
    non_fiction = {}

    for genre, title in args:
        if genre == "fiction":
            fiction[title] = None
        elif genre == "non_fiction":
            non_fiction[title] = None

    for code, title in kwargs.items():
        if title in fiction:
            fiction[title] = code
        elif title in non_fiction:
            non_fiction[title] = code

    sorted_fiction = dict(sorted(fiction.items(), key=lambda x: x[1]))
    sorted_non_fiction = dict(sorted(non_fiction.items(), key=lambda x: x[1], reverse=True))

    result = ""

    if fiction:
        result += "Fiction Books:\n"
        for title, code in sorted_fiction.items():
            result += f"~~~{code}#{title}\n"
    if non_fiction:
        result += "Non-Fiction Books:\n"
        for title, code in sorted_non_fiction.items():
            result += f"***{code}#{title}\n"

    return result


print(classify_books(
    ("fiction", "Brave New World"),
    ("non_fiction", "The Art of War"),
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("non_fiction", "The Art of War"),
    ("fiction", "The Great Gatsby"),
    ("non_fiction", "A Brief History of Time"),
    ("fiction", "Brave New World"),
    FF1234HH="The Great Gatsby",
    NF3845UU="A Brief History of Time",
    NF3421NN="The Art of War",
    FF1234UU="Brave New World"
))
print(classify_books(
    ("fiction", "Brave New World"),
    ("fiction", "The Catcher in the Rye"),
    ("fiction", "1984"),
    FICCITRZZ="The Catcher in the Rye",
    FIC1984XX="1984",
    FICBNWYYY="Brave New World"
))
print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))
