def qatorlar_soni(fayl_nomi):
    try:
        with open(fayl_nomi, 'r') as f:
            qatorlar = f.readlines()
            return len(qatorlar)
    except FileNotFoundError:
        print("Xatolik: Fayl topilmadi!")

fayl_nomi = "matn.txt"
qator_soni = qatorlar_soni(fayl_nomi)
if qator_soni is not None:
    print("Fayl", fayl_nomi, "da", qator_soni, "ta qator mavjud.")
