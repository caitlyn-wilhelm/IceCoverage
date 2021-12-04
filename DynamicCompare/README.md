# Dynamic Case Comparison

This plot shows the outcomes of our 5 [Dynamic Cases](../DynamicCases), grouped by host star spectral type. See the paper for more information on the differences between these cases. Despite wide ranges of assumptions, the outcomes are relatively constant, suggesting that variations in albedo, rotational cycle, or orbital cycle do not strongly influence the climate states.

#### _These instructions assume you have completed the [Dynamic Cases](../DynamicCases) and have built the BigPlanet archive._

To categorize the planets, type the following:

```
python climate_type.py [FolderName]

```

which generates a file called _climateType.log_ that tabulates the different categories of ice state. To generate the figure, type the following code:

```
python makeplot.py <pdf | png>
```

to generate this plot:

![DynamicCompare](DynamicCompare.png)

#### _The exact values in your reproduction may vary slightly (1%) due to differences in random number generation._