# HACC Tech Talk series

The talks will be hosted as Zoom webinars and are free to attend. The format for each session will be two 30-minute talks on topics related to Adaptive Compute.

If you would like to present your work at an HACC Tech Talk, please contact [aup@amd.com](mailto:aup@amd.com) with an outline of your proposal.

## Past talks


### HACC Tech Talk 16

24<sup>th</sup> March 2025 

#### **StreamFlex: Harnessing FPGA Capabilities at Software Compile Time via Virtualization and Precompiled Hardware Binaries** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/w30r6LVvzbc" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Gregory Jun, University of Illinois Urbana Champaign

As we increasingly turn to accelerators to address the demands of modern computing—such as Transformer-based machine learning models, cryptographic applications, and high-performance computing (HPC)—the importance of heterogeneity in computing systems continues to grow. In this dynamic landscape, FPGAs are uniquely positioned to bridge the gap between control-flow-based, irregular workloads suited for CPUs and throughput-oriented, regular computations optimized for GPUs. With the right architectural design, FPGAs have the potential to dynamically optimize and adapt to the evolving algorithms of modern applications, offering a critical balance of flexibility and performance. However, FPGAs have long remained outside the mainstream due to two primary challenges: programmability and cost. Firstly, FPGAs are inherently expensive, driven by high development costs, the complexity of accompanying tools, and the significant silicon area they occupy. Secondly, leveraging FPGAs effectively requires users to design custom bitstreams tailored to specific computational tasks. This process demands extensive effort in hardware design and verification, making it impractical for most individual users or small-scale applications.  In this talk, we propose a solution to these challenges by leveraging the Network-on-Chip (NoC) architecture of the latest Versal family member, the V80. First, we dynamically stitch pre-generated hardware bitstreams, designed and verified by hardware engineers, to significantly lower the barrier for application development. Second, by utilizing virtualization methodologies through Dynamic Function Exchange (DFX), we partition the large FPGA into tiles, enabling applications to request and utilize the minimal necessary hardware resources at runtime. This approach enhances accessibility and efficiency, making FPGAs more practical for a wider range of users and applications. 

#### **FPGA-based SmartNICs: OS4C and Beyond** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/nIxBgIGuCB8" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Scott Smith, University of Illinois Urbana Champaign

Smart network interface cards (SmartNICs) are powerful, high-throughput programmable devices. These devices enable developers to offload specific functionalities to hardware, improving performance and/or reducing CPU overheads. Over the last several years, much work has been done in this research area. This talk will cover three broad strokes. First, we will briefly overview the current state-of-the-art SmartNIC architecture research. Second, we will present our recent work, "OS4C: An Open-Source SR-IOV System for SmartNIC-based Cloud Platforms." This work discussed the limitations of current open-source NICs and extended the open-source NIC Corundum with support for Single Root I/O Virtualization. Third, we will discuss our plans to build a new NIC architecture on the Alveo V80 FPGA. We aim for this project to be the first open-source 200+ Gbps NIC. Furthermore, our architecture will enable greater flexibility and programmability than current state-of-the-art FPGA-based SmartNICs. 


### HACC Tech Talk 15

14<sup>th</sup> November 2024

#### **Optimizing Communication for Latency Sensitive HPC Applications on up to 48 FPGAs Using ACCL** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/gdonRDGj9n4" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Marius Meyer, Paderborn University

Most FPGA boards in the HPC domain are well-suited for parallel scaling because of the direct integration of versatile and high-throughput network ports. However, the utilization of their network capabilities is often challenging and error-prone because the whole network stack and communication patterns have to be implemented and managed on the FPGAs. Also, this approach conceptually involves a trade-off between the performance potential of improved communication and the impact of resource consumption for communication infrastructure, since the utilized resources on the FPGAs could otherwise be used for computations. In this work, we investigate this trade-off, firstly, by using synthetic benchmarks to evaluate the different configuration options of the communication framework ACCL and their impact on communication latency and throughput. Finally, we use our findings to implement a shallow water simulation whose scalability heavily depends on low-latency communication. With a suitable configuration of ACCL, good scaling behaviour can be shown to all 48 FPGAs installed in the system. Overall, the results show that the availability of inter-FPGA communication frameworks as well as the configurability of framework and network stack are crucial to achieve the best application performance with low latency communication.

