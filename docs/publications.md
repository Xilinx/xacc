# Publications

This page lists the research publications which have been carried out in the context of the XACC program, or papers that may be of interest to the XACC community. 

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md) 

## 2021

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| Distributed Recommendation Inference on FPGA Clusters | Yu Zhu *et al.* | ETH Zurich | [Paper](https://www.research-collection.ethz.ch/handle/20.500.11850/485145) | Implementation of an efficient distributed recommendation inference on an FPGA cluster that optimizes both the memory-bound embedding layer and the computation-bound fully-connected layers. The system achieves a maximum speed up of 28.95x, while guaranteeing very low latency.  |
| EasyNet: 100 Gbps Network for HLS | Zhenhao He *et al.* | ETH Zurich | [Paper](https://www.research-collection.ethz.ch/handle/20.500.11850/487920) [GitHub]( https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP)  | Integration of an open-source 100 Gbps TCP/IP stack into Vitis without degrading its performance. A set of MPI-like communication primitives are provided to abstract away low level details of the networking stack. |
| MicroRec: Efficient Recommendation Inference by Hardware and Data Structure Solutions | Wenqi Jiang *et al.* | ETH Zurich | [Paper](https://www.research-collection.ethz.ch/handle/20.500.11850/470540)  |  High-performance inference engine for recommendation systems. MicroRec accelerates recommendation inference by (1) redesigning the data structures to reduce the number of lookups and (2) taking advantage of HBM in FPGA accelerators to tackle the latency by enabling parallel lookups. |



## 2020

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| Do OS abstractions make sense on FPGAs? | Dario Korolija *et al.* | ETH Zurich | [Paper](https://www.usenix.org/conference/osdi20/presentation/roscoe) | To what extent do traditional OS abstractions make sense in the context of an FPGA as part of a hybrid system? This paper introduces Coyote which supports secure spatial and temporal multiplexing of the FPGA between tenants, virtual memory, communication, and memory management inside a uniform execution environment. |
| EMOGI: efficient memory-access for out-of-memory graph-traversal in GPUs| Seung Won Min *et al*| University of Illinois at Urbana-Champaign |  [Paper](https://dl.acm.org/doi/10.14778/3425879.3425883) | Sparse-matrix computation |
| Extending High-Level Synthesis for Task-Parallel Programs | Yuze Chi *et al.* | UCLA | [Paper](https://arxiv.org/abs/2009.11389)  |  Extend the HLS C++ language and present a fully automated framework with programmer-friendly interfaces, universal software simulation, and fast code generation to overcome these limitations. |
| FReaC Cache: Folded-logic Reconfigurable Computing in the Last Level Cache| Ashutosh Dhar *et al*| University of Illinois at Urbana-Champaign |  [Paper](https://ieeexplore.ieee.org/abstract/document/9251953) | Energy efficient computation |
| Making Search Engines Faster by Lowering the Cost of Querying Business Rules Through FPGAs | Fabio Maschi *et al.* | ETH Zurich |[Paper](https://doi.org/10.1145/3318464.3386133) | Explore how to use hardware acceleration to (i) improve the performance of the MCT module (lower latency, higher throughput); and (ii) reduce the amount of computing resources needed |
| Portable Linear Algebra on FPGA using Data-Centric Parallel Programming | Manuel Burger *et al.* | ETH Zurich | [demo](https://github.com/manuelburger/daceBLAS_demo) | 2020 XOHW Winner PhD |
| Specializing the network for scatter-gather workloads | Catalina Alvarez *et al.* | ETH Zurich | [Paper](https://dl.acm.org/doi/10.1145/3419111.3421301) | Explore hardware-offload of the scatter-gather primitive. This approach not only virtually eliminates CPU usage, but with suitable scheduling of responses, it also speeds up scatter by allowing parallel queries  |
| Weighing up the new kid on the block: Impressions of using Vitis for HPC software development | Nick Brown | The University of Edinburgh |[Paper](https://arxiv.org/abs/2010.00289) | Vitis case study using Himeno benchmark as a vehicle for exploring the Vitis platform for building, executing and optimizing HPC codes |


## 2019

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| AcMC²: Accelerating Markov Chain Monte Carlo Algorithms for Probabilistic Models| Subho S. Banerjee *et al*| University of Illinois at Urbana-Champaign |  [Paper](https://dl.acm.org/doi/10.1145/3297858.3304019) | Compiler development transforming probabilistic models into optimized hardware accelerators |
| Cloud-DNN: An Open Framework for Mapping DNN Models to Cloud FPGAs | Yao Chen *et al*| National University of Singapore |  [Paper](https://dl.acm.org/doi/10.1145/3289602.3293915) | Open-source automated tool chain called Cloud-DNN. Our tool chain takes trained CNN models specified in Caffe as input, performs a set of transformations, and maps the model to a cloud-based FPGA. Cloud-DNN can significantly improve the overall design productivity of CNNs on FPGAs while satisfying the emergent computational requirements. |
| Flexible Communication Avoiding Matrix Multiplication on FPGA with HLS | Johannes de Fine Licht, et al. | ETH Zurich |  [Paper](https://arxiv.org/abs/1912.06526) | A flexible, fully HLS-based, high-performance matrix multiplication accelerator, capable of efficiently utilizing all available resources on the target device, including for multi-SLR FPGAs. |
| High-Performance Distributed Memory Programming on Reconfigurable Hardware | Tiziano De Matteis, et al. | ETH Zurich |  [Paper](https://arxiv.org/abs/1909.03231) | SMI is an API that unifies the flexibility and single-program, multiple-data approach of MPI with the streaming programming model of spatial architectures. |
| Inductive-bias-driven Reinforcement Learning for Efficient Schedules in Heterogeneous Clusters| Subho S. Banerjee *et al*| University of Illinois at Urbana-Champaign |  [Paper](https://arxiv.org/abs/1909.02119) | System schedulers |
| **hlslib:** _Software Engineering for Hardware Design_ | Johannes de Fine Licht, et al. | ETH Zurich |  [Paper](https://arxiv.org/abs/1910.04436) | A collection of extensions for Vitis to improve developer quality of life, including CMake integration, better vectorization support, support for simulating dataflow kernels with feedback dependencies. |
| Stateful Dataflow Multigraphs: A Data-Centric Model for Performance Portability on Heterogeneous Architectures | Tal Ben-Nun, et al. | ETH Zurich |  [Paper](https://arxiv.org/abs/1902.10345) | Enables high-level programming of FPGAs from Python using the dataflow-based SDFG representation, allowing productive optimization of programs via provided graph transformations without modifying the input program, and code generating highly efficient FPGA kernels. |


## 2018

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| FINN-R: An End-to-End Deep-Learning Framework for Fast Exploration of Quantized Neural Networks |  Michaela Blott *et al.* |Xilinx Inc | [FINN-R paper](https://arxiv.org/abs/1809.04570) | Framework for Quantized Neural Networks on reconfigurable hardware |
| Transformations of High-Level Synthesis Codes for High-Performance Computing | Johannes de Fine Licht, et al. | ETH Zurich |  [Paper](https://arxiv.org/abs/1805.08288) | A survey of important source-to-source optimization techniques for high-throughput HLS codes to target pipelining, parallelism, and memory bandwidth utilization. |

## 2017

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| Architectural optimizations for high performance and energy efficient Smith-Waterman implementation on FPGAs using OpenCL| Lorenzo Di Tucci *et al*| Xilinx Inc. and Politecnico di Milano|  [Paper](https://ieeexplore.ieee.org/document/7927082) | Smith-Waterman: A key bio-informatics algorithm |

## 2016

| Name | Author(s) | Institution |Link | Notes |
|------|-----------|-------------|-----|-------|
| FINN: A Framework for Fast, Scalable Binarized Neural Network Inference  | Yaman Umuroglu *et al.*  | Xilinx Inc.| [FINN Paper](https://arxiv.org/abs/1612.07119) | Framework for Binarized Neural networks on reconfigurable hardware |

---------------------------------------
<p align="center">Copyright&copy; 2021 Xilinx</p>