# Publications

This page lists the research publications which have been carried out in the context of the HACC program, or papers that may be of interest to the HACC community.

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md)

## 2022

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>Accelerating SSSP for Power-Law Graphs</td>
        <td>Yuze Chi <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://doi.org/10.1145/3490422.3502358">Paper</a></td>
        <td>The single-source shortest path (SSSP) problem is one of the most important and well-studied graph problems widely used in many application domains, such as road navigation, neural image reconstruction, and social network analysis. Although we have known various SSSP algorithms for decades, implementing one for large scale power-law graphs efficiently is still highly challenging today, because ① a work-efficient SSSP algorithm requires priority-order traversal of graph data, ② the priority queue needs to be scalable both in throughput and capacity, and ③ priority-order traversal requires extensive random memory accesses on graph data. In this paper, we present SPLAG to accelerate SSSP for powerlaw graphs on FPGAs. SPLAG uses a coarse-grained priority queue (CGPQ) to enable high-throughput priority-order graph traversal with a large frontier. To mitigate the high-volume random accesses, SPLAG employs a customized vertex cache (CVC) to reduce off-chip memory access and improve the throughput to read and update vertex data. Experimental results on various synthetic and real world datasets show up to a 4.9× speedup over state-of-the-art SSSP accelerators, a 2.6× speedup over 32-thread CPU running at 4.4 GHz, and a 0.9× speedup over an A100 GPU that has 4.1× power budget and 3.4× HBM bandwidth. Such a high performance would place SPLAG in the 14th position of the Graph 500 benchmark for data intensive applications (the highest using a single FPGA) with only a 45 W power budget. SPLAG is written in high-level synthesis C++ and is fully parameterized, which means it can be easily ported to various different FPGAs with different configurations. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>FPGA Acceleration of Pre-Alignment Filters for Short Read Mapping With HLS</td>
        <td>David Castells-Rufas <em>et al.</em></td>
        <td>David Castells-Rufas</td>
        <td><a href="https://ieeexplore.ieee.org/abstract/document/9718100">Paper</a> <a href="https://github.com/davidcastells/OpenCLPrealignmentFilters">GitHub</a></td>
        <td>Pre-alignment filters are useful for reducing the computational requirements of genomic sequence mappers. Most of them are based on estimating or computing the edit distance between sequences and their candidate locations in a reference genome using a subset of the dynamic programming table used to compute Levenshtein distance. Some of their FPGA implementations of use classic HDL toolchains, thus limiting their portability. Currently, most FPGA accelerators offered by heterogeneous cloud providers support C/C++ HLS. This work implements and optimizes several state-of-the-art pre-alignment filters using C/C++ based-HLS to expand their portability to a wide range of systems supporting the OpenCL runtime. A complete analysis of the performance and accuracy is performed. The maximum throughput obtained by an exact filter is 95.1 MPairs/s including memory transfers using 100 bp sequences, which is the highest ever reported for a comparable system and more than two times faster than previous HDL-based results. The best energy efficiency obtained from the accelerator (not considering host CPU) is 2.1 MPairs/J, more than one order of magnitude higher than other accelerator-based comparable approaches from the state of the art.</td>
    </tr>
    <tr>
        <td>Pyxis: An Open-Source Performance Dataset of Sparse Accelerators</td>
        <td>Linghao Song <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://arxiv.org/abs/2110.04280">Paper</a></td>
        <td>Customized accelerators provide gains of performance and efficiency in specific domains of applications. Sparse data structures and/or representations exist in a wide range of applications. However, it is challenging to design accelerators for sparse applications because no architecture or performance-level analytic models are able to fully capture the spectrum of the sparse data. Accelerator researchers rely on real execution to get precise feedback for their designs. In this work, we present PYXIS, a performance dataset for customized accelerators on sparse data. PYXIS collects accelerator designs and real execution performance statistics. Currently, there are 73.8 K instances in PYXIS. PYXIS is open-source, and we are constantly growing PYXIS with new accelerator designs and performance statistics. PYXIS can be a benefit to researchers in the fields of accelerator, architecture, performance, algorithm and many related topics. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>RapidStream: Parallel Physical Implementation of FPGA HLS Designs <img src="./images/best_paper_award.png" alt="Best Paper" height="160"></td>
        <td>Licheng Guo <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://doi.org/10.1145/3490422.3502361">Paper</a></td>
        <td>FPGAs require a much longer compilation cycle than conventional computing platforms like CPUs. In this paper, we shorten the overall compilation time by co-optimizing the HLS compilation (C-to-RTL) and the back-end physical implementation (RTL-to-bitstream). We propose a split compilation approach based on the pipelining flexibility at the HLS level, which allows us to partition designs for parallel placement and routing then stitch the separate partitions together. We outline a number of technical challenges and address them by breaking the conventional boundaries between different stages of the traditional FPGA tool flow and reorganizing them to achieve a fast end-to-end compilation. Our research produces RapidStream, a parallelized and physicalintegrated compilation framework that takes in an HLS dataflow program in C/C++ and generates a fully placed and routed implementation. When tested on the Xilinx U250 FPGA with a set of realistic HLS designs, RapidStream achieves a 5-7× reduction in compile time and up to 1.3× increase in frequency when compared to a commercial-off-the-shelf toolchain. In addition, we provide preliminary results using a customized open-source router to reduce the compile time up to an order of magnitude in the cases with lower performance requirements. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>ReGraph: Scaling Graph Processing on HBM-enabled FPGAs with Heterogeneous Pipelines</td>
        <td>Xinyu Chen<em>et al.</em></td>
        <td>National University of Singapore</td>
        <td><a href="https://arxiv.org/abs/2203.02676">Paper</a></td>
        <td>Proposes a resource-efficient heterogeneous pipeline architecture. This heterogeneous architecture comprises of two types of pipelines: Little pipelines to process dense partitions with good locality and Big pipelines to process sparse partitions with the extremely poor locality. Unlike traditional monolithic pipeline designs, the heterogeneous pipelines are tailored for more specific memory access patterns, and hence are more lightweight, allowing the architecture to scale up to more effectively with limited resources. In addition, an automatic method generates the most efficient pipeline combination and balances workloads. Furthermore, ReGraph is an automated open-source framework. ReGraph outperforms state-of-the-art FPGA accelerators by up to 5.9 times in terms of performance and 12 times in terms of resource efficiency.</td>
    </tr>
    <tr>
        <td>Sextans: A Streaming Accelerator for General-Purpose Sparse-Matrix Dense-Matrix Multiplication</td>
        <td>Linghao Song <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3490422.3502357">Paper</a></td>
        <td>Sparse-Matrix Dense-Matrix multiplication (SpMM) is the key operator for a wide range of applications including scientific computing, graph processing, and deep learning. Architecting accelerators for SpMM is faced with three challenges – (1) the random memory accessing and unbalanced load in processing because of random distribution of elements in sparse matrices, (2) inefficient data handling of the large matrices which can not be fit on-chip, and (3) a non-general-purpose accelerator design where one accelerator can only process a fixed-size problem. In this paper, we present Sextans, an accelerator for general purpose SpMM processing. Sextans accelerator features (1) fast random access using on-chip memory, (2) streaming access to offchip large matrices, (3) PE-aware non-zero scheduling for balanced workload with an II=1 pipeline, and (4) hardware flexibility to enable prototyping the hardware once to support SpMMs of different size as a general-purpose accelerator. We leverage high bandwidth memory (HBM) for the efficient accessing of both sparse and dense matrices. In the evaluation, we present an FPGA prototype Sextans which is executable on a Xilinx U280 HBM FPGA board and a projected prototype Sextans-P with higher bandwidth competitive to V100 and more frequency optimization. We conduct a comprehensive evaluation on 1,400 SpMMs on a wide range of sparse matrices including 50 matrices from SNAP and 150 from SuiteSparse. We compare Sextans with NVIDIA K80 and V100 GPUs. Sextans achieves a 2.50x geomean speedup over K80 GPU and Sextans-P achieves a 1.14x geomean speedup over V100 GPU (4.94x over K80). <br><b>Note</b>: Notes quoted from paper. </td>
    </tr>
    <tr>
        <td>ThunderGP: Resource-Efficient Graph ProcessingFramework on FPGAs with HLS</td>
        <td>Xinyu Chen<em>et al.</em></td>
        <td>National University of Singapore</td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3517141">Paper</a> <a href="https://github.com/Xtra-Computing/ThunderGP">GitHub</a></td>
        <td>ThunderGP, an HLS-based graph processing framework on FPGAs, with which developers could enjoy FPGA-accelerated graph processing with no prior knowledge of hardware design. ThunderGP adopts the gather-apply-scatter (GAS) model as the abstraction of various graph algorithms and realizes the model by a build-in highly parallel and memory-efficient accelerator template. ThunderGP on DRAM-based hardware platforms provides 1.9 × ∼ 5.2 × improvement on bandwidth efficiency over the state-of-the-art, while ThunderGP on HBM-based hardware platforms delivers up to 5.2 × speedup over the state-of-the-art RTL-based approach.</td>
    </tr>
