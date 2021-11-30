# Dynamic Cases 

This subdirectory conatins the files to generate the raw data for the "Dynamic Cases," as described in the paper. In each Case folder (labeled A-E) there is another folder for each of the spectral types (K Dwarf, G Dwarf, and F Dwarf) that contains the files required to perform the parameter sweeps with ``VPLanet``, ``vspace`` and ``multiplanet``, as well as compress the data into a ["bigplanet archive"](https://virtualplanetarylaboratory.github.io/bigplanet/filetypes.html) with ``bigplanet`` for later analysis. The details of each parameter sweep can be found in Table 2 of the publication.

To generate the data run the following commands  in each Case/SpectralType subdirectory:

```
 vspace vspace.in
```

This creates 10,000 subdirectories with initial conditions as prescribed in ``vspace.in``. However, in some cases ``vspace`` will pick an initial eccentricity value and eccentricity amplitude that will result in it dropping below 0 or growing larger than 1! To fix this issue, run the ``rand_dist.py`` script to prevent unphysical values:

```
python rand_dist.py vspace.in
```

Now you are ready to run ``VPLanet``! Since there are 10,000 simulations per spectral type per case, it is _recommended_ to use ``multi-planet``, which is provided by the VPLanet team to efficiently perform the simulations:

```
multi-planet vspace.in -c <number of cores>
```

This repo also relies on bigplanet for data storage and analysis. Because we generate so much data, plotting and analyzing the data from raw ASCII files spread across 10,000 subdirectories can be extremely tedious and time-consuming. ``bigplanet`` creates a single HDF5 file that contains the raw data and can be interrogated in <1/10th the time of reading the raw files. In this case, we run ``bigplanet`` to create a _bigplanet archive_, which contains all the raw data. Once the archive is created, you can safely delete the directories and save about 50% of your disk space. Note that ``bigplanet`` always performs an md5 checksum to ensure data integrity. To generate each bigplanet archive, execute the following command:

```
bigplanet bpl.in
```
This will create files calles X_CaseY.bpa, where X = F,G,K and Y = A,B,C,D,E, i.e. a unique file name for each spectral type-case combination. The other subdirectories in this repository assume that these files exist.

_XXX Missing many bpl.in files! and some vspace.in files!_
