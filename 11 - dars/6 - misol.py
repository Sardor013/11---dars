def eng_uzun_sozi_faylda(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as f:
            eng_uzun_sozi = ''
            for line in f:
                sozlar = line.split()
                for soz in sozlar:
                    if len(soz) > len(eng_uzun_sozi):
                        eng_uzun_sozi = soz
            return eng_uzun_sozi
    except FileNotFoundError:
        print("Xatolik: Fayl topilmadi!")

fayl_nomi = "matn.txt"
uzun_soz = eng_uzun_sozi_faylda(fayl_nomi)
if uzun_soz:
    print("Eng uzun soz:", uzun_soz)
