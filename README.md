# Energy Consumption in Machine Learning & Deep Learning Models 

The exploratory project estimates and measures carbon emissions from various Machine Learning and deep learning datasets to quantify and analyze their impact.

# Installation

Download the project along with a code editor.
Use the terminal to navigate to the source folder. 

Create a virtual environment using `conda` for easier management of dependencies and packages. You can also follow the instructions on the [official conda website](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)

```
conda create --name codecarbon python=3.6
conda activate codecarbon
```

#### Install from PyPI repository
```
pip install codecarbon
```

#### Install from Conda repository

```
conda install -c codecarbon -c conda-forge codecarbon
```

This project requires **Python** and some of the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [tensorflow](https://www.tensorflow.org)

You can install them using 

```
pip install <packagename>
```

To run the code
```
python train.py
```

# About the Dataset 


# Data Visualization


 # Emissions - Red Wine


 
 # Emissions

| Algorithm | Dataset/ Link to code | Instance | Accuracy| Emissions Recorded in Joules* (average) |Emissions Recorded in kg* (average) |
| ------------- |------------- | ------------- | ------------- | ------------- | ------------- |
|Logistic Regression | [IRIS Dataset](https://github.com/blessinvarkey/EcoCoding/blob/main/iris-dataset/train.py)|50 | 95.56%|11322593948.720951 joules|1.2598084791716727e-07 kg |
| Logistic Regression | [ASD Screening](https://github.com/blessinvarkey/EcoCoding/blob/main/asd-dataset/train.py)  | 761  | 99.53% | 23098647146.30177 joules | 2.570071104209542e-07 kg | 
|Support Vector Machines | [IRIS Dataset](https://github.com/blessinvarkey/EcoCoding/blob/main/iris-dataset/train.py)| 50 | 97.78%|11020140817.496267 joules|1.226156029830599e-07 kg|
|K Nearest Neighbors | [IRIS Dataset](https://github.com/blessinvarkey/EcoCoding/blob/main/iris-dataset/train.py)| 50 | 93.33%|11183853335.19536 joules|1.2443715040300566e-07 kg |
| Adam Optimization | [Fashion MNIST](https://github.com/blessinvarkey/EcoCoding/blob/main/fashion-mnist/train.py)  | 70,000 | |52381696453822.83 joules (5 epochs)| |  


[↑ Back to top](https://github.com/blessinvarkey/EcoCoding#energy-consumption-in-machine-learning--deep-learning-models)
