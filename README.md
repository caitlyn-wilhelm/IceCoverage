# Plots and Figures for 2021 Wilhelm et. al Publication

Here are the plots and figures used in the 2021 Wilhelm et. al Publication on The Ice Coverage of Earth-like Planets Orbiting FGK Stars. We used [VPLanet](https://github.com/VirtualPlanetaryLaboratory/vplanet) to examine the formation of polar and equitorial ice and constucted contour plots to look at the range in which polar caps and ice belts are present. We looked at three different spectral classes of stars: K, G and F stars.
It is divided into two different types of simulations:
 - Static Cases (In these cases obliquity, eccentricity, and percession angles **are static**)
 - Dynamic Cases (The values for eccentricity, oblquity, and their amplitutes and periods **are randomly generated through uniform distribution**)

For the Static Cases there are a folder for each spectral type, and they are divided up by *starting eccentricity value*. So if you wanted to look for *Static K star simulation with eccentricity of 0.2* that would be **StaticCases/KDwarf/Ecc02**. For the Dynamic Cases, it divided by Case A-E which are shown in the table on the page for Dynamic Cases.

In each of those folders is the plot generated from the data, a list file with the data, and the VSPACE input file if you would like to examine the raw data by running the simulation on your own machine.

All of the plots use [Bigplanet](https://github.com/VirtualPlanetaryLaboratory/bigplanet), a data analysis suite I developed to aid in the large amount of data generated from the simulations. 

 **Note: To generate the raw data you must have VPLanet installed on your machine**
