#This will be a script to see if the sequence that was put in is either DNA or a protein
#count the amount of letters in said sequence
#and see the difference in lenght of the protein and its corrospondant mRNA

#Author's note: implement a system that uses if and else to see if its DNA or protien.:
        #this can be done by a system that if it recognises any other leters that ATCG it wil see it as protein
#Author's note: implement a simple count system for the letters.


#Fill in a sequence if the sequence contains a M it will list it as a protein if i doesnt have an M its DNA/mRNA
#Proteins will always have an M for its a start codon
sequence = input("Enter your sequence here")
if sequence.find("M") == -1:
    print("This sequence is DNA")
    Ade = sequence.count("A")
    Cyt = sequence.count("C")
    Gua = sequence.count("G")
    Thy = sequence.count("T")
    print("Total amount of A's")
    print(Ade)   
    print("Total amount of C's")
    print(Cyt)
    print("Total amount of G's")
    print(Gua) 
    print("Total amount of T's")
    print(Thy)
    ATCG = Ade + Cyt + Gua + Thy
    print(ATCG)
#It counts the amount of letters for a protein here all revelent letters are listed
else:
    print("This sequence is a protein")
    a=sequence.count("A")
    b=sequence.count("C")
    c=sequence.count("D")
    d=sequence.count("E")
    e=sequence.count("F")
    f=sequence.count("G")
    g=sequence.count("H")
    h=sequence.count("I")
    i=sequence.count("K")
    j=sequence.count("L")
    k=sequence.count("M")
    l=sequence.count("N")
    m=sequence.count("P")
    n=sequence.count("Q")
    o=sequence.count("R")
    p=sequence.count("S")
    q=sequence.count("T")
    r=sequence.count("W")
    s=sequence.count("V")
    t=sequence.count("Y")
    Ptotal = int(a) + int(b) + int(c) + int(d) + int(e) + int(f) + int(g) + int(h) + int(i) + int(j) + int(k) + int(l) + int(m) + int(n) + int(o) + int(p) + int(q) + int(r) + int(s) + int(t)
    print("This is the total amount of letters in the given protein sequence")
    print(Ptotal)
#If Ptotal is the same as the amount of letters for the 5 organisms given to us it will give you the amount of
#letters from its corrospondant mRNA squence that was counted earlier by the atcg counter.
if Ptotal == 919:
   print("The accompanied mRNA sequence has 3125 letters, the organism is the Homo Sapien")
if Ptotal == 1070:
    print("The accompanied mRNA sequence has 3770 letters, the organism is the Xenopus laevis")
if Ptotal == 1192:
    print("The accompanied mRNA sequence has 3579 letters, the organims is the Dictyostelium discoideum")
if Ptotal == 773:
    print("The accompanied mRNA sequence has 2322 letters, the organsim is the Caenorhabditis elegans")
if Ptotal == 790:
    print("The accompanied mRNA sequence has 2754 letters, the organism is the Arabidopsis thaliana")
#DERK% berekend door het gerbuik van c,d,o en i
DERKTotal = int(c) + int(d) + int(o) + int(i)
print("The amount of D's in a protein are")
print(c)
print("The amount of E's in a protein are")
print(d)
print("The amount of R's in a protein are")
print(o)
print("The amount of K's in a protein are")
print(i)
print("The total amount of DERK is")
print(DERKTotal)
#DERK% in the protein is derk / ptotal * 100
DERKP = int(DERKTotal) / int(Ptotal) * int(100)
print("DERK% of the protein")
print(DERKP)
#Using a simple equasion to see if the DERK% in a protein is positive, negative or has no charge
DE = int(c) + int(d)
RK = int(o) + int(i)
lading = int(RK) - int(DE)
if lading == 0:
    print("There is no charge")
if lading > 0:
    print("There is a positive charge")
if lading < 0:
    print("There is a negative charge")
