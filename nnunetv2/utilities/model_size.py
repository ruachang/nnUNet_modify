import torch.nn as nn
from torchstat import stat

input_size = (3, 224, 224)  # example for an image input
stat(model, input_size)

model_path1 = "/root/Desktop/nnUNet/my_nnunet/nnUNet_results/Dataset100_BrainTumour/nnFormerTrainer__nnUNetPlans__3d_fullres/fold_3/checkpoint_best.pth"
model_path2 = "/root/Desktop/nnUNet/my_nnunet/nnUNet_results/Dataset100_BrainTumour/nnFormerTrainer__nnUNetPlans__3d_fullres/fold_4/checkpoint_final.pth"


num_params = sum(p.numel() for p in model.parameters() if p.requires_grad)
print(f'Number of trainable parameters: {num_params}')


