# GNN Playground

> 用一个可观察的消息传播实验理解 GNN 参数。

一个零依赖的图神经网络概念实验场，帮助学生直观看到训练参数如何影响收敛。它使用小型固定图数据运行一个可解释的消息传播式演示，不需要 GPU、账号或云端 API。

## 运行

```bash
python -m gnn_playground --layers 3 --learning-rate 0.12 --epochs 30 -o demo.html
```

命令会输出 JSON 指标并生成可直接打开的 `demo.html`，包含训练损失曲线和节点预测柱状图。修改参数后重新运行即可比较结果。

## 设计动机

这个项目专注于教学：代码很短，每个参数都有可观察的效果，适合作为 GNN 课程演示和实验报告起点。后续可以接入 PyTorch Geometric、真实数据集或 Streamlit 界面。

MIT License · 欢迎提交新的数据集和可视化实验。

## 参数

`--layers` 支持 1–5 层，`--epochs` 支持 1–200 轮；输出 JSON 可用于自己的绘图或实验报告。
