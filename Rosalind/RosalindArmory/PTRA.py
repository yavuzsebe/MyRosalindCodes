from Bio.Seq import translate

with open("/Users/yavuzsebe/Downloads/rosalind_ptra.txt","r") as inputFileRaw:
    inputFile=inputFileRaw.readlines()
    dnaSeq=inputFile[0].strip()
    protSeq=inputFile[1].strip()

tableIndexList=[1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15, 16, 21, 22, 23, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]

for tableIndex in tableIndexList:
    try:
        dnaSeqTrans=translate(dnaSeq,table=tableIndex,to_stop=True)
        if protSeq==dnaSeqTrans:
            print(tableIndex)
    except ValueError:
        pass