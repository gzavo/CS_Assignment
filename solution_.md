# Relevant Papers
- Van Dyke, M.C.C., Teixeira, M.M. and Barker, B.M. (2019) **'Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens'** Current Opinion in Microbiology, 52, pp. 55–63. https://doi.org/10.1016/j.mib.2019.05.002.
- Harvey, J. et al. (2002) **'An analysis of the forces required to drag sheep over various surfaces'** Applied Ergonomics [Preprint]. https://doi.org/10.1016/s0003-6870(02)00071-6.
- Ziegler, Daniel, Tellez, M., Hess, D. and Dipprey, T. (2004). **'Correlation of continuous cardiac output measured by a pulmonary artery catheter versus impedance cardiography in ventilated patients.'** Critical Care. 8. 1-2. 10.1186/cc2525.

# Plots

The data found in the file _istherecorrelation.csv_ includes a table with 3 columns: _Year_, _WO [x1000]_ and _NL Beer consumption [x1000 hectoliter]_.

The contents are plotted here for convenience:

|Year|WO [x1000]|NL Beer consumption [x1000 hectoliter]|
|----|----------|--------------------------------------|
|2006|205,9     |11402                                 |
|2007|208,6     |11492                                 |
|2008|212,7     |11450                                 |
|2009|220,5     |11502                                 |
|2010|233,2     |11474                                 |
|2011|242,4     |11480                                 |
|2012|245,4     |11452                                 |
|2013|241,4     |11484                                 |
|2014|250,2     |11555                                 |
|2015|255,7     |11601                                 |
|2016|261,2     |11731                                 |
|2017|267,9     |11862                                 |
|2018|280,1     |12048                                 |

The _Year_ category indicates the year of the observation. _WO [x1000]_ is interpreted as the number of academic university graduates in the Netherlands (according to the Dutch educational system) for the corresponding year, given in thousands. _NL Beer consumption [x1000 hectoliter]_ is interpreted, as the name suggests, as the amount of consumed beer in the Netherlands measured in thousands of hectoliters.

The second and third category are plotted separately against the years to see their development over time. The name of the file suggests an inquiry into the correlation of the variables, so in the second set of plots we examine a scatterplot of the number of graduates versus the beer consumption. Finally, a linear regression through this scatterplot is visualized to obtain a better understanding of this correlation.

The results show a substantial positive linear correlation between beer drinking and the number of academic graduates.

![alt text](https://github.com/mboyan/CS_Assignment/blob/main/data_plots.jpg?raw=true)
