###PINA multiple seprator
###biomaRt to convert uniprotkb id and symbol to HGNC id and symbol

awk -F " " 'NR==FNR{a[$2]=$2}NR>FNR{if(!($2 in a)) print $0}' PINA_uniprot_id_HGNC.txt PINA_uniprot_symbol_HGNC.txt  > tmp.txt
awk -F '[\t;:;(]' '{print $2"\t"$6;print $4"\t"$9}' Homo\ sapiens-PINA-20140521.tsv | sort | uniq > PINA_uniprotkb_id_symbol.txt
awk 'NR==FNR{a[$2]=$1}NR>FNR{print a[$1]" "$2" "$3}' PINA_uniprotkb_id_symbol.txt tmp.txt > tmp_2.txt
cat PINA_uniprot_id_HGNC.txt tmp_2.txt > PINA_nodes_HGNC.txt
awk -F '[\t;:;(]' '{print $2"\t"$4"\t" $6"\t"$9}' Homo\ sapiens-PINA-20140521.tsv  > tmp.txt
awk 'NR==FNR{a[$1]=$3}NR>FNR{if($1 in a && $2 in a) print a[$1]"\t"a[$2]}' PINA_nodes_HGNC.txt tmp.txt > PINA_edges_HGNC.txt

awk '{if(!($2=="" || $1=="")) print $0}' PINA_edges_HGNC.txt > PINA_HGNC_edges_no_space.txt

###STRING
awk -F '[ ;.]' 'NR==FNR{a[$1]=$3}NR>FNR{if($2 in a && $4 in a) print a[$2]"\t"a[$4]}' STRING_ENSP_HGNC_v77.txt STRING_edges.txt > STRING_HGNC_edges.txt
awk '{if(!($2=="" || $1=="")) print $0}' *HGNC_edges.txt > STRING_HGNC_edges_no_space.txt

###HuRI
awk  'NR==FNR{a[$1]=$3}NR>FNR{if($1 in a && $2 in a) print a[$1]"\t"a[$2]}' HuRI_ENSG_HGNC_v77.txt HuRI_edges.txt > HuRI_HGNC_edges.txt
awk '{if(!($2=="" || $1=="")) print $0}' *HGNC_edges.txt > HuRI_HGNC_edges_no_space.txt 


###merge three databases and remove the self-interacting and redundant pairs
awk '{if($1!=$2) print $0}' HuRI/HuRI_HGNC_edges_no_space.txt | sort | uniq >  HuRI_tmp.txt
awk '{if($1!=$2) print $0}' PINA/PINA_HGNC_edges_no_space.txt | sort | uniq >  PINA_tmp.txt
awk '{if($1!=$2) print $0}' STRING/STRING_HGNC_edges_no_space.txt | sort | uniq >  STRING_tmp.txt

awk 'NR==FNR{t=$1":"$2;m=$2":"$1;a[t]=t;a[m]=m}NR>FNR{n=$1":"$2;if(!(n in a)) print $0}' HuRI_tmp.txt PINA_tmp.txt > PINA_tmp_HuRI.txt
cat HuRI_tmp.txt PINA_tmp_HuRI.txt > HuRI_PINA_tmp.txt
awk 'NR==FNR{t=$1":"$2;m=$2":"$1;a[t]=t;a[m]=m}NR>FNR{n=$1":"$2;if(!(n in a)) print $0}' HuRI_PINA_tmp.txt STRING_tmp.txt > STRING_tmp_HuRI_PINA.txt
cat HuRI_PINA_tmp.txt STRING_tmp_HuRI_PINA.txt > PPI_edges.txt
awk '{m=$1"-"$2;t=$2"-"$1;if(!(t in a)) {a[m] = m;print $0;}}' PPI_edges.txt > PPI_edges_noredundant.txt
awk '{print $1;print $2}' PPI_edges_noredundant.txt | sort | uniq > PPI_nodes_noredundant.txt