#### **OMPC FPGA: Integrating Multi-FPGA Acceleration to OpenMP Distributed Computing** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/yy8IFcPdWTE" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Pedro Di Francia Rosso, Unicamp, Brazil

Programming FPGA accelerated applications often requires the developers to master multiple frameworks and toolchains. This work introduces FPGA offloading support to OpenMP Cluster (OMPC). OMPC is a framework designated to abstract distributed computing from applications that uses CPU and GPUs, programming only with OpenMP. The integration enables developers to use FPGA accelerators with just a few lines of code, through the OpenMP standard directive variant. Experimental results demonstrate speed-ups gains using different heterogeneous accelerator arrangements with CPU, FPGA and GPU. Through the Halstead Metrics measurements, the framework is capable of reducing 45% of the implementation effort. Furthermore, enabling communication acceleration using ACCL resulted in speed-ups up to 1.41x over the default communication mechanism (MPI) on a synthetic benchmark (Task Bench). 


### HACC Tech Talk 14

29<sup>th</sup> October 2024

#### **Energy-Efficient Computation for Machine Learning Workloads** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/UpbYGnpIHcA" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr. Viveka Konandur Rajanna, Indian Institute of Science (IISc)

Energy-efficient systems for machine learning are in high demand, especially for power-constrained edge devices. Static Random-Access Memories (SRAMs) are key to system-on-chips (SoCs), and in-memory computation (IMC) enhances efficiency by combining data storage with processing. We introduce an SRAM macro that supports continuous sensing, low-power event detection, and reduces bitline activity for energy-efficient bulk reads without the need for data prediction.
Secure systems rely on dynamic entropy from True Random Number Generators (TRNGs) and static entropy from Physically Unclonable Functions (PUFs). Our SRAM integrates both TRNG and multi-bit PUF for low-cost, area-efficient security. For applications like sensor-rich robotics and prosthetics, our tactile sensing system supports high receptor density, achieving sub-0.01mm² per receptor and sub-µW power, enabling efficient, long-lasting operation on stretchable substrates.

#### **Performance Analysis of GEMM Workloads on the AMD Versal Platform** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/pG-dKlNtqH8" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Kaustubh Mhatre, Arizona State University

AMD Versal is a new heterogeneous computing hardware architecture comprised of adaptive intelligence (AI) engines, programmable logic, and a processing system. General Matrix Multiplication (GEMM) is the fundamental building block of modern deep learning (DL) applications such as ChatGPT. GEMM workloads can be mapped onto Versal in many ways, each with distinct trade-offs. In this talk, we will present multiple research questions related to performance scaling, sensitivity and efficiency of GEMM workloads on the AMD Versal platform. We will discuss a few ways of mapping GEMM onto the AI engines, and share results from our thorough analysis of GEMM workloads of different shapes and sizes that help us understand the Versal architecture better. We will provide guidelines and insights for enhancing GEMM performance on AMD Versal.  


### HACC Tech Talk 13

10<sup>th</sup> October 2024

#### **RoCE Balboa – RDMA Deep Packet Inspection at Line Rate with ML-models on FPGAs** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/M_Jn7t7A3nc" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Maximilian Heer, Benjamin Ramhorst,  ETH Zurich

