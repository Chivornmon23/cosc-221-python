def count_gifts(box):
    count = 0
    for item in box:
        if isinstance(item, list):
            count += count_gifts(item)
        else:
            count += 1
    return count

nested_box = ["Pen", ["Book", ["Toy", "Sticker"]], "Notebook"]
print(count_gifts(nested_box))