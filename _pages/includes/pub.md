# 📝 Selected Publications

<!-- My full paper list can be found at <a href='https://scholar.google.com/citations?user=lFZpfE4AAAAJ'><img src="https://img.shields.io/endpoint?url=https://cdn.jsdelivr.net/gh/circleLZY/circleLZY.github.io@google-scholar-stats/gs_data_shieldsio.json&logo=Google%20Scholar&labelColor=f6f6f6&color=9cf&style=flat&label=citations"></a>). -->

## Remote Sensing Change Detection

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/m2cd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[M$^2$CD: A Unified MultiModal Framework for Optical-SAR Change Detection with Mixture of Experts and Self-Distillation](https://arxiv.org/abs/2503.19406) \\
**Ziyuan Liu**, Jiawei Zhang, Wenyu Wang, Yuantao Gu
  -  We propose a unified **M**ulti**M**odal **CD** framework (M$^2$CD), which is highly versatile and robust, compatible with various backbone architectures.
  -  By introducing modality-specialized MoE modules into the backbone and innovatively proposing an Optical-to-SAR transition path (O2SP) for self-distillation guidance, we reduce the feature space discrepancies between different modalities and alleviate the model’s burden in processing multimodal data.
  -  Extensive experiments on the CAU-Flood dataset demonstrate that M2CD outperforms all SOTA methods.
</div>
</div>


<div class='paper-box'><div class='paper-box-image'><div><div class="badge">arXiv 2025</div><img src='images/mtkd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[JL1-CD: A New Benchmark for Remote Sensing Change Detection and a Robust Multi-Teacher Knowledge Distillation Framework](https://arxiv.org/pdf/2502.13407) \\
**Ziyuan Liu**, Ruifei Zhu, Long Gao, Yuanxiu Zhou, Jingyu Ma, Yuantao Gu

[**Code**](https://github.com/circleLZY/MTKD-CD) ![](https://img.shields.io/github/stars/circleLZY/MTKD-CD?style=social)
  -  We introduce **JL1-CD**, a new sub-meter, all-inclusive open-source CD dataset comprising 5,000 pairs of remote sensing image patches with a resolution of 0.5–0.75 meters. 
  -  We propose a multi-teacher knowledge distillation (MTKD) framework, which significantly improves the performance of CD models with various network architectures and parameter sizes without increasing any computational or time cost during inference.
</div>
</div>


## SAR Image Processing

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TGRS 2024</div><img src='images/dsrkd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DSRKD: Joint Despecking and Super-Resolution of SAR Images via Knowledge Distillation](https://ieeexplore.ieee.org/abstract/document/10606284) \\
**Ziyuan Liu**, Shaoping Wang, Ying Li, Yuantao Gu, Quan Yu

  - We propose the DSRKD network, with an encoder–upscaling–decoder architecture that allows for SR at various resolution scales. The encoder and decoder can also be replaced with various more complex modules, and various distillation methods can be easily added, making it a simple and efficient baseline for despeckling SR.
  - We innovatively combine the SR of speckled images with denoising using knowledge distillation (KD), significantly improving the performance of the model without introducing any additional computational overhead during inference.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GRSL 2024</div><img src='images/grsl.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[SAR Image Compression With Inherent Denoising Capability Through Knowledge Distillation](https://ieeexplore.ieee.org/abstract/document/10495338) \\
**Ziyuan Liu**, Shaoping Wang , Yuantao Gu

  - We innovatively utilize a KD mechanism to combine compression with denoising for speckled images. Our method exhibits superior performance compared to other methods on both synthetic and SAR datasets.
  - The distillation mechanism is applicable to various learned image compression algorithms and consistently enhances their performance.
  - This enhancement is achieved without introducing extra complexity in terms of computational time and memory utilization during inference.
</div>
</div>

## Others

- **[Diffusion Model]** [Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Learnable Linear Extrapolation](https://arxiv.org/pdf/2503.10103), Jiawei Zhang, **Ziyuan Liu**, Leon Yan, Gen Li, Yuantao Gu. arXiv 2025.