from Bio.Seq import Seq
with open("/Users/yavuzsebe/Downloads/rosalind_ini.txt","r") as sequence:
    sequence=sequence.readlines()[0]
print(sequence.count("A"),sequence.count("C"),sequence.count("G"),sequence.count("T"))