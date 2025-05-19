import json
from collections import Counter

# Dosya yolu
corpus_path = "corpus_structured_500.txt"
with open(corpus_path, "r", encoding="utf-8") as f:
    lines = f.read().splitlines()

# Tüm kelimeleri topla
all_words = []
for line in lines:
    words = line.strip().split()
    all_words.extend(words)

# Özel token'lar
special_tokens = ["<PAD>", "<UNK>", "<BOS>", "<EOS>"]

# Kelimeleri sırala (önce özel token'lar)
word_counts = Counter(all_words)
vocab_words = special_tokens + sorted(set(word_counts) - set(special_tokens))

# word2idx ve idx2word sözlükleri oluştur
word2idx = {w: i for i, w in enumerate(vocab_words)}
idx2word = {i: w for w, i in word2idx.items()}

# JSON formatında kaydet
vocab = {"word2idx": word2idx, "idx2word": idx2word}
with open("word_vocab_structured_110.json", "w", encoding="utf-8") as f:
    json.dump(vocab, f, ensure_ascii=False, indent=2)

print(f"Toplam kelime sayısı: {len(word2idx)}")
