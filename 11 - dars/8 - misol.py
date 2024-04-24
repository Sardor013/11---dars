def antiqa_sonmi(n):
    n_str = str(n)
    valid_digits = {'0', '1', '8'}
    for i in n_str:
        if i not in valid_digits:
            return "NO"
    if n_str != n_str[::-1]:
        return "NO"
    return "YES"

n = int(input("Sonni kiriting: "))
print(antiqa_sonmi(n))