</table>

## 2021

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>ACCL: FPGA-Accelerated Collectives over 100 Gbps TCP-IP</td>
        <td>Zhenhao He <em>et al.</em></td>
        <td>Xilinx Research Labs</td>
        <td><a href="https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/510849/H2RC21_Xilinx_submitted_version.pdf">Paper</a> <a href="https://github.com/Xilinx/ACCL">GitHub</a></td>
        <td>ACCL is a Vitis kernel and associated Pynq and XRT drivers which together provide MPI-like collectives for Xilinx FPGAs. ACCL is designed to enable compute kernels resident in FPGA fabric to communicate directly under host supervision but without requiring data movement between the FPGA and host. Instead, ACCL uses Vitis-compatible TCP and UDP stacks to connect FPGAs directly over Ethernet at up to 100 Gbps on Alveo cards.</td>
    </tr>
    <tr>
        <td>AutoBridge: Coupling Coarse-Grained Floorplanning and Pipelining for High-Frequency HLS Design on Multi-Die FPGAs <img src="./images/best_paper_award.png" alt="Best Paper" height="160"></td>
        <td>Licheng Guo <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3431920.3439289">Paper</a> <a href="https://github.com/Licheng-Guo/AutoBridge">GitHub</a></td>
        <td>Despite an increasing adoption of high-level synthesis (HLS) for its design productivity advantages, there remains a significant gap in the achievable frequency between an HLS design and a handcrafted RTL one. A key factor that limits the timing quality of the HLS outputs is the difficulty in accurately estimating the interconnect delay at the HLS level. This problem becomes even worse when large HLS designs are implemented on the latest multi-die FPGAs. To tackle this challenge, we propose AutoBridge, an automated framework that couples a coarse-grained floorplanning step with pipelining during HLS compilation. First, our approach provides HLS with a view on the global physical layout of the design, allowing HLS to more easily identify and pipeline the long wires, especially those crossing the die boundaries. Second, by exploiting the flexibility of HLS pipelining, the floorplanner is able to distribute the design logic across multiple dies on the FPGA device without degrading clock frequency. This prevents the placer from aggressively packing the logic on a single die which often results in local routing congestion that eventually degrades timing. Since pipelining may introduce additional latency, we further present analysis and algorithms to ensure the added latency will not compromise the overall throughput. AutoBridge can be integrated into the existing CAD toolflow for Xilinx FPGAs. In our experiments with a total of 43 design configurations, we improve the average frequency from 147 MHz to 297 MHz (a 102% improvement) with no loss of throughput and a negligible change in resource utilization. Notably, in 16 experiments we make the originally unroutable designs achieve 274 MHz on average. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>AutoSA: A Polyhedral Compiler for High-Performance Systolic Arrays on FPGA</td>
        <td>Jie Wang <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3431920.3439292">Paper</a></td>
        <td>While systolic array architectures have the potential to deliver tremendous performance, it is notoriously challenging to customize an efficient systolic array processor for a target application. Designing systolic arrays requires knowledge for both high-level characteristics of the application and low-level hardware details, thus making it a demanding and inefficient process. To relieve users from the manual iterative trial-and-error process, we present AutoSA, an end-to-end compilation framework for generating systolic arrays on FPGA. AutoSA is based on the polyhedral framework, and further incorporates a set of optimizations on different dimensions to boost performance. An efficient and comprehensive design space exploration is performed to search for high-performance designs. We have demonstrated AutoSA on a wide range of applications, on which AutoSA achieves high performance within a short amount of time. As an example, for matrix multiplication, AutoSA achieves 934 GFLOPs, 3.41 TOPs, and 6.95 TOPs in floating point, 16-bit and 8-bit integer data types on Xilinx Alveo U250. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>Distributed Recommendation Inference on FPGA Clusters</td>
        <td>Yu Zhu <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/485145">Paper</a></td>
        <td>Implementation of an efficient distributed recommendation inference on an FPGA cluster that optimizes both the memory-bound embedding layer and the computation-bound fully-connected layers. The system achieves a maximum speed up of 28.95x, while guaranteeing very low latency.</td>
    </tr>
    <tr>
        <td>EasyNet: 100 Gbps Network for HLS</td>
        <td>Zhenhao He <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/487920">Paper</a>
            <a href="https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP">GitHub</a></td>
        <td>Integration of an open-source 100 Gbps TCP/IP stack into Vitis without degrading its performance. A set of MPI-like communication primitives are provided to abstract away low level details of the networking stack.</td>
    </tr>
    <tr>
        <td>Elastic-DF: Scaling Performance of DNN Inference in FPGA Clouds through Automatic Partitioning</td>
        <td> Tobias Alonso <em>et al.</em></td>
        <td>Xilinx Research Labs</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3470567">Paper</a></td>
        <td>Elastic-DF allocates FPGA resources to DNN layers and layers to individual FPGA dies to maximize the total performance of the multi-FPGA system. In the resulting Elastic-DF mapping, the accelerator may be instantiated multiple times, and each instance may be segmented across multiple FPGAs transparently, whereby the segments communicate peer-to-peer through 100 Gbps Ethernet FPGA infrastructure, without host involvement.</td>
    </tr>
    <tr>
        <td>Extending High-Level Synthesis for Task-Parallel Programs</td>
        <td>Yuze Chi <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=9444053">Paper</a></td>
        <td>C/C++/OpenCL-based high-level synthesis (HLS) becomes more and more popular for field-programmable gate array (FPGA) accelerators in many application domains in recent years, thanks to its competitive quality of results (QoR) and short development cycles compared with the traditional register transfer level design approach. Yet, limited by the sequential C semantics, it remains challenging to adopt the same highly productive high-level programming approach in many other application domains, where coarse-grained tasks run in parallel and communicate with each other at a fine-grained level. While current HLS tools do support task-parallel programs, the productivity is greatly limited ① in the code development cycle due to the poor programmability, ② in the correctness verification cycle due to restricted software simulation, and ③ in the QoR tuning cycle due to slow code generation. Such limited productivity often defeats the purpose of HLS and hinder programmers from adopting HLS for task-parallel FPGA accelerators. In this paper, we extend the HLS C++ language and present a fully automated framework with programmer-friendly interfaces, unconstrained software simulation, and fast hierarchical code generation to overcome these limitations and demonstrate how task-parallel programs can be productively supported in HLS. Experimental results based on a wide range of real-world task parallel programs show that, on average, the lines of kernel and host code are reduced by 22% and 51%, respectively, which considerably improves the programmability. The correctness verification and the iterative QoR tuning cycles are both greatly shortened by 3.2× and 6.8×, respectively. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>FleetRec: Large-Scale Recommendation Inference on Hybrid GPU-FPGA Clusters</td>
        <td>Wenqi Jiang <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/485153">Paper</a>
            <a href="https://github.com/fpgasystems/GPU-FPGA-Recommendation-System">GitHub</a></td>
        <td>A high-performance and scalable recommendation inference system within tight latency constraints. FleetRec takes advantage of both GPUs and FPGAs by disaggregating computation and memory to different types of accelerators and bridging their connections by high-speed network, FleetRec gains the best of both worlds, and can naturally scale out by adding nodes to the cluster</td>
    </tr>
    <tr>
        <td>Graviton: A Reconfigurable Memory-Compute Fabric for Data Intensive Applications</td>
        <td>Ashutosh Dhar <em>et al.</em></td>
        <td>UIUC</td>
        <td><a href="https://link.springer.com/chapter/10.1007/978-3-030-79025-7_18">Book Chapter</a></td>
        <td>The rigid organization and distribution of computational and memory resources often limits how well accelerators can cope with changing algorithms and increasing dataset sizes and limits how efficiently they use their computational and memory resources. In this work, we leverage a novel computing paradigm and propose a new memory-based reconfigurable fabric, Graviton. We demonstrate the ability to dynamically trade memory for compute and vice versa, and can tune the architecture of the underlying hardware to suit the memory and compute requirements of the application. On a die-to-die basis, Graviton provides up to 47X more on-chip memory capacity over an Alveo U250 SLR, with just an additional 1.7% area on a die-to-die basis than modern FPGAs, and is 28.7X faster, on average, on a range of compute and data intensive tasks</td>
    </tr>
    <tr>
        <td>HBM Connect: High-Performance HLS Interconnect for FPGA HBM</td>
        <td>Young-kyu Choi <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3431920.3439301">Paper</a></td>
        <td>With the recent release of High Bandwidth Memory (HBM) based FPGA boards, developers can now exploit unprecedented external memory bandwidth. This allows more memory-bounded applications to benefit from FPGA acceleration. However, fully utilizing the available bandwidth may not be an easy task. If an application requires multiple processing elements to access multiple HBM channels, we observed a significant drop in the effective bandwidth. The existing high-level synthesis (HLS) programming environment had limitation in producing an efficient communication architecture. In order to solve this problem, we propose HBM Connect, a high-performance customized interconnect for FPGA HBM board. Novel HLS-based optimization techniques are introduced to increase the throughput of AXI bus masters and switching elements. We also present a high-performance customized crossbar that may replace the built-in crossbar. The effectiveness of HBM Connect is demonstrated using Xilinx’s Alveo U280 HBM board. Based on bucket sort and merge sort case studies, we explore several design spaces  and find the design point with the best resource-performance tradeoff. The result shows that HBM Connect improves the resource performance metrics by 6.5X–211X. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>Large Graph Convolutional Network Training with GPU-Oriented Data Communication Architecture</td>
        <td>Seung Won Min <em>et al.</em></td>
        <td>UIUC</td>
        <td><a href="https://dl.acm.org/doi/10.14778/3476249.3476264">Paper</a></td>
        <td>Graph Convolutional Networks (GCNs) are increasingly adopted in large-scale graph-based recommender systems. Training GCN requires the minibatch generator traversing graphs and sampling the sparsely located neighboring nodes to obtain their features. Since real-world graphs often exceed the capacity of GPU memory, current GCN training systems keep the feature table in host memory and rely on the CPU to collect sparse features before sending them to the GPUs. This approach, however, puts tremendous pressure on host memory bandwidth and the CPU. This is because the CPU needs to (1) read sparse features from memory, (2) write features into memory as a dense format, and (3) transfer the features from memory to the GPUs</td>
    </tr>
    <tr>
        <td>MicroRec: Efficient Recommendation Inference by Hardware and Data Structure Solutions</td>
        <td>Wenqi Jiang <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/470540">Paper</a></td>
        <td>High-performance inference engine for recommendation systems. MicroRec accelerates recommendation inference by (1) redesigning the data structures to reduce the number of lookups and (2) taking advantage of HBM in FPGA accelerators to tackle the latency by enabling parallel lookups.</td>
    </tr>
    <tr>
        <td>Optimized Implementation of the HPCG Benchmark on Reconfigurable Hardware</td>
        <td>Alberto Zeni <em>et al.</em></td>
        <td>Xilinx Inc.</td>
        <td><a href="https://link.springer.com/chapter/10.1007/978-3-030-85665-6_38">Paper</a></td>
        <td>The HPCG benchmark represents a modern complement to the HPL benchmark in the performance evaluation of HPC systems. This paper presents the details of the first FPGA-based implementation of HPCG that takes advantage customized compute architectures. The results show that the high-performance multi-FPGA implementation, using 1 and 4 Xilinx Alveo U280 achieves up to 108.3 GFlops and 346.5 GFlops respectively. Comparable performance with respect to modern GPUs are also demonstrated.</td>
    </tr>
    <tr>
        <td>Skew-oblivious Data Routing for Data Intensive Applications on FPGAs with HLS</td>
        <td>Xinyu Chen <em>et al.</em></td>
        <td>UIUC</td>
        <td><a href="https://experts.illinois.edu/en/publications/skew-oblivious-data-routing-for-data-intensive-applications-on-fp">Paper</a></td>
        <td>FPGAs have become emerging computing infrastructures for accelerating applications in datacenters. Meanwhile, high-level synthesis (HLS) tools have been proposed to ease the programming of FPGAs. Even with HLS, irregular data-intensive applications require explicit optimizations, among which multiple processing elements (PEs) with each owning a private BRAM-based buffer are usually adopted to process multiple data per cycle. Data routing, which dynamically dispatches multiple data to designated PEs, avoids data replication in buffers compared to statically assigning data to PEs, hence saving BRAM usage. However, the workload imbalance among PEs vastly diminishes performance when processing skew datasets</td>
    </tr>
    <tr>
        <td>SKT: A One-Pass Multi-Sketch Data Analytics Accelerator</td>
        <td>Monica Chiosa <em>et al.</em></td>
        <td>ETH Zurich/Accemic Technologies</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/505690">Paper</a>
            <a href="https://github.com/fpgasystems/SKT">GitHub</a></td>
        <td>SKT is an FPGA-based accelerator that can compute several sketches along with basic statistics (average, max, min, etc.) in a single pass over the data streams. SKT has been designed to characterize a data set by calculating its cardinality, its second frequency moment, and its frequency distribution. The design processes data streams coming either from PCIe or TCP/IP, and it is built to fit emerging cloud service architectures </td>
    </tr>
    <tr>
        <td>TwinDNN: A Tale of Two Deep Neural Networks</td>
        <td>Hyunmin Jeong <em>et al.</em></td>
        <td>UIUC</td>
        <td><a href="https://experts.illinois.edu/en/publications/twindnn-a-tale-of-two-deep-neural-networks">Paper</a></td>
        <td>Machine learning is one of the most popular fields in the current era. It is used in various areas, such as speech recognition, face recognition, medical diagnosis, etc. However, the problem is that the neural networks for machine learning applications are becoming too large and slow as they get more complicated and powerful. This problem gets especially serious when neural networks are used for edge devices with a small chip. As a result, researchers have proposed two major solutions to solve this problem</td>
    </tr>
    <tr>
        <td>WinoCNN: Kernel Sharing Winograd Systolic Array for Efficient Convolutional Neural Network Acceleration on FPGAs</td>
        <td>Xinheng Liu <em>et al.</em></td>
        <td>UIUC</td>
        <td><a href="https://experts.illinois.edu/en/publications/winocnn-kernel-sharing-winograd-systolic-array-for-efficient-conv">Paper</a></td>
        <td>The combination of Winograd's algorithm and systolic array architecture has demonstrated the capability of improving DSP efficiency in accelerating convolutional neural networks (CNNs) on FPGA platforms. However, handling arbitrary convolution kernel sizes in FPGA-based Winograd processing elements and supporting efficient data access remain under explored. In this work, we are the first to propose an optimized Winograd processing element (WinoPE), which can naturally support multiple convolution kernel sizes with the same amount of computing resources and maintains high runtime DSP efficiency. Using the proposed WinoPE, we construct a highly efficient systolic array accelerator, termed WinoCNN. We also propose a dedicated memory subsystem to optimize the data access. Based on the accelerator architecture, we build accurate resource and performance modeling to explore optimal accelerator configurations under different resource constraints. We implement our proposed accelerator on multiple FPGAs, which outperforms the state-of-the-art designs in terms of both throughput and DSP efficiency</td>
    </tr>
