# University of California, Los Angeles
The Heterogeneous Accelerated Compute Cluster at the [University of California, Los Angeles](https://www.ucla.edu/) (UCLA), is directed by [Prof. Jason Cong](https://vast.cs.ucla.edu/people/faculty/jason-cong), Director for the Center for Customizable Domain-Specific Computing and Director for VLSI Architecture, Synthesis, and Technology (VAST) Laboratory at UCLA Samueli School of Engineering.   
   
The cluster at UCLA will focus on energy-efficient computing, customized computing for big-data applications and highly scalable algorithms.   
   
[UCLA VAST lab](https://github.com/UCLA-VAST) is actively working on 4 open-sourced research projects, and has published 5 research articles. Please find the details below. 
   
## The HACC Cluster
The cluster is running in full capacity. All host servers run Ubuntu 18.04.   
Users can choose to run Ubuntu 16.04/18.04/20.04 in their containers.   
   
![](/images/ucla/xacc_ucla.png)
 
## Research Descriptions
#### 1. AutoSA   
We developed an open-source systolic array compiler, AutoSA, targeting Xilinx FPGAs. This compiler offers FPGA programmers an easy solution to generate high-performance systolic arrays on Xilinx FPGAs. We are using the Alveo U250 board to verify our designs. Also, we are collaborating with Cornell to integrate AutoSA into HeteroCL.  
   
> *Open-sourced Github page:* [AutoSA](https://github.com/UCLA-VAST/AutoSA)    

#### 2. HBM Connect    
HBM Connect is a high-performance customized interconnect for FPGA HBM boards. It solves the limitation of existing high-level synthesis (HLS) programming environment and the built-in crossbar when multiple processing elements to access HBM board's large number of external memory channels. HBM Connect introduces novel HLS-based optimization to increase the throughput of AXI bus masters and switching elements. It also presents a high-performance customized crossbar architecture that could replace the built-in crossbar. This project will help FPGA programmers to maximize the bandwidth between accelerators and HBM.    
   
> *Open-sourced Github page:* [HBM Connect](https://github.com/UCLA-VAST/hbmbench)   

#### 3. TAPA     
C/C++/OpenCL-based high-level synthesis (HLS) becomes more and more popular for field-programmable gate array (FPGA) accelerators in many application domains in recent years, thanks to its competitive quality of result (QoR) and short development cycle compared with the traditional register-transfer level (RTL) design approach. Yet, limited by the sequential C semantics, it remains challenging to adopt the same highly productive high-level programming approach in many other application domains, where coarse-grained tasks run in parallel and communicate with each other at a fine-grained level. While current HLS tools support task-parallel programs, the productivity is greatly limited in the code development, correctness verification, and QoR tuning cycles, due to the poor programmability, restricted software simulation, and slow code generation, respectively. Such limited productivity often defeats the purpose of HLS and hinder programmers from adopting HLS for task-parallel FPGA accelerators. In this project, we extend the HLS C++ language and present a fully automated framework with programmer-friendly interfaces, universal software simulation, and fast code generation to overcome these limitations. Experimental results based on a wide range of real-world task-parallel programs show that, on average, the lines of kernel and host code are reduced by 22% and 51%, respectively, which considerably improves the programmability. The correctness verification and the iterative QoR tuning cycles are both greatly accelerated by 3.2xand 6.8x, respectively. The Xilinx Alveo boards are used as synthesis targets in the experimental evaluations.     
   
> *Open-sourced Github page:* [TAPA](https://github.com/UCLA-VAST/tapa)   
   
#### 4. AutoBridge   
Despite an increasing adoption of high-level synthesis (HLS) for its design productivity advantages, there remains a significant gap in  the achievable clock frequency between an HLS-generated design and an optimized handcrafted RTL.
A key factor that limits the timing quality of the HLS outputs is the difficulty in accurately estimating the interconnect delay at the HLS level. Unfortunately, this problem becomes even worse when large HLS designs are implemented on the latest multi-die FPGAs, where die-crossing interconnects incur a high delay penalty.
    
To tackle this challenge, we propose AutoBridge, an automated framework that couples a coarse-grained floorplanning step with pipelining during HLS compilation. First, our approach provides HLS with a view on the global physical layout of the design, allowing HLS to more easily identify and pipeline the long wires, especially those crossing the die boundaries. Second, by exploiting the flexibility of HLS pipelining, the  floorplanner is able to distribute the design logic across multiple dies on the FPGA device without degrading clock frequency. This keeps the placer from aggressively packing the logic on a single die which often results in local routing congestion that eventually degrades timing. Since pipelining may introduce additional latency, we further present analysis and algorithms to ensure the added latency will not compromise the overall throughput.
    
AutoBridge can be integrated into the existing CAD toolflow for Xilinx FPGAs targeting the Alveo U250 and the U280 board. In our experiments with a total of 43 design configurations, we improve the average frequency from 147 MHz to 297 MHz (a 102\% improvement) with no loss of throughput and a negligible change in resource utilization. Notably, in 16 experiments we make the originally unroutable designs achieve 274 MHz on average. 
   
This work is in collaboration with Prof. Zhiru Zhang from Cornell University.    
   
> *Open-sourced Github page:* [AutoBridge](https://github.com/Licheng-Guo/AutoBridge)  
    
## Research Articles
1. Jie Wang, Licheng Guo, Jason Cong, "AutoSA: A Polyhedral Compiler for High-Performance Systolic Arrays on FPGA," FPGA 2021.       
2. Y. Choi, Y. Chi, W. Qiao, N. Samardzic, and J. Cong, "HBM Connect: High-Performance HLS Interconnect for FPGA HBM," FPGA 2021.        
3. Y. Choi, Y. Chi, J. Wang, L. Guo, and J. Cong “When HLS meets FPGA HBM: Benchmarking and bandwidth optimization,” [Link to Document](https://arxiv.org/abs/2010.06075).   
4. Y. Chi, L. Guo, Y. Choi, J. Wang, and J. Cong “Extending high-level synthesis for task-parallel programs,” [Link to Document](https://arxiv.org/abs/2009.11389).   
5. Licheng Guo, Yuze Chi, Jie Wang, Jason Lau, Weikang Qiao, Ecenur Ustun, Zhiru Zhang and Jason Cong, "AutoBridge: Coupling Coarse-Grained Floorplanning with Pipelining for High-Frequency HLS Design on Multi-Die FPGAs," FPGA 2021.   


---------------------------------------
<p align="center">Copyright&copy; 2022 Advanced Micro Devices</p>