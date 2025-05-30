import re

def check_str(s: str) -> bool:
    sentence = re.sub('[^A-z0-9]', '', s).lower()
    flag = True

    for x in range(len(sentence) // 2):
        if sentence[x] != sentence[-1 - x]:
            flag = False

    return flag
