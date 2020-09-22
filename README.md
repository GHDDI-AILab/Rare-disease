# Rare-disease workflow

*This repo contain all source codes and descriptions for TTR disease analysis*

Download gene-disease association(GDA) from public database using API or from the website directly.

###  1) DisGeNET database (including Orphanet)

   DisGeNET database contains multiple public database, and we use API (UMLS CUI:C2751492,disease_name:'AMYLOIDOSIS, HEREDITARY, TRANSTHYRETIN-RELATED') to download GDAs. 74 genes are extracted from this database.
   At finally, we get 74 genes (HGNC format) from DisGeNET.

| TTR    | RBP4       | CYP2A7  | GPC5  | LCT    | NOTCH1   | BGN     | MIA    |
| ------ | ---------- | ------- | ----- | ------ | -------- | ------- | ------ |
| APC    | MFT2       | AGER    | PART1 | C4orf3 | NTF3     | TNMD    | AXIN2  |
| MUTYH  | MIA-RAB4B  | DPYD    | GCG   | MLH1   | SERPINA1 | DCLRE1B | CASP3  |
| GSN    | MTCO2P12   | EIF2S1  | GLB1  | MMP9   | PLA2G2A  | SNCA    | EIF2S2 |
| PTGS2  | NLRP3      | EIF2S3  | GPSM2 | MRC1   | PPP1R1A  | TRIM21  |        |
| CTNNB1 | CLU        | EPO     | IAPP  | MSH2   | PYY      | SST     |        |
| APOA1  | COL11A1    | ALB     | IL6   | COX2   | RDH5     | VEGFA   |        |
| APOE   | CRP        | FAP     | IL10  | NUDT1  | RLBP1    | VIP     |        |
| NPPB   | CTSE       | ALDH1A3 | KRAS  | NEFL   | ATXN1    | CACNA1A |        |
| B2M    | CYLDCYP2A7 | FBN1    | LCN2  | NGF    | ATXN2    | CAL     |        |

### 2) OMIM database

   This database aren`t free. Only available for website research. TTR gene was extracted.

### 3) KEGG database

   KEGG have multiple subdatabases. We use pathway (no result) and disease (family amyloidosis) database for GDAs research. 5 genes were extracted from KEGG disease database.

| Gene symbols | Gene symbols | Gene symbols | Gene symbols | Gene symbols |
| :----------: | ------------ | ------------ | ------------ | :----------: |
|     TTR      | FGA          | APOA1        | LYZ          |     B2M      |

### 4) DECIPHER

​    No API available for this database.There are no feedback for transthtretin amyloidsis.

### 5) PheGenI

   You should input the phenotype (mainly from mayo clinic and ICD-10) of disease. 14 genes were extracted from PheGenI trait.

### 6) Enrichr database

   This database are curated for 




