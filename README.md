Quantifying the treatment effects on prolonging the freshness of apples, bananas and avocados
=============================================================================================
#### MIDS W241 Fa2020
#### Bill Chung, Justin Trobec, Nobu Yamaguchi

### Table of Contents

* [Introduction](#introduction)
* [Experiment Design](#experiment_design)
* [Analysis](#analysis)
* [Conclusions](#conclusions)
* [Structure of This Repo](#structure_of_this_repo)
* [Reproducing our Results](#reproducing_our_results)
* [Links and References](#links_and_references)

## Introduction <a name='introduction' />

Reducing food waste is a global problem. United Nations set 17 sustainable development goals in 2015 and the goal No 12 is "Responsible consumption and production [1](#ref1). According to United Nations, 13.8% of food is lost in the supply chains in 2016 [2](#ref2). Therefore, we can say that finding a good way to keep the food fresh for a long time is important for our lives.

There are many startups that tackle this global problem. A startup in the East Coast tries to find out the best timing to eat apples by measuring the ethylene gas [3](#ref3). This startup has already raised $3.8M as of December 2020 [4](#ref4). Another startup in the West Coast developed special coating technology which adds a layer of tasteless, odorless, plant-based protection on the surface of fruits and vegetables to keep them fresh for a long time [5](#ref5). This startup has raised $390M as of December 2020 [6](#ref6). These startups show that reducing food waste has a big business impact.
Moreover, several companies developed special containers which can keep the freshness of the food. Although those startups try to implement very complex methods, we can do something in much simpler way. Especially, people like very simple way to store foods in their home because they do not want to pay a lot of money for this problem and they do not want to continue complicated habits.
    
## Experiment Design <a name='experiment_design' />

### Objective and hypothesis of the experiment
The objective of our experiment is to evaluate the average treatment effect of different fruit storage methods in prolonging the freshness of fruits. Our hypothesis is that even when we stored fruits at a room temperature, how they are stored can affect the longevity of their freshness. We came up with several simple fruit storage methods for this project, and ran multiple experiments with a variety of fruits to evaluate them.

### Measuring the freshness of fruit
Ideally we would have a simple device and metric that would allow us to evaluate the freshness of a given piece of fruit. Unfortunately, freshness is more of an objective, multidimensional concept. In order to operationalize freshness, we focused on the appearance of visible blemishes on the skin of the fruit under experiment. This was for two reasons: first, we found that many of the common issues with fruit storage manifested in such dark blemishes [7](#ref7); and second, there is much evidence that consumers and buyers are extrememly sensitive to visible blemishes, and will often reject fruit based on its appearance.

### Experiments
We ran multiple experiments, and each of us ran a separate block per experiment.

#### Pre-experiment: Apples
Our first experiment was with apples. We purchased organic apples from Costco. Each apple was assigned an ID, and then randomized into control or treatment. Apples in the control group were placed upside down, and apples in the treatment group right side up. Every day, we took a picture of each apple, and recorded the temperature and humidity of the room on that day.

It was our intention to process the images of the apples to quantify the appearance of blemishes, and compare across treatment and control. However, we found that apples can stay out for a long time (> 23 days) without much visible change. We decided to use this as a learning experience, and focus on fruits better known for rapid browning.

#### Experiment 2:
Our second experiment was on bananas. Again, we purchased bananas, assigned them IDs, and then randomized them 50/50 into treatment and control. Control bananas were set by themselves, and treatment bananas were set near an apple. Apples emit ethylene gas, which is a ripening agent, and we wanted to measure the causal effect of close proximit apples on ripening. We took images of the bananas every day for 10 days, recorded temperature and humidity on those days, and then stopped.

#### Experiments 3/4:
Our final experiments were with avocados. We wanted to see if wrapping avocados in various ways caused them to last any longer. We purchased avocados, and randomized them into control and treatment groups as before. Control avocados were left unwrapped. For treatment, Bill wrapped his avocados in a paper bag, Nobu put his in a plastic bag, and Justin wrapped his avocados in foil. The avocados were then left alone for ten days. On the tenth day, all the avocados were cut and we took pictures of each avocado.

### Randomization
Randomization is very simple: after we purchase the fruit, each item is given an ID, then we use a simple R sample() call to randomize assignment to treatment/control.

We found no indicators that would lead us to believe randomization was faulty. For example, if we look at the covariate ‘weight’ prior to experimentation, we see similar distributions.

Experiment power calculations are performed in the [power_avocado.Rmd](src/R/power_avocado.Rmd) and [power_banana.Rmd](src/R/power_banana.Rmd) files.

## Analysis <a name='analysis' />

For each experiment, we did analysis in two parts. The first part involved converting images into Hue/Value/Saturation format, and varying the hue while other values stayed fixed. This allowed us to separate out light and dark parts of the fruits. We evaluated this separation in two ways. For bananas, we watched how the area of darkness changed over time. We called the day that it turned more dark the measure d_turn. For avocados, since we only took one image, we called the hue at which the percentage of black in the image abruptly increased the hue turn. We used change detection algorithms (CUMSUM and BCP) to identify these points.

Our results did reveal some significance in different avocado blocks between treatment and control. However, we observed that in treatment, the block using plastic bags were still inedible inspite of insignificant darkening. They had become mushy and grown mold on the outside.

Please see the [banana](Data_cleaning_Banana.pdf) and [avocado](Data_cleaning_Avocado.pdf) documents for a walkthrough of the analysis and detailed results.

## Conclusions <a name='conclusions' />

For charts of our analyzed data and accompanying images, please see our [final presentation](media/final_presentation/Final Presentation.pdf).

* A single value response may not be able to capture the treatment effect that you wish to capture.
* Rather than using a scalar value, using a vector or hyperplane can a solution.
* When you buy avocado, wrapping in a paper bag or foil can help. Don’t put them inside a plastic bag
* When you buy apple, you can leave it at room temperature for a long time.

## Structure of This Repo
<a name='structure_of_this_repo' />

```
├───data (contains raw images we gathered during the experiments)
│   ├───B
│   │   ├───experiment1
│   │   ├───experiment2
│   │   ├───experiment3
│   │   └───experiment4
│   ├───J
│   │   ├───experiment1
│   │   ├───experiment2
│   │   └───experiment3
│   └───N
│       ├───experiment1
│       ├───experiment3
│       └───experiment4
├───media (contains images and media we used for reports and presentations)
└───src (contains source code and notebooks we used for processing and analysis)
    ├───notebooks
    ├───python
    └───R     
├───README.md  (this file; an explanation of our experiment and results)
```

## Reproducing our Results
<a name='reproducing_our_results' />
The `data` folder contains all the images we took for the experiments, along with csv files containing the covariates we recorded. We used pieces of 8 1/2x11 paper divided into quarters to keep our subjects organized, each square labeled with the subject ID. The more consistent one can make the picture taking process, the easier we believe subsequent analysis will be.

For the avocado experiment, the [process_avocados.py](https://github.com/jtrobec/mids-w241-fa2020-fp/blob/main/src/python/process_avocados.py) file can be modified to process new avocado images. The subject names and paths in lines 12-18 must be updated to point to the new images, but once that is done simply executing the script using `python process_avocados.py` will generate the table of blackness percentages at varying hues. The [Data_cleaning_avocado.Rmd](https://github.com/jtrobec/mids-w241-fa2020-fp/blob/main/src/R/Data_cleaning_Avocado.Rmd) file can use the resulting CSV and run our analysis to calculate hue_turn and significance using the KS test.

For bananas, the [code_banana_calculation.ipynb](https://github.com/jtrobec/mids-w241-fa2020-fp/blob/main/src/notebooks/code_banana_calculation.ipynb) file can be used to process the banana images into their day turn values, and the [Data_cleaning_banana.Rmd](https://github.com/jtrobec/mids-w241-fa2020-fp/blob/main/src/R/Data_cleaning_banana.Rmd) file can use the resulting CSV and run our analysis.

## Links and References
<a name='links_and_references' />

1. [THE 17 GOALS | Sustainable Development](https://sdgs.un.org/goals) <a name='ref1' />
2. [Goal 12 | Department of Economic and Social Affairs](https://sdgs.un.org/goals/goal12) <a name='ref2' />  
3. [Strella Biotechnology – Fighting Food Waste](https://www.strellabiotech.com/) <a name='ref3' />  
4. [Strella Biotechnology - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/strella-biotechnology) <a name='ref4' />
5. [Apeel | Food Gone Good](https://www.apeel.com/) <a name='ref5' />
6. [Apeel Sciences - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/apeel-sciences) <a name='ref6' />
7. [Fruit storage disorders](https://extension.umaine.edu/fruit/harvest-and-storage-of-tree-fruits/storage-disorders/) <a name='ref7' />
