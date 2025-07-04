from Bio import SeqIO

with open("/Users/yavuzsebe/Downloads/rosalind_bphr.txt","r") as inputFileRaw:
    inputFile=inputFileRaw.readlines()
    thresholdAndpercentage=inputFile.pop(0).strip()
    threshold=thresholdAndpercentage.split()[0]
quality = int(threshold)

with open("/Users/yavuzsebe/Downloads/rosalind_bphr_main.txt","w") as outputFile:
	for i in inputFile:
		outputFile.write(i)

records = list(SeqIO.parse("/Users/yavuzsebe/Downloads/rosalind_bphr_main.txt", "fastq"))

recordLen=len(records[0].letter_annotations["phred_quality"])
recordCount=len(records)

qualityList=[[] for _ in range(recordLen)]
for i in records:
	for j in range(0,recordLen):
	    qualityList[j].append(i.letter_annotations["phred_quality"][j])

columnSum=0
belowCount=0
for i in qualityList:
	columnSum=0
	for j in i:
		columnSum+=j
	if (columnSum/recordCount)<quality:
		belowCount+=1

print(belowCount)