---
title: "Quick guide for parameters in tophat-cufflinks in nematode RNA-seq analysis"
date: 2015/05/17 12:00
---

## The summary of tophat-cufflinks protocol is like that:

### step1: generate a tophat_out folder with bam files

```sh
tophat  -G genes.gtf <index>  sample1_1.fq  sample1_2.fq
tophat  -G genes.gtf <index>  sample2_1.fq  sample2_2.fq
```
### step2: generate new .gtf files (assemble isoform)

```sh
cufflinks sample1/accepted_hits.bam
cufflinks sample2/accepted_hits.bam
```

### step3: prepare a text file named assemblies.txt with following gtf files

```sh
cat << EOF > assemblies.txt
>sample1/transcript.gtf
>sample2/transcript.gtf
>EOF
```

### step4: run cuffmerge to generate merged.gtf

```sh
cuffmerge -g genes.gtf -s genome.fa assemblies.txt
```

### step5: compare gene expressions of two samples

```sh
cuffdiff merged.gtf  sample1/accepted_hits.bam  sample2/accepted_hits.bam
```

---------------------------------------------------
## The protocol specifically used for our data

### step0: access to the data
Open the web serve at ***, the passwd is ***

The result can be downloaded and viewed in ***

in the shell, type: 'cd ~/new2/RNAseq/trim'

### step1: generate a tophat_out folder with bam files, using only JU1421-1 as example
"-N 8 \ --read-gap-length 8 \ --read-edit-dist 8 \" are generally called mismatch, this means the mismatch for the mapping is 8.
Using this parameter, we can only find 69% JU1421 reads are mapped.

```sh
tophat2 -p 15 -i 20 -I 5000 -g 10 \
-N 8 \
--read-gap-length 8 \
--read-edit-dist 8 \
-o ./tophat_out/JU1421-1  \
-G ../genome/GENES.gff3 \
../genome/cb4_ws242 \
JU1421-1_S1_L001_R1_001_trimpair.fastq.gz,JU1421-1_S1_L001_R2_001_trimpair.fastq.gz\
```
All reads should be mapped using the same parameters. For AF16, the example is:

```sh
tophat2 -p 15 -i 20 -I 5000 -g 10 \
-N 8 \
--read-gap-length 8 \
--read-edit-dist 8 \
-o ./tophat_out/AF16-1  \
-G ../genome/GENES.gff3 \
../genome/cb4_ws242 \
AF16-1_S1_L001_R1_001_trimpair.fastq.gz,AF16-1_S1_L001_R2_001_trimpair.fastq.gz\
```

### step2: generate new .gtf files (assemble isoform)

```sh
cufflinks -p 8 -o ./tophat_out/JU1421-1 ./tophat_out/JU1421-1/accepted_hits.bam
cufflinks -p 8 -o ./tophat_out/JU1421-2 ./tophat_out/JU1421-2/accepted_hits.bam
cufflinks -p 8 -o ./tophat_out/JU1421-3 ./tophat_out/JU1421-3/accepted_hits.bam
cufflinks -p 8 -o ./tophat_out/AF16-1 ./tophat_out/AF16-1/accepted_hits.bam
cufflinks -p 8 -o ./tophat_out/AF16-2 ./tophat_out/AF16-2/accepted_hits.bam
cufflinks -p 8 -o ./tophat_out/AF16-3 ./tophat_out/AF16-3/accepted_hits.bam
```

### step3: prepare a text file named assemblies.txt with following gtf files

```sh
cat << EOF > assemblies.txt
>JU1421-1/transcript.gtf
>JU1421-2/transcript.gtf
>JU1421-3/transcript.gtf
>AF16-1/transcript.gtf
>AF16-2/transcript.gtf
>AF16-3/transcript.gtf
>EOF
```

### step4: run cuffmerge to generate merged.gtf

```sh
cuffmerge -g ../genome/GENES.gff3 -s ../genome/cb4_ws242.fa assemblies.txt
```

### step5: compare gene expressions of two samples

```sh
cuffdiff -p 8 merged.gtf –L JU1421,AF16\
./JU1421-1/accepted_hits.bam,\
./JU1421-2/accepted_hits.bam,\
./JU1421-3/accepted_hits.bam \
./AF16-1/accepted_hits.bam,\
./AF16-2/accepted_hits.bam,\
./AF16-3/accepted_hits.bam \
```
