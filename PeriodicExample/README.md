# Periodic Example

This plot shows a simulation in which the planet was oorbiting a G dwarf star, but the ice grown was periodic, resulting in seasonal ice growth on the polar caps and ice belts. *Top left:* Surface temperature. *Top middle left:* Top of atmosphere albedo. *Bottom middle left:* Ice sheet height. *Bottom left:* Bedrock height (note the negative scale). *Top right:* Annual average instellation. *Top middle right:* Obliquity. *Bottom middle right:* Eccentricity. *Bottom right:* Climate obliquity precession parameter (COPP).

Below is a table of inital values for the case:

| Parameter              | Initial Value  |
|------------------------|----------------|
| Instellation           | 0.9931         |
| Obliquity              | 52             |
| Obliquity Amplitude    | 50             |
| Obliquity Period       | 100000         |
| Eccentricity           | 0              |


To generate the plot, run the following code in the command line:
```
vplanet vpl.in
python makeplot.py <pdf | png>
```

This should generate the following plot:

![PeriodicCase](https://github.com/caitlyn-wilhelm/IceSheet/blob/master/PeriodicExample/PeriodicExample.png)
