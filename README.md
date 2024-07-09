> *In this repository, you will discover a data engineering and data science project, along with exercises leveraging open data sources as an integral component of the MADE ([Methods of Advanced Data Engineering](https://oss.cs.fau.de/teaching/specific/saki/)) course. The course was conducted by the FAU Chair for Open-Source Software (OSS) during the Summer 24' semester. This repository has been forked from the [jvalue-made-template](https://github.com/jvalue/made-template) repository.*

### Badges

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![CI/CD](https://github.com/AkashWelkin/made-template-fork-ss24/actions/workflows/project-workflow-check.yml/badge.svg)](https://github.com/AkashWelkin/made-template-fork-ss24/actions/workflows/project-workflow-check.yml)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
![](https://byob.yarr.is/AkashWelkin/made-template-fork-ss24/score_ex1) ![](https://byob.yarr.is/AkashWelkin/made-template-fork-ss24/score_ex2) ![](https://byob.yarr.is/AkashWelkin/made-template-fork-ss24/score_ex3) ![](https://byob.yarr.is/AkashWelkin/made-template-fork-ss24/score_ex4) ![](https://byob.yarr.is/AkashWelkin/made-template-fork-ss24/score_ex5)

## Exploring the Links Between Population Growth, CO2 Emissions, and Climate Change 🌎🔥🤷😬 🥴
![image](https://github.com/AkashWelkin/made-template-fork-ss24/assets/32175280/c3d8beaa-40d2-4816-9b9a-69b89c48e2df) <b>Image Credits:</b> Bryce Durbin / TechCrunch

### Overview
In recent years(this year 2024 also), problems like drought, severe heat waves, ever-increasing temperatures, heavy rainfall causing floods, seasonal cycle inconsistency, and hunger crises have beenescalating, highlighting the urgent need to understand the main causes of environmental damage. With the global population continuing to rise at an unpredictable rate, the increase in CO2 emissions fromforest fires, crop cultivation, pesticide manufacturing, and agrifood waste disposal presents a significant challenge to sustainable development and climate stability.To understand the impact of CO2 emissionsfrom all possible sources and the causes of increasing temperatures, deep data analysis has been performed on existing data to draw conclusions.

### Project Goal
How does population distribution and density influence the climate impact of CO2 emissions across different regions?

### Key project files and their functions:

- `project/pipeline.sh`: To run an automated ETL pipeline for the project.
- `project/tests.sh` : To run Unit Test cases.
- `project/DataAnalysis.ipynb` : To get insights of data.
- `project/ExtractData.py` : ETL python file.

### Pipeline Structure
![image](https://github.com/AkashWelkin/made-template-fork-ss24/assets/32175280/84b26bb9-1694-4352-97d1-7f51df1311b5)

### Run Pipeline Locally
1. Clone the github repo:
```
git clone https://github.com/AkashWelkin/made-template-fork-ss24.git
```
2. Create virtual environment:(Optional)
```
python -m venv pipeline
```
3. Activate the virtual environment:
```
.\pipeline\Scripts\activate
```
4. Install requirements:
```
pip install -r requirements.txt
```
5. Run the pipeline:
```
python ./project/pipeline.sh
```
This will start a virtual environment and create a SQL database out of data sources named `ClimateDB` in `\data` directory.

### Running Tests
Run the unit testcases:
```
python ./project/test.sh
```

Project analysis report [here](/project/analysis-report.pdf), [data report](/project/data-report.pdf) and [presentation report](/project/presentation-video.md)

### Final Note
To recapitulate, the above visualizations, analysis, and figures provide a thorough understanding of CO2emissions and the impact of an increasing population on climate. At a high level, this analysissuccessfully answers the objective question. To support my initial hypothesis, I have provided an in-depth analysis and shown the correlation among population, temperature, and emissions. However,there were a few points where temperature and emissions had an inverse relationship, which requiresadditional information or may indicate that the data had some flaws.

### Contributing

Contributions are always welcome!

## Feedback

If you have any feedback, please reach out to me at ay1820098@.gmail.com






