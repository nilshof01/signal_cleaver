import requests as r
from io import StringIO
from Bio import SeqIO
import os
from tkinter.filedialog import askopenfilename

def createFasta(proteinID, filename = "sequences_2_analyze"): #list
    main_dir = os.path.abspath("")
    baseUrl = "http://www.uniprot.org/uniprot/"
    sequences = []
    fastaname = os.path.join(main_dir, filename + ".fasta")
    if os.path.exists(fastaname) == True:
        os.remove(fastaname)
    else:
        pass
    cID = proteinID
    currentUrl = baseUrl + cID + ".fasta"
    response = r.post(currentUrl)
    cData = ''.join(response.text)
    Seq = StringIO(cData)
    for record in SeqIO.parse(Seq, 'fasta'):
        sequences.append(record)
        SeqIO.write(sequences, fastaname, "fasta")

    return fastaname

def signalP6(proteinIDs, output_formats = "txt", preferred_mode = ''):
    """

    :param proteinIDs: type "file". If you have your IDs in a txt file with one ID per line. Otherwise you have to give them in a list
    :param output_formats: Default is txt.
    :param preferred_mode: ""
    :return: returns you in a loop for all protein IDs in the given file or list the output from signalp6
    """
    main_dir = os.path.abspath("")
    output_folder = os.path.join(main_dir, "results")
    if os.path.isdir(output_folder) == False:
        os.mkdir("results")
    else:
        pass
    if proteinIDs == 'file':
        filename = askopenfilename()
        filename = os.path.abspath(filename)
        with open(filename, 'r') as f:
            proteinids = f.read().splitlines()
    else:
        if type(proteinIDs) != list:
            proteinids = []
            proteinids.append(proteinIDs)
        else:
            proteinids = proteinIDs
    for proteinID in proteinids:
        fastadir = createFasta(proteinID)
        local_output = os.path.join(output_folder, proteinID)
        if not os.path.exists(local_output):
            os.mkdir(local_output)
            fastafile = "--fastafile" + ' ' + fastadir
            output_dir = '--output_dir' + ' ' + local_output
            format = '--format' + ' ' + output_formats
            mode = '--mode' + ' ' + preferred_mode
            run = "signalp6 " + fastafile + ' ' + output_dir + ' ' + ' ' + format + ' ' + mode + ' '
            os.system(run)
        else:
            pass


if __name__ == "__main__":
    print("Enter a protein ID")
    signalP6(proteinIDs = input())
