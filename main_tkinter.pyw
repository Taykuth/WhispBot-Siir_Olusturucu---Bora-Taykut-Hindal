import tkinter as tk
from tkinter import messagebox

# Örnek şiirler
poems = {
    "aşk": [
        "kalbim gülüşünde umut kalbim",
        "kalbim sana her başlar",
        "her gülüşünde umut dost",
        "kalbim yankılanır tek başıma"
    ],
    "umut": [
        "her yeni günle doğar içimde",
        "bir ışık gibi parlar umut",
        "karanlık gecelerde bile",
        "umudun adı yankılanır sessizce"
    ],
    "yalnızlık": [
        "sessiz duvarlara anlatırım içimi",
        "bir sandal gibi salınır kalbim",
        "sokaklar doludur içimdeki boşlukla",
        "yalnızlıkla konuşur sesim"
    ],
    "mutluluk": [
        "güneş gibi içimi aydınlatır gülüşün",
        "her renkte bir sevinç var",
        "çocuklar gibi koşar kalbim",
        "mutluluğun adı senle anılır"
    ],
    "kızgınlık": [
        "ateş gibi yakar içimdeki sözler",
        "sessizliğin bile sesi var bu gece",
        "öfkem yazar duvarlara isyanla",
        "sabır biter bazen, taşar aniden"
    ]
}

# Şiir üretme fonksiyonu
def generate_poem():
    feeling = entry.get().strip().lower()
    if feeling in poems:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "\n".join(poems[feeling]))
    else:
        messagebox.showerror("Hata", "Geçerli bir duygu giriniz: aşk, umut, yalnızlık, mutluluk, kızgınlık")

# Arayüz oluştur
root = tk.Tk()
root.title("Şiir Üretici (WhispBot)")

tk.Label(root, text="Hangi duyguya göre şiir istersin?").pack()
entry = tk.Entry(root, width=40)
entry.pack(pady=5)

tk.Button(root, text="Şiiri Üret", command=generate_poem).pack(pady=10)

result_text = tk.Text(root, height=6, width=50)
result_text.pack()

root.mainloop()
