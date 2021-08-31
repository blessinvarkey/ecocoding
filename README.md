# Energy Consumption in Machine Learning Algorithms 

The project estimates and measures carbon emissions from various Machine Learning datasets to quantify and analyze their impact.

<br/>

- [About Green Coding](#about-Green-Coding)
- [About Code Carbon](#about-code-carbon)
- [Installation](https://github.com/blessinvarkey/Energy-Consumption-In-Machine-Learning/blob/main/README.md#installation)
- [IRIS-Dataset](https://github.com/blessinvarkey/Estimation-of-Energy-Consumption-In-Machine-Learning/blob/main/README.md#1-iris-dataset)
- [ASD-Screening with AQ-10 Questionaire](https://github.com/blessinvarkey/Estimation-of-Energy-Consumption-In-Machine-Learning/blob/main/README.md#2-autism-spectrum-quotient-aq-10--q-chat)

# About Green Coding 

Green coding is a term recently popularized for its environmental intentions and refers to programming code that is written to produce algorithms that have minimal energy consumption.

The projects in the repo uses code carbon taking into account the computing infrastructure, location, usage and running time


# About Code Carbon
CodeCarbon is a Python package for tracking the carbon emissions produced by various kinds of computer programs, from straightforward algorithms to deep neural networks. Visit their [repo](https://github.com/mlco2/codecarbon) to learn more.


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

This project requires **Python** and the following Python libraries installed:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org/)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

You can install them using 

```
pip install <write the packagename you want to download>
```

To run the code
```
python run.py
```


## 1. IRIS-Dataset
The IRIS data set contains 3 classes of 50 instances each, where each class refers to a type of iris plant. One class is linearly separable from the other 2; the latter are NOT linearly separable from each other. 

The details on the dataset can be found [here](https://archive.ics.uci.edu/ml/datasets/iris)

| Dataset | Repository | Algorithm(s) used | Emissions Recorded |
| ------------- |------------- | ------------- | ------------- | 
| IRIS Dataset  | UCI Machine Learning Repository | Logistic Regression, Support Vector Machines | |


### Sepal Length vs Width & Petal Length vs Width
|![Screenshot](images/Figure_1.png)|![Screenshot](images/Figure_2.png)|![Screenshot](images/Figure_3.png)|
| ------------- | ------------- |------------- |

[↑ Back to top](https://github.com/blessinvarkey/Estimation-of-Energy-Consumption-In-Machine-Learning/blob/main/README.md#datasets)

## 2. Autism Spectrum Quotient (AQ-10) | Q-CHAT
The Autism-Spectrum Quotient publisehed by Baron-Cohen, Wheelwright, Skinner, Martin, & Clubley was developed to assess how adults with 'normal' intelligence has the traits associated with autism spectrum conditions. According to Wikia, "the test consists of fifty statements, each of which is in a forced-choice format. Each question allows the subject to indicate "Definitely agree", "Slightly agree", "Slightly disagree" or "Definitely disagree". Approximately half the questions are worded to elicit an "agree" response from normal individuals, and half to elicit a "disagree" response. The subject scores one point for each question which is answered "autistically" either slightly or definitely." The questions cover five different domains associated with the autism spectrum: social skills; communication skills; imagination; attention to detail; and attention switching/tolerance of change.

| Dataset | Repository | Algorithm(s) used |  Emissions Recorded |
| ------------- |------------- | ------------- | ------------- | 
| ASD Screening  | UCI Machine Learning Repository | Logistic Regression | | 

According to the dataset, 'Yes' indicates that the individual is on the Autism Spectum and 'No' is indicated when the final score is less than or equal to 7. You can refer the questions from [here](https://www.nice.org.uk/guidance/cg142/resources/autism-spectrum-quotient-aq10-test-pdf-186582493).

### AQ-10 questions
A1 I often notice small sounds when others do not.  
A2 I usually concentrate more on the whole picture, rather than the small details.   
A3 I find it easy to do more than one thing at once.    
A4 If there is an interruption, I can switch back to what I was doing very quickly.    
A5 I find it easy to ‘read between the lines’ when someone is talking to me.   
A6 I know how to tell if someone listening to me is getting bored.   
A7 When I’m reading a story I find it difficult to work out the characters’ intentions.    
A8 I like to collect information about categories of things (e.g. types of car, types of bird, types of train, types of plant etc).    
A9 I find it easy to work out what someone is thinking or feeling just by looking at their face. 
A10 I find it difficult to work out people’s intentions


### Dataset 

The Dataset can be downloaded from the UCI Repository which is publicly available [here](https://archive.ics.uci.edu/ml/datasets/Autism+Screening+Adult). 

[↑ Back to top](https://github.com/blessinvarkey/Estimation-of-Energy-Consumption-In-Machine-Learning/blob/main/README.md#datasets)




[↑ Back to top](https://github.com/blessinvarkey/Estimation-of-Energy-Consumption-In-Machine-Learning/blob/main/README.md#datasets)
