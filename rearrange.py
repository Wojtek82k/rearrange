#!/usr/bin/env python3
 

def rearrange_string(s: str, mode: str = "alphabetical") -> str:
    if mode == "alphabetical":
        return ''.join(sorted(s))
    elif mode == "reverse":
        return s[::-1]
    elif mode == "vowels_first":
        vowels = 'aeiouAEIOU'
        return ''.join([c for c in s if c in vowels]) + ''.join([c for c in s if c not in vowels])
    elif mode == "by_length":
        words = s.split()
        return ' '.join(sorted(words, key=len))
    else:
        raise ValueError("Unsupported mode. Try: alphabetical, reverse, vowels_first, by_length")


if __name__ == "__main__":
    input_str = input("Enter a string: ")
    print("Modes: alphabetical | reverse | vowels_first | by_length")
    mode = input("Choose mode: ")
    
    try:
        result = rearrange_string(input_str, mode)
        print("Rearranged string:", result)
    except ValueError as e:
        print(e)
