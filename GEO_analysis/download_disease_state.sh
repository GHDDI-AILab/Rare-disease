rm result.txt
for i in `cat list.txt`
do
  python download_disease_state.py -name ${i} -out ${i}
  echo ${i} >> result.txt
  awk '{if(FNR==291) print $0}' ${i} >> result.txt
  rm ${i}
done

awk -F ">" '{if($1~/^GSM/) tmp=$1;else {split($2,a,"<");print tmp"\t"a[1]}}' result.txt > result_list.txt 
awk 'NR==FNR{a[$1]=$2}NR>FNR{if($1 in a) print $1"_"a[$1]"\t"$2"_"$3}' ../../RNA_samples/list.txt result_list.txt > sample_attribute.txt
awk '{if($2~/Control/) {split($2,a,"_"); print $1":"$1"_"a[2]"_"a[1]} else {print $1":"$1"_"$2}}' ../../RNA_samples/sample_attribute.txt > convert_name.txt
for i in `cat convert_name.txt`; do   array=(${i//:/ });   cp ${array[0]}.CEL ${array[1]}.CEL; done
