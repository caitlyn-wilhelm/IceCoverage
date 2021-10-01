# Eccentricity Comparison

This plot shows the comparisons of ice belt regimes for planets orbiting K (top), G (middle), and F (bottom) as a function of eccentricity, with e = 0 solid, e = 0.1 dashed, e = 0.2 dotted, and e = 0.3 dash-dotted. Ice belts are unstable at e > 0.3 for G star planets and e > 0.1 for F star planets, thus the respective curves are omitted.

Prior to generating the plot, the simulations the following cases need to be completed, all of which are in the `StaticCases/` directory:

KStar/WarmStart
Kstar/Ecc01
Kstar/Ecc02
Kstar/Ecc03
Kstar/Ecc04

GStar/WarmStart
GStar/Ecc01
GStar/Ecc02

FStar/WarmStart
FStar/Ecc01

To run each of the parameter sweeps, cd into the directory and type `vspace vspace.in` This generates the 10,000 test cases that generates the figure. After that run multiplanet to run the simulations by typing `multiplanet vspace.in`. Once each of the simulations is completed (this will take some time), come back to this directory and generate the plot.

To generate the plot, type the following code:
```
python makeplot.py <pdf | png>
```

This should generate the plot:
![EccCompare](https://github.com/caitlyn-wilhelm/IceSheet/blob/master/EccCompare/EccCompare.png)
