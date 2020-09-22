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
	parser.add_argument('-out',type=str,default='test',help='output result to txt file')
	args = parser.parse_args()

	return parser

def main(args):
	#url='https://www.uniprot.org/uploadlists/'
	#======URL=========
	url='%s'%args.url
	#print(url)
	params = {
	'from': 'ACC+ID'
	'to': ''
	'format': 'tab'
	'query': ''
	}
	resp = requests.get(url)

	data = resp.text

	
	#==write the time to file name==
	time = datetime.datetime.now().strftime('%Y_%m_%d')
	txtfile = open('%s_%s.csv'%(args.out,time),'w')
	txtfile.write(data)	
	txtfile.close()

if __name__ == '__main__':
	argparser = get_parser()
	args = argparser.parse_args()

	main(args)
