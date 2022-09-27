def solution(new_id):
    id = ""
    for word in new_id.lower():
        if word.isdigit() or word.isalpha():
            id += word
        elif word == ".":
            if id:
                if id[-1] != ".":
                    id += word
            else:
                id += word
        elif word in ["-", "_"]:
            id += word

    if id:
        id = id.strip(".")

    if len(id) == 0:
        id += "a"


    if len(id) >= 16:
        id = id[:15]
        if id[-1] == ".":
            id = id[:-1]

    if len(id) <= 2:
        while len(id) < 3:
            str_add = id[-1]
            id += str_add

    return id


#   new_id = "...!@BaT#*..y.abcdefghijklm"
#   result = "bat.y.abcdefghi"