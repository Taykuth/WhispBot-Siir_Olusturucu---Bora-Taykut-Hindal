import torch
from model import WordTransformer
from utils.vocab import encode, word2idx
from torch.nn import CrossEntropyLoss
from torch.optim import AdamW
from torch.utils.data import Dataset, DataLoader
import random

# Özellikler
vocab_size = len(word2idx)
block_size = 32
batch_size = 32
epochs = 20
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Dataset Sınıfı
class PoemDataset(Dataset):
    def __init__(self, path):
        with open(path, encoding="utf-8") as f:
            self.lines = [line.strip() for line in f if line.strip()]

    def __len__(self):
        return len(self.lines)

    def __getitem__(self, idx):
        line = self.lines[idx]
        tokens = encode(line)
        x = torch.tensor(tokens[:-1], dtype=torch.long)
        y = torch.tensor(tokens[1:], dtype=torch.long)
        return x, y

# Collate Fonksiyonu

def collate(batch):
    X, Y = zip(*batch)
    X = [torch.nn.functional.pad(x, (0, block_size - len(x)), value=word2idx["<PAD>"])[:block_size] for x in X]
    Y = [torch.nn.functional.pad(y, (0, block_size - len(y)), value=word2idx["<PAD>"])[:block_size] for y in Y]
    return torch.stack(X), torch.stack(Y)

# Veri Yükleme
train_dataset = PoemDataset("corpus_structured_500.txt")
train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, collate_fn=collate)

# Model Tanımlama
model = WordTransformer(vocab_size=vocab_size, block_size=block_size).to(device)
optimizer = AdamW(model.parameters(), lr=3e-4)
loss_fn = CrossEntropyLoss(ignore_index=word2idx["<PAD>"])

# Eğitim Döngüsü
model.train()
for epoch in range(epochs):
    total_loss = 0
    for xb, yb in train_loader:
        xb, yb = xb.to(device), yb.to(device)
        logits = model(xb)
        loss = loss_fn(logits.view(-1, vocab_size), yb.view(-1))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1} / {epochs} - Loss: {total_loss:.4f}")

# Modeli Kaydet
torch.save(model.state_dict(), "models/word_transformer.pt")
print("\n✅ Model kaydedildi: models/word_transformer.pt")
