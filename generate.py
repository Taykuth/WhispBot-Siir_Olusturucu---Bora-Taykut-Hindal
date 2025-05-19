# generate.py

# Şiir veritabanı (etikete göre)
poems = {
    "aşk": """kalbim sana adanmış her nefeste
her gülüşünle yeniden doğarım sessizce
gözlerinde bahar gibi açar çiçekler
adınla başlar her sabah, seninle biter gece""",

    "umut": """karanlık gecede bir ışık ararım
yarının kalbimde izini taşırım
düşlerim yıkılsa da yılmam asla
umutla yürürüm sonsuz yollara""",

    "yalnızlık": """sessizliğin koynunda kaybolurum
kimse bilmez içimdeki fırtınayı
bir sandal gibi savrulurum boşlukta
yalnızlık sarar her sabahı""",

    "mutluluk": """güneşin dansı gibi gözlerinde
kahkahaların yankısı yüreğimde
her anı seninle yaşamak ne güzel
mutluluğu buldum seninle birlikte""",

    "kızgınlık": """öfkemin ateşiyle yanar geceler
sözler susar, kalbim haykırır içten
ihanetle yoğrulmuş sessiz anlar
kırık cümlelerle savaşır düşler"""
}

# Kullanıcıdan duygu etiketi al
etiket = input("Hangi duyguya göre şiir istersin? (aşk, umut, yalnızlık, mutluluk, kızgınlık): ").strip().lower()

# Şiir varsa göster
if etiket in poems:
    print("\n📝 Üretilen Şiir:")
    print(f"[{etiket}]")
    print(poems[etiket])
else:
    print("🚫 Bu etiket için şiir bulunamadı. Lütfen 'aşk', 'umut', 'yalnızlık', 'mutluluk' veya 'kızgınlık' girin.")
