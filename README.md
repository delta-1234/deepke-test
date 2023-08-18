## 创建环境

```shell
conda create -n deepke python=3.8

conda activate deepke
```

## 安装deepke

直接pip安装，通过源码安装会报错！

```shell
pip install deepke
```

## 数据

数据保存在`./data/origin`中，可以进行修改，具体格式看各个csv文件

## 训练

支持多卡训练，修改`trian.yaml`中的`use_multi_gpu`参数为True，`gpu_ids`设置为所选gpu，以逗号为间隔，第一张卡为计算主卡，需使用略多内存。设置`show_plot`为True可对当前epoch的loss进行可视化展示，默认为False。（没尝试过）

训练相关参数在`.\conf\train.yaml`中进行调整，保存模型的路径在`.\conf\predict.yaml`进行调整

如果要使用[wandb](https://docs.wandb.ai/quickstart)可视化调参，先在网站进行注册，获得api（可以显示训练速度、丢失率等）

```shell
python run.py
```

## 预测

```shell
python predict.py
```

