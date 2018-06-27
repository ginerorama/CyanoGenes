# CyanoGenes v.0.1
![alt text](https://github.com/ginerorama/CyanoGenes/blob/master/images/Logo.gif)
<br />
<br />
CyanoGenes is an user-friendly gene annotation tool for cyanobacteria developed in Python using a Tkinter graphical interface. CyanoGenes uses a list of genes to annotate and calculate functional categories enrinchment according to Cyanobase classification. Functional categories enrichment analysis is calculated using a t-test analysis. To date only the Synechocystis sp. PCC 6803 genome is available for CyanoGenes analysis, although more cyanobacteria will be incorporated soon.





<br />
<br />
<p align="center">
<img src="https://github.com/ginerorama/CyanoGenes/blob/master/images/picture1.png" width="330" height="420">
<br />
<br />

## Requires
	
Tkinter, Numpy and Scipy modules

<br />

<br />

## Usage
Install CyanoGenes using cloning git button and type in your console:
<br />

`python CyanoGenes.py`

<br />
CyanoGenes can be run in UNIX and MAC systems with python 2.7. GUI is optimized for Tkinter in MacOSX, weird aspects for main Tkinter window can be observed in UNIX systems.
<br />


## Input file
<br />


CyanoGenes requieres a txt file containing all the orfs in a single column. CyanoGenes admits both Gene symbols and orfs (petE; sll0199). 
<br /><br />


<p align="center">
<img src="https://github.com/ginerorama/CyanoGenes/blob/master/images/Input1.png" width="690" height="480">
<br />
<br />


## Parameters
<br />
CyanoGenes only need set the desired p-value for the t-test used for gene set enrichment analysis (By default 0.05). It is also neccesary to indicate the path to the orf list txt file by clicking in the Browse buttom.
<br /><br />



## Ouput

<br />
CyanoGenes generates a txt file as output with all three different sections that could be opened in excel making easy the data analysis:

1) Gene annotation section: which contains the GeneID, Gene Symbol, gene Description and Functional Category.
2) Gene set enrichment analysis: Functional Categories that were enriched in your set of genes according to t-test analysis.
3) Functional Categories description: complete analysis of gene distribution along the funcional categories, including number of genes and percentages.
