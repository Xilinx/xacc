# Publications

This page lists the research publications which have been carried out in the context of the XACC program, or papers that may be of interest to the XACC community. 

## Contribute

If you would like to contribute to this page by adding a reference to your publication, please follow the [contribution guidelines](contributing.md) 

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
        <td><a href="https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/510849/H2RC21_Xilinx_submitted_version.pdf">Paper</a> <a href="https://github.com/Xilinx/ACCL">Github</a></td>
        <td>ACCL is a Vitis kernel and associated Pynq and XRT drivers which together provide MPI-like collectives for Xilinx FPGAs. ACCL is designed to enable compute kernels resident in FPGA fabric to communicate directly under host supervision but without requiring data movement between the FPGA and host. Instead, ACCL uses Vitis-compatible TCP and UDP stacks to connect FPGAs directly over Ethernet at up to 100 Gbps on Alveo cards.</td>
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
            <a href="https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP">Github</a></td>
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
        <td>FleetRec: Large-Scale Recommendation Inference on Hybrid GPU-FPGA Clusters</td>
        <td>Wenqi Jiang <em>et al.</em></td>
        <td>ETH Zurich</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/485153">Paper</a>
            <a href="https://github.com/fpgasystems/GPU-FPGA-Recommendation-System">Github</a></td>
        <td>A high-performance and scalable recommendation inference system within tight latency constraints. FleetRec takes adventage of both GPUs and FPGAs by disaggregating computation and memory to different types of accelerators and bridging their connections by high-speed network, FleetRec gains the best of both worlds, and can naturally scale out by adding nodes to the cluster</td>
    </tr>
    <tr>
        <td>FLOWER: A Comprehensive Dataflow Compiler for High-Level Synthesis</td>
        <td>Puya Amiri <em>et al.</em></td>
        <td>DFKI</td>
        <td><a href="https://arxiv.org/abs/2112.07789">Paper</a>
            <a href="https://github.com/AnyDSL/flower">Github</a></td>
        <td>A compiler infrastructure that provides automatic canonical transformations for high-level synthesis from a domain-specific library. This allows programmers to focus on algorithm implementations rather than low-level optimizations for dataflow architectures. FLOWER generates efficient implementations for streaming applications, in the context of image processing and computer vision. Moreover, this tool makes it possible to generate both device and host codes from a single description of an application.</td>
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
        <td>SKT: A One-Pass Multi-Sketch Data Analytics Accelerator</td>
        <td>Monica Chiosa <em>et al.</em></td>
        <td>ETH Zurich/Accemic Technologies</td>
        <td><a href="https://www.research-collection.ethz.ch/handle/20.500.11850/505690">Paper</a>
            <a href="https://github.com/fpgasystems/SKT">Github</a></td>
        <td>SKT is an FPGA-based accelerator that can compute several sketches along with basic statistics (av- erage, max, min, etc.) in a single pass over the data streams. SKT has been designed to characterize a data set by calculating its cardinality, its second frequency moment, and its frequency distribution. The design processes data streams coming either from PCIe or TCP/IP, and it is built to fit emerging cloud service architectures </td>
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
        <td>Extending High-Level Synthesis for Task-Parallel Programs</td>
        <td>Yuze Chi <em>et al.</em></td>
        <td>UCLA</td>
        <td><a href="https://arxiv.org/abs/2009.11389">Paper</a></td>
        <td>Extend the HLS C++ language and present a fully automated framework with programmer-friendly interfaces, universal software simulation, and fast code generation to overcome these limitations.</td>
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
        <td><a href="https://github.com/manuelburger/daceBLAS_demo">Paper</a></td>
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
<p align="center">Copyright&copy; 2021 Xilinx</p>
