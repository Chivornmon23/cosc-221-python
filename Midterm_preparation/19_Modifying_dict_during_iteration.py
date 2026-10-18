scores = {"John": 45, "Sara": 88, "Alex": 32, "David": 75}
try:
    for student, score in scores.items():
        if score < 50:
            del scores[student]
except RuntimeError:
    print("Modifying a collection's size (adding or removing items)\b")
    print("while iterating over it causes RunTimeError Exception")
finally:
    print("The solution: ")
    print("Iterate over a copy of the keys using (in list(scores.items()")
    for student, score in list(scores.items()):
        if score < 50:
            del scores[student]
    print(scores)
