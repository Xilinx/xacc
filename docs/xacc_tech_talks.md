# XACC Tech Talk series

The talks will be hosted as Zoom webinars and are free to attend. The format for each session will be two 30-minute talks on topics related to Adaptive Compute. 

If you would like to present your work at an XACC Tech Talk, please contact [xup@xilinx.com](xup@xilinx.com) with an outline of your proposal. 



## XACC Tech Talk 4

22<sup>nd</sup>  July 2021, 17:00-18:00 (CET/GMT+2)

[![](./images/zoom_30.png)]((https://xilinx.zoom.us/webinar/register/WN_PQxFA2rFRRmuzXU7bJrA0Q))   Register for the [XACC Tech Talk 4 Zoom webinar](https://xilinx.zoom.us/webinar/register/WN_PQxFA2rFRRmuzXU7bJrA0Q)

### Fletcher: A framework for high-performance big data analytics using FPGAs

Joost Hoozemans, Postdoctoral researcher, TU Delft

This talk will present a vision for transparent acceleration of analytics workloads on FPGAs.
The *Fletcher* project allows integrating FPGAs into scalable software frameworks, to efficiently utilize them in a cloud hardware infrastructure. Fletcher supports Alveo FPGA cards in the XACC cluster, AWS F1 and Azure instances.
We demonstrate the integration of FPGA implementations of various analytics operations into a number of popular analytics frameworks (Apache Spark, Dremio, Dask) and show significant speedup.

### ThundeRiNG: Generating Multiple Independent Random Number Sequences on FPGAs

Hongshi Tan, Master student, National  University of Singapore

*ThundeRiNG* is a high-throughput system for generating multiple independent sequences of random numbers on FPGAs. The experimental results show that ThundeRiNG passes the strictest randomness tests, BigCrush, achieving a throughput of 20.95 Tb/s. 
Compared to a state-of-the-art GPU library, ThundeRiNG demonstrates a 10x speedup in throughput and 9x performance and 26x power efficiency improvement on two applications (pi estimation and Monte Carlo option pricing).




# Past talks

## XACC Tech Talk 1

10<sup>th</sup> June 2021

[![](./images/youtube_social_circle_white.png)](https://www.youtube.com/watch?v=un7wck0IkGs)  View the recording [XACC Tech Talk 1 recording](https://www.youtube.com/watch?v=un7wck0IkGs)

### Coyote: Do OS abstractions make sense in FPGAs?

Dario Korolija, Doctoral Student, Systems Group, ETH Zurich

Hybrid computing systems, consisting of a CPU server coupled with a Field-Programmable Gate Array (FPGA) for application acceleration, are today a common facility in datacenters and clouds. FPGAs can deliver tremendous improvements in performance and energy efficiency for a range or workloads, but development and deployment of FPGA-based applications remains cumbersome, leading to recent work which replicates subsets of the traditional OS execution environment (virtual memory, processes, etc.) on the FPGA.

We ask a different question: to what extent do traditional OS abstractions make sense in the context of an FPGA as part of a hybrid system, particularly when taken as a complete package, as they would be in an OS? To answer this, we built and evaluated *Coyote*, an open source, portable, configurable “shell” for FPGAs which provides a full suite of OS abstractions, working with the host OS. Coyote supports secure spatial and temporal multiplexing of the FPGA between tenants, virtual memory, communication, and memory management inside a uniform execution environment. The overhead of Coyote is small and the performance benefit is significant, but more importantly it allows us to reflect on whether importing OS abstractions wholesale to FPGAs is the best way forward.

Coyote: [https://github.com/fpgasystems/Coyote](https://github.com/fpgasystems/Coyote)

### Data-Centric FPGA Programming with Multi-Level Design

Johannes de Fine Licht, Doctoral Student, Scalable Parallel Computing Laboratory, ETH Zurich

Although high-level synthesis (HLS) tools have significantly improved programmer productivity over hardware description languages, developing for FPGAs remains tedious and error prone. Programmers must learn and implement a large set of vendor-specific syntax, patterns, and tricks to optimize (or even successfully compile) their applications, while dealing with ever-changing toolflows from the FPGA vendors. We propose a new way to develop, optimize, and compile FPGA programs. The Data-Centric parallel programming (*DaCe*) framework allows applications to be defined by their dataflow and control flow through the Stateful DataFlow multiGraph (SDFG) representation, capturing the abstract program characteristics, and exposing a plethora of optimization opportunities. SDFGs are extended by multi-level library nodes, which incorporate both domain-specific and platform-specific optimizations into the design flow, enabling knowledge transfer across application domains and FPGA vendors. We show how the powerful code-generating backend of DaCe emits efficient HLS code that is structured and annotated to implement the desired architectures and achieve high performance in practice.

DaCe: [https://github.com/spcl/dace](https://github.com/spcl/dace)



## XACC Tech Talk 2

24<sup>th</sup> June 2021

[![](./images/youtube_social_circle_white.png)](https://www.youtube.com/watch?v=P93WlrBVxoM)  View the recording [XACC Tech Talk 2 recording](https://www.youtube.com/watch?v=P93WlrBVxoM)


### VNx and EasyNet

Dr. Mario Ruiz, Xilinx University Program; Zhenhao He, Doctoral Student, Systems Group, ETH Zurich 

This presentation will introduce *VNx* which adds 100Gbps UDP/IP support to Vitis designs. *EasyNet* extends VNx to support 100Gbps TCP/IP from HLS. 
Both VNx and EasyNet are open-source and supported from Vitis and can be used to add high-speed networking interfaces to Alveo platforms. 



Vnx: [https://github.com/Xilinx/xup_vitis_network_example](https://github.com/Xilinx/xup_vitis_network_example)

EasyNet: [https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP](https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP)


### Elastic-DF: Scaling Performance of DNN Inference in FPGA Clouds through Automatic Partitioning

Dr. Lucian Petrica, Xilinx Research Labs 

Customized compute acceleration in the datacenter is key to the wider roll-out of applications based on deep neural network (DNN) inference.

In this presentation we discuss how to maximize the performance and scalability of FPGA-based pipeline dataflow DNN inference accelerators (DFAs) automatically on computing infrastructures consisting of multi-die, network-connected FPGAs. We present *Elastic-DF*, a novel resource partitioning tool which integrates with the [DNN compiler FINN](https://github.com/Xilinx/finn) and utilizes 100Gbps Ethernet FPGA infrastructure, to achieve low-latency model-parallel inference without host involvement. Elastic-DF was applied to popular image classifiers ResNet50 and MobileNetV1 at XACC and provides significant throughput increase with no adverse impact on latency.



## XACC Tech Talk 3

8<sup>th</sup>  July, 2021

[![](./images/youtube_social_circle_white.png)](https://www.youtube.com/watch?v=P93WlrBVxoM)  View the recording <u>[XACC Tech Talk 3 recording](https://youtu.be/D8ZunBYc5xI)</u>

### Blockchain Machine: Accelerating Validation Bottlenecks in Hyperledger Fabric

Dr. Haris Javaid, Senior Staff Researcher, Xilinx

Blockchain Machine is a hardware accelerator for validation of blocks in Hyperledger Fabric, one of the most widely used permissioned blockchain platforms. It is targeted for a server with network-attached FPGA acceleration card and can be adapted to applications and their smart contracts (built on top of Fabric). The Blockchain Machine retrieves block/transaction data in hardware directly from the network interface, which is then processed through a configurable and efficient block-level and transaction-level pipeline. The results are then accessed by the host CPU where non-bottleneck operations are executed. From our implementation integrated with Fabric v1.4 LTS, we observed up to 17x speedup in block validation when compared to software-only implementation.

Blockchain: [https://github.com/Xilinx/hyperledger-fabric](https://github.com/Xilinx/hyperledger-fabric)

### ThunderGP: HLS-based Graph Processing on FPGAs

Xinyu Chen, Doctoral Student, National University of Singapore 

*ThunderGP* is proposed to bridge the gap between high-level graph processing applications and underlying CPU-FPGA platforms. With ThunderGP, developers could enjoy the performance of FPGA-accelerated graph processing by writing only a few high-level functions with no knowledge of the hardware.

ThunderGP: [https://github.com/Xtra-Computing/ThunderGP](https://github.com/Xtra-Computing/ThunderGP)


---------------------------------------
<p align="center">Copyright&copy; 2021 Xilinx</p>