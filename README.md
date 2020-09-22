# Rare-disease workflow
This repo contain all source codes and descriptions for TTR disease analysis

Download gene-disease association(GDA) from public database using API

1)DisGeNET database (including Orphanet)
   DisGeNET database contains multiple public database, and we use API (UMLS CUI:C2751492,disease_name:'AMYLOIDOSIS, HEREDITARY, TRANSTHYRETIN-RELATED') to download GDAs. 74 genes are extracted from this database.
   At finally, we get 74 genes from DisGeNET.

2)OMIM database
   This database aren`t free. Only available for website research

3)KEGG database
   KEGG have multiple subdatabases. We use pathway (no result) and disease (family amyloidosis) database for GDAs research. 5 genes were extracted from KEGG disease database.

4)DECIPHER
    No API available for this database.There are no feedback for transthtretin amyloidsis.

5)PheGenI
   You should input the phenotype (mainly from mayo clinic and ICD-10) of disease. 14 genes were extracted from PheGenI trait.
  



