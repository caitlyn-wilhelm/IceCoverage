# Dynamic Evolution Example

This plot shows a stable Icebelt from the Dynamic Cases, specifically the Case A G Dwarf. _Top left:_ Surface temperature. _Top middle left:_ Top of atmosphere albedo. _Bottom middle left:_ Ice sheet height. _Bottom left:_ Bedrock height (note the negative scale). _Top right:_ Annual average instellation. _Top middle right:_ Obliquity. _Bottom middle right:_ Eccentricity. _Bottom right:_ Climate obliquity precession parameter (COPP).

Below is a table of inital values for the case:

| Parameter              | Initial Value |
| ---------------------- | ------------- |
| Instellation           | 0.9405        |
| Obliquity              | 90.5          |
| Obliquity Amplitude    | 26.5          |
| Obliquity Period       | 53,325        |
| Eccentricity           | 0.077         |
| Eccentricity Amplitude | 0.129         |
| Eccentricity Period    | 44656         |

This figure uses bigplanet's single simulation extraction process. To grab the data from a single simulation, first you must do the following in the _DynamicCases/CaseA/GDwarf/_ Directory.

Run vspace with the command:

```
vspace vspace.in
```

Then to offset the Obliquity and Ecc ossilation, run the helper script found in the DynamicCases directory:

```
python ../../rand_dist.py G_CaseA vspace.in
```

Now we only need one particular simulation to be ran, so let's _only_ run that particular case:

```
cd CaseA/GDwarf/G_CaseA/testrand_0251
vplanet vpl.in
```

Finally, now we come back to this directory, and run bigplanet to generate a bigplanet filtered file:

```
bigplanet bpl.in
```

This will generate a bpf file called _DynamicExample.bpf_

Now that we have all the data, run the following code in the command line:

```
python makeplot.py <pdf | png>
```

This should generate the following plot:

![DynamicExample](DynamicExample.png)
