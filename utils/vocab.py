import json

with open("word_vocab_structured_110.json", "r", encoding="utf-8") as f:
    vocab = json.load(f)

word2idx = vocab["word2idx"]
idx2word = {int(k): v for k, v in vocab["idx2word"].items()}


def encode(words):
    return [word2idx.get(w, word2idx["<UNK>"]) for w in words]

def decode(indices):
    return [idx2word.get(i, "<UNK>") for i in indices]