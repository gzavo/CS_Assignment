# The title of papers pivotal to our knowledge:

Fantastic yeasts and where to find them: the hidden diversity of dimorphic fungal pathogens 

An analysis of the forces required to drag sheep over various surfaces

Correlation of continuous cardiac output measured by a pulmonary artery catheter versus impedance cardiography in ventilated patients

```python
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("istherecorrelation.csv", delimiter = ",")
plt.plot(data["Year"], data["WO x1000"] )
```
