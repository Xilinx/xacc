# HACC Tech Talk series

The talks will be hosted as Zoom webinars and are free to attend. The format for each session will be two 30-minute talks on topics related to Adaptive Compute. 

If you would like to present your work at an HACC Tech Talk, please contact [xup@xilinx.com](mailto:xup@xilinx.com) with an outline of your proposal. 

# Past talks

## XACC Tech Talk 8

30<sup>th</sup> March 2022

### **ACCL: an open-source FPGA accelerated communication library for scale-out applications**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://youtube.com/embed/jqrziE9cZg4" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Lucian Petrica, AMD AECG Research Labs.

This talk will present ACCL, an open-source FPGA-accelerated communication collectives library designed to enable scale-out of applications running primarily on AMD FPGAs. Compared to previous collective communication solutions for FPGA, ACCL is flexible and extensible, easily portable, and fast. We evaluate ACCL on 8 Alveo nodes at XACC ETHZ and demonstrate that ACCL outperforms OpenMPI over 100 Gbps TCP-IP for large messages.

### **Efficient Recommendation Inference on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/SJ0ze3p0GzU" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Wengi Jiang, ETH Zurich.

Deep neural networks are widely used in personalized recommendation systems. Recommendation inference is largely bound by memory due to random memory accesses needed to lookup the embedding tables. 
This talk will introduce MicroRec, a high-performance FPGA inference engine for recommendation systems that tackles the memory bottleneck. This is extended to implement two high-performance recommendation inference clusters; one using FPGAs and the other using combined FPGAs and GPUs. 
Experiments on three production models show that our cluster-based solutions outperform the CPU baseline by more than one order of magnitude while achieving significantly lower latency.

## XACC Tech Talk 7

16<sup>th</sup>  December 2021

### **Easy deployment, scaling and resource management of Alveo FPGA​**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/NGhgmryVTm0" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Chris Kachis, InAccel

In this talk we will present an easy way to deploy, scale and manage FPGA application on Alveo clusters such as XACC. InAccel will present the Coral resource manager that abstract away the FPGA resources for easy utilization and instant scaling of FPGA designs. It will also show how we managed to support multi-FPGA accelerators (such as FINN) using a custom InAccel runtime for synchronization between accelerators. Finally, we will show how Coral resource manager can be used for easier deployment of the Vitis AI and Vitis libraries. 

### **Lucent: A language for developing application specific dataflow machines on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/z9LsKxfP_-w" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
</iframe></section>

Dr Nick Brown, EPCC, University of Edinburgh

Writing fast, high performance FPGA codes is difficult, even with HLS. However potentially we can learn from work done in the 1970s/1980s which studied programming general purpose dataflow machines, as the reconfigurability of FPGAs enable us to present the abstraction of dataflow machines which are specific to an application. In this talk I will describe Lucent, a modern version of the Lucid dataflow language, which targets AMD Alveo hardware and aims to empower the development of fast by construction dataflow codes on FPGAs.

## XACC Tech Talk 6

19<sup>th</sup>  August 2021

### **Multes on Alveo: An FPGA-based Smart Key-Value Store Running on XACC**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/lkxw6OUMtNU?" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>

Zsolt István, Assoc. Prof, IT University of Copenhagen

In this talk, we will present Multes, an FPGA-based Key-Value Store (KVS) with user-defined query offloading (the “smarts”) and explain how it has been ported to the Alveo cards in XACC using the Vitis Shell with 100Gbps networking. We will also present an example of offloading to the KVS, namely, a privacy-preserving perturbation for ML training.



### **TAPA: Efficient Support for Task-Parallel High-Level Synthesis**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/lkxw6OUMtNU?start=1667" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>
Yuze Chi, Computer Science Department, UCLA

This talk will present TAPA, a fully automated framework for task-parallel HLS programs with programmer-friendly interfaces, unconstrained software simulation, and fast hierarchical code generation. 

Experimental results based on a wide range of real-world task-parallel programs show that the lines of kernel and host code, the correctness verification cycle, and the iterative QoR tuning cycle are all greatly shortened, which considerably improves the programmability.



## XACC Tech Talk 5

05<sup>th</sup>  August 2021

### **Optimized Implementation of the HPCG Benchmark on Reconfigurable Hardware**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/9pq2GxBC32Q?start=66" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
	</iframe></section>
Alberto Zeni, Politecnico Di Milano

