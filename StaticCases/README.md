# Static Cases

This is where the raw data for the Static Cases are stored. It is divided byt spectral type and then what is being changed. For example, inside the GDwarf/ Folder, there are the following folders:

WarmStart/

ColdStart/

Ecc01/

Ecc02/

In each of those folders is the source files as well as the `vspace.in` file which is needed for running VPLanet.

To generate the data, you **MUST** have VPLanet installed and both vspace and multi-planet setup completed.
To get started, run the follwing in WarmStart/ and ColdStart/ folders:

```
vspace vspace.in
```

This creates all the simulation folders to run.
Now you are ready to run VPLanet! Since there are 10,000 simulations per spectral type per case, it is _recommended_ to use multiplanet, which can be done by typing the following:

```
multiplanet vspace.in <number of cores>
```

After each simulation has completed, type the following to generate a bigplanet archive file, which will be used for plotting purposes:

```
bigplanet bpl.in -a
```

Once that's done, type the following in the Spectral type folder (GDwarf/ for example) to generate the figure:

```
python makeplot.py <pdf | png>
```