FPGAs are becoming increasingly important in the cloud and data centers, especially as network-attached accelerators or reconfigurable NICs. In the cloud, RDMA over Converged Ethernet (RoCEv2) has emerged as the de facto protocol for data transport due to its low latency and high throughput. However, RDMA has several security weaknesses that limit its applicability. We explore using machine learning-based deep packet inspection as an enhancement to an open-source FPGA RDMA-stack. The ultra-low-latency ML model is integrated on the RDMA data path and allows for detection of executable code in RDMA-payloads at line rate of 100Gbps while using less than 1% of the available resources. This solution operates on the message payload, at the transport level, and on a complete RDMA stack without sacrificing compatibility with RoCEv2 and existing applications, proving the significant potential of the proposed approach as an end-to-end solution.

#### **TaPaSCo on Versal: AIE, QDMA Streaming and MRMAC** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/7PdZ1SiObpA" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Torben Kalkhof, TU Darmstadt

The Task Parallel System Composer (TaPaSCo) is an open-source framework designed to simplify the construction of heterogeneous computing systems by efficiently offloading tasks to hardware accelerators. In this presentation, we explore how TaPaSCo leverages key features of the AMD Versal architecture, including AI Engines (AIE) for high-performance compute, Queue Direct Memory Access (QDMA) for efficient data streaming, and Multi-rate MAC (MRMAC) for high-speed networking.

### HACC Tech Talk 12

19<sup>th</sup> September 2024

#### **Pruning in the Datafree regime: A Distributional approach to Structured Pruning** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/dxXPNWm43Vw" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr. Chiranjib Bhattacharyya, IISc


Minimizing Inference time in Deep Networks is one of the biggest challenges in modern day AI systems. Model pruning is considered an important approach in addressing this issue. In this talk we highlight our recent progress in developing novel algorithms for structured pruning which do not require access to the original Training dataset,  a requirement for many existing methods.  We consider a distributional perspective on Model pruning, a novel view ,  which proposes to prune filters which have poor discriminative ability. The discriminative ability of a filter is identified through a novel lower bound on Toral Variation distance.
Experimental results show that the approach is superior to existing methods.



#### **Energy-efficient 2.5D System for LLM Inference** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/fiHV9G9mH8A" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr. Sumit Kumar Mandal, IISc


Large Language Models (LLMs) are used to perform various tasks, especially in the domain of natural language processing (NLP). State-of-the-art LLMs consist of a large number of parameters that necessitate a high volume of computations. Currently, GPUs are the preferred choice of hardware platform to execute LLM inference. However, monolithic GPU-based systems executing large LLMs pose significant drawbacks in terms of fabrication cost and energy efficiency. In this work, we propose a heterogeneous 2.5D chiplet-based architecture for accelerating LLM inference. Thorough experimental evaluations with a wide variety of LLMs show that the proposed 2.5D system provides up to 972× improvement in latency and 1600× improvement in energy consumption with respect to state-of-the-art edge devices equipped with GPU. 



### HACC Tech Talk 11

22<sup>nd</sup> August 2024

#### **ROCm Ecosystem and HIP Programming** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/m2dU5gyImno" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Tom Papatheodore, AMD University Program.


ROCm is an open-source software stack that consists of a collection of drivers, development tools, and APIs that enable GPU programming from low-level kernel to end-user applications.
The ROCm ecosystem will be introduced along with the Heterogeneous-Compute Interface for Portability (HIP), which is a C++ Runtime API and Kernel Language that allows developers to create portable applications for AMD and NVIDIA GPUs from a single source code.

#### **Profiling Tools for AMD Hardware** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/-ZjMnUVx5yM" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>


Giacomo Capodaglio, AMD HPC Solutions & Performance Analysis

This talk will introduce three powerful open-source profiling tools:
rocprof profiles all hardware counters on your GPU during execution.
Omnitrace profiles and traces parallel applications, including HIP and machine learning packages, across multiple languages (C, C++, Fortran, HIP, OpenCL, and Python) on both CPU and GPU.
Omniperf is a system performance profiler designed for HPC and ML workloads using AMD Instinct GPUs.

### HACC Tech Talk 10

17<sup>th</sup> July 2024

#### **Serpens and Callipepla** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/gxpSAd-_nv4" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr. Linghao Song, UCLA.

