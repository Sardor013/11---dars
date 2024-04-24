def oxirgi_indeks(txt, belgi):
    indeks = -1
    for i in range(len(txt)):
        if txt[i] == belgi:
            indeks = i
    return indeks

txt = "Hello, welcome to my world."
belgi = 'o'
print(oxirgi_indeks(txt, belgi))
