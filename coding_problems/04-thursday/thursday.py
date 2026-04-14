# def best_friend(txt: str, a: str, b: str) -> bool:
#     txt = list(txt)
#     value = None
#     for letter in txt:
#         if letter in [b]:
#             txt.remove(letter)
#         if letter in [a]:
#             if txt.index(letter) == txt.index(b) - 1:
#                 txt.remove(a)
#                 value = True
#             else:
#                 return False
#     return value

def best_friend(txt: str, a: str, b: str) -> bool:
    empty_list = []
    instance = []
    txt += " "
    for i in range(len(txt)-1):
        empty_list.append(txt[i] + txt[i+1])
    for pair in empty_list:
        if pair[0] == a:
            if pair[1] == b:  # must check that its only h followed by e
                instance.append(True)
            else:
                instance.append(False)
    return all(instance)
