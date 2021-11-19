# Dynamic Case Comparison

This plot shows the outcomes of our 5 Cases of evolving planets dubbed 'Dynamic Cases', grouped by host star spectral type. Despite wide ranges of assumptions, the outcomes are relatively constant, suggesting that variations in albedo, rotational cycle, or orbital cycle do not strongly influence the climate states.

To generate the data run the following in each of the Spectral Types for each Case in the DynamicCases/ Directory:

```
vspace vspace.in
```

Then to offset the Obliquity and Ecc ossilation, run the rand*dist helper script found in the DynamicCases directory \_where folder name is the name of the folder generated from vspace*:

```
python ../../rand_dist.py [FolderName] vspace.in
```

Then run multi-planet:

```
multiplanet vspace.in
```

Once all of the cases have finished (this might take some time), run the climate script in the DynamicCases Directory, _where folder name is the name of the folder generated from vspace_:

```
python climate_type.py [FolderName]

```

The numbers in the climateType.log file should match that of the numbers in the figure.

To generate the plot, type the following code:

```
python makeplot.py <pdf | png>
```

This should generate the plot:
![DynamicCompare](DynamicCompare.png)
