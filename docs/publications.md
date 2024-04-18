# Publications

This page lists the research publications which have been carried out in the context of the HACC program, or papers that may be of interest to the HACC community.

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md)

## 2024

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>SSR: Spatial Sequential Hybrid Architecture for Latency Throughput Tradeoff in Transformer Acceleration (FPGA'24)</td>
        <td>Jinming Zhuang <em>et al.</em></td>
        <td>University of Pittsburgh, University of Maryland, University of Notre Dame</td>
        <td><a href="https://arxiv.org/pdf/2401.10417.pdf">Paper</a> <a href="https://github.com/arc-research-lab/SSR">GitHub</a></td>
        <td>
            With the increase in the computation intensity of the chip, the mismatch between computation layer shapes and the available computation resource significantly limits the utilization of the chip. Driven by this observation, prior works discuss spatial accelerators or dataflow architecture to maximize the throughput. However, using spatial accelerators could potentially increase the execution latency. In this work, we first systematically investigate two execution models: (1) sequentially (temporally) launch one monolithic accelerator, and (2) spatially launch multiple accelerators. From the observations, we find that there is a latency throughput tradeoff between these two execution models, and combining these two strategies together can give us a more efficient latency throughput Pareto front. To achieve this, we propose spatial sequential architecture (SSR) and SSR design automation framework to explore both strategies together when deploying deep learning inference. We use the 7nm AMD Versal ACAP VCK190 board to implement SSR accelerators for four end-to-end transformer-based deep learning models. SSR achieves average throughput gains of 2.53x, 35.71x, and 14.20x under different batch sizes compared to the 8nm Nvidia GPU A10G, 16nm AMD FPGAs ZCU102, and U250. The average energy efficiency gains are 8.51x, 6.75x, and 21.22x, respectively. Compared with the sequential-only solution and spatial-only solution on VCK190, our spatial-sequential-hybrid solutions achieve higher throughput under the same latency requirement and lower latency under the same throughput requirement. We also use SSR analytical models to demonstrate how to use SSR to optimize solutions on other computing platforms, e.g., 14nm Intel Stratix 10 NX.
        </td>
    </tr>
</table>

## 2023

<table width="100%">
    <tr>
        <th width="200">Name</th>
        <th width="120">Author(s)</th>
        <th width="120">Institution</th>
        <th width="120">Link</th>
        <th width="500">Notes</th>
    </tr>
    <tr>
        <td>AMNES: Accelerating the computation of data correlation using FPGAs</td>
        <td>Monica Chiosa <em>et al.</em></td>
        <td>ETH Zurich and AMD</td>
        <td><a href="https://dl.acm.org/doi/10.14778/3625054.3625056">Paper</a> <a href="https://github.com/fpgasystems/amnes">GitHub</a></td>
        <td>
            A widely used approach to characterize input data in both databases and ML is computing the correlation between attributes. The operation is supported by all major database engines and ML platforms. However, it is an expensive operation as the number of attributes involved grows. To address the issue, in this paper we introduce AMNES, a stream analytics system offloading the correlation operator into an FPGA-based network interface card. AMNES processes data at network line rate and the design can be used in combination with smart storage or SmartNICs to implement near data or in-network data processing. AMNES design goes beyond matrix multiplication and offers a customized solution for correlation computation bypassing the CPU. Our experiments show that AMNES can sustain streams arriving at 100 Gbps over an RDMA network, while requiring only ten milliseconds to compute the correlation coefficients among 64 streams, an order of magnitude better than competing CPU or GPU designs.
        </td>
    </tr>
    <tr>
        <td>Callipepla: Stream Centric Instruction Set and Mixed Precision for Accelerating Conjugate Gradient Solver</td>
        <td>Linghao Song <em>et al.</em></td>
        <td>UCLA and Ansys</td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3543622.3573182">Paper</a> <a href="https://github.com/UCLA-VAST/Callipepla">GitHub</a></td>
        <td>
            The continued growth in the processing power of FPGAs coupled with high bandwidth memories (HBM), makes systems like the Xilinx U280 credible platforms for linear solvers which often dominate the run time of scientific and engineering applications. In this paper, we present Callipepla, an accelerator for a preconditioned conjugate gradient linear solver (CG). FPGA acceleration of CG faces three challenges: (1) how to support an arbitrary problem and terminate acceleration processing on the fly, (2) how to coordinate long-vector data flow among processing modules, and (3) how to save off-chip memory bandwidth and maintain double (FP64) precision accuracy. To tackle the three challenges, we present (1) a stream-centric instruction set for efficient streaming processing and control, (2) vector streaming reuse (VSR) and decentralized vector flow scheduling to coordinate vector data flow among modules and further reduce off-chip memory access latency with a double memory channel design, and (3) a mixed precision scheme to save bandwidth yet still achieve effective double precision quality solutions. To the best of our knowledge, this is the first work to introduce the concept of VSR for data reusing between on-chip modules to reduce unnecessary off-chip accesses and enable modules working in parallel for FPGA accelerators. We prototype the accelerator on a Xilinx U280 HBM FPGA. Our evaluation shows that compared to the Xilinx HPC product, the XcgSolver, Callipepla achieves a speedup of 3.94x, 3.36x higher throughput, and 2.94x better energy efficiency. Compared to an NVIDIA A100 GPU which has 4x the memory bandwidth of Callipepla, we still achieve 77% of its throughput with 3.34x higher energy efficiency. The code is available at https://github.com/UCLA-VAST/Callipepla.
        </td>
    </tr>
    <tr>
        <td>CHARM: Composing Heterogeneous AcceleRators for Matrix Multiply on Versal ACAP Architecture</td>
        <td>Jinming Zhuang <em>et al.</em></td>
        <td>University of Pittsburgh, UCLA, UIUC, AMD</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3543622.3573210">Paper</a> <a href="https://github.com/arc-research-lab/CHARM">GitHub</a></td>
        <td>
            Dense matrix multiply (MM) serves as one of the most heavily used kernels in deep learning applications. To cope with the high computation demands of these applications, heterogeneous architectures featuring both FPGA and dedicated ASIC accelerators have emerged as promising platforms. For example, the AMD/Xilinx Versal ACAP architecture combines general-purpose CPU cores and programmable logic (PL) with AI Engine processors (AIE) optimized for AI/ML. An array of 400 AI Engine processors executing at 1 GHz can theoretically provide up to 6.4 TFLOPs performance for 32-bit floating-point (fp32) data. However, machine learning models often contain both large and small MM operations. While large MM operations can be parallelized efficiently across many cores, small MM operations typically cannot. In our investigation, we observe that executing some small MM layers from the BERT natural language processing model on a large, monolithic MM accelerator in Versal ACAP achieved less than 5% of the theoretical peak performance. Therefore, one key question arises: How can we design accelerators to fully use the abundant computation resources under limited communication bandwidth for end-to-end applications with multiple MM layers of diverse sizes? We identify the biggest system throughput bottleneck resulting from the mismatch of massive computation resources of one monolithic accelerator and the various MM layers of small sizes in the application. To resolve this problem, we propose the CHARM framework to compose multiple diverse MM accelerator architectures working concurrently towards different layers within one application. CHARM includes analytical models which guide design space exploration to determine accelerator partitions and layer scheduling. To facilitate the system designs, CHARM automatically generates code, enabling thorough onboard design verification. We deploy the CHARM framework for four different deep learning applications, including BERT, ViT, NCF, MLP, on the AMD/Xilinx Versal ACAP VCK190 evaluation board. Our experiments show that we achieve 1.46 TFLOPs, 1.61 TFLOPs, 1.74 TFLOPs, and 2.94 TFLOPs inference throughput for BERT, ViT, NCF, MLP, respectively, which obtain 5.40x, 32.51x, 1.00x and 1.00x throughput gains compared to one monolithic accelerator.
        </td>
    </tr>
    <tr>
        <td>Democratizing Domain-Specific Computing</td>
        <td>Yuze Chi<em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://doi.org/10.1145/3524108">Paper</a></td>
        <td>
            Creating a programming environment and compilation flow that empowers programmers to create their own DSAs efficiently and affordably on FPGAs.
        </td>
    </tr>
    <tr>
        <td>Distributed large-scale graph processing on FPGAs</td>
        <td>Sahebi <em>et al.</em></td>
        <td>University of Siena, University of Florence, Imperial College London</td>
        <td><a href="https://doi.org/10.1186/s40537-023-00756-x">Paper</a> <a href="https://github.com/AminSahebi/distributed-graph-fpga">GitHub</a></td>
        <td>
            This work proposes an FPGA processing engine that overlaps, hides and customises all data transfers so that the FPGA accelerator is fully utilised. This engine is integrated into a framework for using FPGA clusters and is able to use an offline partitioning method to facilitate the distribution of large-scale graphs. The proposed framework uses Hadoop at a higher level to map a graph to the underlying hardware platform. The higher layer of computation is responsible for gathering the blocks of data that have been pre-processed and stored on the host’s file system and distribute to a lower layer of computation made of FPGAs. We show how graph partitioning combined with an FPGA architecture will lead to high performance, even when the graph has Millions of vertices and Billions of edges. In the case of the PageRank algorithm, widely used for ranking the importance of nodes in a graph, compared to state-of-the-art CPU and GPU solutions, our implementation is the fastest, achieving a speedup of 13 compared to 8 and 3 respectively. Moreover, in the case of the large-scale graphs, the GPU solution fails due to memory limitations while the CPU solution achieves a speedup of 12 compared to the 26x achieved by our FPGA solution. Other state-of-the-art FPGA solutions are 28 times slower than our proposed solution. When the size of a graph limits the performance of a single FPGA device, our performance model shows that using multi-FPGAs in a distributed system can further improve the performance by about 12x. This highlights our implementation efficiency for large datasets not fitting in the on-chip memory of a hardware device.
        </td>
    </tr>
    <tr>
        <td>Fortran High-Level Synthesis: Reducing the barriers to accelerating HPC codes on FPGAs</td>
        <td>Gabriel Rodriguez-Canal <em>et al.</em></td>
        <td><a href="https://arxiv.org/pdf/2308.13274.pdf">Paper</a> <a href="https://gitlab.com/cerl/fortran-hls">GitLab</a></td>
        <td>The University of Edinburgh</td>
        <td>
            In recent years the use of FPGAs to accelerate scientific applications has grown, with numerous applications demonstrating the benefit of FPGAs for high performance workloads. However, whilst High Level Synthesis (HLS) has significantly lowered the barrier to entry in programming FPGAs by enabling programmers to use C++, a major challenge is that most often these codes are not originally written in C++. Instead, Fortran is the lingua franca of scientific computing and-so it requires a complex and time consuming initial step to convert into C++ even before considering the FPGA. In this paper we describe work enabling Fortran for AMD Xilinx FPGAs by connecting the LLVM Flang front end to AMD Xilinx's LLVM back end. This enables programmers to use Fortran as a first-class language for programming FPGAs, and as we demonstrate enjoy all the tuning and optimisation opportunities that HLS C++ provides. Furthermore, we demonstrate that certain language features of Fortran make it especially beneficial for programming FPGAs compared to C++. The result of this work is a lowering of the barrier to entry in using FPGAs for scientific computing, enabling programmers to leverage their existing codebase and language of choice on the FPGA directly.
        </td>
    </tr>
    <tr>
        <td>High Performance, Low Power Matrix Multiply Design on ACAP: from Architecture, Design Challenges and DSE Perspectives</td>
        <td>Jinming Zhuang <em>et al.</em></td>
        <td>University of Pittsburgh</td>
        <td><a href="https://doi.org/10.1109/DAC56929.2023.10247981">Paper</a> <a href="https://github.com/arc-research-lab/CHARM">GitHub</a></td>
        <td>
            As the increasing complexity of Neural Network(NN) models leads to high demands for computation, AMD introduces a heterogeneous programmable system-on-chip (SoC), i.e., Versal ACAP architectures featured with programmable logic(PL), CPUs, and dedicated AI engines (AIE) ASICs which has a theoretical throughput up to 6.4 TFLOPs for FP32, 25.6 TOPs for INT16 and 102.4 TOPs for INT8. However, the higher level of complexity makes it non-trivial to achieve the theoretical performance even for well-studied applications like matrix-matrix multiply. In this paper, we provide AutoMM, an automatic white-box framework that can systematically generate the design for MM accelerators on Versal which achieves 3.7 TFLOPs, 7.5 TOPs, and 28.2 TOPs for FP32, INT16, and INT8 data type respectively. Our designs are tested on board and achieve gains of 7.20x (FP32), 3.26x (INT16), 6.23x (INT8) energy efficiency than AMD U250, 2.32x (FP32) than Nvidia Jetson TX2, 1.06x (FP32), 1.70x (INT8) than Nvidia A100.
        </td>
    </tr>
    <tr>
        <td>Multi-FPGA Designs and Scaling of HPC Challenge Benchmarks via MPI and Circuit-Switched Inter-FPGA Networks</td>
        <td>Marius Meyer <em>et al.</em></td>
        <td>Paderborn University</td>
        <td><a href="https://doi.org/10.1145/3576200">Paper</a> <a href="https://github.com/pc2/HPCC_FPGA">GitHub</a></td>
        <td>
            Extension of the HPCC benchmark suite for FPGAs with multi-FPGA benchmarks and support of inter-FPGA communication.
        </td>
    </tr>
    <tr>
        <td>Optimistic Data Parallelism for FPGA-Accelerated Sketching</td>
        <td>Martin Kiefer <em>et al.</em></td>
        <td>TU Berlin, DFKI, ITU Copenhagen</td>
        <td><a href="https://www.vldb.org/pvldb/vol16/p1113-kiefer.pdf">Paper</a> <a href="https://github.com/martinkiefer/optimistic-sketching">GitHub</a></td>
        <td>
            Sketches are a popular approximation technique for large datasets and high-velocity data streams. While custom FPGA-based hardware has shown admirable throughput at sketching, the state-of-the-art exploits data parallelism by fully replicating resources and constructing independent summaries for every parallel input value. We consider this approach pessimistic, as it guarantees constant processing rates by provisioning resources for the worst case. We propose a novel optimistic sketching architecture for FPGAs that partitions a single sketch into multiple independent banks shared among all input values, thus significantly reducing resource consumption. However, skewed input data distributions can result in conflicting accesses to banks and impair the processing rate. To mitigate the effect of skew, we add mergers that exploit temporal locality by combining recent updates.Our evaluation shows that an optimistic architecture is feasible and reduces the utilization of critical FPGA resources proportionally to the number of parallel input values. We further show that FPGA accelerators provide up to 2.6𝑥 higher throughput than a recent CPU and GPU, while larger sketch sizes enabled by optimistic architectures improve accuracy by up to an order of magnitude in a realistic sketching application.
        </td>
    </tr>
</table>

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
        <td>Enzian: An Open, General, CPU/FPGA Platform for Systems Software Research</td>
        <td>David Cock <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3503222.3507742">Paper</a></td>
        <td>Hybrid computing platforms, comprising CPU cores and FPGA logic, are increasingly used for accelerating data-intensive workloads in cloud deployments, and are a growing topic of interest in systems research. However, from a research perspective, existing hardware platforms are limited: they are often optimized for concrete, narrow use-cases and, therefore lack the flexibility needed to explore other applications and configurations. We show that a research group can design and build a more general, open, and affordable hardware platform for hybrid systems research. The platform, Enzian, is capable of duplicating the functionality of existing CPU/FPGA systems with comparable performance but in an open, flexible system. It couples a large FPGA with a server-class CPU in an asymmetric cache-coherent NUMA system. Enzian also enables research not possible with existing hybrid platforms, through explicit access to coherence messages, extensive thermal and power instrumentation, and an open, programmable baseboard management processor. Enzian is already being used in multiple projects, is open source (both hardware and software), and available for remote use. We present the design principles of Enzian, the challenges in building it, and evaluate it with a range of existing research use-cases alongside other, more specialized platforms, as well as demonstrating research not possible on existing platforms.</td>
    </tr>
    <tr>
        <td>Farview: Disaggregated Memory with Operator Off-loading for Database Engines</td>
        <td>Dario Korolija <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.cidrdb.org/cidr2022/papers/p11-korolija.pdf">Paper</a></td>
        <td>Cloud deployments disaggregate storage from compute, providing more flexibility to both the storage and compute layers. In this paper, we explore disaggregation by taking it one step further and applying it to memory (DRAM). Disaggregated memory uses network attached DRAM as a way to decouple memory from CPU. In the context of databases, such a design offers significant advantages in terms of making a larger memory capacity available as a central pool to a collection of smaller processing nodes. To explore these possibilities, we have implemented Farview, a disaggregated memory solution for databases, operating as a remote buffer cache with operator offloading capabilities. Farview is implemented as an FPGA-based smart NIC making DRAM available as a disaggregated, network attached memory pool capable of performing data processing at line rate over data streams to/from disaggregated memory. Farview supports query offloading using operators such as selection, projection, aggregation, regular expression matching and encryption. In this paper we focus on analytical queries and demonstrate the viability of the idea through an extensive experimental evaluation of Farview under different workloads. Farview is competitive with a local buffer cache solution for all the workloads and outperforms it in a number of cases, proving that a smart disaggregated memory can be a viable alternative for databases deployed in cloud environments.</td>
    </tr>
    <tr>
        <td>FlexCNN: An End-to-End Framework for Composing CNN Accelerators on FPGA</td>
        <td>Suhail Basalama<em>et al.</em></td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3570928">Paper</a> <a href="https://gitlab.com/cerl/fortran-hls">GitLab</a></td>
        <td>UCLA</td>
        <td>
            With reduced data reuse and parallelism, recent convolutional neural networks (CNNs) create new challenges for FPGA acceleration. Systolic arrays (SAs) are efficient, scalable architectures for convolutional layers, but without proper optimizations, their efficiency drops dramatically for reasons: (1) the different dimensions within same-type layers, (2) the different convolution layers especially transposed and dilated convolutions, and (3) CNN’s complex dataflow graph. Furthermore, significant overheads arise when integrating FPGAs into machine learning frameworks. Therefore, we present a flexible, composable architecture called FlexCNN, which delivers high computation efficiency by employing dynamic tiling, layer fusion, and data layout optimizations. Additionally, we implement a novel versatile SA to process normal, transposed, and dilated convolutions efficiently. FlexCNN also uses a fully pipelined software-hardware integration that alleviates the software overheads. Moreover, with an automated compilation flow, FlexCNN takes a CNN in the ONNX1 representation, performs a design space exploration, and generates an FPGA accelerator. The framework is tested using three complex CNNs: OpenPose, U-Net, and E-Net. The architecture optimizations achieve 2.3× performance improvement. Compared to a standard SA, the versatile SA achieves close-to-ideal speedups, with up to 5.98× and 13.42× for transposed and dilated convolutions, with a 6% average area overhead. The pipelined integration leads to a 5× speedup for OpenPose.
        </td>
    </tr>
    <tr>
        <td>FPGA Acceleration of Pre-Alignment Filters for Short Read Mapping With HLS</td>
        <td>David Castells-Rufas <em>et al.</em></td>
        <td>David Castells-Rufas</td>
        <td><a href="https://ieeexplore.ieee.org/abstract/document/9718100">Paper</a></td>
        <td>Pre-alignment filters are useful for reducing the computational requirements of genomic sequence mappers. Most of them are based on estimating or computing the edit distance between sequences and their candidate locations in a reference genome using a subset of the dynamic programming table used to compute Levenshtein distance. Some of their FPGA implementations of use classic HDL toolchains, thus limiting their portability. Currently, most FPGA accelerators offered by heterogeneous cloud providers support C/C++ HLS. This work implements and optimizes several state-of-the-art pre-alignment filters using C/C++ based-HLS to expand their portability to a wide range of systems supporting the OpenCL runtime. A complete analysis of the performance and accuracy is performed. The maximum throughput obtained by an exact filter is 95.1 MPairs/s including memory transfers using 100 bp sequences, which is the highest ever reported for a comparable system and more than two times faster than previous HDL-based results. The best energy efficiency obtained from the accelerator (not considering host CPU) is 2.1 MPairs/J, more than one order of magnitude higher than other accelerator-based comparable approaches from the state of the art.</td>
    </tr>
    <tr>
        <td>FPT: a Fixed-Point Accelerator for Torus Fully Homomorphic Encryption</td>
        <td>Van Beirendonck <em>et al.</em></td>
        <td>COSIC KU LEUVEN</td>
        <td><a href="https://eprint.iacr.org/2022/1635">Paper</a></td>
        <td>
            Fully Homomorphic Encryption is a technique that allows computation on encrypted data. It has the potential to drastically change privacy considerations in the cloud, but high computational and memory overheads are preventing its broad adoption. TFHE is a promising Torus-based FHE scheme that heavily relies on bootstrapping, the noise-removal tool that must be invoked after every encrypted gate computation. We present FPT, a Fixed-Point FPGA accelerator for TFHE bootstrapping. FPT is the first hardware accelerator to heavily exploit the inherent noise present in FHE calculations. Instead of double or single-precision floating-point arithmetic, it implements TFHE bootstrapping entirely with approximate fixed-point arithmetic. Using an in-depth analysis of noise propagation in bootstrapping FFT computations, FPT is able to use noise-trimmed fixed-point representations that are up to 50% smaller than prior implementations using floating-point or integer FFTs. FPT's microarchitecture is built as a streaming processor inspired by traditional streaming DSPs: it instantiates high-throughput computational stages that are directly cascaded, with simplified control logic and routing networks. We explore different throughput-balanced compositions of streaming kernels with a user-configurable streaming width in order to construct a full bootstrapping pipeline. FPT's streaming approach allows 100% utilization of arithmetic units and requires only small bootstrapping key caches, enabling an entirely compute-bound bootstrapping throughput of 1 BS / 35 us. This is in stark contrast to the established classical CPU approach to FHE bootstrapping acceleration, which tends to be heavily memory and bandwidth-constrained. FPT is fully implemented and evaluated as a bootstrapping FPGA kernel for an Alveo U280 datacenter accelerator card. FPT achieves almost three orders of magnitude higher bootstrapping throughput than existing CPU-based implementations, and 2.5x higher throughput compared to recent ASIC emulation experiments.
        </td>
    </tr>
    <tr>
        <td>In-depth FPGA accelerator performance evaluation with single node benchmarks from the HPC challenge benchmark suite for Intel and Xilinx FPGAs using OpenCL</td>
        <td>Marius Meyer <em>et al.</em></td>
        <td>Paderborn University</td>
        <td><a href="https://doi.org/10.1016/j.jpdc.2021.10.007">Paper</a>  <a href="https://github.com/pc2/HPCC_FPGA">GitHub</a></td>
        <td>In-depth evaluation of the HPCC benchmark suite for FPGAs. We look into the power consumption and efficiency of the benchmarks. Also, we evaluate the impact of different floating-point precisions on the performance and resource utilization and give an example how the benchmarks can be used to evaluate the behavior of the underlying runtime environments.</td>
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
        <td>Shuhai: A Tool for Benchmarking High Bandwidth Memory on FPGAs</td>
        <td>Zeke Wang <em>et al.</em></td>
        <td>Zhejiang University</td>
        <td><a href="https://doi.org/10.1109/TC.2021.3075765">Paper</a></td>
        <td>FPGAs are starting to be enhanced with High Bandwidth Memory (HBM) as a way to reduce the memory bandwidth bottleneck encountered in some applications and to give the FPGA more capacity to deal with application state. However, the performance characteristics of HBM are still not well specified, especially in the context of FPGAs. In this paper, we bridge the gap between nominal specifications and actual performance by benchmarking HBM on a state-of-the-art FPGA, i.e., a Xilinx Alveo U280 featuring a two-stack HBM subsystem. To this end, we propose Shuhai, a benchmarking tool that allows us to demystify all the underlying details of HBM on an FPGA. FPGA-based benchmarking should also provide a more accurate picture of HBM than doing so on CPUs/GPUs, since CPUs/GPUs are noisier systems due to their complex control logic and cache hierarchy. Since the memory itself is complex, leveraging custom hardware logic to benchmark inside an FPGA provides more details as well as accurate and deterministic measurements. We observe that 1) HBM is able to provide up to 425 GB/s memory bandwidth, and 2) how HBM is used has a significant impact on performance, which in turn demonstrates the importance of unveiling the performance characteristics of HBM so as to select the best approach. As a yardstick, we also apply Shuhai to DDR4 to show the differences between HBM and DDR4. Shuhai can be easily generalized to other FPGA boards or other generations of memory, e.g., HBM3, and DDR3. We will make Shuhai open-source, benefiting the community.</td>
    </tr>
    <tr>
        <td>ThunderGP: Resource-Efficient Graph ProcessingFramework on FPGAs with HLS</td>
        <td>Xinyu Chen<em>et al.</em></td>
        <td>National University of Singapore</td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3517141">Paper</a> <a href="https://github.com/Xtra-Computing/ThunderGP">GitHub</a></td>
        <td>ThunderGP, an HLS-based graph processing framework on FPGAs, with which developers could enjoy FPGA-accelerated graph processing with no prior knowledge of hardware design. ThunderGP adopts the gather-apply-scatter (GAS) model as the abstraction of various graph algorithms and realizes the model by a build-in highly parallel and memory-efficient accelerator template. ThunderGP on DRAM-based hardware platforms provides 1.9 × ∼ 5.2 × improvement on bandwidth efficiency over the state-of-the-art, while ThunderGP on HBM-based hardware platforms delivers up to 5.2 × speedup over the state-of-the-art RTL-based approach.</td>
    </tr>
    <tr>
        <td>TopSort: A High-Performance Two-Phase Sorting Accelerator Optimized on HBM-Based FPGAs</td>
        <td>Weikang Qiao<em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://ieeexplore.ieee.org/document/9992222">Paper</a></td>
        <td>
            The emergence of high-bandwidth memory (HBM) brings new opportunities to boost the performance of sorting acceleration on FPGAs, which was conventionally bounded by the available off-chip memory bandwidth. However, it is nontrivial for designers to fully utilize this immense bandwidth. First, the existing sorter designs cannot be directly scaled at the increasing rate of available off-chip bandwidth, as the required on-chip resource usage grows at a much faster rate and would bound the sorting performance in turn. Second, designers need an in-depth understanding of HBM's characteristics to effectively utilize the HBM bandwidth. To tackle these challenges, we present TopSort, a novel two-phase sorting solution optimized for HBM-based FPGAs. In the first phase, 16 merge trees work in parallel to fully utilize 32 HBM channels’ bandwidth. In the second phase, TopSort reuses the logic from phase one to form a wider merge tree to merge the partially sorted results from phase one. TopSort also adopts HBM-specific optimizations to reduce resource overhead and improve bandwidth utilization. TopSort can sort up to 4 GB data using all 32 HBM channels, with an overall sorting performance of 15.6 GB/s. TopSort is 6.7× and 2.7× faster than state-of-the-art CPU and FPGA sorters.
        </td>
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
        <td>AMD Research Labs</td>
        <td><a href="https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/510849/H2RC21_Xilinx_submitted_version.pdf">Paper</a> <a href="https://github.com/Xilinx/ACCL">GitHub</a></td>
        <td>ACCL is a Vitis kernel and associated Pynq and XRT drivers which together provide MPI-like collectives for AMD FPGAs. ACCL is designed to enable compute kernels resident in FPGA fabric to communicate directly under host supervision but without requiring data movement between the FPGA and host. Instead, ACCL uses Vitis-compatible TCP and UDP stacks to connect FPGAs directly over Ethernet at up to 100 Gbps on Alveo cards.</td>
    </tr>
    <tr>
        <td>AutoBridge: Coupling Coarse-Grained Floorplanning and Pipelining for High-Frequency HLS Design on Multi-Die FPGAs <img src="./images/best_paper_award.png" alt="Best Paper" height="160"></td>
        <td>Licheng Guo <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3431920.3439289">Paper</a> <a href="https://github.com/Licheng-Guo/AutoBridge">GitHub</a></td>
        <td>Despite an increasing adoption of high-level synthesis (HLS) for its design productivity advantages, there remains a significant gap in the achievable frequency between an HLS design and a handcrafted RTL one. A key factor that limits the timing quality of the HLS outputs is the difficulty in accurately estimating the interconnect delay at the HLS level. This problem becomes even worse when large HLS designs are implemented on the latest multi-die FPGAs. To tackle this challenge, we propose AutoBridge, an automated framework that couples a coarse-grained floorplanning step with pipelining during HLS compilation. First, our approach provides HLS with a view on the global physical layout of the design, allowing HLS to more easily identify and pipeline the long wires, especially those crossing the die boundaries. Second, by exploiting the flexibility of HLS pipelining, the floorplanner is able to distribute the design logic across multiple dies on the FPGA device without degrading clock frequency. This prevents the placer from aggressively packing the logic on a single die which often results in local routing congestion that eventually degrades timing. Since pipelining may introduce additional latency, we further present analysis and algorithms to ensure the added latency will not compromise the overall throughput. AutoBridge can be integrated into the existing CAD toolflow for AMD FPGAs. In our experiments with a total of 43 design configurations, we improve the average frequency from 147 MHz to 297 MHz (a 102% improvement) with no loss of throughput and a negligible change in resource utilization. Notably, in 16 experiments we make the originally unroutable designs achieve 274 MHz on average. <br><b>Note</b>: Notes quoted from paper</td>
    </tr>
    <tr>
        <td>AutoSA: A Polyhedral Compiler for High-Performance Systolic Arrays on FPGA</td>
        <td>Jie Wang <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3431920.3439292">Paper</a></td>
        <td>While systolic array architectures have the potential to deliver tremendous performance, it is notoriously challenging to customize an efficient systolic array processor for a target application. Designing systolic arrays requires knowledge for both high-level characteristics of the application and low-level hardware details, thus making it a demanding and inefficient process. To relieve users from the manual iterative trial-and-error process, we present AutoSA, an end-to-end compilation framework for generating systolic arrays on FPGA. AutoSA is based on the polyhedral framework, and further incorporates a set of optimizations on different dimensions to boost performance. An efficient and comprehensive design space exploration is performed to search for high-performance designs. We have demonstrated AutoSA on a wide range of applications, on which AutoSA achieves high performance within a short amount of time. As an example, for matrix multiplication, AutoSA achieves 934 GFLOPs, 3.41 TOPs, and 6.95 TOPs in floating point, 16-bit and 8-bit integer data types on Alveo Alveo U250. <br><b>Note</b>: Notes quoted from paper</td>
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
        <td>AMD Research Labs</td>
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
        <td>FLOWER: A Comprehensive Dataflow Compiler for High-Level Synthesis</td>
        <td>Puya Amiri <em>et al.</em></td>
        <td>DFKI</td>
        <td><a href="https://arxiv.org/abs/2112.07789">Paper</a>
            <a href="https://github.com/AnyDSL/flower">Github</a></td>
        <td>A compiler that provides automatic transformations for high-level synthesis from a domain-specific library. This allows programmers to focus on algorithm implementations rather than low-level optimizations for dataflow architectures. FLOWER generates efficient implementations for high-performance streaming applications, in the context of image processing and computer vision. The implementation covers the generation of both device and corresponding host codes.</td>
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
        <td>The HPCG benchmark represents a modern complement to the HPL benchmark in the performance evaluation of HPC systems. This paper presents the details of the first FPGA-based implementation of HPCG that takes advantage customized compute architectures. The results show that the high-performance multi-FPGA implementation, using 1 and 4 AMD Alveo U280 achieves up to 108.3 GFlops and 346.5 GFlops respectively. Comparable performance with respect to modern GPUs are also demonstrated.</td>
    </tr>
    <tr>
        <td>Scotch: Generating FPGA-Accelerators for Sketching at Line Rate</td>
        <td>Martin Kiefer <em>et al.</em></td>
        <td>TU Berlin, DFKI</td>
        <td><a href="http://www.vldb.org/pvldb/vol14/p281-kiefer.pdf">Paper</a> <a href="https://github.com/martinkiefer/Scotch">GitHub</a></td>
        <td>Sketching algorithms  are a powerful tool for single-pass data summarization. Their numerous  applications include approximate query processing, machine learning, and  large-scale network monitoring. In the presence of high-bandwidth  interconnects or in-memory data, the throughput of summary maintenance  over input data becomes the bottleneck. While FPGAs have shown admirable  throughput and energy-efficiency for data processing tasks, developing  FPGA accelerators requires a sophisticated hardware design and expensive  manual tuning by an expert.  We propose Scotch, a novel system for accelerating sketch maintenance  using FPGAs. Scotch provides a domain-specific language for the  user-friendly, high-level definition of a broad class of sketching  algorithms. A code generator performs the heavy-lifting of hardware  description, while an auto-tuning algorithm optimizes the summary size.  Our evaluation shows that FPGA accelerators generated by Scotch  outperform CPU- and GPU-based sketching by up to two orders of magnitude  in terms of throughput and up to a factor of five in terms of energy  efficiency.
</td>
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
        <td>Evaluating FPGA Accelerator Performance with a Parameterized OpenCL Adaptation of Selected Benchmarks of the HPCChallenge Benchmark Suite</td>
        <td>Marius Meyer <em>et al.</em></td>
        <td>Paderborn University</td>
        <td><a href="https://dl.acm.org/doi/10.1109/H2RC51942.2020.00007">Paper</a> <a href="https://github.com/pc2/HPCC_FPGA">GitHub</a></td>
        <td>OpenCL-based open-source implementation of the HPCC benchmark suite for FPGAs.</td>
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
