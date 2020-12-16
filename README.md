Quantifying the treatment effects on prolonging the freshness of apples, bananas and avocados
=============================================================================================
#### MIDS W241 Fa2020
#### Bill Chung, Justin Trobec, Nobu Yamaguchi

### Table of Contents

* Introduction
* Experiment Design
* Analysis
* Conclusions
* Structure of This Repo
* Reproducing our Results
* Links and References

## Introduction

Reducing food waste is a global problem. United Nations set 17 sustainable development goals in 2015 and the goal No 12 is "Responsible consumption and production [1] [THE 17 GOALS | Sustainable Development](https://sdgs.un.org/goals). According to United Nations, 13.8% of food is lost in the supply chains in 2016. [2] [Goal 12 | Department of Economic and Social Affairs](https://sdgs.un.org/goals/goal12) Therefore, we can say that finding a good way to keep the food fresh for a long time is important for our lives.
There are many startups that tackle this global problem. A startup in the East Coast tries to find out the best timing to eat apples by measuring the ethylene gas. [3] [Strella Biotechnology – Fighting Food Waste](https://www.strellabiotech.com/) This startup has already raised $3.8M as of December 2020. [4] [Strella Biotechnology - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/strella-biotechnology)Another startup in the West Coast developed special coating technology which adds a layer of tasteless, odorless, plant-based protection on the surface of fruits and vegetables to keep them fresh for a long time.  [5] [Apeel | Food Gone Good](https://www.apeel.com/)This startup has raised $390M as of December 2020. [6] [Apeel Sciences - Crunchbase Company Profile & Funding](https://www.crunchbase.com/organization/apeel-sciences) These startups show that reducing food waste has a big business impact.
Moreover, several companies developed special containers which can keep the freshness of the food. Although those startups try to implement very complex methods, we can do something in much simpler way. Especially, people like very simple way to store foods in their home because they do not want to pay a lot of money for this problem and they do not want to continue complicated habits.

### Objective and hypothesis of the experiment
We came up with several simple fruit storage methods for this experiment.
The objective of our experiment is to evaluate the average treatment effect of different fruit storage methods in prolonging the freshness of fruits.  
Also, our hypothesis is that even when we stored fruits at a room temperature, how they are stored can affect the longevity of their freshness.

### Control groups and treatment groups

We used three fruits: avocados, bananas, and apples.

We summarize the control group and treatment group for each fruit.

* Avocados
	* Control: we left control avocados on the desk
	* Treatment: we kept treatment avocados in three ways for 8 days:
		* paper bags
		* plastic bags (ziplocks)
		* aluminum foil
* Bananas
	* Control: we left control bananas on the desk
	* Treatment: we left control bananas next to apples for 10 days
	(It is said that ethylene gas emitted from apples will accelerate the ripening process)
* Apples
	* Control: we left control apples upside down
	* Treatment: we left treatment apples upside up for 25 days.
    
    
    
    
    
    
    
    
----------------------------    
# Summary of meeting with Professor Hughes

- Advice. Make sure we talk about how the procedure can be used to measure for cancer spread. Other spatioal changes with respect to initial condition in the 
report and during the presentation.

## Changing experiment subject from apples to other fruits

### 1.	Avocado: random assignment
- 	`Control`: leave it is
- 	`Treatments`: Plastic bag, paper bag and plastic wrap
    - paper bag, T1
    - plastic bag, T2
    - plastic wrap, T3
-   Evaluate which treatment was more effective than the other.  See Problem set 4 part 5.4
-  Cut avocado 10 days later.
    - Take picture and develop cdf.  green to brown scale on the x-axis, and y ranges from 0 to 1. 
    - [LINK](https://www.schemecolor.com/green-with-brown-color-combination.php)
- Mad cow [LINK](https://www.mayoclinic.org/diseases-conditions/creutzfeldt-jakob-disease/diagnosis-treatment/drc-20371230#:~:text=Only%20a%20brain%20biopsy%20or,presence%20of%20Creutzfeldt%2DJakob%20disease.)
- **need to develop the computer vision system without knowing if the object is assigned to any group.**

### Banana: random assignment
-	`Control`: leave it as it is
-	`Treatments`: leave apple next it to see if leaving apple next it makes the bananas go bad sooner
-    Add anchor points in the paper during the observation in order to detect the center of the objects. 

### Apple: random assignment
- `Control`: upside up
- `Treatments`: upside up with banana
- Evaluate if the effect of leaving banana next to apple
-    Add anchor point in the paper during the observation. 










# MIDS W241 Final Project
### Experiment Process

#### Setup
- Buy organic apples (Fuji), 1 box (
- Draw a 5cm x 5cm box on a piece of paper.
- Write the apple's information 
  - day you're starting the experiment
  - apple ID
- Place the apple on the paper, leave in the same place over course of the experiment
- When you take a measurement:
  - draw a tick (do NOT touch apple!)
  - write down the temperature, humidity
  - take a picture (using camera phone)
