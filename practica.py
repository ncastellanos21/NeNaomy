from Bio import Entrez
from Bio import SeqIO
from Bio import Seq
Entrez.email = "ncastellanos21@ilg.cat"  # Always tell NCBI who you are

# NM_001354619.2
# NM_001324522.1

with open("resultatexemple.txt", "w") as fitxer:
    handle = Entrez.efetch(db="nucleotide", id="NM_001354619.2,NM_001324522.1", rettype="gb", retmode="text")

    for rec in SeqIO.parse(handle, "gb"):
        k = 0

        fitxer.write("\n")
        fitxer.write(rec.description)
        fitxer.write("\n")

        for i in (rec.features):
            if i.type == 'exon':
                k += 1
                fitxer.write(str("El numero de exon " + str(k) + ": \n"))
                fitxer.write(str(i.location) + "\n")

        for i in (rec.features):
            if i.type == 'CDS':
                k += 1
                fitxer.write(str("El CDS es:" + str(k)) + "\n")
                fitxer.write(str(i.location) + "\n")
                fitxer.write(str(i.qualifiers['translation']) + "\n")

                letras = 0
                for c in i.qualifiers['translation']:
                    if c.isalpha():
                        letras += 1

                return letras
