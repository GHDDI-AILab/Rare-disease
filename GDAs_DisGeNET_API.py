#This file for download DisGeNET database with API
#build by Xiaoying Lv at 2020.9.8

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
	parser.add_argument('-url',type=str,default='&&',help='input your URL')
	parser.add_argument('-out',type=str,default='test',help='output result to csv file')
	args = parser.parse_args()

	return parser

def main(args):
	#url='https://www.disgenet.org/api/gda/disease/C2751492?source=ALL&type=disease'
	#======URL=========
	url='%s'%args.url
	#print(url)
	resp = requests.get(url)

	data = json.loads(resp.text)
	#print(data[0])

        #=====extract data====
	uniprotid_list = []
	gene_symbol_list = []
	for i in range(len(data)):
		uniprotid_list.append(data[i].get('uniprotid'))
		gene_symbol_list.append(data[i].get('gene_symbol'))
	
	#==write the time to file name==
	time = datetime.datetime.now().strftime('%Y_%m_%d')
	csvfile = open('%s_%s.csv'%(args.out,time),'w')
	#csvfile = open('test_%s.csv'%time,'w')
	writer = csv.writer(csvfile)
	writer.writerows(zip(uniprotid_list,gene_symbol_list))	
	csvfile.close()

if __name__ == '__main__':
	argparser = get_parser()
	args = argparser.parse_args()

	main(args)