Two FPGA-based HBM accelerators for enhanced computational efficiency will be introduced. 
Callipepla accelerates preconditioned conjugate gradient solvers, achieving significant speedup and energy efficiency over existing solutions. 
Serpens, designed for sparse matrix-vector multiplication (SpMV), outperforms the latest accelerators and GPUs in throughput and efficiency. These advancements demonstrate the potential of HBM-based FPGAs in scientific and engineering applications.

#### **HiHiSpMV: Sparse Matrix Vector Multiplication with Hierarchical Row Reductions on FPGAs with High Bandwidth Memory** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/Q0A78uenjuA" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr. Tobias Kenter, University of Paderborn

Using the full potential of Alveo U280 for Sparse Matrix Vector Multiplications FPGAs with High Bandwidth Memory are a promising architecture for sparse linear algebra, but so far it has been challenging to fully utilize the bandwidth their potential. This talk presents HiHiSpMV, a new approach for sparse matrix vector multiplication on FPGAs using hierarchical row reductions, and a corresponding design implemented with Vitis. The design can fully utilize all 32 HBM channels on the Alveo U280 card, reaches up to 396 GB/s measured bandwidth and has a higher bandwidth utilization than alternative designs on many input matrices.

### HACC Tech Talk 9

26<sup>th</sup> June 2024

#### **XDNA™ Architecture and Programming Model** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/smZKj7GUuWE" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Mario Ruiz, AMD University Program.

AMD XDNA™ is a multi-generation spatial dataflow architecture consisting of two-dimension array of VLIW and SIMD AI Engine cores that provide high compute density in addition to an efficient network of interconnects for optimized data movement.
The programming model is defined by a data flow graph where nodes describe computation, and edges specify data movement. XDNA technology is integrated in multiple AMD products, including Adaptive SoC and Ryzen AI.

#### **CHARM: Composing Heterogeneous Accelerators for Matrix Multiply on Versal ACAP devices** 

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/KaNvGittGVo" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Jinming Zhuang, University Pittsburgh.

AMD Versal offer a powerful platform for dense Matrix Multiplication for deep learning. Large MM operations can be efficiently parallelized, but small ones often underperform.
CHARM optimizes MM architectures for better throughput. Analytical models help customize accelerators, partition hardware resources, and schedule layers.
For BERT, ViT, NCF, and MLP, we achieved gains of 5.40x, 32.51x, 1.00x, and 1.00x respectively compared to a single monolithic accelerator.

### XACC Tech Talk 8

30<sup>th</sup> March 2022

#### **ACCL: an open-source FPGA accelerated communication library for scale-out applications**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/jqrziE9cZg4" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Lucian Petrica, AMD AECG Research Labs.

This talk will present ACCL, an open-source FPGA-accelerated communication collectives library designed to enable scale-out of applications running primarily on AMD FPGAs. Compared to previous collective communication solutions for FPGA, ACCL is flexible and extensible, easily portable, and fast. We evaluate ACCL on 8 Alveo nodes at XACC ETHZ and demonstrate that ACCL outperforms OpenMPI over 100 Gbps TCP-IP for large messages.

#### **Efficient Recommendation Inference on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/SJ0ze3p0GzU" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Wengi Jiang, ETH Zurich.

Deep neural networks are widely used in personalized recommendation systems. Recommendation inference is largely bound by memory due to random memory accesses needed to lookup the embedding tables. 
This talk will introduce MicroRec, a high-performance FPGA inference engine for recommendation systems that tackles the memory bottleneck. This is extended to implement two high-performance recommendation inference clusters; one using FPGAs and the other using combined FPGAs and GPUs. 
Experiments on three production models show that our cluster-based solutions outperform the CPU baseline by more than one order of magnitude while achieving significantly lower latency.

### XACC Tech Talk 7

16<sup>th</sup>  December 2021

