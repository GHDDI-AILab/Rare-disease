###PINA multiple seprator
awk -F '[\t;:;(]' 'FNR>1{print $6"\t"$9}' Homo\ sapiens-PINA-20140521.tsv > PINA_HGNC_edges.txt

###STRING
awk -F '[ ;.]' 'NR==FNR{a[$1]=$3}NR>FNR{if($2 in a && $4 in a) print a[$2]"\t"a[$4]}' STRING_ENSP_HGNC_v77.txt STRING_edges.txt > STRING_HGNC_edges.txt
awk '{if(!($2=="" || $1=="")) print $0}' *HGNC_edges.txt > STRING_HGNC_edges_no_space.txt

###HuRI
awk  'NR==FNR{a[$1]=$3}NR>FNR{if($1 in a && $2 in a) print a[$1]"\t"a[$2]}' HuRI_ENSG_HGNC_v77.txt HuRI_edges.txt > HuRI_HGNC_edges.txt
awk '{if(!($2=="" || $1=="")) print $0}' *HGNC_edges.txt > HuRI_HGNC_edges_no_space.txt 
