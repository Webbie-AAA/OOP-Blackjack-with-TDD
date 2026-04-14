# Best Friend

Given a string, return if a given letter always appears immediately before another given letter.

## Worked Example

```
("he headed to the store", "h", "e") ➞ True

# All occurences of "h": ["he", "headed", "the"]
# All occurences of "h" have an "e" after it.
# Return True

('abcdee', 'e', 'e') ➞ False

# For first "e" we can get "ee"
# For second "e" we cannot have "ee"
# Return False
```

## Examples

```
("i found an ounce with my hound", "o", "u") ➞ True

("we found your dynamite", "d", "y") ➞ False
```

## Notes

- All sentences will be given in lowercase.

# Algorithm
Inputs: 3 strings. How do I isolate each input? oh yeah. by the parameter value.
Output: Boolean
How do I say if something followed by something else:
    Maybe find the index. .index()
    so first_letter_index = sentence.index(a)
    second_letter_index = first_letter_index + 1
    for letter in sentence:
        if letter in [a]


