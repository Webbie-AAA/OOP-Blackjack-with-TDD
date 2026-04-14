# pylint: skip-file
import pytest
from friday import is_anagram


def test_anagram_1():
    assert is_anagram("anagram", "nagaram") == True


def test_anagram_2():
    assert is_anagram("rat", "car") == False


def test_anagram_3():
    assert is_anagram("listen", "silent") == True


def test_anagram_4():
    assert is_anagram("elbow", "below") == True


def test_anagram_5():
    assert is_anagram("elbows", "below") == False


def test_anagram_6():
    assert is_anagram("a", "ab") == False


def test_anagram_7():
    assert is_anagram("ab", "a") == False


def test_anagram_8():
    assert is_anagram("ab", "ba") == True


def test_anagram_9():
    assert is_anagram("abc", "cba") == True


def test_anagram_10():
    assert is_anagram("abbc", "cba") == False


def test_anagram_11():
    assert is_anagram("abbc", "cbad") == False


def test_anagram_12():
    assert is_anagram("abbc", "cbab") == True


def test_anagram_13():
    assert is_anagram("aabb", "abbb") == False


def test_anagram_14():
    assert is_anagram("abbc", "cbacd") == False


def test_anagram_15():
    assert is_anagram("abbc", "cbacd") == False


def test_anagram_empty_1():
    assert is_anagram("", "") == True


def test_anagram_empty_2():
    assert is_anagram("", "a") == False


def test_anagram_empty_3():
    assert is_anagram("a", "") == False


def test_anagram_empty_4():
    assert is_anagram("", "ab") == False


def test_anagram_empty_5():
    assert is_anagram("ab", "") == False


def test_anagram_empty_6():
    assert is_anagram("", "abc") == False


def test_anagram_empty_7():
    assert is_anagram("abc", "") == False


def test_anagram_empty_8():
    assert is_anagram("", "abbc") == False


def test_anagram_empty_9():
    assert is_anagram("abbc", "") == False
