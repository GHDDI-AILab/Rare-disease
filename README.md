# Rare-disease workflow

***

> # A. Gene direction
>
> ![TTR_workflow](https://github.com/XiaoyingLv/images/master/img/20200925180445.png)
>
> ![TTR_workflow](https://github.com/XiaoyingLv/images/master/img/20200925180704.png)

## I. TTR-related genes from public databases

*This repo contains all source codes and files for TTR disease analysis*

Download gene-disease association(GDA) from public database using API or from the website directly.

###  1) DisGeNET database (including Orphanet)

   DisGeNET database contains multiple public database, and we use API (UMLS CUI:C2751492,disease_name:'AMYLOIDOSIS, HEREDITARY, TRANSTHYRETIN-RELATED') to download GDAs. 74 genes are extracted from this database.
   At finally, we got 74 genes (HGNC format) from DisGeNET.

|  TTR   |    RBP4    | CYP2A7  | GPC5  |  LCT   |  NOTCH1  |   BGN   |  MIA   |
| :----: | :--------: | :-----: | :---: | :----: | :------: | :-----: | :----: |
|  APC   |    MFT2    |  AGER   | PART1 | C4orf3 |   NTF3   |  TNMD   | AXIN2  |
| MUTYH  | MIA-RAB4B  |  DPYD   |  GCG  |  MLH1  | SERPINA1 | DCLRE1B | CASP3  |
|  GSN   |  MTCO2P12  | EIF2S1  | GLB1  |  MMP9  | PLA2G2A  |  SNCA   | EIF2S2 |
| PTGS2  |   NLRP3    | EIF2S3  | GPSM2 |  MRC1  | PPP1R1A  | TRIM21  |        |
| CTNNB1 |    CLU     |   EPO   | IAPP  |  MSH2  |   PYY    |   SST   |        |
| APOA1  |  COL11A1   |   ALB   |  IL6  |  COX2  |   RDH5   |  VEGFA  |        |
|  APOE  |    CRP     |   FAP   | IL10  | NUDT1  |  RLBP1   |   VIP   |        |
|  NPPB  |    CTSE    | ALDH1A3 | KRAS  |  NEFL  |  ATXN1   | CACNA1A |        |
|  B2M   | CYLDCYP2A7 |  FBN1   | LCN2  |  NGF   |  ATXN2   |   CAL   |        |

### 2) OMIM database

   This database aren`t free， only available for website research. TTR gene was extracted.

### 3) KEGG database

   KEGG have multiple subdatabases. We use pathway (no result) and disease (family amyloidosis) database for GDAs research. 5 genes (HGNC format) were extracted from KEGG disease database.

| Gene symbols | Gene symbols | Gene symbols | Gene symbols | Gene symbols |
| :----------: | :----------: | :----------: | :----------: | :----------: |
|     TTR      |     FGA      |    APOA1     |     LYZ      |     B2M      |

### 4) DECIPHER

​    No API available for this database.There are no feedback for transthtretin amyloidsis.

### 5) PheGenI

   You should input the phenotype (mainly from mayo clinic and ICD-10) of disease. 14 genes (HGNC format) were extracted from PheGenI trait.

|   NTN5   | SEC1P  |  BAG3  |  MAML3  |  FUT2   |  CCND1   | RNA5SP56 |
| :------: | :----: | :----: | :-----: | :-----: | :------: | :------: |
| PSMC1P12 | ZBTB17 | DNAH11 | SMARCD3 | SLC44A5 | PAFAH1B1 |   CBX7   |



### 6) Enrichr database

   This database integrated the expert curated database. However, the information maybe cann`t be updata timely.  So the gene number from Enricher DisGeNET and KEGG is lower than that from origin databases.

At finally, we get 498 non redundant genes (HGNC format). 

## Summary: 93 genes in total with 91 unique gene list

***

***

# II. TTR-related genes from GEO dataset

### 1) download the data and install the Partek genomics Suite

​      We download the raw CEL file from this URL: https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE67784

​    