</table>

## 2020

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="480">Notes</th>
    </tr>
    <tr>
        <td>Do OS abstractions make sense on FPGAs?</td>
        <td>Dario Korolija <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.usenix.org/conference/osdi20/presentation/roscoe">Paper</a></td>
        <td>To what extent do traditional OS abstractions make sense in the context of an FPGA as part of a hybrid system? This paper introduces Coyote which supports secure spatial and temporal multiplexing of the FPGA between tenants, virtual memory, communication, and memory management inside a uniform execution environment.</td>
    </tr>
    <tr>
        <td>EMOGI: efficient memory-access for out-of-memory graph-traversal in GPUs</td>
        <td>Seung Won Min <em>et al.</em></td>
        <td>University of Illinois at Urbana-Champaign</td>
        <td><a href="https://dl.acm.org/doi/10.14778/3425879.3425883">Paper </a></td>
        <td>Sparse-matrix computation</td>
    </tr>
    <tr>
        <td>FReaC Cache: Folded-logic Reconfigurable Computing in the Last Level Cache</td>
        <td>Ashutosh Dhar <em>et al.</em></td>
        <td>University of Illinois at Urbana-Champaign</td>
        <td><a href="https://ieeexplore.ieee.org/abstract/document/9251953">Paper</a></td>
        <td>Energy efficient computation</td>
    </tr>
    <tr>
        <td>Making Search Engines Faster by Lowering the Cost of Querying Business Rules Through FPGAs</td>
        <td>Fabio Maschi <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://doi.org/10.1145/3318464.3386133">Paper</a></td>
        <td>Explore how to use hardware acceleration to (i) improve the performance of the MCT module (lower latency, higher throughput); and (ii) reduce the amount of computing resources needed</td>
    </tr>
    <tr>
        <td>Portable Linear Algebra on FPGA using Data-Centric Parallel Programming</td>
        <td>Manuel Burger <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://github.com/manuelburger/daceBLAS_demo">GitHub</a></td>
        <td>2020 XOHW Winner PhD</td>
    </tr>
    <tr>
        <td>Specializing the network for scatter-gather workloads</td>
        <td>Catalina Alvarez <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3419111.3421301">Paper</a></td>
        <td>Explore hardware-offload of the scatter-gather primitive. This approach not only virtually eliminates CPU usage, but with suitable scheduling of responses, it also speeds up scatter by allowing parallel queries</td>
    </tr>
    <tr>
        <td>Weighing up the new kid on the block: Impressions of using Vitis for HPC software development</td>
        <td>Nick Brown <em>et al.</em></td>
        <td>The University of Edinburgh</td>
        <td><a href="https://arxiv.org/abs/2010.00289">Paper</a></td>
        <td>Vitis case study using Himeno benchmark as a vehicle for exploring the Vitis platform for building, executing and optimizing HPC codes</td>
    </tr>
