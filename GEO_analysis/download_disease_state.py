#This file for download disease state in website
#build by XiaoyingLv at 2020.10.10

import requests
import json
import csv
import datetime
import argparse  #get paramter from the external environment

def get_parser():
	"""
	Parameters Parser
	"""
	
	parser = argparse.ArgumentParser(description="Using the URL API to store output to csv file")
	parser.add_argument('-name',type=str,default='&&',help='input file name')
	parser.add_argument('-out',type=str,default='test',help='output result to csv file')
	args = parser.parse_args()

	return parser

def main(args):
	#disease_name=input("Please input the disease name and We will obtain the UMLS CUI string.")
	#url='https://www.disgenet.org/api/gda/disease/C2751492?source=ALL&type=disease'
	#======URL=========
	url='https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=%s'%args.name
	#print(url)
	resp = requests.get(url)

	
	#==write the time to file name==
	#time = datetime.datetime.now().strftime('%Y_%m_%d')
	#csvfile = open('%s_%s.csv'%(args.out,time),'w')
	#csvfile = open('test_%s.csv'%time,'w')
	txtfile = open(args.out,'w')
	#writer = csv.writer(csvfile)
	#writer.writerows(zip(uniprotid_list,gene_symbol_list))	
	txtfile.write(resp.text)
	txtfile.close()

if __name__ == '__main__':
	argparser = get_parser()
	args = argparser.parse_args()

	main(args)
