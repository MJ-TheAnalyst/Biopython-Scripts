
# reading a fasta file.

with open("sequence.fasta.txt","r") as file:

    for line in file:
        print(line)

# remove empty spaces and new lines

with open("sequence.fasta.txt", "r") as file:
    for line in file:

        line = line.strip()
        print(line)           # notice how there's no space in the result because the strip command removes newline character.



# to separate headers from sequence:

with open("sequence.fasta.txt", "r") as file:
    for line in file:
        line = line.strip()

        if line.startswith(">"):
            print("headers:", line)

        else:
            print("sequence:", line)


# sample biological analysis
with open("Sequence.fasta.txt", "r") as file:

    for line in file:
        line = line.strip()

        if not line.startswith(">"):

            print("sequence:", line)

            print("A:", line.count("A"))
            print("G:", line.count("G"))
            print("C:", line.count("C"))
            print("T:", line.count(""))


# reading FASTQ files
with open("sequence.fastq.txt", "r") as file2:
    while True:
        header = file2.readline().strip()
        sequence = file2.readline().strip()
        plus = file2.readline().strip()
        quality = file2.readline().strip()

        if not header:
            break

        print("Header:", header)
        print("Sequence:", sequence)
        print("plus:", plus)
        print("Quality:", quality)

# Because of the nature of the file having 4 lines we have to group each command into 4 lines to represent 
# the 4 lines in the files


# reading CSV files

with open("genes.csv", "r") as file3:
    for line in file3:
        line = line.strip()
        print(line)


import csv 
with open("genes.csv", "r") as file3:
    reader = csv.reader(file3)
    for row in header:
        print (row)