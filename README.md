# MycoApollo 

MycoApollo (Mycobacterium + Apollo, Greek God of healing, diseases, and knowledge) is a tool built in Python that allows orthologs visualisation. It also provides summarised information from each gene for Mycobacterium tuberculosis variant bovis AF2122/97, Mycobacterium tuberculosis H37Ra, Mycobacterium tuberculosis H37Rv and Mycolicibacterium smegmatis MC2 155.

## Content
- H37RA.fasta = FASTA file for Mycobacterium tuberculosis H37Ra.
- H37RA.gbk = GenBank file for Mycobacterium tuberculosis H37Ra.
- H37RA_data1.csv = Content created with 'Pre-MycoApollo.py' for Mycobacterium tuberculosis H37Ra. The 1 indicates the version number.

- Tuberculosis.fasta = FASTA file for Mycobacterium tuberculosis H37Rv.
- Tuberculosis.gbk = GenBank file for Mycobacterium tuberculosis H37Rv.
- Tuberculosis_data1.csv = Content created with 'Pre-MycoApollo.py' for Mycobacterium tuberculosis H37Rv. The 1 indicates the version number.

- Smegmatis.fasta = FASTA file for Mycolicibacterium smegmatis MC2 155.
- Smegmatis.gbk = GenBank file for Mycolicibacterium smegmatis MC2 155.
- Smegmatis_data1.csv = Content created with 'Pre-MycoApollo.py' for Mycolicibacterium smegmatis MC2 155. The 1 indicates the version number.

- Bovis.fasta = FASTA file for Mycobacterium tuberculosis H37Ra.
- Bovis.gbk = GenBank file for Mycobacterium tuberculosis H37Ra.
- Bovis_data1.csv = Content created with 'Pre-MycoApollo.py' for Mycobacterium tuberculosis H37Ra. The 1 indicates the version number.
-
- locus_alignment_info.csv = CSV file with summarised information for orthologs. This file was created in Mauve and edited manually in Excel.
- MycoApollo.ipynb = It contains the script for MycoApollo. The format is in JupyterNotebook to facilitate its use.
- Pre-MycoApollo.py = It contains the script to create the CSV files. You only need this script if you wish to change the genomes used for MycoApollo.

## What you need to do to run MycoApollo

1.Download all the content to your computer.

2.If you are using macOS or Linux, download MUSCLE from: http://www.drive5.com/muscle/. No installation is needed. If you are using Windows, download MUSCLE from the previous website and make sure you add the PATH for MUSCLE to the list of paths recognised by Windows so that it can run MUSCLE from JupyterNoteBook instead of the CommandLine.

3.This code is intended to work for JupyterNotebook. You can make any necessary changes if you wish to run it elsewhere. However, you must change all the paths where you have the code, and the content saved. For example, path_to_bovis = "/Users/dissertation/Documents/Dissertation-real/cgi-mycoapollo/db/genomes/Bovis_data1.csv", you need to adapt this so that it works on your laptop.

## Change the selected genomes.
1. Download the GenBank files and FASTA files for the genomes.
2. Run the GenBank files using Mauve. 
3. Edit the alignment orthologs information to much 'locus_alignment_info.csv.'
4. Edit all the paths for the new genomes and rename them.
5. Follow the steps and 'what you need to do to run MycoApollo'.
