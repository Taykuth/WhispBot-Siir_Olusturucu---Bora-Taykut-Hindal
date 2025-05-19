import torch
import torch.nn.functional as F

def top_p_sample(logits, p=0.9):
    probs = F.softmax(logits, dim=-1)
    sorted_probs, sorted_indices = torch.sort(probs, descending=True)
    cumulative_probs = torch.cumsum(sorted_probs, dim=-1)

    sorted_indices_to_remove = cumulative_probs > p
    sorted_probs[sorted_indices_to_remove] = 0
    sorted_probs /= sorted_probs.sum()

    idx_next = torch.multinomial(sorted_probs, num_samples=1)
    next_token = sorted_indices[0, idx_next]
    return next_token