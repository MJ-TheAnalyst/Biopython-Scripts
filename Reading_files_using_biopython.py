# reading a fasta file using the parse() (reading) function from the seqIO (Sequence input/output module)
from Bio import SeqIO
for record in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
    print(record.id)
    print(record.seq)

# reading a fasta file using the parse() (reading), repr() (detailed summary of data type), len() function 
# from the seqIO (Sequence input/output module)

from Bio import SeqIO
from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.fasta.txt","fasta"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))

# genbank example

from Bio import SeqIO
for seq_record in SeqIO.parse("ls_orchid.gbk.txt","genbank"):
    print(seq_record.id)
    print(repr(seq_record.seq))
    print(len(seq_record))
    
    

from Bio.Seq import Seq
my_seq = Seq(input("Enter your sequence here:").upper())
print("Sequence:", my_seq)
print("Complement od sequence:", my_seq.complement())
print("Reverse complement:", my_seq.reverse_complement())
