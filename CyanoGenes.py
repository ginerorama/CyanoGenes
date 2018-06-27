#!/usr/bin/python
# primergenerator v0.2 
#MIT License
#
#Copyright (c) 2018 Joaquin Giner Lamia
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.




##########################################################################
#
#                   Import  Modules
#
##########################################################################
from __future__ import division
import subprocess
import os
from Tkinter import *
from tkFileDialog import *
import tkMessageBox

import datetime   #module for date and hour
import numpy as np
import scipy.stats as stats # for t-test
hour = datetime.datetime.now()




##########################################################################
#
#                   Initzialize main Tkinter window
#
##########################################################################

master = Tk() #Declaring of main window
master.geometry("330x420")
master.title("CyanoGenes")
dir_path = os.path.dirname(os.path.realpath(__file__))
imagen1=PhotoImage(file=dir_path+"/images/Logo.gif") 
label1 = Label(master, image=imagen1).pack() 






#### Load Synechocystis sp. PCC 6803 dictionary containning genome annotation. #####

Cyano_dictionary = np.load('cyanobase.npy').item()
Category_dictionary = np.load('Category.npy').item()


#### Tinter Label and variable

#filename = dir_path+"/sequences.txt"
myvar = DoubleVar()
description1= Label(master, text="GSEA analysis pvalue (df: p<0.05)", anchor="nw").pack()
text_entry = Entry(master, textvariable=myvar)
text_entry.pack()
myvar.set(0.05)




##########################################################################
#
#                   Utility functions
#
##########################################################################




def ProceedButtonCommand(mainframe, master): #Command to attach to proceed button
    mainframe.destroy()
    DrawSecondScreen(master) #This line is what lets the command tied to the button call up the second screen

def QuitButtonCommand(master):
    master.destroy()



