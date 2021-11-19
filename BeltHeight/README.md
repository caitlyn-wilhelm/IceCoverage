# Belt Height Plot

This plot shows the range and average ice heights of ice belts as a function of latitude for stars orbiting F (top), G (middle) and K (bottom) dwarf stars. Note the different scales of the x-axes. Light grey curves show 100 randomly selected individual simulations, while black shows the average of all simulates that concluded with an ice belts. Although the averages are all symmetric about the equator, some individual ice belts are significantly displaced.

This plot uses bigplanet's filtered file feature. To generate the bigplanet filtered file, type the following in each of spectral type folders in the _DynamicCases/CaseA/_ folder:

```
bigplanet bpl.in
```

That should generate a _Test.bpf_ file. Once that has completed, to generate the plot type the following code:

```
python makeplot.py <pdf | png>
```

This should generate the plot:
![BeltHeight](BeltHeight.png)
