import torch
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader, random_split

# basic transformation: Convert to Tensor and Normalize (Mean/Std for CIFAR-10)
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Download the full dataset
full_train_dataset = torchvision.datasets.CIFAR10(root='./data', train=True, 
                                                download=True, transform=transform)

# TODO: Add training data
# test_set = torchvision.datasets.CIFAR10(root='./data', train=False, 
#                                        download=True, transform=transform)

# Define split sizes
train_size = 45000
val_size = 5000

# Perform the split
train_set, val_set = random_split(full_train_dataset, [train_size, val_size])

print(f"Training samples: {len(train_set)}")
print(f"Validation samples: {len(val_set)}")
print(f"Test samples: {len(test_set)}")

# Create loaders for each set
train_loader = DataLoader(train_set, batch_size=64, shuffle=True)
val_loader = DataLoader(val_set, batch_size=64, shuffle=False)
test_loader = DataLoader(test_set, batch_size=64, shuffle=False)

