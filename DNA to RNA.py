input = input("Insert strand here ")
strand = ""
Useful = False
STOP = "UAA", "UAG", "UGA"
MET = "AUG"
PHE = "UUC", "UUU"
LEU = "UUA", "UUG", "CUU", "CUC", "CUA", "CUG"
ILE = "AUU", "AUC", "AUA"
VAL = "GUU", "GUC", "GUA", "GUG"
SER = "UCU", "UCC", "UCG", "UCA", "AGU", "AGC"
PRO = "CCU", "CCC", "CCG", "CCA"
THR = "ACU", "ACC", "ACG", "ACA"
TYR = "UAU", "UAC"
HIS = "CAU", "CAC"
GLN = "CAA", "CAG"
ASN = "AAU", "AAC"
LYS = "AAG", "AAA"
CYS = "UGU", "UGC"
TRP = "UGG"
ARG = "CGU", "CGA", "CGG", "CGC", "AGA", "AGG"
ASP = "GAU", "GAC"
GLU = "GAA", "GAG"
ALA = "GCC", "GCU", "GCA", "GCG"
GLY = "GGC", "GGU", "GGA", "GGG"
AA = "MET", "PHE", "LEU", "ILE", "VAL", "SER", "PRO", "THR", "TYR", "HIS", "GLN", "ASN", "LYS", "CYS", "TRP", "ARG", "ASP", "GLU", "ALA", "GLY", "STOP"
input = input.upper()
for x in input:
    if x == "T" or x == "A" or x == "C" or x == "G":
        strand += x
strand = strand.replace("A", "U")
strand = strand.replace("T", "A")
strand = strand.replace("C", "!")
strand = strand.replace("G", "C")
strand = strand.replace("!", "G")
print("Raw Code:", strand)
rna = ""
y = 0
for x in strand:
    y += 1
    rna += x
    if y == 3:
        rna += " "
        y = 0
print("Codons:", rna)
rna = rna.split(" ")
strand = ""
for x in rna:
    if x in MET:
        Useful = True
    if Useful == True:
        strand += x + " "
    if x in STOP:
        Useful = False
print("NO JUNK:", strand)
nojunkstrand = strand.split(" ")
strand = ""
nojunk = ""
for x in rna:
    if len(x) > 2:
        for y in AA:
            if x in globals()[y]:
                strand += y + " "
for x in nojunkstrand:
    if len(x) > 2:
        for y in AA:
            if x in globals()[y]:
                nojunk += y + " "
print("Amino Acids:", strand)
print("Amino Acids With No Junk:", nojunk)