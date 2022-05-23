# Paderborn University

The Heterogeneous Accelerated Compute Cluster at the [Paderborn Center for Parallel Computing](https://pc2.uni-paderborn.de) (PC2) lead by principal investigator [Prof. Christian Plessl](https://en.cs.uni-paderborn.de/hpc/team/group/members/plessl), who is the director of PC2 and holds the chair for High-Performance Computing at the Department of Computer Science at [Paderborn University, Germany](https://www.uni-paderborn.de/en). [Prof. Marco Platzner](https://en.cs.uni-paderborn.de/ceg/team/group/people/marco-platzner) who holds the [Chair for Computer Engineering](https://en.cs.uni-paderborn.de/ceg) and is also a member of PC2, will serve as co-PI for the HACC at Paderborn University. 

As a national HPC center, PC2 provides computing resources, consulting and services for academic users from Germany. A key part of the scientific mission of PC2 is research in highly scalable and energy-efficient numerical methods and simulation techniques, targeting HPC systems with heterogeneous computing resources. Specifically, PC2 has a long standing experience and pioneering role of moving FPGAs from the testbed to real HPC systems and operates some of the largest and most modern HPC production systems with FPGA accelerators.

The specific role of PC2 in the HACC program, will be to contribute its dual expertise in HPC and FPGA acceleration and the development of FPGA-accelerated libraries for scientific computing, domain-specific toolflows for simplifiying the design of FPGA accelerators, and ready to use open source HPC codes with FPGA support.

As part of the HACC program, PC2 makes the Noctua 2 system available to qualified researchers worldwide, for technology evaluation and joint tool and application development..


## The Noctua 2 HPC System with FPGAs

Noctua 2 is an Atos BullSequana XH2000 heterogeneous computing platform with CPU, GPU, and FPGA partitions:

    * an CPU partition with 1,056 dual-socket servers populated with AMD Milan 7763 CPUs, for a total of more than 43,872 CPUs,
    * a GPU partition comprising 128 Nvidia A100 GPUs, 
    * an FPGA partition with 48 Xilinx Alveo U280 accelerator cards, each equipped with 8 Gbytes of HBM2 and 32 Gbytes of DDR4 memory and 32 BittWare 520N FPGA accelerator cards

The compute nodes in these partitions are connected by a 100Gbps Inifiniband network. Additionally, all FPGA cards card will be connected to a Calient S320 full-crossbar, optical layer-1 circuit switch that provides a configurable optical network dedicated to FPGA acceleration.



---------------------------------------
<p align="center">Copyright&copy; 2022 Advanced Micro Devices</p>
