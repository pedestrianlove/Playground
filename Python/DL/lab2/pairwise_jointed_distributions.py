import os
import matplotlib.pyplot as plot
import seaborn
import pandas

interested_data = pandas.read_csv (
        'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data', 
        header = None
)

interested_data.columns = [
        'Class label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash',
        'Magnesium', 'Total phenols', 'Flavanoids', 'Nonflavanoid phenols',
        'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
        'Prolinee'
]

X = interested_data.drop ('Class label', axis = 'columns')
Y = interested_data['Class label']

print (interested_data.head ())
seaborn.set (style = 'whitegrid', context = 'notebook')
seaborn.pairplot (interested_data, hue = 'Class label', height = 2.5)   #FIXME Singular matrix error
plot.tight_layout ()
if not os.path.exists ('./output') :
	os.makedirs ('./output')
plot.savefig ('./output/fig-wine-scatter.png', dpi = 300)
plot.show ()

