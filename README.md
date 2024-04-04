  quantile_v2.py   
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
   
Dependencies: NumPy   
