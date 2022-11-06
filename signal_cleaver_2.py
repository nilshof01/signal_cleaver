import requests as r
from io import StringIO
from Bio import SeqIO
import os
from tkinter.filedialog import askopenfilename

def createFasta(proteinID, filename = "sequences_2_analyze", directory = os.path.dirname(os.path.abspath('lab_project'))): #list
    baseUrl = "http://www.uniprot.org/uniprot/"
    sequences = []
    fastaname = directory + '\\' + filename + '.fasta'
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

def signalP6(proteinIDs, output_folder = os.path.dirname(os.path.abspath('lab_project')) + '\\results', output_formats = 'txt', preferred_mode = ''):
    if os.path.isdir(output_folder) == False and output_folder == os.path.dirname(os.path.abspath('lab_project')) + '\\results':
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
        local_output = output_folder + '\\' + proteinID
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
    signalP6(proteinIDs = input())