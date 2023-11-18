---

# Analysis of a Wind Turbine 

---

**Author:** Chung Anthony, Gouders Louis, Lambotte Augustin, Laridon Amaury

Project done for the part B of the *LENVI2007-Renewable Energy Sources* courses. 

**Goal** :  

- Based on the 15-Megawatt Offshore Reference Wind Turbine and from wind data we have to derive the annual energy production and the load factor. 
- Understand the algorithm of the BEM and explain it in the form of a pseudo-code. 
- Apply the BEM algorithm to estimate the torsque and power of the 15MW turbine at selected wind speeds and look at the induction factors obtained. 
	- Compare the calculated values with the actual torque/power curves and comment on the hypotheses, simplifications, etc. 

**Structure of the files :**

- The *Data* folder contains the weather data files needed for the annual energy production and load factor computation.

- The *Documentation* folder contains all the relevant references for the project.

- The *BEM* folder contains the algorithm's script for the Blade Element Theory used for computations of the flow and turbine interactions.

	- *BEM.py* and *NREL_5MW.py* are given script made by Romain Debroeyer. The first is a traduction of the BEM alogorithm while the second one is an application on the NREL 5MW Wind Turbine.

	- The *Project.ipynb* notebook contains an explanation of the BEM algorithm and its implementation as well as the application on the IEA 15 MW Wind Turbine. We also made the computations for the annual energy production and load factor in this notebook. 

