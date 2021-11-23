Plots and Figures for 
# The Ice Coverage of Earth-like Planets Orbiting FGK Stars

This repository contains the scripts to generate the data and figures used in the  "The Ice Coverage of Earth-like Planets Orbiting FGK Stars" by Wilhelm et al. (2021), accepted to the Planetary Science Journal. We used [VPLanet](https://github.com/VirtualPlanetaryLaboratory/vplanet) v2.1 to simulate the formation of polar and equitorial ice of "Earth-like planets" orbiting F, G, and K type stars for a range of orbital and rotational parameters. 

We performed two qualitatively different types of simulations:

- [Static Cases](StaticCases) in which the obliquity, eccentricity, and precession angle of the planets are held fixed.
- [Dynamic Cases](DynamicCases) in which the eccentricity and obliquity vary sinusoidally and the precession angle is calculated self-consistently. The  amplitudes and periods of eccentricity and obliquity are randomly generated with various assumptions.

These parameter sweeps were performed with [vspace](https://github.com/VirtualPlanetaryLaboratory/vspace) and [multiplanet](https://github.com/VirtualPlanetaryLaboratory/multiplanet), which are Python codes that generate initial conditions for VPLanet simulations and then perform those simulations across multiple cores, respectively. We then used [bigplanet](https://github.com/VirtualPlanetaryLaboratory/bigplanet) to compress and organize the data for analysis and long-term storage.

#### _The instructions presented here assume you have installed ``vplanet``, ``vspace``, ``multiplanet``, and ``bigplanet``.

To reproduce the results in Wilhelm et al., first follow the instructions in the [StaticCases](StaticCases) and [DynamicCases](DynamicCases) directories to generate the raw data. You can then reproduce the figures by following the instructions in the other subdirectories.
