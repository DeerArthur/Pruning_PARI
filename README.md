# Pruning_PARI

github URL: 

## introduction
  This file includes the instruction you need to conduct some experiments included in the paper "Pruning the Unimportant or Reduntdant Filters? Synergy makes Better". The tools and datasets you need is listed below:
  - Tools
  -   Python 3.6
  -   Pytorch 1.0.1
  -   TorchVision 0.2.1
  - Datasets
  -   CIFAR-10
  -   CIFAR-100
  -   ILSVRC-2012
  
## Training ResNet on CIFAR dataset
  In the paper, we conduct experiments on both CIFAR-10 and CIFAR-100 and the details of settings could be seen below.
  **CIFAR-10 experiments**
  ` python ./PARI/pruning_cifar_mine.py --arch resnet32 --batch_size 128 --dataset cifar10 --save_path ./PARI/snapshots/CIFAR_10/resnet32-rate-0.6-mine/ --epochs 200 --schedule 60 120 160 --gammas 0.2 0.2 0.2 --learning_rate 0.1 --decay 0.0005 --prune_rate 0.4 --weight_factor 0.7 --layer_begin 0 --layer_end 90 --layer_inter 3 --epoch_prune 1 ./dataset/
  
  python ./PARI/pruning_cifar_mine.py --arch resnet56 --batch_size 128 --dataset cifar10 --save_path ./PARI/snapshots/CIFAR_10/resnet56-rate-0.6-mine/ --epochs 200 --schedule 60 120 160 --gammas 0.2 0.2 0.2 --learning_rate 0.1 --decay 0.0005 --prune_rate 0.4 --weight_factor 0.7 --layer_begin 0 --layer_end 164 --layer_inter 3 --epoch_prune 1 ./dataset/
  
  python ./PARI/pruning_cifar_mine.py --arch resnet110 --batch_size 128 --dataset cifar10 --save_path ./PARI/snapshots/CIFAR_10/resnet110-rate-0.6-mine/ --epochs 200 --schedule 60 120 160 --gammas 0.2 0.2 0.2 --learning_rate 0.1 --decay 0.0005 --prune_rate 0.4 --weight_factor 0.7 --layer_begin 0 --layer_end 324 --layer_inter 3 --epoch_prune 1 ./dataset/ `
  In the commands above, *prune_rate* means the proportion of the pruned seciton of the network. *weight_factor* indicates the trade-off parameter, the value of which is 0.1, 0.3, 0.5, 0.7, 0.9 in the paper.
  
  **CIFAR-100 experiments**
  ` python ./PARI/pruning_cifar_mine.py --arch resnet20 --batch_size 128 --dataset cifar100 --save_path ./PARI/snapshots/CIFAR_100/resnet20-rate-0.6-mine/ --epochs 200 --schedule 60 120 160 --gammas 0.2 0.2 0.2 --learning_rate 0.1 --decay 0.0005 --prune_rate 0.4 --weight_factor 0.7 --layer_begin 0 --layer_end 54 --layer_inter 3 --epoch_prune 1 ./dataset/
  
  python ./PARI/pruning_cifar_mine.py --arch resnet56 --batch_size 128 --dataset cifar100 --save_path ./PARI/snapshots/CIFAR_100/resnet56-rate-0.6-mine/ --epochs 200 --schedule 60 120 160 --gammas 0.2 0.2 0.2 --learning_rate 0.1 --decay 0.0005 --prune_rate 0.4 --weight_factor 0.7 --layer_begin 0 --layer_end 164 --layer_inter 3 --epoch_prune 1 ./dataset/`
  
## Traing ResNet on ImageNet (ILSVRC-2012)
  **ILSVRC-2012 experiments**
  `
  python ./PARI/pruning_imagenet_mine.py -arch resnet18 --batch_size 128 --workers 4 --save_dir ./PARI/snapshots/IMAGENET/resnet18-rate-0.6-mine/ --prune_rate 0.3 --weight_factor 0.7 --layer_begin 0 --layer_end 57 --layer_inter 3 --epoch_prune 1 ./dataset/
  
  python ./PARI/pruning_imagenet_mine.py -arch resnet50 --batch_size 128 --workers 4 --save_dir ./PARI/snapshots/IMAGENET/resnet50-rate-0.6-mine/ --prune_rate 0.3 --weight_factor 0.7 --layer_begin 0 --layer_end 156 --layer_inter 3 --epoch_prune 1 ./dataset/
  `

## some other functions
  - parameter visualization : refer to parameter_visualization.py please
