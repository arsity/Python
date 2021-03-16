import string

def shift(letter, value, alpha=string.ascii_uppercase):
    ch = letter
    if letter.isalpha:
        if letter.upper() in alpha :
            idx = alpha.find(letter.upper())+value
            idx = idx % len(alpha)
            ch = alpha[idx]
        return ch if letter.isupper() else ch.lower()
    return letter


def shift_cipher(msg, value):
    ans = ''
    for character in msg:
        ans += (shift(character, value))
    return ans


m = "SPY coder"
ans = shift_cipher(m, 5)
print(m, "\t", ans)
