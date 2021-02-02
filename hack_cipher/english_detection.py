from math import ceil

PERCENT_MATCH = 0.4

def detect_english(text):
    text = text.replace('.', '').replace(',', '').replace('?', '').replace('!', '')
    words = text.lower().split()
    words_nm = len(words)
    count = 0
    goal_nm = ceil(words_nm*PERCENT_MATCH)
    with open('words.txt', 'r') as f:
        eng_words = f.read().split()
        for word in words:
            if word in eng_words:
                count = count + 1
            else:
                pass
            if count == goal_nm:
                return True
        return False
if (__name__ == "__main__"):
    text = input()
    print(detect_english(text))
