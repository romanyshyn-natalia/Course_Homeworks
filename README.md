# Project_name: MEDex
Final project of Programming Basics course at Ukrainian Catholic University.
# Description:
With the rapid growth of electronic health records (EHRs), it is wonderful that we are able to collect information and knowledge from EHRs to support automated systems at the point of care and to enable secondary use of EHRs for clinical research.
<br>
The MEDex aims to process raw medical reports and extract specific named entities:
* ID
* Admission Date
* Discharge Date
* Age
* Gender
* Medications
* Diseases

<br>
The results of the program are written to a json file with named entities as keys and lists with extracted data.
Also, there is an example of Exploratory Analysis of extracted medical information with interactive plots and charts. You can try it or just use extracted dataset for your own research work. All the information about the process of developing that project and research is available on the project's wiki. 

# Table of Contents:

Wiki pages:                                                                          |
------------------------------------------------------------------------------------ |
  [Homework0](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework0) |
  [Homework1](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework1) |     
  [Homework2](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework2) |
  [Homework3](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework3) |
  [Homework4](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework4) |
  [Homework5](https://github.com/romanyshyn-natalia/Course_Homeworks/wiki/Homework5) |
  
  ### Main modules:
  * [RecordADT.py](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/modules/RecordADT.py) - realised abstarct data type for extracting named entities, based on [linkedQueue.py](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/modules/linkedQueue.py) and [abstarct_collection.py](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/modules/abstract_collection.py).
  * [data_analysis.ipynb](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/modules/data_analysis.ipynb) notebook with my example of exploring collected medical information, due to the fact that there are interactive plots, you have to switch to nbviewer on GitHub to fully play with charts.

## Data:
For this program use n2c2 NLP Research Data Sets, it is unstructured notes from the Research Patient Data Repository at Partners Healthcare. Datasets are free to use, but you have to get access to it, [register here](https://portal.dbmi.hms.harvard.edu/projects/n2c2-nlp/). 
<br>
Input Data is raw, unstructured medical report in plaintext format. Some examples of medical reports you can [find](https://github.com/romanyshyn-natalia/Course_Homeworks/tree/master/docs) at this folder. 
<br>
Output data is json file with extracted entities, check for [example](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/tests/report1.json).

## Usage:
There are two main usage purposes for this project:
* actual extracting named entities for your reports, which produce an easy and fast method for getting needed information.
* using extracted dataset for your own research in the medical field or whatever reason, you are free to use data extracted by me, it is available [here](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/modules/results.csv) 

## Example:
You can test my program using the Python module and report example, that is located at the test folder. After running the main program you will obtain extracted [results](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/tests/report1.json) in json file.
Also, you are highly welcomed to look through my result's dataset exploring:
1) With the help of this pie chart, I obtained a general gender distribution among patients in a convenient visual format:
![](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/docs/gender_distribution.png)  
2) Also, interesting for me was age distrubution among male and female patients:
![](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/docs/age_by_gender.png)
3) The most valuable information is the most common diseases and accordingly medications that can cure or alleviate it:
![](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/docs/common_diseases.png)
![](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/docs/most_common_drugs.png)

## Instalattion:
All required Python libs are available in [requirements.txt](https://github.com/romanyshyn-natalia/Course_Homeworks/blob/master/requirements.txt). So, for running this program you have to type in your cmd:
```
pip install requirements.txt
```
Need to admit, that you are supposed  to install `sciSpacy` lib's model `en_ner_bc5cdr_md`, using provided [link](https://s3-us-west-2.amazonaws.com/ai2-s2-scispacy/releases/v0.2.4/en_ner_bc5cdr_md-0.2.4.tar.gz).

## Credits:
* Natalia Romanyshyn, Ukrainian Catholic University, 2020
