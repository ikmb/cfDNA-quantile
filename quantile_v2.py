#!/opt/miniconda3/envs/test_env/bin/python
#!/bin/python

## conda env test_env

import sys
import numpy

#Chromosome	Position	Name	HGVS_Coding	HGVS_Protein	HROC520-1-A_PL_Quality	HROC520-1-B_PL_Quality	HROC520-2-A_PL_Quality	HROC520-2-B_PL_Quality	HROC520-A_PL_Quality	HROC520-B_PL_Quality	HROC528-1-A_PL_Quality	HROC528-1-B_PL_Quality	HROC528-A_PL_Quality	HROC528-B_PL_Quality	HROC534-2-A_PL_Quality	HROC534-2-B_PL_Quality	HROC534-3-A_PL_Quality	HROC534-3-B_PL_Quality	HROC534-A_PL_Quality	HROC534-B_PL_Quality	HROC535-1-A_PL_Quality	HROC535-1-B_PL_Quality	HROC535-A_PL_Quality	HROC535-B_PL_Quality	HROC536-1-A_PL_Quality	HROC536-1-B_PL_Quality	HROC536-A_PL_Quality	HROC536-B_PL_Quality	HROC539-2-A_PL_Quality	HROC539-3-A_PL_Quality	HROC539-3-B_PL_Quality	HROC539-A_PL_Quality	HROC539-B_PL_Quality	HROC540-1-A_PL_Quality	HROC540-1-B_PL_Quality	HROC540-A_PL_Quality	HROC540-B_PL_Quality	HROC544-1-A_PL_Quality	HROC544-1-B_PL_Quality	HROC544-2-A_PL_Quality	HROC544-2-B_PL_Quality	HROC544-A_PL_Quality	HROC544-B_PL_Quality	HROC547-1-A_PL_Quality	HROC547-1-B_PL_Quality	HROC547-A_PL_Quality	HROC547-B_PL_Quality	HROC554-2-A_PL_Quality	HROC554-2-B_PL_Quality	HROC554-A_PL_Quality	HROC554-B_PL_Quality	HROC556-1-A_PL_Quality	HROC556-1-B_PL_Quality	HROC556-A_PL_Quality	HROC556-B_PL_Quality	HROC558-1-A_PL_Quality	HROC558-1-B_PL_Quality	HROC558-A_PL_Quality	HROC558-B_PL_Quality	HROC562-1-A_PL_Quality	HROC562-1-B_PL_Quality	HROC562-A_PL_Quality	HROC562-B_PL_Quality	HROC566-1-A_PL_Quality	HROC566-1-B_PL_Quality	HROC566-A_PL_Quality	HROC566-B_PL_Quality	HROC574-1-A_PL_Quality	HROC574-1-B_PL_Quality	HROC574-A_PL_Quality	HROC574-B_PL_Quality	HROC586-1-A_PL_Quality	HROC586-1-B_PL_Quality	HROC586-A_PL_Quality	HROC601-1-A_PL_Quality	HROC601-1-B_PL_Quality	HROC601-A_PL_Quality	HROC601-B_PL_Quality	HROC520-1-A_PL_Frequency	HROC520-1-B_PL_Frequency	HROC520-2-A_PL_Frequency	HROC520-2-B_PL_Frequency	HROC520-A_PL_Frequency	HROC520-B_PL_Frequency	HROC528-1-A_PL_Frequency	HROC528-1-B_PL_Frequency	HROC528-A_PL_Frequency	HROC528-B_PL_Frequency	HROC534-2-A_PL_Frequency	HROC534-2-B_PL_Frequency	HROC534-3-A_PL_Frequency	HROC534-3-B_PL_Frequency	HROC534-A_PL_Frequency	HROC534-B_PL_Frequency	HROC535-1-A_PL_Frequency	HROC535-1-B_PL_Frequency	HROC535-A_PL_Frequency	HROC535-B_PL_Frequency	HROC536-1-A_PL_Frequency	HROC536-1-B_PL_Frequency	HROC536-A_PL_Frequency	HROC536-B_PL_Frequency	HROC539-2-A_PL_Frequency	HROC539-3-A_PL_Frequency	HROC539-3-B_PL_Frequency	HROC539-A_PL_Frequency	HROC539-B_PL_Frequency	HROC540-1-A_PL_Frequency	HROC540-1-B_PL_Frequency	HROC540-A_PL_Frequency	HROC540-B_PL_Frequency	HROC544-1-A_PL_Frequency	HROC544-1-B_PL_Frequency	HROC544-2-A_PL_Frequency	HROC544-2-B_PL_Frequency	HROC544-A_PL_Frequency	HROC544-B_PL_Frequency	HROC547-1-A_PL_Frequency	HROC547-1-B_PL_Frequency	HROC547-A_PL_Frequency	HROC547-B_PL_Frequency	HROC554-2-A_PL_Frequency	HROC554-2-B_PL_Frequency	HROC554-A_PL_Frequency	HROC554-B_PL_Frequency	HROC556-1-A_PL_Frequency	HROC556-1-B_PL_Frequency	HROC556-A_PL_Frequency	HROC556-B_PL_Frequency	HROC558-1-A_PL_Frequency	HROC558-1-B_PL_Frequency	HROC558-A_PL_Frequency	HROC558-B_PL_Frequency	HROC562-1-A_PL_Frequency	HROC562-1-B_PL_Frequency	HROC562-A_PL_Frequency	HROC562-B_PL_Frequency	HROC566-1-A_PL_Frequency	HROC566-1-B_PL_Frequency	HROC566-A_PL_Frequency	HROC566-B_PL_Frequency	HROC574-1-A_PL_Frequency	HROC574-1-B_PL_Frequency	HROC574-A_PL_Frequency	HROC574-B_PL_Frequency	HROC586-1-A_PL_Frequency	HROC586-1-B_PL_Frequency	HROC586-A_PL_Frequency	HROC601-1-A_PL_Frequency	HROC601-1-B_PL_Frequency	HROC601-A_PL_Frequency	HROC601-B_PL_Frequency	HROC520-1-A_PL_Coverage	HROC520-1-B_PL_Coverage	HROC520-2-A_PL_Coverage	HROC520-2-B_PL_Coverage	HROC520-A_PL_Coverage	HROC520-B_PL_Coverage	HROC528-1-A_PL_Coverage	HROC528-1-B_PL_Coverage	HROC528-A_PL_Coverage	HROC528-B_PL_Coverage	HROC534-2-A_PL_Coverage	HROC534-2-B_PL_Coverage	HROC534-3-A_PL_Coverage	HROC534-3-B_PL_Coverage	HROC534-A_PL_Coverage	HROC534-B_PL_Coverage	HROC535-1-A_PL_Coverage	HROC535-1-B_PL_Coverage	HROC535-A_PL_Coverage	HROC535-B_PL_Coverage	HROC536-1-A_PL_Coverage	HROC536-1-B_PL_Coverage	HROC536-A_PL_Coverage	HROC536-B_PL_Coverage	HROC539-2-A_PL_Coverage	HROC539-3-A_PL_Coverage	HROC539-3-B_PL_Coverage	HROC539-A_PL_Coverage	HROC539-B_PL_Coverage	HROC540-1-A_PL_Coverage	HROC540-1-B_PL_Coverage	HROC540-A_PL_Coverage	HROC540-B_PL_Coverage	HROC544-1-A_PL_Coverage	HROC544-1-B_PL_Coverage	HROC544-2-A_PL_Coverage	HROC544-2-B_PL_Coverage	HROC544-A_PL_Coverage	HROC544-B_PL_Coverage	HROC547-1-A_PL_Coverage	HROC547-1-B_PL_Coverage	HROC547-A_PL_Coverage	HROC547-B_PL_Coverage	HROC554-2-A_PL_Coverage	HROC554-2-B_PL_Coverage	HROC554-A_PL_Coverage	HROC554-B_PL_Coverage	HROC556-1-A_PL_Coverage	HROC556-1-B_PL_Coverage	HROC556-A_PL_Coverage	HROC556-B_PL_Coverage	HROC558-1-A_PL_Coverage	HROC558-1-B_PL_Coverage	HROC558-A_PL_Coverage	HROC558-B_PL_Coverage	HROC562-1-A_PL_Coverage	HROC562-1-B_PL_Coverage	HROC562-A_PL_Coverage	HROC562-B_PL_Coverage	HROC566-1-A_PL_Coverage	HROC566-1-B_PL_Coverage	HROC566-A_PL_Coverage	HROC566-B_PL_Coverage	HROC574-1-A_PL_Coverage	HROC574-1-B_PL_Coverage	HROC574-A_PL_Coverage	HROC574-B_PL_Coverage	HROC586-1-A_PL_Coverage	HROC586-1-B_PL_Coverage	HROC586-A_PL_Coverage	HROC601-1-A_PL_Coverage	HROC601-1-B_PL_Coverage	HROC601-A_PL_Coverage	HROC601-B_PL_Coverage	HROC520-1-A_PL_Reads	HROC520-1-B_PL_Reads	HROC520-2-A_PL_Reads	HROC520-2-B_PL_Reads	HROC520-A_PL_Reads	HROC520-B_PL_Reads	HROC528-1-A_PL_Reads	HROC528-1-B_PL_Reads	HROC528-A_PL_Reads	HROC528-B_PL_Reads	HROC534-2-A_PL_Reads	HROC534-2-B_PL_Reads	HROC534-3-A_PL_Reads	HROC534-3-B_PL_Reads	HROC534-A_PL_Reads	HROC534-B_PL_Reads	HROC535-1-A_PL_Reads	HROC535-1-B_PL_Reads	HROC535-A_PL_Reads	HROC535-B_PL_Reads	HROC536-1-A_PL_Reads	HROC536-1-B_PL_Reads	HROC536-A_PL_Reads	HROC536-B_PL_Reads	HROC539-2-A_PL_Reads	HROC539-3-A_PL_Reads	HROC539-3-B_PL_Reads	HROC539-A_PL_Reads	HROC539-B_PL_Reads	HROC540-1-A_PL_Reads	HROC540-1-B_PL_Reads	HROC540-A_PL_Reads	HROC540-B_PL_Reads	HROC544-1-A_PL_Reads	HROC544-1-B_PL_Reads	HROC544-2-A_PL_Reads	HROC544-2-B_PL_Reads	HROC544-A_PL_Reads	HROC544-B_PL_Reads	HROC547-1-A_PL_Reads	HROC547-1-B_PL_Reads	HROC547-A_PL_Reads	HROC547-B_PL_Reads	HROC554-2-A_PL_Reads	HROC554-2-B_PL_Reads	HROC554-A_PL_Reads	HROC554-B_PL_Reads	HROC556-1-A_PL_Reads	HROC556-1-B_PL_Reads	HROC556-A_PL_Reads	HROC556-B_PL_Reads	HROC558-1-A_PL_Reads	HROC558-1-B_PL_Reads	HROC558-A_PL_Reads	HROC558-B_PL_Reads	HROC562-1-A_PL_Reads	HROC562-1-B_PL_Reads	HROC562-A_PL_Reads	HROC562-B_PL_Reads	HROC566-1-A_PL_Reads	HROC566-1-B_PL_Reads	HROC566-A_PL_Reads	HROC566-B_PL_Reads	HROC574-1-A_PL_Reads	HROC574-1-B_PL_Reads	HROC574-A_PL_Reads	HROC574-B_PL_Reads	HROC586-1-A_PL_Reads	HROC586-1-B_PL_Reads	HROC586-A_PL_Reads	HROC601-1-A_PL_Reads	HROC601-1-B_PL_Reads	HROC601-A_PL_Reads	HROC601-B_PL_Reads	HROC520-1-A_PL_Variant balance	HROC520-1-B_PL_Variant balance	HROC520-2-A_PL_Variant balance	HROC520-2-B_PL_Variant balance	HROC520-A_PL_Variant balance	HROC520-B_PL_Variant balance	HROC528-1-A_PL_Variant balance	HROC528-1-B_PL_Variant balance	HROC528-A_PL_Variant balance	HROC528-B_PL_Variant balance	HROC534-2-A_PL_Variant balance	HROC534-2-B_PL_Variant balance	HROC534-3-A_PL_Variant balance	HROC534-3-B_PL_Variant balance	HROC534-A_PL_Variant balance	HROC534-B_PL_Variant balance	HROC535-1-A_PL_Variant balance	HROC535-1-B_PL_Variant balance	HROC535-A_PL_Variant balance	HROC535-B_PL_Variant balance	HROC536-1-A_PL_Variant balance	HROC536-1-B_PL_Variant balance	HROC536-A_PL_Variant balance	HROC536-B_PL_Variant balance	HROC539-2-A_PL_Variant balance	HROC539-3-A_PL_Variant balance	HROC539-3-B_PL_Variant balance	HROC539-A_PL_Variant balance	HROC539-B_PL_Variant balance	HROC540-1-A_PL_Variant balance	HROC540-1-B_PL_Variant balance	HROC540-A_PL_Variant balance	HROC540-B_PL_Variant balance	HROC544-1-A_PL_Variant balance	HROC544-1-B_PL_Variant balance	HROC544-2-A_PL_Variant balance	HROC544-2-B_PL_Variant balance	HROC544-A_PL_Variant balance	HROC544-B_PL_Variant balance	HROC547-1-A_PL_Variant balance	HROC547-1-B_PL_Variant balance	HROC547-A_PL_Variant balance	HROC547-B_PL_Variant balance	HROC554-2-A_PL_Variant balance	HROC554-2-B_PL_Variant balance	HROC554-A_PL_Variant balance	HROC554-B_PL_Variant balance	HROC556-1-A_PL_Variant balance	HROC556-1-B_PL_Variant balance	HROC556-A_PL_Variant balance	HROC556-B_PL_Variant balance	HROC558-1-A_PL_Variant balance	HROC558-1-B_PL_Variant balance	HROC558-A_PL_Variant balance	HROC558-B_PL_Variant balance	HROC562-1-A_PL_Variant balance	HROC562-1-B_PL_Variant balance	HROC562-A_PL_Variant balance	HROC562-B_PL_Variant balance	HROC566-1-A_PL_Variant balance	HROC566-1-B_PL_Variant balance	HROC566-A_PL_Variant balance	HROC566-B_PL_Variant balance	HROC574-1-A_PL_Variant balance	HROC574-1-B_PL_Variant balance	HROC574-A_PL_Variant balance	HROC574-B_PL_Variant balance	HROC586-1-A_PL_Variant balance	HROC586-1-B_PL_Variant balance	HROC586-A_PL_Variant balance	HROC601-1-A_PL_Variant balance	HROC601-1-B_PL_Variant balance	HROC601-A_PL_Variant balance	HROC601-B_PL_Variant balance	HROC520-1-A_PL_Position balance	HROC520-1-B_PL_Position balance	HROC520-2-A_PL_Position balance	HROC520-2-B_PL_Position balance	HROC520-A_PL_Position balance	HROC520-B_PL_Position balance	HROC528-1-A_PL_Position balance	HROC528-1-B_PL_Position balance	HROC528-A_PL_Position balance	HROC528-B_PL_Position balance	HROC534-2-A_PL_Position balance	HROC534-2-B_PL_Position balance	HROC534-3-A_PL_Position balance	HROC534-3-B_PL_Position balance	HROC534-A_PL_Position balance	HROC534-B_PL_Position balance	HROC535-1-A_PL_Position balance	HROC535-1-B_PL_Position balance	HROC535-A_PL_Position balance	HROC535-B_PL_Position balance	HROC536-1-A_PL_Position balance	HROC536-1-B_PL_Position balance	HROC536-A_PL_Position balance	HROC536-B_PL_Position balance	HROC539-2-A_PL_Position balance	HROC539-3-A_PL_Position balance	HROC539-3-B_PL_Position balance	HROC539-A_PL_Position balance	HROC539-B_PL_Position balance	HROC540-1-A_PL_Position balance	HROC540-1-B_PL_Position balance	HROC540-A_PL_Position balance	HROC540-B_PL_Position balance	HROC544-1-A_PL_Position balance	HROC544-1-B_PL_Position balance	HROC544-2-A_PL_Position balance	HROC544-2-B_PL_Position balance	HROC544-A_PL_Position balance	HROC544-B_PL_Position balance	HROC547-1-A_PL_Position balance	HROC547-1-B_PL_Position balance	HROC547-A_PL_Position balance	HROC547-B_PL_Position balance	HROC554-2-A_PL_Position balance	HROC554-2-B_PL_Position balance	HROC554-A_PL_Position balance	HROC554-B_PL_Position balance	HROC556-1-A_PL_Position balance	HROC556-1-B_PL_Position balance	HROC556-A_PL_Position balance	HROC556-B_PL_Position balance	HROC558-1-A_PL_Position balance	HROC558-1-B_PL_Position balance	HROC558-A_PL_Position balance	HROC558-B_PL_Position balance	HROC562-1-A_PL_Position balance	HROC562-1-B_PL_Position balance	HROC562-A_PL_Position balance	HROC562-B_PL_Position balance	HROC566-1-A_PL_Position balance	HROC566-1-B_PL_Position balance	HROC566-A_PL_Position balance	HROC566-B_PL_Position balance	HROC574-1-A_PL_Position balance	HROC574-1-B_PL_Position balance	HROC574-A_PL_Position balance	HROC574-B_PL_Position balance	HROC586-1-A_PL_Position balance	HROC586-1-B_PL_Position balance	HROC586-A_PL_Position balance	HROC601-1-A_PL_Position balance	HROC601-1-B_PL_Position balance	HROC601-A_PL_Position balance	HROC601-B_PL_Position balance	Genes	Transcript	Type	Classification	Known	Prediction	MAF	
#1	6257783	g.6257784_6257785insT			0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0.006	0.005	0.009	0.008	0.007	0.008	0.006	0.008	0.012	0.008	0.005	0.008	0.008	0.007	0.009	0.007	0.008	0.009	0.006	0.006	0.007	0.007	0.01	0.008	0.008	0.009	0.006	0.007	0.006	0.006	0.007	0.006	0.009	0.005	0.007	0.008	0.006	0.007	0.007	0.008	0.009	0.008	0.008	0.008	0.005	0.006	0.008	0.006	0.007	0.004	0.006	0.008	0.007	0.005	0.005	0.005	0.006	0.008	0.008	0.007	0.009	0.007	0.008	0.005	0.008	0.005	0.006	0.006	0.007	0.008	0.006	0.007	0.005	0.006	8366	12884	15471	13057	13389	13171	13629	13216	8409	6355	9557	9822	8254	6720	11213	10841	12490	8649	10275	4435	9298	7650	13350	5908	15147	10264	9983	9476	5923	15372	12239	10435	10508	13772	14833	14000	15918	9615	17974	8483	11880	7730	7006	9102	13029	8508	12623	9175	16482	7825	10356	10773	12136	6530	8397	15492	15336	11072	16570	8924	8565	15147	8692	9167	16219	10749	9230	10229	10973	7463	13920	14728	15095	10799	50	60	142	109	96	99	88	101	104	50	44	83	62	48	97	79	106	77	57	25	69	56	129	49	119	94	57	65	38	96	83	63	95	68	109	110	96	71	117	69	111	60	55	71	70	54	102	55	121	35	67	87	83	34	40	74	85	88	125	65	73	99	66	50	137	58	56	66	77	56	86	104	82	68	1	0.818	0.972	0.912	0.778	0.98	0.796	0.98	1	1	0.833	0.886	0.938	0.714	0.83	0.795	0.893	0.974	0.9	0.923	0.971	0.931	0.955	0.96	0.983	0.88	0.839	0.97	0.9	0.846	0.844	0.909	0.759	0.889	0.912	1	0.959	0.821	0.887	0.769	0.914	0.935	0.774	0.919	1	0.929	0.759	0.719	0.952	0.75	0.675	0.933	0.886	1	0.667	1	0.932	0.956	0.812	0.97	0.825	0.904	0.941	0.852	0.93	0.933	0.931	0.941	0.974	1	1	0.962	1	0.889	0.975	0.979	0.981	0.969	0.938	0.984	0.947	0.986	0.962	0.935	0.957	0.957	0.988	0.978	0.972	0.995	0.983	0.976	0.982	0.997	0.983	0.985	0.957	0.955	0.992	0.958	0.997	0.957	0.989	0.988	0.975	0.998	0.995	0.962	0.972	0.954	0.965	0.983	0.996	0.985	0.998	0.977	0.985	0.99	0.963	0.965	0.976	0.956	0.973	0.97	0.979	0.973	0.966	0.99	0.952	0.979	0.963	0.966	0.989	0.998	0.984	1	0.967	0.991	0.969	0.958	0.979	0.994	0.963	0.954	0.991	0.977	0.983	0.971				Uncertain	rs777006564			

