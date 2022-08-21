#!/usr/bin/python3

"""
This is the database, extracting the information that we need from the genbank files.
This is to be run only once. Once the csv file is obtained, we do not need to run this further.
"""

from Bio import SeqIO
from Bio.SeqUtils import GC
from Bio.Seq import Seq
from Bio.SeqUtils.ProtParam import ProteinAnalysis
import pandas as pd
import operator

#We open the file the genbank file tuberculosis
gb_file_h37ra = "../dissertation/cgi-mycoapollo/db/genomes/H37RA.gbk"
sequence_h37ra = SeqIO.read(gb_file_h37ra, "gb")

def genes_extractor(path_file):
    genes = []
    for rec in SeqIO.parse(path_file, "genbank"):
        if rec.features:
            for feature in rec.features:
                #Not every gen contains a name or locus name. Therefore, when parsing genbank files
                #We make sure that we obtain all this information
                if feature.type == "gene":
                    if "gene" in feature.qualifiers:
                        fq_gene = feature.qualifiers["gene"][0]
                    else:
                        fq_gene = ""
                    if "locus_tag" in feature.qualifiers:
                        fq_locus = feature.qualifiers["locus_tag"][0]
                    else:
                        fq_locus = ""
                    #All the information obtained is stored then in a line that corresponds to each gen from the parsed
                    #genbank file
                    line = str(feature.location.start.position) +'\t'+ str(feature.location.end.position)+ '\t' + str(feature.location.strand) + '\t'+ fq_locus + '\t' + fq_gene + '\n'
                    genes.append(line)

    #This function returns a list (start position, end, strand location, locus and/or gen name)
    return(genes)

genes = genes_extractor(gb_file_h37ra)

#The gen information will be separated and stored into a new list of data
genes_fixed = []
for info in genes:
    info = info.split('\t')
    genes_fixed.append(info)

#This new list is converted into the information that we have obtained from the previous function
start = [i[0] for i in genes_fixed]
end = [i[1] for i in genes_fixed]
strand = [i[2] for i in genes_fixed]
locus_name = [i[3] for i in genes_fixed]
gen_name = [i[4] for i in genes_fixed]

#To avoid problems created when getting the size of the genes, we copied the necessary lists
#and simply create a new list for the size of each gen
copy_start = start
copy_end = end
size_gen = []
zip_object = zip(copy_start, copy_end)
for copy_start, copy_end in zip_object:
    size_gen.append(int(copy_end)-int(copy_start))

def sequence_extractor(path_file):
    sequences = []
    genes = []
    for feature in path_file.features:
        if feature.type=='gene':
            genes.append(feature)
    ref = genes[0]
    #Using Biopython we can simply obtain references once we've got the genes
    for ref in genes:
        ref_extract = ref.extract(path_file)
        seq = ref_extract.seq
        sequences.append(seq)
    #This function returns a list of sequences
    return(sequences)

sequences = sequence_extractor(sequence_h37ra)

#The lists of data are zipped together and sent to a csv file for the BL layer to use
h37ra_data = pd.DataFrame(list(zip(start, end, difference, strand, locus_name, gen_name, sequences),
                              columns = ['Start position', 'End position', 'Size gen',
                                         'Strand Location', 'Locus', 'Gen name', 'Sequences']))

h37ra.to_csv('../dissertation/cgi-mycoapollo/db/genomes/H37RA_data.csv')
