# generate_from_corpus.py

corpus = {
    "aşk": [
        "kalbim gülüşünde umut kalbim",
        "kalbim sana her başlar",
        "her gülüşünde umut dost",
        "kalbim yankılanır tek başıma"
    ],
    "umut": [
        "umuda doğru bir adım at",
        "gökkuşağı gibi içimde renkler",
        "her yeni gün yeni bir başlangıç",
        "karanlığı deler umutla kalbim"
    ],
    "yalnızlık": [
        "geceye düşünce bir başıma kaldım",
        "duvarlarla konuşan gölgem var",
        "sokak lambası altında sessizliğim",
        "yalnızlık bana kendini anlatır"
    ],
    "mutluluk": [
        "gülüşünle başlar her yeni sabah",
        "güz mevsimi gibi içimde huzur",
        "bir şarkı söylerim şehirle birlikte",
        "mutluluk dolu adımlar gökyüzüne"
    ],
    "kızgınlık": [
        "sözlerim yangın gibi dudaklarımda",
        "içimde bir volkan patlamaya hazır",
        "sessizlik bile öfkeyle yoğrulur",
        "gözlerimde Şamdan gibi parlayan hırs"
    ]
}

duygu = input("Hangi duyguya göre şiir istersin? (aşk, umut, yalnızlık, mutluluk, kızgınlık): ").strip().lower()

print("\n\U0001F4DD Üretilen Şiir:")
if duygu in corpus:
    for mısra in corpus[duygu]:
        print(mısra)
else:
    print("Üzgünüm, bu duygu için bir şiir bulunamadı.")
