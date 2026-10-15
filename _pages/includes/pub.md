# 📝 Selected Publications

{% capture scholar_badge_data_url %}https://raw.githubusercontent.com/{{ site.repository }}/google-scholar-stats/gs_data_shieldsio.json{% endcapture %}
My full paper list can be found at <a href="{{ site.author.googlescholar }}"><img src="https://img.shields.io/endpoint?url={{ scholar_badge_data_url | url_encode }}&amp;logo=Google%20Scholar&amp;labelColor=f6f6f6&amp;color=9cf&amp;style=flat&amp;label=citations&amp;cacheSeconds=300" alt="Total citations on Google Scholar" style="vertical-align: middle;"></a>.

## LLM

<!-- Figure 1 from Iris, arXiv:2609.04304v2, page 1. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2026</div><img src='images/iris.png' alt="Iris performance across four agentic search benchmarks" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Iris: Climbing to the Search Frontier](https://arxiv.org/pdf/2609.04304) \\
AllSpark Team (First core contributor: **Ziyuan Liu**)

[**Code**](https://github.com/AllSpark-Research/Iris) ![](https://img.shields.io/github/stars/AllSpark-Research/Iris?style=social) | [**Models**](https://huggingface.co/collections/AllSpark-Research/iris)
  - We develop **Iris-mini and Iris-pro**, search agents trained through multi-hop task construction, trajectory filtering, and iterative SFT-RL climbing against live web search.
  - With context management, Iris achieves the strongest overall results among open-source search agents in the same parameter ranges across BrowseComp, BrowseComp-ZH, DeepSearchQA, and HLE.
</div>
</div>

<!-- Figure 2 from MiroFlow, arXiv:2602.22808v1, page 4. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2026</div><img src='images/miroflow.png' alt="Overview of the three-tier MiroFlow agent framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks](https://arxiv.org/pdf/2602.22808) \\
MiroMind Team

[**Code**](https://github.com/MiroMindAI/MiroFlow) ![](https://img.shields.io/github/stars/MiroMindAI/MiroFlow?style=social)
  - We introduce **MiroFlow**, an open-source framework for general deep research, combining flexible agent graphs, robust workflow execution, and an optional heavy-reasoning mode.
  - A unified configuration delivers strong, reproducible results across GAIA, BrowseComp, HLE, xBench-DeepSearch, and FutureX.
</div>
</div>

<!-- Figure 2 from MiroThinker, arXiv:2511.11793v3, page 4. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2025</div><img src='images/mirothinker.png' alt="MiroThinker architecture with tools, context management, and interactive scaling" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://arxiv.org/pdf/2511.11793) \\
MiroMind Team

[**Code**](https://github.com/MiroMindAI/MiroThinker) ![](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) | [**Model**](https://huggingface.co/miromind-ai/MiroThinker-v1.0-72B)
  - We introduce **MiroThinker v1.0**, an open-source research agent that scales model size, context length, and the depth of agent-environment interactions.
  - With a 256K context window and up to 600 tool calls per task, the model sustains long research trajectories and achieves strong results on GAIA, HLE, and BrowseComp.
</div>
</div>

## Remote Sensing Change Detection

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TIM 2026</div><img src='images/mtkd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[JL1-CD: A New Benchmark for Remote Sensing Change Detection and a Robust Multi-Teacher Knowledge Distillation Framework](https://arxiv.org/pdf/2502.13407) \\
**Ziyuan Liu**, Ruifei Zhu, Long Gao, Yuanxiu Zhou, Jingyu Ma, Yuantao Gu

[**Code**](https://github.com/circleLZY/MTKD-CD) ![](https://img.shields.io/github/stars/circleLZY/MTKD-CD?style=social)
  -  We introduce **JL1-CD**, a new sub-meter, all-inclusive open-source CD dataset comprising 5,000 pairs of remote sensing image patches with a resolution of 0.5–0.75 meters. 
  -  We propose a multi-teacher knowledge distillation (MTKD) framework, which significantly improves the performance of CD models with various network architectures and parameter sizes without increasing any computational or time cost during inference.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JSTARS 2026</div><img src='images/unlearningcd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[UnlearningCD: Distill to Forget in Change Detection via Perturbed Knowledge](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11359002) \\
**Ziyuan Liu**, Jiawei Zhang, Qitan Shi, Yuantao Gu
  -  We propose **U**nlearning algorithm based on **P**erturbed **K**nowledge distillation (UPK), a machine unlearning method applied to CD tasks for the first time.
  -  The proposed method requires only 10% of the iterations for training the original model and surpasses existing approaches across both closed-box and open-box settings, in both SCD and BDA tasks, and on CNN, Transformer, and Mamba model backbones.
</div>
</div>


<!-- Figure 1 from Open-CD, arXiv:2407.15317v2, page 6. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">ACM MM 2025</div><img src='images/opencd.png' alt="Overview of the Open-CD toolbox architecture" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Open-CD: A Comprehensive Toolbox for Change Detection](https://arxiv.org/pdf/2407.15317) \\
Kaiyu Li\*, Jiawei Jiang\*, ..., **Ziyuan Liu\***, Yuantao Gu, ..., Xiangyong Cao

[**Code**](https://github.com/likyoo/open-cd) ![](https://img.shields.io/github/stars/likyoo/open-cd?style=social)
  - We introduce **Open-CD**, a unified, modular toolbox for binary and semantic change detection, integrating diverse models, datasets, training pipelines, and analysis tools.
  - We benchmark representative methods under a unified evaluation protocol, providing a flexible platform for reproducing existing algorithms and developing new change detectors.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">JSTARS 2025</div><img src='images/mbsd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[A Novel Multi-Branch Self-Distillation Framework for Optimizing Remote Sensing Change Detection](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=11122566) \\
**Ziyuan Liu**, Jiawei Zhang, Wenyu Wang, Yuantao Gu
  -  We propose the MBSD training framework, a novel and generalizable self-distillation learning paradigm designed for CD tasks.
  -  The proposed framework is single-stage, end-to-end, and incurs only a modest memory and time increase during training, with no extra cost during inference.
</div>
</div>

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">GRSL 2025</div><img src='images/m2cd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[M$^2$CD: A Unified MultiModal Framework for Optical-SAR Change Detection with Mixture of Experts and Self-Distillation](https://arxiv.org/abs/2503.19406) \\
**Ziyuan Liu**, Jiawei Zhang, Wenyu Wang, Yuantao Gu
  -  We propose a unified **M**ulti**M**odal **CD** framework (M$^2$CD), which is highly versatile and robust, compatible with various backbone architectures.
  -  By introducing modality-specialized MoE modules into the backbone and innovatively proposing an Optical-to-SAR transition path (O2SP) for self-distillation guidance, we reduce the feature space discrepancies between different modalities and alleviate the model’s burden in processing multimodal data.
  -  Extensive experiments on the CAU-Flood dataset demonstrate that M2CD outperforms all SOTA methods.
</div>
</div>


## Others
- **[Diffusion Model]** [Stage-wise Distortion-Perception Traversal in Zero-shot Inverse Problems with Diffusion Models](https://arxiv.org/abs/2605.28711), Jiawei Zhang, **Ziyuan Liu**, ..., Yuantao Gu. ICML 2026.
- **[Diffusion Model]** [Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Learnable Linear Extrapolation](https://arxiv.org/pdf/2503.10103), Jiawei Zhang, **Ziyuan Liu**, ..., Yuantao Gu. NeurIPS 2025.
- **[Knowledge Distillation]** [S3AT: Self-Paced, Self-Distilled, and Self-Finetuned Adversarial Training for Robust Automatic Modulation Recognition](https://ieeexplore.ieee.org/abstract/document/11298184/), Wenyu Wang, Zhu Lei, **Ziyuan Liu**, ... . TCCN 2025.

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
