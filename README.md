# CyanoGenes v.0.1
![alt text](https://github.com/ginerorama/CyanoGenes/blob/master/images/Logo.gif)
<br />
<br />
CyanoGenes is an user-friendly gene annotation tool for cyanobacteria developed in Python using a Tkinter graphical interface. CyanoGenes uses a list of genes to annotate and calculate functional categories enrinchment according to Cyanobase classification.





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
<img src="https://github.com/ginerorama/CyanoGenes/blob/master/images/Input1.png" width="650" height="480">
<br />
<br />


## Parameters
<br />
All these parameters appears in the Tkinter GUI of PrimerGenerator
<br /><br />

`primer size:` desired size of primers that PrimerGenerators have to find.

`max GC percentage:` maximum % GC admited for primers. 

`min GC percentage:` minimun % GC admited for primers (have to be 1 below to max GC value). 

`QPCR checkbox:` if check it, PrimerGenerators will find a pair of primers that amplify a band of size
				between the maximum and minimum size set for the amplicon.  
				

`max size for amplicon:` maximun size of amplicon that should be amplified in the QPCR. 

`min size for amplicon:` minimum size of amplicon that should be amplified in the QPCR. 	

<br /><br />
*important note: difference between max and min size for amplicon have to be greater than primer size

## Ouput

<br />
PrimergGnerators generates a txt file as output with all the forwards and reverse primers listed for all
the genes presents in the fasta/multifasta file. 
