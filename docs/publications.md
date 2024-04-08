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
        <td>Callipepla: Stream Centric Instruction Set and Mixed Precision for Accelerating Conjugate Gradient Solver</td>
        <td>Linghao Song <em>et al.</em></td>
        <td>UCLA and Ansys</td>
        <td><a href="https://dl.acm.org/doi/abs/10.1145/3543622.3573182">Paper</a> <a href="https://github.com/UCLA-VAST/Callipepla">GitHub</a></td>
        <td>
            The continued growth in the processing power of FPGAs coupled with high bandwidth memories (HBM), makes systems like the Xilinx U280 credible platforms for linear solvers which often dominate the run time of scientific and engineering applications. In this paper, we present Callipepla, an accelerator for a preconditioned conjugate gradient linear solver (CG). FPGA acceleration of CG faces three challenges: (1) how to support an arbitrary problem and terminate acceleration processing on the fly, (2) how to coordinate long-vector data flow among processing modules, and (3) how to save off-chip memory bandwidth and maintain double (FP64) precision accuracy. To tackle the three challenges, we present (1) a stream-centric instruction set for efficient streaming processing and control, (2) vector streaming reuse (VSR) and decentralized vector flow scheduling to coordinate vector data flow among modules and further reduce off-chip memory access latency with a double memory channel design, and (3) a mixed precision scheme to save bandwidth yet still achieve effective double precision quality solutions. To the best of our knowledge, this is the first work to introduce the concept of VSR for data reusing between on-chip modules to reduce unnecessary off-chip accesses and enable modules working in parallel for FPGA accelerators. We prototype the accelerator on a Xilinx U280 HBM FPGA. Our evaluation shows that compared to the Xilinx HPC product, the XcgSolver, Callipepla achieves a speedup of 3.94x, 3.36x higher throughput, and 2.94x better energy efficiency. Compared to an NVIDIA A100 GPU which has 4x the memory bandwidth of Callipepla, we still achieve 77% of its throughput with 3.34x higher energy efficiency. The code is available at https://github.com/UCLA-VAST/Callipepla.
        </td>
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
        <td>CHARM: Composing Heterogeneous AcceleRators for Matrix Multiply on Versal ACAP Architecture</td>
        <td>Jinming Zhuang <em>et al.</em></td>
        <td>University of Pittsburgh, UCLA, UIUC, AMD</td>
        <td><a href="https://dl.acm.org/doi/10.1145/3543622.3573210">Paper</a> <a href="https://github.com/arc-research-lab/CHARM">GitHub</a></td>
        <td>
            Dense matrix multiply (MM) serves as one of the most heavily used kernels in deep learning applications. To cope with the high computation demands of these applications, heterogeneous architectures featuring both FPGA and dedicated ASIC accelerators have emerged as promising platforms. For example, the AMD/Xilinx Versal ACAP architecture combines general-purpose CPU cores and programmable logic (PL) with AI Engine processors (AIE) optimized for AI/ML. An array of 400 AI Engine processors executing at 1 GHz can theoretically provide up to 6.4 TFLOPs performance for 32-bit floating-point (fp32) data. However, machine learning models often contain both large and small MM operations. While large MM operations can be parallelized efficiently across many cores, small MM operations typically cannot. In our investigation, we observe that executing some small MM layers from the BERT natural language processing model on a large, monolithic MM accelerator in Versal ACAP achieved less than 5% of the theoretical peak performance. Therefore, one key question arises: How can we design accelerators to fully use the abundant computation resources under limited communication bandwidth for end-to-end applications with multiple MM layers of diverse sizes? We identify the biggest system throughput bottleneck resulting from the mismatch of massive computation resources of one monolithic accelerator and the various MM layers of small sizes in the application. To resolve this problem, we propose the CHARM framework to compose multiple diverse MM accelerator architectures working concurrently towards different layers within one application. CHARM includes analytical models which guide design space exploration to determine accelerator partitions and layer scheduling. To facilitate the system designs, CHARM automatically generates code, enabling thorough onboard design verification. We deploy the CHARM framework for four different deep learning applications, including BERT, ViT, NCF, MLP, on the AMD/Xilinx Versal ACAP VCK190 evaluation board. Our experiments show that we achieve 1.46 TFLOPs, 1.61 TFLOPs, 1.74 TFLOPs, and 2.94 TFLOPs inference throughput for BERT, ViT, NCF, MLP, respectively, which obtain 5.40x, 32.51x, 1.00x and 1.00x throughput gains compared to one monolithic accelerator.
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



---------------------------------------
<p class="copyright">Copyright&copy; 2022 Advanced Micro Devices</p>