#### **Easy deployment, scaling and resource management of Alveo FPGA​**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/NGhgmryVTm0" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Chris Kachis, InAccel

In this talk we will present an easy way to deploy, scale and manage FPGA application on Alveo clusters such as XACC. InAccel will present the Coral resource manager that abstract away the FPGA resources for easy utilization and instant scaling of FPGA designs. It will also show how we managed to support multi-FPGA accelerators (such as FINN) using a custom InAccel runtime for synchronization between accelerators. Finally, we will show how Coral resource manager can be used for easier deployment of the Vitis AI and Vitis libraries. 

#### **Lucent: A language for developing application specific dataflow machines on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/z9LsKxfP_-w" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Nick Brown, EPCC, University of Edinburgh

Writing fast, high performance FPGA codes is difficult, even with HLS. However potentially we can learn from work done in the 1970s/1980s which studied programming general purpose dataflow machines, as the reconfigurability of FPGAs enable us to present the abstraction of dataflow machines which are specific to an application. In this talk I will describe Lucent, a modern version of the Lucid dataflow language, which targets AMD Alveo hardware and aims to empower the development of fast by construction dataflow codes on FPGAs.

### XACC Tech Talk 6

19<sup>th</sup>  August 2021

#### **Multes on Alveo: An FPGA-based Smart Key-Value Store Running on XACC**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/lkxw6OUMtNU?" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>

Zsolt István, Assoc. Prof, IT University of Copenhagen

In this talk, we will present Multes, an FPGA-based Key-Value Store (KVS) with user-defined query offloading (the “smarts”) and explain how it has been ported to the Alveo cards in XACC using the Vitis Shell with 100Gbps networking. We will also present an example of offloading to the KVS, namely, a privacy-preserving perturbation for ML training.

#### **TAPA: Efficient Support for Task-Parallel High-Level Synthesis**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/lkxw6OUMtNU?start=1667" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>
Yuze Chi, Computer Science Department, UCLA

This talk will present TAPA, a fully automated framework for task-parallel HLS programs with programmer-friendly interfaces, unconstrained software simulation, and fast hierarchical code generation.

Experimental results based on a wide range of real-world task-parallel programs show that the lines of kernel and host code, the correctness verification cycle, and the iterative QoR tuning cycle are all greatly shortened, which considerably improves the programmability.

### XACC Tech Talk 5

05<sup>th</sup>  August 2021

#### **Optimized Implementation of the HPCG Benchmark on Reconfigurable Hardware**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/9pq2GxBC32Q?start=66" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>
Alberto Zeni, Politecnico Di Milano

The HPCG benchmark represents a modern complement to the HPL benchmark in the performance evaluation of HPC systems, as it has been recognized as a more representative benchmark to reflect real-world applications and, consequently, its popularity and acceptance continue to rise within the HPC community. This talk will present the first FPGA-based implementation of the HPCG benchmark, which takes full advantage of reconfigurable architectures. Our implementation shows performance up to 108.4 and 346.5 GFlops on 1 and 4 AMD Alveo U280 cards on the XACC cluster, demonstrating significant performance improvements against the CPU implementation and comparable performance with GPU implementations with better power efficiency. 

#### **ScaleHLS: Scalable High-Level Synthesis through MLIR**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/9pq2GxBC32Q?start=2117" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Hanchen Ye, UIUC

High-level Synthesis (HLS) has been widely adopted as it significantly improves the hardware design productivity and enables efficient design space exploration (DSE). HLS tools can be used to deliver solutions for many different kinds of design problems, and different problems are often better solved with different levels of abstraction. While existing HLS tools are built using compiler infrastructures largely based on a single-level abstraction (e.g., LLVM), we propose ScaleHLS, a next-generation HLS compilation flow, on top of a multi-level compiler infrastructure called MLIR, for the first time. ScaleHLS is able to optimize HLS designs at multiple levels of abstraction and provides an HLS-dedicated transform and analysis library to solve the optimization problems at the suitable abstraction levels. On top of the library, we also build an automated DSE engine to explore the multi-dimensional design space highly efficiently. In addition, we develop an HLS C front-end and a C/C++ emission back-end to translate HLS designs into/from MLIR for enabling the end-to-end ScaleHLS flow. Experimental results show that, comparing to the baseline designs only optimized by AMD Vivado HLS, ScaleHLS improves the performances with amazing quality-of-results -- up to 768.1x better on computation kernel level programs and up to 3825.0x better on neural network models.

