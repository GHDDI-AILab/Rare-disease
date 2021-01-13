### Created by Xiaoying lv for calculating the shortest distance for target gene and drug gene.

import numpy as np
import math
from collections import Counter
import datetime
import argparse
import scipy
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path
import networkx as nx

def get_parser():
	"""
	Parameters Parser
	"""

	parser = argparse.ArgumentParser(description="Calculating the shortest distance to store output to csv file and figure")
	parser.add_argument('-targetgene',type=str,default='test',help='input your target gene list')
	parser.add_argument('-druggene',type=str,default='test',help='input your drug target')
	parser.add_argument('-ppi',type=str,default='test',help='input your protein-protein interaction')
	parser.add_argument('-ppi_length',type=int,help='input the length of protein-protein interaction')
	parser.add_argument('-out',type=str,default='test',help='put matrix and figure of the shortest distance out')
	args = parser.parse_args()

	return parser

def readfile(file_targetgene,file_druggene,file_ppigene,len_ppigene):
	
	global targetgene_list
	global druggene_list
	targetgene_list = []
	druggene_list = {}
	
	file_target = open(file_targetgene,'r')
	for line in file_target.readlines():
		line = line.strip()
		targetgene_list.append(line)
	
	file_drug = open(file_druggene,'r')
	for line in file_drug.readlines():
		line = line.strip().split("\t")
		druggene_list[line[0]] = line[1]
	#print(druggene_list)
	
	global drug_gene
	drug_gene = []
	for drug in druggene_list.keys():
		for druggene in druggene_list[drug].split(','):
			drug_gene.append(druggene)

	global ppi_list
	ppi_list = [[0 for i in range(2)] for i in range(len_ppigene)]
	file_ppi = open(file_ppigene,'r')
	i = 0
	for line in file_ppi.readlines():
		line = line.strip().split("\t")
		ppi_list[i][0] = line[0]
		ppi_list[i][1] = line[1]
		i = i+1
	
	global ppi_gene_list
	ppi_gene_list = []
	tmp = np.array(ppi_list) ### convert to array for reshape
	tmp2 = tmp.reshape((-1))
	ppi_gene_list = list(tmp2)
	
	file_target.close()
	file_drug.close()
	file_ppi.close()
	return targetgene_list,druggene_list,ppi_list 

def weight():

	weight_list = {}
	weight_list_tmp = {}
	tmp = np.array(ppi_list) ### convert to array for reshape
	global ppi_list_1d_redundant
	ppi_list_1d_redundant = tmp.reshape((-1))
	weight_list_tmp = Counter(ppi_list_1d_redundant)
	for druggene in drug_gene:
		weight_list[druggene] = 0
		if druggene in weight_list_tmp.keys():
			weight_list[druggene] = -1*math.log(weight_list_tmp[druggene]+1) ### default parameter is e, as (ln)
		elif druggene in targetgene_list:
			weight_list[druggene] = 0
	return weight_list

def cal_dist_matrix():
	
	global total_list

	total_list_tmp = drug_gene + targetgene_list + ppi_gene_list
	total_list = list(set(total_list_tmp))

	ppi_matrix = [[0 for i in range(len(total_list))] for j in range(len(total_list))]
	for i in ppi_list:
		ppi_matrix[total_list.index(i[0])][total_list.index(i[1])] = 1
		ppi_matrix[total_list.index(i[1])][total_list.index(i[0])] = 1
	#Graph_ppi = nx.from_numpy_array(np.array(ppi_matrix))
	#ppi_matrix = csr_matrix(ppi_matrix)
	#dist_matrix = shortest_path(csgraph=ppi_matrix, directed=False, indices=0, return_predecessors=False)
	dist_matrix = shortest_path(np.array(ppi_matrix), directed=False,  return_predecessors=False)
	
	#return Graph_ppi
	return dist_matrix
	
def dist_set(dist_matrix,weight_list):
	dist = 0
	drug_target_dist_list = {}
	for drug in druggene_list.keys():
		value = 0
		length = len(druggene_list[drug])
		for druggene in druggene_list[drug].split(","): 
			gene_gene_dist_list = []
			for targetgene in targetgene_list:
				dist = dist_matrix[total_list.index(targetgene),total_list.index(druggene)] + weight_list[druggene] 
				gene_gene_dist_list.append(dist)
			if min(gene_gene_dist_list) != float("inf"):
				value += min(gene_gene_dist_list)
			else:
				length = length-1
		if length==0:
			drug_target_dist_list[drug] = "inf"
		else:
			drug_target_dist_list[drug] = value/length
	#print(len(drug_target_dist_list))
	return drug_target_dist_list

def main(args):
	#==write the time to file name==

	targetgene_list,druggene_list,ppi_list = readfile(args.targetgene,args.druggene,args.ppi,args.ppi_length)
	weight_list = weight()
	dist_matrix = cal_dist_matrix()
	drug_target_dist_list = dist_set(dist_matrix,weight_list)	
	time = datetime.datetime.now().strftime('%Y_%m_%d')
	outfile = open('%s_%s.csv'%(args.out,time),'w')
	#csvfile = open('test_%s.csv'%time,'w')
	outfile.write(str(drug_target_dist_list))
	outfile.close()

if __name__ == '__main__':
	argparser = get_parser()
	args = argparser.parse_args()

	main(args)
	
