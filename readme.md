# nnUNetv2 exploration

This is the modification of nnUNet v2, which is simply a exploration of the new released nnUNet. 

nnUNet is a complete work flow, guiding the auto adaptation to various datasets through preprocessing, postprocessing, network topology changing and some other non-architectural techniques. The rep is built to store some experimented changing on nnUNetv2 by myself. The original readme link of nnUNetv2 is [here](readme_ori.md). 

The current applied change is 

* Integret another transformer based network nnFormer [arXiv link](https://arxiv.org/abs/2109.03201) to the nnUNetv2. The previous network is based on version 1 and has some bugs. The current version fix the bug and allows it to run in the nnUNet v2. The changed Trainer file and network file is
  * [Trainer](nnunetv2\training\nnUNetTrainer\nnFormerTrainer.py) 
  * [network](nnunetv2\training\nnUNetTrainer\variants\network_architecture\nnFormer_tumor.py)
* Adding group convolution to the nnFormer. The changed Trainer file and network file is
  * [Trainer](nnunetv2\training\nnUNetTrainer\nnFormer2Trainer.py)
  * [network](nnunetv2\training\nnUNetTrainer\variants\network_architecture\nnFormer_tumour_group.py)
* Adding axial transformer to the nnFormer. The changed Trainer file and network file is
  * [Trainer](nnunetv2\training\nnUNetTrainer\nnFormerAxialTrainer.py)
  * [network](nnunetv2\training\nnUNetTrainer\variants\network_architecture\nnformer_axial.py)

The results of them are all stored into [result_path](my_nnunet\nnUNet_results). As the file is too large and contains all of the segmentation of the result, I didn't upload the result file of it. But some of the picture of training is stored here.