The HPCG benchmark represents a modern complement to the HPL benchmark in the performance evaluation of HPC systems, as it has been recognized as a more representative benchmark to reflect real-world applications and, consequently, its popularity and acceptance continue to rise within the HPC community. This talk will present the first FPGA-based implementation of the HPCG benchmark, which takes full advantage of reconfigurable architectures. Our implementation shows performance up to 108.4 and 346.5 GFlops on 1 and 4 AMD Alveo U280 cards on the XACC cluster, demonstrating significant performance improvements against the CPU implementation and comparable performance with GPU implementations with better power efficiency. 



### **ScaleHLS: Scalable High-Level Synthesis through MLIR**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/9pq2GxBC32Q?start=2117" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Hanchen Ye, UIUC

High-level Synthesis (HLS) has been widely adopted as it significantly improves the hardware design productivity and enables efficient design space exploration (DSE). HLS tools can be used to deliver solutions for many different kinds of design problems, and different problems are often better solved with different levels of abstraction. While existing HLS tools are built using compiler infrastructures largely based on a single-level abstraction (e.g., LLVM), we propose ScaleHLS, a next-generation HLS compilation flow, on top of a multi-level compiler infrastructure called MLIR, for the first time. ScaleHLS is able to optimize HLS designs at multiple levels of abstraction and provides an HLS-dedicated transform and analysis library to solve the optimization problems at the suitable abstraction levels. On top of the library, we also build an automated DSE engine to explore the multi-dimensional design space highly efficiently. In addition, we develop an HLS C front-end and a C/C++ emission back-end to translate HLS designs into/from MLIR for enabling the end-to-end ScaleHLS flow. Experimental results show that, comparing to the baseline designs only optimized by AMD Vivado HLS, ScaleHLS improves the performances with amazing quality-of-results -- up to 768.1x better on computation kernel level programs and up to 3825.0x better on neural network models.




## XACC Tech Talk 4

22<sup>nd</sup>  July 2021

### **ThundeRiNG: Generating Multiple Independent Random Number Sequences on FPGAs**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/q4BcSNVNR2A?start=84" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Hongshi Tan, Master student, National  University of Singapore

*ThundeRiNG* is a high-throughput system for generating multiple independent sequences of random numbers on FPGAs. The experimental results show that ThundeRiNG passes the strictest randomness tests, BigCrush, achieving a throughput of 20.95 Tb/s. 
Compared to a state-of-the-art GPU library, ThundeRiNG demonstrates a 10x speedup in throughput and 9x performance and 26x power efficiency improvement on two applications (pi estimation and Monte Carlo option pricing).



### **Fletcher: A framework for high-performance big data analytics using FPGAs**


<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/q4BcSNVNR2A?start=1642" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Joost Hoozemans, Postdoctoral researcher, TU Delft

This talk will present a vision for transparent acceleration of analytics workloads on FPGAs.
The *Fletcher* project allows integrating FPGAs into scalable software frameworks, to efficiently utilize them in a cloud hardware infrastructure. Fletcher supports Alveo FPGA cards in the XACC cluster, AWS F1 and Azure instances.
We demonstrate the integration of FPGA implementations of various analytics operations into a number of popular analytics frameworks (Apache Spark, Dremio, Dask) and show significant speedup.






## XACC Tech Talk 3

8<sup>th</sup>  July, 2021

### **Blockchain Machine: Accelerating Validation Bottlenecks in Hyperledger Fabric**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/D8ZunBYc5xI?start=75" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Haris Javaid, Senior Staff Researcher, Xilinx

Blockchain Machine is a hardware accelerator for validation of blocks in Hyperledger Fabric, one of the most widely used permissioned blockchain platforms. It is targeted for a server with network-attached FPGA acceleration card and can be adapted to applications and their smart contracts (built on top of Fabric). The Blockchain Machine retrieves block/transaction data in hardware directly from the network interface, which is then processed through a configurable and efficient block-level and transaction-level pipeline. The results are then accessed by the host CPU where non-bottleneck operations are executed. From our implementation integrated with Fabric v1.4 LTS, we observed up to 17x speedup in block validation when compared to software-only implementation.

