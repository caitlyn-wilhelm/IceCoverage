# Chaotic Example

This plot shows a simulation in which the planet was orbiting a F dwarf star, but the planet's oblquity and ecentricity cycle causes the planet's climate to evolve chaotically, with epochs of both equitorial and polar ice. _Top left:_ Surface temperature. _Top middle left:_ Top of atmosphere albedo. _Bottom middle left:_ Ice sheet height. _Bottom left:_ Bedrock height (note the negative scale). _Top right:_ Annual average instellation. _Top middle right:_ Obliquity. _Bottom middle right:_ Eccentricity. _Bottom right:_ Climate obliquity precession parameter (COPP).

Below is a table of inital values for the case:

| Parameter              | Initial Value |
| ---------------------- | ------------- |
| Instellation           | 0.9953        |
| Obliquity              | 63.39         |
| Obliquity Amplitude    | 5.743         |
| Obliquity Period       | 48192         |
| Eccentricity           | 0.326         |
| Eccentricity Amplitude | 0.650         |
| Eccentricity Period    | 65292         |

This figure uses bigplanet's single simulation extraction process. To grab the data from a single simulation, first you must do the following in the _DynamicCases/CaseA/FDwarf/_ Directory.

Run vspace with the command:

```
vspace vspace.in
```

Then to offset the Obliquity and Ecc ossilation, run the helper script found in the DynamicCases directory:

```
python ../../rand_dist.py F_CaseA vspace.in
```

Now we only need one particular simulation to be ran, so let's _only_ run that particular case:

```
cd CaseA/FDwarf/F_CaseA/testrand_4407
vplanet vpl.in
```

Finally, now we come back to this directory, and run bigplanet to generate a bigplanet filtered file:

```
bigplanet bpl.in
```

This will generate a bpf file called _ChaoticExample.bpf_

Now that we have all the data, run the following code in the command line:

```
python makeplot.py <pdf | png>
```

This should generate the following plot:

![ChaoticExample](ChaoticExample.png)