</table>

## 2019

<table>
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="480">Notes</th>
    </tr>
    <tr>
        <td>AcMC²: Accelerating Markov Chain Monte Carlo Algorithms for Probabilistic Models</td>
        <td>Subho S. Banerjee <em>et al.</em></td>
        <td>University of Illinois at Urbana-Champaign</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3297858.3304019">Paper</a></td>
        <td>Compiler development transforming probabilistic models into optimized hardware accelerators</td>
    </tr>
    <tr>
        <td>Cloud-DNN: An Open Framework for Mapping DNN Models to Cloud FPGAs</td>
        <td>Yao Chen <em>et al.</em></td>
        <td>National University of Singapore</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3289602.3293915">Paper </a></td>
        <td>Open-source automated tool chain called Cloud-DNN. Our tool chain takes trained CNN models specified in Caffe as input, performs a set of transformations, and maps the model to a cloud-based FPGA. Cloud-DNN can significantly improve the overall design productivity of CNNs on FPGAs while satisfying the emergent computational requirements.</td>
    </tr>
    <tr>
        <td>Flexible Communication Avoiding Matrix Multiplication on FPGA with HLS</td>
        <td>Johannes de Fine Licht <em>et al.</em></td>
        <td>ETH Zurich </td>
        <td><a href="https://arxiv.org/abs/1912.06526">Paper</a></td>
        <td>A flexible, fully HLS-based, high-performance matrix multiplication accelerator, capable of efficiently utilizing all available resources on the target device, including for multi-SLR FPGAs.</td>
    </tr>
    <tr>
        <td>High-Performance Distributed Memory Programming on Reconfigurable Hardware</td>
        <td>Tiziano De Matteis <em>et al.</em></td>
        <td>ETH Zurich </td>
        <td><a href="https://arxiv.org/abs/1909.03231">Paper</a></td>
        <td>SMI is an API that unifies the flexibility and single-program, multiple-data approach of MPI with the streaming programming model of spatial architectures.</td>
    </tr>
    <tr>
        <td>Inductive-bias-driven Reinforcement Learning for Efficient Schedules in Heterogeneous Clusters</td>
        <td>Subho S. Banerjee <em>et al.</em></td>
        <td>University of Illinois at Urbana-Champaign</td>
        <td><a href="https://arxiv.org/abs/1909.02119">Paper</a></td>
        <td>System schedulers</td>
    </tr>
    <tr>
        <td><strong>hlslib:</strong> Software Engineering for Hardware Design</td>
        <td>Johannes de Fine Licht <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://arxiv.org/abs/1910.04436">Paper</a></td>
        <td>A collection of extensions for Vitis to improve developer quality of life, including CMake integration, better vectorization support, support for simulating dataflow kernels with feedback dependencies.</td>
    </tr>
    <tr>
        <td>Stateful Dataflow Multigraphs: A Data-Centric Model for Performance Portability on Heterogeneous Architectures</td>
        <td>Tal Ben-Nun <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://arxiv.org/abs/1902.10345">Paper</a></td>
        <td>Enables high-level programming of FPGAs from Python using the dataflow-based SDFG representation, allowing productive optimization of programs via provided graph transformations without modifying the input program, and code generating highly efficient FPGA kernels.</td>
    </tr>
