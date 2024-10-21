with open('/Users/yavuzsebe/Downloads/rosalind_gc.txt', 'r') as inputfasta:
    fasta_dictionary = {}
    fasta_header = ""
    for line in inputfasta:
        line = line.strip()
        if not line:
            continue
        if line.startswith(">"):
            fasta_header = line[1:]
            if fasta_header not in fasta_dictionary:
                fasta_dictionary[fasta_header] = []
            continue
        sequence = line
        fasta_dictionary[fasta_header].append(sequence)
def gc_percent(fastatogc):
    i=0
    gc=0
    while i<len(fastatogc):
        if fastatogc[i]=="G" or fastatogc[i]=="C":
            gc+=1
        i+=1
    gcpercentvalue=gc/len(fastatogc)*100
    return gcpercentvalue   
j=0
compare_dict={}
fasta_dictionary_copy=fasta_dictionary.copy()
while j<len(list(fasta_dictionary)):
    for fasta_elements in list(fasta_dictionary):
        stringsample=""
        list1=stringsample
        list1=fasta_dictionary[list(fasta_dictionary)[j]]
        m=0
        gc_results=0
        stringsample=""
        while m<len(list1):
            for elements in list1:
                stringsample=stringsample+list1[m]
                m+=1
        gc_results=gc_percent(stringsample)
        print(list(fasta_dictionary)[j],gc_results)
        compare_dict[list(fasta_dictionary)[j]]=gc_results
        j+=1
print("\n")
print(list(compare_dict.keys())[list(compare_dict.values()).index(max(list(compare_dict.values())))])
print(max(list(compare_dict.values())))