def numpy_quantiles (infile, outfile, qs, min_cov, min_reads):
	'''        #######################################################################################
	#  quantile_v2.py
	#######################################################################################
	#  Scans GenSearchNGS Variant-Verifier-tsv-file and computes VAF-quantiles
	#
	#  Usage:   quantile_v2.py <in> <out> <mincov> <minreads> <pq>
	#
	#  where
	#
	#  <in>       GenSearchNGS Variant-Verifier-tsv-file 
	#  <out>      Tab-separated output file
	#  <mincov>   Min read depth at VAF, else ignore VAF
	#  <minreads> Min ALT reads at VAF, else ignore VAF
	#  <pq>       p-quantiles (variable number of p-quantiles, 0 < pq < 1
	#######################################################################################
	#  Author: Michael Forster, m.forster@ikmb.uni-kiel.de            Date: 1 November 2022
	#  Correction: 27.02.23 max(vaf2) instead of max(quantvaf)
	#  Correction: 28.02.23 exception if vaf2 empty
	#######################################################################################
	'''

	print ("infile:   ", infile)
	print ("outfile:  ", outfile)
	print ("mincov:   ", min_cov)
	print ("minreads: ", min_reads)
	print ("pq:       ", qs)

	inf=open(infile,"r")
	out=open(outfile,"w")
	
	# Decipher tsv-file header line:
	header=inf.readline()
	cols=header.split("\t")
	# print (cols)
	vaf_start=0
	vaf_end=0
	cov_start=0
	cov_end=0
	reads_start=0
	reads_end=0
	i = -1
	for c in cols:
		i += 1
		if vaf_start == 0:
			if c.find("_Frequency") > 0:
				# print (c, i)
				vaf_start = i
		elif vaf_end == 0:
			if c.find("_Coverage") > 0:
				vaf_end = i
				cov_start = i
		elif cov_end == 0:
			if c.find("_Reads") > 0:
				cov_end = i
				reads_start = i
		elif reads_end == 0:
			if c.find("_Variant balance") > 0:
				reads_end = i
				
	# print (vaf_start, vaf_end, cov_start, cov_end, reads_start, reads_end)
	
	# Write header line:
	outheader = "Chromosome\tPosition\tName\tNumber_of_samples\tNumber_of_QCpassing_samples\tMinVal\tMaxVal"
	for i in qs:
		outheader += "\tQuantile_%s" % (i)
	outheader += "\n"
	out.write (outheader)
	
	# Loop over all variant-calls in tsv-file
	
	while True:
		line = inf.readline()
		# print (line)
		if line == "":
			break
		else:
			cols = line.split("\t")
			#print (cols)
			vaf=[]
			cov=[]
			reads=[]
			for i in range(vaf_start,vaf_end):
				try:
					vaf.append(float(cols[i]))
				except:
					vaf.append("NA")
			for i in range(cov_start,cov_end):
				cov.append(float(cols[i]))
			for i in range(reads_start,reads_end):
				reads.append(float(cols[i]))
	
			print ("len(vaf)", len(vaf))
			print (vaf)
			# use VAFs whose read depth and variant reads are above min thresholds
			vaf2 = []
			for j in range(0,len(vaf)):
				if cov[j] >= min_cov and reads[j] >= min_reads and vaf[j] != "NA":
					vaf2.append(vaf[j])
			n = len(vaf)
			nqcpass = len(vaf2)
			
			print (vaf2)
	
			# quantiles of VAFs:
			quantvaf = []
			if nqcpass > 0:
				for i in qs:
					q = numpy.quantile(vaf2, float(i))
					quantvaf.append (q)
					minvaf = min(vaf2)
					maxvaf = max(vaf2)
			else:
				for i in qs:
					quantvaf.append (-1)
					minvaf = -1
					maxvaf = -1
			
			# write output line for variant-call:
			outline = "%s\t%s\t%s\t%s\t%s" % (cols[0],cols[1],cols[2],n,nqcpass)
			outline += "\t%s\t%s" % (minvaf, maxvaf)
			for i in quantvaf:
				outline += "\t%s" % (i)
			outline += "\n"
			out.write (outline)
	
	out.close()
	inf.close()
	
##############################################
# the actual main
##############################################

if len(sys.argv) < 6:
	print (numpy_quantiles.__doc__)
	sys.exit()
else:
	infile = sys.argv[1]
	outfile = sys.argv[2]
	min_cov = int(sys.argv[3])
	min_reads = int(sys.argv[4])
	qs = []
	for i in range (5,len(sys.argv)):
		pq = float(sys.argv[i])
		qs.append (pq)

numpy_quantiles (infile, outfile, qs, min_cov, min_reads)

print('Done')

		
