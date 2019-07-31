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

X = interested_data.drop ('Class label', 1)
Y = interested_data['Class label']

print (interested_data)
