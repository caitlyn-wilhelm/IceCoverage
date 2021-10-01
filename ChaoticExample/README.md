# Chaotic Example

This plot shows a simulation in which the planet was orbiting a F dwarf star, but the planet's oblquity and ecentricity cycle causes the planet's climate to evolve chaotically, with epochs of both equitorial and polar ice. *Top left:* Surface temperature. *Top middle left:* Top of atmosphere albedo. *Bottom middle left:* Ice sheet height. *Bottom left:* Bedrock height (note the negative scale). *Top right:* Annual average instellation. *Top middle right:* Obliquity. *Bottom middle right:* Eccentricity. *Bottom right:* Climate obliquity precession parameter (COPP).

Below is a table of inital values for the case:

| Parameter              | Initial Value  |
|------------------------|----------------|
| Instellation           | 0.9953         |
| Obliquity              | 63.39          |
| Obliquity Amplitude    | 5.743          |
| Obliquity Period       | 48192          |
| Eccentricity           | 0.326          |
| Eccentricity Amplitude | 0.650          |
| Eccentricity Period    | 65292          |

To generate the plot, run the following code in the command line:
```
vplanet vpl.in
python makeplot.py <pdf | png>
```

This should generate the following plot:

![PeriodicCase](https://github.com/caitlyn-wilhelm/IceSheet/blob/master/ChaoticExample/ChaoticExample.png)