Blockchain: [https://github.com/Xilinx/hyperledger-fabric](https://github.com/Xilinx/hyperledger-fabric)



### **ThunderGP: HLS-based Graph Processing on FPGAs**


<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/D8ZunBYc5xI?start=1792" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Xinyu Chen, Doctoral Student, National University of Singapore 

*ThunderGP* is proposed to bridge the gap between high-level graph processing applications and underlying CPU-FPGA platforms. With ThunderGP, developers could enjoy the performance of FPGA-accelerated graph processing by writing only a few high-level functions with no knowledge of the hardware.

ThunderGP: [https://github.com/Xtra-Computing/ThunderGP](https://github.com/Xtra-Computing/ThunderGP)




## XACC Tech Talk 2

24<sup>th</sup> June 2021

### **VNx and EasyNet**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/P93WlrBVxoM?start=120" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Mario Ruiz, Xilinx University Program; Zhenhao He, Doctoral Student, Systems Group, ETH Zurich 

This presentation will introduce *VNx* which adds 100Gbps UDP/IP support to Vitis designs. *EasyNet* extends VNx to support 100Gbps TCP/IP from HLS. 
Both VNx and EasyNet are open-source and supported from Vitis and can be used to add high-speed networking interfaces to Alveo platforms. 

Vnx: [https://github.com/Xilinx/xup_vitis_network_example](https://github.com/Xilinx/xup_vitis_network_example)

EasyNet: [https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP](https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP)



### **Elastic-DF: Scaling Performance of DNN Inference in FPGA Clouds through Automatic Partitioning**


<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/P93WlrBVxoM?start=1851" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dr. Lucian Petrica, Xilinx Research Labs 

Customized compute acceleration in the datacenter is key to the wider roll-out of applications based on deep neural network (DNN) inference.

In this presentation we discuss how to maximize the performance and scalability of FPGA-based pipeline dataflow DNN inference accelerators (DFAs) automatically on computing infrastructures consisting of multi-die, network-connected FPGAs. We present *Elastic-DF*, a novel resource partitioning tool which integrates with the [DNN compiler FINN](https://github.com/Xilinx/finn) and utilizes 100Gbps Ethernet FPGA infrastructure, to achieve low-latency model-parallel inference without host involvement. Elastic-DF was applied to popular image classifiers ResNet50 and MobileNetV1 at XACC and provides significant throughput increase with no adverse impact on latency.




## XACC Tech Talk 1

10<sup>th</sup> June 2021

### **Coyote: Do OS abstractions make sense in FPGAs?**

<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/un7wck0IkGs?start=88" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Dario Korolija, Doctoral Student, Systems Group, ETH Zurich

Hybrid computing systems, consisting of a CPU server coupled with a Field-Programmable Gate Array (FPGA) for application acceleration, are today a common facility in datacenters and clouds. FPGAs can deliver tremendous improvements in performance and energy efficiency for a range or workloads, but development and deployment of FPGA-based applications remains cumbersome, leading to recent work which replicates subsets of the traditional OS execution environment (virtual memory, processes, etc.) on the FPGA.

We ask a different question: to what extent do traditional OS abstractions make sense in the context of an FPGA as part of a hybrid system, particularly when taken as a complete package, as they would be in an OS? To answer this, we built and evaluated *Coyote*, an open source, portable, configurable “shell” for FPGAs which provides a full suite of OS abstractions, working with the host OS. Coyote supports secure spatial and temporal multiplexing of the FPGA between tenants, virtual memory, communication, and memory management inside a uniform execution environment. The overhead of Coyote is small and the performance benefit is significant, but more importantly it allows us to reflect on whether importing OS abstractions wholesale to FPGAs is the best way forward.

Coyote: [https://github.com/fpgasystems/Coyote](https://github.com/fpgasystems/Coyote)



### **Data-Centric FPGA Programming with Multi-Level Design**


<section style="text-align:center"><iframe class="you-container" style="text-align:center; border: 0px; background:transparent" src="https://www.youtube.com/embed/un7wck0IkGs?start=1743" title="YouTube video player" frameborder="0" width="80%" height="auto" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen="">
        </iframe></section>
Johannes de Fine Licht, Doctoral Student, Scalable Parallel Computing Laboratory, ETH Zurich

Although high-level synthesis (HLS) tools have significantly improved programmer productivity over hardware description languages, developing for FPGAs remains tedious and error prone. Programmers must learn and implement a large set of vendor-specific syntax, patterns, and tricks to optimize (or even successfully compile) their applications, while dealing with ever-changing toolflows from the FPGA vendors. We propose a new way to develop, optimize, and compile FPGA programs. The Data-Centric parallel programming (*DaCe*) framework allows applications to be defined by their dataflow and control flow through the Stateful DataFlow multiGraph (SDFG) representation, capturing the abstract program characteristics, and exposing a plethora of optimization opportunities. SDFGs are extended by multi-level library nodes, which incorporate both domain-specific and platform-specific optimizations into the design flow, enabling knowledge transfer across application domains and FPGA vendors. We show how the powerful code-generating backend of DaCe emits efficient HLS code that is structured and annotated to implement the desired architectures and achieve high performance in practice.

DaCe: [https://github.com/spcl/dace](https://github.com/spcl/dace)




---------------------------------------
<p class="copyright">Copyright&copy; 2022 Advanced Micro Devices</p>