### XACC Tech Talk 4

22<sup>nd</sup>  July 2021

#### **ThundeRiNG: Generating Multiple Independent Random Number Sequences on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/q4BcSNVNR2A?start=84" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Hongshi Tan, Master student, National  University of Singapore

*ThundeRiNG* is a high-throughput system for generating multiple independent sequences of random numbers on FPGAs. The experimental results show that ThundeRiNG passes the strictest randomness tests, BigCrush, achieving a throughput of 20.95 Tb/s. 
Compared to a state-of-the-art GPU library, ThundeRiNG demonstrates a 10x speedup in throughput and 9x performance and 26x power efficiency improvement on two applications (pi estimation and Monte Carlo option pricing).

#### **Fletcher: A framework for high-performance big data analytics using FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/q4BcSNVNR2A?start=1642" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Joost Hoozemans, Postdoctoral researcher, TU Delft

This talk will present a vision for transparent acceleration of analytics workloads on FPGAs.
The *Fletcher* project allows integrating FPGAs into scalable software frameworks, to efficiently utilize them in a cloud hardware infrastructure. Fletcher supports Alveo FPGA cards in the XACC cluster, AWS F1 and Azure instances.
We demonstrate the integration of FPGA implementations of various analytics operations into a number of popular analytics frameworks (Apache Spark, Dremio, Dask) and show significant speedup.

### XACC Tech Talk 3

8<sup>th</sup>  July, 2021

#### **Blockchain Machine: Accelerating Validation Bottlenecks in Hyperledger Fabric**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/D8ZunBYc5xI?start=75" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Haris Javaid, Senior Staff Researcher, Xilinx

Blockchain Machine is a hardware accelerator for validation of blocks in Hyperledger Fabric, one of the most widely used permissioned blockchain platforms. It is targeted for a server with network-attached FPGA acceleration card and can be adapted to applications and their smart contracts (built on top of Fabric). The Blockchain Machine retrieves block/transaction data in hardware directly from the network interface, which is then processed through a configurable and efficient block-level and transaction-level pipeline. The results are then accessed by the host CPU where non-bottleneck operations are executed. From our implementation integrated with Fabric v1.4 LTS, we observed up to 17x speedup in block validation when compared to software-only implementation.

