# Dynamic Cases (Monte Carlo simulations)

This is where the raw data for the Dynamic Cases are stored. In each Case folder (labeled A-E) there is another folder for each of the spectral types (K Dwarf,G Dwarf, and F Dwarf). In each of the spectral case folder is the source files as well as the `vspace.in` file which is needed for running VPLanet. So if you wanted to run Case A G Star it would be in *CaseA/GDwarf*.

Each Case is explained in depth below:

In Case A, our baseline model, we assume all albedos have the values shown in Table 1 and the amplitudes and periods of the eccentrisity and obliquity oscillations are chosen to represent typical values for the terrestrial planets in our Solar System.

In Case B, we allowed the albedos to take values within &pm;0.05 the values (with a uniform distribution) from Table 1, *ie* the general trend in albedo and effective global temperature is preserved, but some variations in ice albedo are permitted. The external forcing oscillations are the same as in Case A. 

In Case C, the ice albedos for all planets, regardless of host star spectral type, are allowed to vary uniformly between 0.55 and 0.75 to further evaluate variable albedo, while the external forcing periods are shifted to larger values. 

In Case D, the albedos are the same as Case C, but the external forcing parameters have normally distributed periods. 

In Case E, the values are the same as Case A but we changed the rotation rate to vary uniformly between 0.5 to 5 days, which changes the evolution of precession angle.

To generate the data, you **MUST** have VPLanet installed and vspace, multi-planet and bigplanet setup completed.
To get started, run `vspace vspace.in` in the command line while in the folder for that particular spectral star. This creates all the simulation folders to run.
Then, run the rand_dist.py file with `python rand_dist.py vspace.in`. This script changes the values of the eccentricity amplitude to be the proper values.
Now you are ready to run VPLanet! Since there are 10,000 simulations per spectral type per case, it is *recommended* to use multi-planet, which can be done by typing the following:

```
multi-planet vspace.in <number of cores>
```

Because of the seed in the vspace.in file, you should generate identical data to that in Wilhelm et al. 2021. Once multi-planet has finished, run bigplanet to grab the data needed to plot the figures later. Run the following command in the command line:
```
bigplanet bpl.in
```
