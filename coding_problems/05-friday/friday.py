from collections import Counter


def is_anagram(s: str, t: str) -> bool:
    s_items = list(s)
    t_items = list(t)
    true_or_false = []
    if len(s_items) != len(t_items):
        return False
    s_count = Counter(s)
    t_count = Counter(t)
    if s_count != t_count:
        return False
    one = all(item in s_items for item in t_items)
    true_or_false.append(one)
    two = all(item in t_items for item in s_items)
    true_or_false.append(two)
    return all(true_or_false)


print(is_anagram('abbc', 'cba'))
