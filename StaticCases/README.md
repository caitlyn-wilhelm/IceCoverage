# Static Cases

This directory contains the files to generate the raw data for the "Static Cases" as described in the paper. The data are labeled by host star spectral type (F, G, K), initial ice state (ColdStart, WarmStart), and eccentricity (ecc). This directory also contains instructions for generating Figures 3-5 in the paper.

Each of the subsubfolders contains the ``vspace.in`` file that generates the each trial's initial conditions:

```
vspace vspace.in
```

To simulate the systems across a certain number of cores, type the following:

```
multiplanet vspace.in -c <number of cores>
```

After all simulations have completed, type the following to generate a ["bigplanet archive"](https://virtualplanetarylaboratory.github.io/bigplanet/filetypes.html), which will be used for plotting purposes:

```
bigplanet bpl.in -a
```

Once that's done, type the following in the spectral type folder (GDwarf, for example) to generate the figure:

```
python makeplot.py <pdf | png>
```
where the two arguments after makeplot.py set the output to either a pdf or png.