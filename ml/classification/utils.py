import torch


def save_checkpoint(model, save_path):

    torch.save(model.state_dict(), save_path)

    print(f"\n✓ Model saved to: {save_path}")