</table>

## 2018

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>FINN-R: An End-to-End Deep-Learning Framework for Fast Exploration of Quantized Neural Networks</td>
        <td>Michaela Blott <em>et al.</em></td>
        <td>Xilinx Inc.</td>
        <td><a href="https://arxiv.org/abs/1809.04570">FINN-R Paper</a></td>
        <td>Framework for Quantized Neural Networks on reconfigurable hardware</td>
    </tr>
    <tr>
        <td>Transformations of High-Level Synthesis Codes for High-Performance Computing</td>
        <td>Johannes de Fine Licht <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://arxiv.org/abs/1805.08288">Paper</a></td>
        <td>A survey of important source-to-source optimization techniques for high-throughput HLS codes to target pipelining, parallelism, and memory bandwidth utilization.</td>
    </tr>
</table>

## 2017

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>Architectural optimizations for high performance and energy efficient Smith-Waterman implementation on FPGAs using OpenCL</td>
        <td>Lorenzo Di Tucci <em>et al.</em></td>
        <td>Xilinx Inc. and Politecnico di Milano</td>
        <td><a href="https://arxiv.org/abs/1809.04570">Paper</a></td>
        <td>Smith-Waterman: A key bio-informatics algorithm</td>
    </tr>
</table>

## 2016

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="470">Notes</th>
    </tr>
    <tr>
        <td>FINN: A Framework for Fast, Scalable Binarized Neural Network Inference</td>
        <td>Yaman Umuroglu <em>et al.</em></td>
        <td>Xilinx Inc.</td>
        <td><a href="https://arxiv.org/abs/1612.07119">FINN Paper</a></td>
        <td>Framework for Binarized Neural networks on reconfigurable hardware</td>
    </tr>
</table>

---------------------------------------
<p class="copyright">Copyright&copy; 2022 Advanced Micro Devices</p>
