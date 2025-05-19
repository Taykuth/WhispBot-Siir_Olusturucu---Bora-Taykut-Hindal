import tkinter as tk
from tkinter import messagebox

# Sabit şiirler corpusu
poems = {
    "aşk": [
        "Kalbim gülüşünde umut kalbim",
        "Kalbim sana her başlar",
        "Her gülüşünde umut dost",
        "Kalbim yankılanır tek başıma"
    ],
    "umut": [
        "Umudum yıldızlara uzanır geceden",
        "Karanlıkta bile ışık ararım hep",
        "Her düşümde bir yol bir serüven",
        "Umutla dolu yarına bir adım"
    ],
    "yalnızlık": [
        "Gecede yankılanır sessizliğim",
        "Bir sandal gibi boşlukta savrulurum",
        "Kendime anlatamam içimdeki boşluğu",
        "Yalnızlık bir hayal gibi sarar"
    ],
    "mutluluk": [
        "Bir çocuk kahkahasında gizli",
        "Güneş gibi doğar içime sevinç",
        "Mutluluk bir an, bir dokunuş",
        "Birlikte geçen her saniye ölümsüz"
    ],
    "kızgınlık": [
        "Öfkem sığmaz dar sokaklara",
        "Alev gibi yakar her kelimeyi",
        "Kızgınlıkla tutuşur ellerim",
        "Ve suskunluğum bir çığlıktır içimde"
    ]
}

def generate_poem():
    mood = entry.get().strip().lower()
    if mood in poems:
        poem = "\n".join(poems[mood])
        result_label.config(text=poem)
    else:
        messagebox.showerror("Geçersiz Duygu", "Lütfen geçerli bir duygu girin: aşk, umut, yalnızlık, mutluluk, kızgınlık")

# Arayüz oluşturuluyor
root = tk.Tk()
root.title("Şiir Üretici (WhispBot)")

# Giriş etiketi
label = tk.Label(root, text="Hangi duyguya göre şiir istersin? (aşk, umut, yalnızlık, mutluluk, kızgınlık)")
label.pack(pady=10)

# Giriş alanı
entry = tk.Entry(root, width=40)
entry.pack()

# Buton
button = tk.Button(root, text="Şiiri Üret", command=generate_poem)
button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", justify="left", font=("Courier", 12))
result_label.pack(pady=10)

# Arayüzü başlat
root.mainloop()