Blockchain: [https://github.com/Xilinx/hyperledger-fabric](https://github.com/Xilinx/hyperledger-fabric)

#### **ThunderGP: HLS-based Graph Processing on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/D8ZunBYc5xI?start=1792" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Xinyu Chen, Doctoral Student, National University of Singapore 

*ThunderGP* is proposed to bridge the gap between high-level graph processing applications and underlying CPU-FPGA platforms. With ThunderGP, developers could enjoy the performance of FPGA-accelerated graph processing by writing only a few high-level functions with no knowledge of the hardware.

ThunderGP: [https://github.com/Xtra-Computing/ThunderGP](https://github.com/Xtra-Computing/ThunderGP)

### XACC Tech Talk 2

24<sup>th</sup> June 2021

#### **VNx and EasyNet**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/P93WlrBVxoM?start=120" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Mario Ruiz, Xilinx University Program; Zhenhao He, Doctoral Student, Systems Group, ETH Zurich 

This presentation will introduce *VNx* which adds 100Gbps UDP/IP support to Vitis designs. *EasyNet* extends VNx to support 100Gbps TCP/IP from HLS. 
Both VNx and EasyNet are open-source and supported from Vitis and can be used to add high-speed networking interfaces to Alveo platforms. 

Vnx: [https://github.com/Xilinx/xup_vitis_network_example](https://github.com/Xilinx/xup_vitis_network_example)

EasyNet: [https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP](https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP)

#### **Elastic-DF: Scaling Performance of DNN Inference in FPGA Clouds through Automatic Partitioning**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/P93WlrBVxoM?start=1851" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Lucian Petrica, Xilinx Research Labs

Customized compute acceleration in the datacenter is key to the wider roll-out of applications based on deep neural network (DNN) inference.

In this presentation we discuss how to maximize the performance and scalability of FPGA-based pipeline dataflow DNN inference accelerators (DFAs) automatically on computing infrastructures consisting of multi-die, network-connected FPGAs. We present *Elastic-DF*, a novel resource partitioning tool which integrates with the [DNN compiler FINN](https://github.com/Xilinx/finn) and utilizes 100Gbps Ethernet FPGA infrastructure, to achieve low-latency model-parallel inference without host involvement. Elastic-DF was applied to popular image classifiers ResNet50 and MobileNetV1 at XACC and provides significant throughput increase with no adverse impact on latency.

### XACC Tech Talk 1

10<sup>th</sup> June 2021

#### **Coyote: Do OS abstractions make sense in FPGAs?**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/un7wck0IkGs?start=88" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dario Korolija, Doctoral Student, Systems Group, ETH Zurich

Hybrid computing systems, consisting of a CPU server coupled with a Field-Programmable Gate Array (FPGA) for application acceleration, are today a common facility in datacenters and clouds. FPGAs can deliver tremendous improvements in performance and energy efficiency for a range or workloads, but development and deployment of FPGA-based applications remains cumbersome, leading to recent work which replicates subsets of the traditional OS execution environment (virtual memory, processes, etc.) on the FPGA.

We ask a different question: to what extent do traditional OS abstractions make sense in the context of an FPGA as part of a hybrid system, particularly when taken as a complete package, as they would be in an OS? To answer this, we built and evaluated *Coyote*, an open source, portable, configurable “shell” for FPGAs which provides a full suite of OS abstractions, working with the host OS. Coyote supports secure spatial and temporal multiplexing of the FPGA between tenants, virtual memory, communication, and memory management inside a uniform execution environment. The overhead of Coyote is small and the performance benefit is significant, but more importantly it allows us to reflect on whether importing OS abstractions wholesale to FPGAs is the best way forward.

Coyote: [https://github.com/fpgasystems/Coyote](https://github.com/fpgasystems/Coyote)

#### **Data-Centric FPGA Programming with Multi-Level Design**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/un7wck0IkGs?start=1743" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Johannes de Fine Licht, Doctoral Student, Scalable Parallel Computing Laboratory, ETH Zurich

Although high-level synthesis (HLS) tools have significantly improved programmer productivity over hardware description languages, developing for FPGAs remains tedious and error prone. Programmers must learn and implement a large set of vendor-specific syntax, patterns, and tricks to optimize (or even successfully compile) their applications, while dealing with ever-changing toolflows from the FPGA vendors. We propose a new way to develop, optimize, and compile FPGA programs. The Data-Centric parallel programming (*DaCe*) framework allows applications to be defined by their dataflow and control flow through the Stateful DataFlow multiGraph (SDFG) representation, capturing the abstract program characteristics, and exposing a plethora of optimization opportunities. SDFGs are extended by multi-level library nodes, which incorporate both domain-specific and platform-specific optimizations into the design flow, enabling knowledge transfer across application domains and FPGA vendors. We show how the powerful code-generating backend of DaCe emits efficient HLS code that is structured and annotated to implement the desired architectures and achieve high performance in practice.

DaCe: [https://github.com/spcl/dace](https://github.com/spcl/dace)

---------------------------------------
<p class="copyright">Copyright&copy; 2022 Advanced Micro Devices</p>
