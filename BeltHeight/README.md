# Belt Height Plot

This plot shows the range and average ice heights of ice belts as a function of latitude for stars orbiting F (top), G (middle) and K (bottom) dwarf stars. Light grey curves show 100 randomly selected individual simulations, while black shows the average of all simulations that concluded with an ice belts. Although the averages are all symmetric about the equator, some individual ice belts are significantly displaced.

#### _These instructions assume you have completed the [Dynamic Cases](../DynamicCases) and have built the bigplanet archive._

To generate the plot, execute the following command:

```
python makeplot.py <pdf | png>
```
where the two arguments after makeplot.py set the output to either a pdf or png. This should generate the plot:

![BeltHeight](BeltHeight.png)

#### _The exact values in your reproduction may vary slightly (1%) due to differences in random number generation._
