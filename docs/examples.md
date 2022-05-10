# Examples

The following page is a list of example designs that may be used with the HACCs. Each HACC may have different Alveo hardware, with different shells installed, so you will need to check the details of each project against the cluster hardware you want to run it on. 

## Contribute

If you would like to contribute to this page by adding a reference to your project, please follow the [contribution guidelines](contributing.md)

## Projects

**_Note:_** Note that these designs are untested, and may need some updates to get them to work with specific tool versions/shell versions or different Alveo boards to the versions they were originally developed with. 

<table width="100%">
  <thead>
    <tr>
      <th width="33%">Project</th>
      <th width="33%">Authors</th>
      <th width="33%">Platform(s)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="https://bitbucket.org/necst/xohw18_5points_public/">5-point motion estimation</a></td>
      <td>Marco Rabozzi, Emanuele Del Sozzo, Lorenzo Di Tucci, Marco Domenico Santambrogio, Politecnico Di Milano</td>
      <td>AWS F1 / Alveo U200</td>
    </tr>
    <tr>
      <td><a href="https://bitbucket.org/necst/xohw2020_approximate-pagerank_public/">Approximate Page Rank</a></td>
      <td>Alberto Parravicini, Francesco Sgherzi, Marco Santambrogio, Politecnico Di Milano</td>
      <td>Alveo U200</td>
    </tr>
    <tr>
      <td><a href="https://github.com/fpgasystems/Coyote">Coyote</a></td>
      <td>Dario Korolija <em>et al.</em>, ETH Zurich</td>
      <td>Alveo U250 / U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/davidcastells/KmerFilterAWS">DNA sequence analysis</a></td>
      <td>Zaina Salym, Marc Codina, David Castells-Rufas, UAB</td>
      <td>AWS F1</td>
    </tr>
    <tr>
      <td><a href="https://github.com/fpgasystems/Vitis_with_100Gbps_TCP-IP">EasyNet</a></td>
      <td>Zhenhao He <em>et al.</em>, ETH Zurich</td>
      <td>Alveo U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/fpgasystems/erbium">ERBium</a></td>
      <td>Fabio Maschi <em>et al.</em>, ETH Zurich</td>
      <td>AWS F1 / Alveo U250/ U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Xilinx/finn-examples">FINN Dataflow DNN Accelerator Compiler</a></td>
      <td>Xilinx Research</td>
      <td>Alveo U250 / U280</td>
    </tr>
    <tr>
      <td>Fletcher on Alveo example: <a href="https://github.com/abs-tudelft/wiki-search-alveo">Wikipedia search </a></td>
      <td>Matthijs Brobbel, Jeroen van Straten, Joost Hoozemans, Delft University of Technology</td>
      <td>Alveo U200 / U250</td>
    </tr>
    <tr>
      <td><a href="https://github.com/spcl/gemm_hls">Flexible Communication Avoiding Matrix Multiplication on FPGA with HLS</a></td>
      <td>Johannes de Fine Licht, Torsten Hoefler, ETH Zurich</td>
      <td>Alveo U250</td>
    </tr>
    <tr>
      <td><a href="https://github.com/KULeuven-COSIC/HEAT">FPGA Accelerated Homomoprhic Computation on AWS</a></td>
      <td>Furkan Turan, KU Leuven</td>
      <td>AWS F1</td>
    </tr>
    <tr>
      <td><a href="https://bitbucket.org/necst/xohw2020_fidelta_public">FPGA-based Incremental Delaunay Triangulation Acceleration - parallelized Delaunay Triangulation builder</a></td>
      <td>Alberto Giusti, Saverio Ricci, Marco D. Santambrogio, Politecnico Di Milano</td>
      <td>Alveo U200</td>
    </tr>
    <tr>
      <td><a href="https://bitbucket.org/necst/xohw2020_maeve_public">FPGA implementation of KMP algorithm</a></td>
      <td>Sofia Breschi, Beatrice Branchini, Marco D. Santambrogio, Politecnico Di Milano</td>
      <td>Alveo U200</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Xilinx/HPCG_FPGA">HPCG Benchmark on FPGA</a></td>
      <td>Xilinx Research</td>
      <td>Alveo U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/zistvan/Multes_for_Vitis_with_100Gbps_TCP-IP">Key-Value Store with user-defined processing (Multes)</a></td>
      <td>Zsolt Istvan, ITU Copenhagen (with help from Zhenhao He, ETH Zurich)</td>
      <td>Alveo U250 / U280</td>
    </tr>
    <tr>
      <td><a href="https://bitbucket.org/necst/xohw17_bibbidin-bobbidyboo_public/">N-body simulation</a></td>
      <td>Emanuele Del Sozzo, Marco Rabozzi, Marco Nanni, Prof. Marco Santambrogio, Politecnico Di Milano</td>
      <td>&nbsp;</td>
    </tr>
    <tr>
      <td><a href="https://github.com/spcl/nbody_hls">N-body simulation</a></td>
      <td>Johannes de Fine Licht ETH Zurich</td>
      <td>Alveo U250</td>
    </tr>
    <tr>
      <td><a href="https://github.com/abs-tudelft/octoray">OctoRay: Framework for Scalable FPGA Cluster Acceleration of Python Big Data Applications</a></td>
      <td>Jakoba Petri-König, Shashank Aggarwal, Joost Hoozemans, Zaid Al-Ars, Delft University of Technology</td>
      <td>Alveo U50 / U250 / U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/manuelburger/daceBLAS_demo">Portable Linear Algebra on FPGA using Data-Centric Parallel Programming</a></td>
      <td>Manuel Burger, Johannes de Fine Licht and Torsten Hoefler, ETH Zurich</td>
      <td>Alveo U250</td>
    </tr>
    <tr>
      <td><a href="https://github.com/inaccel/runtime/tree/Xilinx-MP/">Single-FPGA and Multi-FPGA ResNet50 / MobileNet Accelerators using FINN and InAccel Coral</a></td>
      <td>Tobias Alonso, Lucian Petrica, Mario Ruiz, Jakoba Petri-Koenig, Yaman Umuroglu, Ioannis Stamelos, Elias Koromilas, Michaela Blott, Kees Vissers</td>
      <td>Alveo U250 / U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/albertozeni/XDropXOHW-Public">X-drop on FPGA</a></td>
      <td>Alberto Zeni, Guido Walter Di Donato, Marco D. Santambrogio, Politecnico Di Milano</td>
      <td>U280</td>
    </tr>
    <tr>
      <td><a href="https://github.com/Xilinx/xup_vitis_network_example">Vitis Network Examples</a></td>
      <td>Mario Ruiz, XUP</td>
      <td>Alveo U50 / U250 / U280</td>
    </tr>
  </tbody>
</table>

## PYNQ examples

PYNQ Alveo examples can be found on the [PYNQ community](http://www.pynq.io/community.html).



---------------------------------------
<p align="center">Copyright&copy; 2022 AMD</p>