def run(filename):
	output = asksaveasfile(mode='w', defaultextension=".txt")
	
	try:
		pval = float(myvar.get())
	except:
		return tkMessageBox.showinfo("ERROR:","evalue is empty")	

	
		
	
	f = open(filename,"r")	
	output.write("\n"+ "## CyanoGenes v0.1 ##\n"+"date: "+str(hour)+"\n")
	output.write("\nGeneID\tGene symbol\tDescription\n")
	output.write("------\t-----------\t-----------\n\n")
	sum_categories = " "
	count_gene = 0

	print("\n\n")
	for line in f:
		gene = str(line.rstrip("\n"))
		if gene in Cyano_dictionary and Category_dictionary:
	#		print Cyano_dictionary[gene] and Category_dictionary
			description = Cyano_dictionary[gene].replace("@","	")
			category = Category_dictionary[gene]
			count_gene = count_gene +1
			sum_categories = sum_categories + str(category)
			output.write(gene.rjust(10)+"\t"+description.rjust(15)+"\t"+category.rjust(15)+"\n")
		else:
			output.write(gene.rjust(10)+"\t"+gene.rjust(15)+"\t"+gene.rjust(15)+"\n")
		
	A = sum_categories.count("Amino acid biosynthesis")
	B = sum_categories.count("Biosynthesis of cofactors, prosthetic groups, and carriers")
	C = sum_categories.count("Cell envelope")
	D = sum_categories.count("Cellular processes")
	E = sum_categories.count("Central intermediary metabolism")
	F = sum_categories.count("Energy metabolism")
	G = sum_categories.count("Fatty acid, phospholipid and sterol metabolism")
	H = sum_categories.count("Photosynthesis and respiration")
	I = sum_categories.count("Purines, pyrimidines, nucleosides, and nucleotides")
	J = sum_categories.count("Regulatory functions")
	K = sum_categories.count("DNA replication, restriction, modification, recombination, and repair")
	L = sum_categories.count("Transcription")
	M = sum_categories.count("Translation")
	N = sum_categories.count("Transport and binding proteins")
	O = sum_categories.count("Other categories")
	P = sum_categories.count("Hypothetical")
	Z = sum_categories.count("Unknown")
	R = sum_categories.count("RNA")



	output.write("\n\n\n\nGene Set Enrichment Analysis (F-test (pvalue < " +str(float(pval))+ " )\n")
	output.write("----------------------------------------------------\n\n")
	if A >=1:
		oddsratio, pvalue = stats.fisher_exact([[A,(count_gene-A)],[(97-A),(3683-count_gene)]], alternative="greater")
		if float(pvalue) <= pval:
			output.write("Amino acid biosynthesis category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if B >=1:
		oddsratio, pvalue = stats.fisher_exact([[B,(count_gene-B)],[(125-B),(3683-count_gene)]], alternative="greater")
		if float(pvalue) <= pval:
			output.write("Biosynthesis of cofactors, prosthetic groups, and carriers category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if C >=1:
		oddsratio, pvalue = stats.fisher_exact([[C,(count_gene-C)],[(67-C),(3683-count_gene)]], alternative="greater")
		if float(pvalue) <= pval:
			output.write("Cell envelope category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if D >=1:
		oddsratio, pvalue = stats.fisher_exact([[D,(count_gene-D)],[(80-D),(3683-count_gene)]], alternative="greater")
		if float(pvalue) <= pval:
			output.write("Cellular processes is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if E >=1:
		oddsratio, pvalue = stats.fisher_exact([[E,(count_gene-E)],[(30-E),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Central intermediary metabolism is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if F >=1:
		oddsratio, pvalue = stats.fisher_exact([[F,(count_gene-F)],[(93-F),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Energy metabolism category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if G >=1:
		oddsratio, pvalue = stats.fisher_exact([[G,(count_gene-G)],[(39-G),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Fatty acid, phospholipid and sterol metabolism category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if H >=1:
		oddsratio, pvalue = stats.fisher_exact([[H,(count_gene-H)],[(143-H),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Photosynthesis and respiration is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if I >=1:
		oddsratio, pvalue = stats.fisher_exact([[I,(count_gene-I)],[(43-I),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Purines, pyrimidines, nucleosides, and nucleotides is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if J >=1:
		oddsratio, pvalue = stats.fisher_exact([[J,(count_gene-J)],[(156-J),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Regulatory functions is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if K >=1:
		oddsratio, pvalue = stats.fisher_exact([[K,(count_gene-K)],[(75-K),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("DNA replication, restriction, modification, recombination, and repair is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if L >=1:
		oddsratio, pvalue = stats.fisher_exact([[L,(count_gene-L)],[(29-L),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Transcription is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if M >=1:
		oddsratio, pvalue = stats.fisher_exact([[M,(count_gene-M)],[(168-M),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Translation is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if N >=1:
		oddsratio, pvalue = stats.fisher_exact([[N,(count_gene-N)],[(200-N),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Transport and binding proteins is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if O >=1:
		oddsratio, pvalue = stats.fisher_exact([[O,(count_gene-O)],[(369-O),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("Other categories is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n")
	if R >=1:
		oddsratio, pvalue = stats.fisher_exact([[R,(count_gene-R)],[(53-R),(3683-count_gene)]], alternative="greater")
		if float(pvalue) < pval:
			output.write("RNA category is statisticaly enriched!!  F-test(p-value): \t"+str(pvalue)+"\n\n\n")



	perc_A = float(A/97)*100
	perc_B = float(B/125)*100
	perc_C = float(C/67)*100
	perc_D = float(D/80)*100
	perc_E = float(E/30)*100
	perc_F = float(F/93)*100
	perc_G = float(G/39)*100
	perc_H = float(H/143)*100
	perc_I = float(I/43)*100
	perc_J = float(J/156)*100
	perc_K = float(K/75)*100
	perc_L = float(L/29)*100
	perc_M = float(M/168)*100
	perc_N = float(N/200)*100
	perc_O = float(O/369)*100
	perc_P = float(P/1277)*100
	perc_Z = float(Z/679)*100
	perc_R = float(R/53)*100

	output.write("\n\n\n\nFunctional Category\tnum genes:genes of that category\t\n")
	output.write("-------------------\t--------------------------------\t\n\n")


	if A >=1:	
		output.write("Amino acid biosynthesis\t"+str(A)+":97 (%5.3f %%)" % perc_A +"\n")
	if B >=1:	
		output.write("Biosynthesis of cofactors, prosthetic groups, and carriers\t"+str(B)+":125 (%5.3f %%)" % perc_B +"\n")
	if C >=1:	
		output.write("Cell envelope\t"+str(C)+":67 (%5.3f %%)" % perc_C +"\n")	
	if D >=1:	
		output.write("Cellular processes\t"+str(D)+":80 (%5.3f %%)" % perc_D +"\n")	
	if E >=1:	
		output.write("Central intermediary metabolism\t"+str(E)+":30 (%5.3f %%)" % perc_E +"\n")		
	if F >=1:	
		output.write("Energy metabolism\t"+str(F)+":93 (%5.3f %%)" % perc_F +"\n")	
	if G >=1:	
		output.write("Fatty acid, phospholipid and sterol metabolism\t"+str(G)+":39 (%5.3f %%)" % perc_G +"\n")		
	if H >=1:	
		output.write("Photosynthesis and respiration\t"+str(H)+":143 (%5.3f %%)" % perc_H +"\n")		
	if I >=1:	
		output.write("Purines, pyrimidines, nucleosides, and nucleotides\t"+str(I)+":43 (%5.3f %%)" % perc_I +"\n")		
	if J >=1:	
		output.write("Regulatory functions\t"+str(J)+":156 (%5.3f %%)" % perc_J +"\n")		
	if K >=1:	
		output.write("DNA replication, restriction, modification, recombination, and repair\t"+str(K)+":75 (%5.3f %%)" % perc_K +"\n")		
	if L >=1:	
		output.write("Transcription\t"+str(L)+":29 (%5.3f %%)" % perc_L +"\n")		
	if M >=1:	
		output.write("Translation\t"+str(M)+":168 (%5.3f %%)" % perc_M +"\n")		
	if N >=1:	
		output.write("Transport and binding proteins\t"+str(N)+":200 (%5.3f %%)" % perc_N +"\n")		
	if O >=1:	
		output.write("Other categories\t"+str(O)+":369 (%5.3f %%)" % perc_O +"\n")		
	if P >=1:	
		output.write("Hypothetical\t"+str(P)+":1277 (%5.3f %%)" % perc_P +"\n")		
	if Z >=1:	
		output.write("Unknown\t"+str(Z)+":679 (%5.3f %%)" % perc_Z +"\n")		
	if R >=1:	
		output.write("RNA\t"+str(R)+":53 (%5.3f %%)" % perc_R +"\n")	
	
	
	tkMessageBox.showinfo("CyanoGenes:","analysis is done!!")



def openinfo(dir):
	dir_path = os.path.dirname(os.path.realpath(__file__))
	subprocess.call(['open', '-a', 'TextEdit', dir_path +'/info.txt'])


def browsefunc():
	global filename
	filename = askopenfilename()
	pathlabel.config(text=filename.split("/")[-1])


browsebutton = Button(master, text="Browse", command=browsefunc)	
browsebutton.pack()
pathlabel = Label(master, text="\nInput file\n(df: sequences.txt)\n", fg="blue", anchor= CENTER)
pathlabel.pack()	





def DrawFirstScreen(master):
	var = StringVar()
	
 	mainframe = Frame(master) #This is a way to semi-cheat when drawing new screens, destroying a frame below master frame clears everything from the screen without having to redraw the window, giving the illusion of one seamless transition
	

	ProceedButton = Button(mainframe, text="Run", command=lambda: run(filename), anchor="nw") #Lambda just allows you to pass variables with the command
	QuitButton = Button(mainframe, text = "Quit", command=lambda: QuitButtonCommand(master))
	InfoButton = Button(mainframe, text="Info", command=lambda:openinfo(master))
#	SaveButton = Button(mainframe, text="Save", command=lambda:browsefunc())
	


	
	mainframe.pack()  
	ProceedButton.pack()
#	SaveButton.pack(side = RIGHT)
	InfoButton.pack(side=LEFT)
	QuitButton.pack(side = RIGHT)
	




DrawFirstScreen(master) 
description5 = (Label(master, text="\nCyanoGenes v0.1.\nProgram designed by Joaquin Giner Lamia. 2018.", fg="green4",font=(None, 10), height=40, width=40) ).pack()

master.mainloop() #The mainloop handles all the	 
