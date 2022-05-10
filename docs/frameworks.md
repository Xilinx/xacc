# Frameworks

This page cover other software and frameworks that may be useful to generate or to deploy your designs. If you would like to contribute your framework to this page, please follow the [contribution guidelines](contributing.md) 

## PYNQ

PYNQ is an open-source project from Xilinx that makes it easier to use Xilinx platforms. Using the Python language and libraries, designers can exploit the benefits of programmable logic and to build more capable and exciting electronic systems. PYNQ can be used with Zynq, Zynq UltraScale+, Zynq RFSoC, **Alveo accelerator cards** and AWS-F1 to create high performance applications. PYNQ is available by default on the ETH HACC. Find out more in the [pynq.io](http://www.pynq.io/) page

## Machine Learning

### FINN

Fast, Scalable Quantized Neural Network Inference on FPGAs. Explore deep neural network inference on FPGAs. It specifically targets quantized neural networks, with emphasis on generating dataflow-style architectures customized for each network. Find out more in the [finn repository](https://github.com/Xilinx/finn)


## Networking

### EasyNet

This framework is ideal to scale out your application without CPU intervention, full TCP/IP support in the Alveo card. ETH Zurich provides example designs with TCP/IP support at 100 Gbps in Vitis. Find out more in the [Vitis 100Gbps TCP/IP repository](https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP)

### VNx

This framework is ideal to scale out your application without CPU intervention. Note that UDP is lightweight but no reliable. XUP provides example designs with UDP support at 100 Gbps in Vitis, this repository is also tightly coupled with the PYNQ project and provides support for distributed Alveo configuration on top of Dask. Find out more in the [VNx repository](https://github.com/Xilinx/xup_vitis_network_example)


## Programming Frameworks

### AutoBridge 

Floorplanning tool for Vivado HLS dataflow designs. [AutoBridge repository](https://github.com/Licheng-Guo/AutoBridge)

### AutoSA

Polyhedral-Based Systolic Array Auto-Compilation. [AutoSA repository](https://github.com/UCLA-VAST/AutoSA)

### Coyote

Reconfigurable Heterogeneous Architecture Framework aiming to provide operating system abstractions. [Coyote repository](https://github.com/fpgasystems/Coyote)

### DaCe

Data-Centric Parallel Programming compiles code in various programming languages and paradigms (Python/Numpy, MATLAB, TensorFlow) and maps it efficiently to CPUs, GPUs, and FPGAs with high utilization, on par with the state-of-the-art. Find out more in the [DaCe repository](https://github.com/spcl/dace)

### Fletcher

Allows easy kernel development and integration with various popular Big Data analytics frameworks based on Apache Arrow.
Fletcher will generate all the interfaces and provide the kernel designer with simple and easy to understand interface coresponding to the data types of their application.
This raises the abstraction to records and tables instead of buffers and bytes.
[Fletcher](https://github.com/abs-tudelft) has platform support for [Alveo](https://github.com/abs-tudelft/fletcher-alveo)

### hlslib

A collection of extensions for Vitis to improve developer quality of life, including CMake integration, better vectorization support, support for simulating dataflow kernels with feedback dependencies. [hlslib repository](https://github.com/definelicht/hlslib)

### ThunderGP

HLS-based Graph Processing Framework on FPGAs. [ThunderGP repository](https://github.com/Xtra-Computing/ThunderGP)

## Scheduling & Distributed

### InAccel

Fully integrated framework that allows to speedup your C/C++, Python, Java and Scala applications with zero code changes. InAccel Coral is a framework that allows the distributed acceleration of large data sets across clusters of FPGA resources using simple programming models. The InAccel framework is available by default on the ETH HACC. Find out more [InAccel](https://inaccel.com/coral-fpga-resource-manager/).

Universities can also access to InAccel technology [InAccel University](https://inaccel.com/university/)

### OctoRay
OctoRay is a Python framework which allows the user to easily scale up any FPGA application to multiple FPGAs using Dask. It supports at the moment all FPGA boards that are supported by PYNQ, so all PYNQ boards and Alveo cards. [OctoRay repository](https://github.com/abs-tudelft/octoray)

---------------------------------------
<p align="center">Copyright&copy; 2022 Advanced Micro Devices</p>
