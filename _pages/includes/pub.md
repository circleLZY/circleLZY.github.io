# 📝 Selected Publications

{% capture scholar_badge_data_url %}https://raw.githubusercontent.com/{{ site.repository }}/google-scholar-stats/gs_data_shieldsio.json{% endcapture %}
My full paper list can be found at <a href="{{ site.author.googlescholar }}"><img src="https://img.shields.io/endpoint?url={{ scholar_badge_data_url | url_encode }}&amp;logo=Google%20Scholar&amp;labelColor=f6f6f6&amp;color=9cf&amp;style=flat&amp;label=citations&amp;cacheSeconds=300" alt="Total citations on Google Scholar" style="vertical-align: middle;"></a>.

## LLM

{% capture iris_downloads_url %}https://raw.githubusercontent.com/{{ site.repository }}/model-download-stats/iris.json{% endcapture %}
{% capture mirothinker_downloads_url %}https://raw.githubusercontent.com/{{ site.repository }}/model-download-stats/mirothinker-v1.json{% endcapture %}

<!-- Figure 1 from Navalia, arXiv:2610.26887v1, page 3. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2026</div><img src='images/navalia.png' alt="Navalia pipeline for verifiable task synthesis and long-horizon post-training" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Navalia: Advancing Cowork Agents through Verifiable Task Synthesis and Long-Horizon Post-Training](https://arxiv.org/pdf/2610.26887) \\
AllSpark Team (**Core contributor**)

[**Project**](https://github.com/AllSpark-Research/AgentEnv/tree/main/Navalia) [![AgentEnv GitHub stars](https://img.shields.io/github/stars/AllSpark-Research/AgentEnv?style=social)](https://github.com/AllSpark-Research/AgentEnv/tree/main)
  - We introduce **Navalia**, combining verifiable task synthesis from financial reports with cold-start SFT and long-horizon RL to improve Cowork Agents.
  - Navalia-35B-A3B delivers competitive performance with leading open- and closed-source models on several financial analysis and general-purpose Cowork benchmarks, scoring 62.66% on OfficeQA Pro and 59.27% on Workspace-Bench-Lite.
</div>
</div>

<!-- Figure 1 from Iris, arXiv:2609.04304v2, page 1. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2026</div><img src='images/iris.png' alt="Iris performance across four agentic search benchmarks" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[Iris: Climbing to the Search Frontier](https://arxiv.org/pdf/2609.04304) \\
AllSpark Team (**First core contributor**)

[**Project**](https://github.com/AllSpark-Research/Iris) ![](https://img.shields.io/github/stars/AllSpark-Research/Iris?style=social) | <span style="white-space: nowrap;"><a href="https://huggingface.co/collections/AllSpark-Research/iris"><strong>Weights</strong></a> <a href="https://huggingface.co/collections/AllSpark-Research/iris" title="Cumulative Hugging Face downloads: Iris-mini + Iris-pro. Updated daily."><img src="https://img.shields.io/endpoint?url={{ iris_downloads_url | url_encode }}&amp;style=social&amp;logo=huggingface" alt="Iris cumulative model downloads" style="vertical-align: middle;"></a></span>
  - We develop **Iris-mini** (35B) and **Iris-pro** (397B).
  - Iris achieves the strongest overall results among open-source search agents in the same parameter ranges across BrowseComp, BrowseComp-ZH, DeepSearchQA, and HLE.
</div>
</div>

<!-- Figure 2 from MiroFlow, arXiv:2602.22808v1, page 4. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2026</div><img src='images/miroflow.png' alt="Overview of the three-tier MiroFlow agent framework" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MiroFlow: Towards High-Performance and Robust Open-Source Agent Framework for General Deep Research Tasks](https://arxiv.org/pdf/2602.22808) \\
MiroMind Team

[**Project**](https://github.com/MiroMindAI/MiroFlow) ![](https://img.shields.io/github/stars/MiroMindAI/MiroFlow?style=social)
  - We introduce **MiroFlow**, an open-source framework for general deep research, combining flexible agent graphs, robust workflow execution, and an optional heavy-reasoning mode.
  - A unified configuration delivers strong, reproducible results across GAIA, BrowseComp, HLE, xBench-DeepSearch, and FutureX.
</div>
</div>

<!-- Figure 2 from MiroThinker, arXiv:2511.11793v3, page 4. -->
<div class='paper-box'><div class='paper-box-image'><div><div class="badge">Tech Report 2025</div><img src='images/mirothinker.png' alt="MiroThinker architecture with tools, context management, and interactive scaling" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[MiroThinker: Pushing the Performance Boundaries of Open-Source Research Agents via Model, Context, and Interactive Scaling](https://arxiv.org/pdf/2511.11793) \\
MiroMind Team

[**Project**](https://github.com/MiroMindAI/MiroThinker) ![](https://img.shields.io/github/stars/MiroMindAI/MiroThinker?style=social) | <span style="white-space: nowrap;"><a href="https://huggingface.co/miromind-ai/MiroThinker-v1.0-72B"><strong>Weights</strong></a> <a href="https://huggingface.co/miromind-ai/MiroThinker-v1.0-72B" title="Cumulative Hugging Face downloads: MiroThinker v1.0 8B + 30B + 72B. Updated daily."><img src="https://img.shields.io/endpoint?url={{ mirothinker_downloads_url | url_encode }}&amp;style=social&amp;logo=huggingface" alt="MiroThinker v1.0 cumulative model downloads" style="vertical-align: middle;"></a></span>
  - We introduce **MiroThinker**, an open-source research agent that scales model size, context length, and the depth of agent-environment interactions.
  - With a 256K context window and up to 600 tool calls per task, the model sustains long research trajectories and achieves strong results on GAIA, HLE, and BrowseComp.
</div>
</div>

## Remote Sensing Change Detection

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TIM 2026</div><img src='images/mtkd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[JL1-CD: A New Benchmark for Remote Sensing Change Detection and a Robust Multi-Teacher Knowledge Distillation Framework](https://arxiv.org/pdf/2502.13407) \\
**Ziyuan Liu**, Ruifei Zhu, Long Gao, Yuanxiu Zhou, Jingyu Ma, Yuantao Gu

[**Project**](https://github.com/circleLZY/MTKD-CD) ![](https://img.shields.io/github/stars/circleLZY/MTKD-CD?style=social)
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

[**Project**](https://github.com/likyoo/open-cd) ![](https://img.shields.io/github/stars/likyoo/open-cd?style=social)
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


## SAR Image Processing

<div class='paper-box'><div class='paper-box-image'><div><div class="badge">TGRS 2024</div><img src='images/dsrkd.png' alt="sym" width="100%"></div></div>
<div class='paper-box-text' markdown="1">

[DSRKD: Joint Despecking and Super-Resolution of SAR Images via Knowledge Distillation](https://ieeexplore.ieee.org/abstract/document/10606284) \\
**Ziyuan Liu**, Shaoping Wang, Ying Li, Yuantao Gu, Quan Yu

  - We propose the **DSRKD** network, with an encoder–upscaling–decoder architecture that allows for SR at various resolution scales. The encoder and decoder can also be replaced with various more complex modules, and various distillation methods can be easily added, making it a simple and efficient baseline for despeckling SR.
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
- **[Diffusion Model]** [Manifold-Constrained Noise Optimization for Diverse Diffusion Sampling](https://arxiv.org/abs/2607.23937), Qitan Shi, Cheng Jin, **Ziyuan Liu**, Yuantao Gu. arXiv 2026.
- **[Diffusion Model]** [Stage-wise Distortion-Perception Traversal in Zero-shot Inverse Problems with Diffusion Models](https://arxiv.org/abs/2605.28711), Jiawei Zhang, **Ziyuan Liu**, ..., Yuantao Gu. ICML 2026.
- **[Diffusion Model]** [Improving Diffusion-based Inverse Algorithms under Few-Step Constraint via Learnable Linear Extrapolation](https://arxiv.org/pdf/2503.10103), Jiawei Zhang, **Ziyuan Liu**, ..., Yuantao Gu. NeurIPS 2025.
- **[Knowledge Distillation]** [S3AT: Self-Paced, Self-Distilled, and Self-Finetuned Adversarial Training for Robust Automatic Modulation Recognition](https://ieeexplore.ieee.org/abstract/document/11298184/), Wenyu Wang, Zhu Lei, **Ziyuan Liu**, ... . TCCN 2025.
