import urllib
from collections import namedtuple
import pandas as pd
from glob import glob

def read_gff(output_name):
    global_dataframe = pd.DataFrame()
    gffInfoFields = ["seqid", "source", "type", "start", "end", "score", "strand", "phase", "attributes"]
    GFFRecord = namedtuple("GFFRecord", gffInfoFields)
    folders = glob(r"C:\Users\nils\PycharmProjects\lab_project\results\*")
    for folder in folders:
        files = glob(folder + "\*")
        for file in files:
            if file.endswith("output.gff3") and not file.endswith("region_output.gff3"):
                with open(file) as infile:
                    for line in infile:
                        parts = line.strip().split("\t")
                        if len(parts) > 2:


                            # If this fails, the file format is not standard-compatible

                            assert len(parts) == len(gffInfoFields)
                                # Normalize data
                            normalizedInfo = {
                                    "seqid": None if parts[0] == "." else urllib.parse.unquote(parts[0]),
                                    "source": None if parts[1] == "." else urllib.parse.unquote(parts[1]),
                                    "type": None if parts[2] == "." else urllib.parse.unquote(parts[2]),
                                    "start": None if parts[3] == "." else int(parts[3]),
                                    "end": None if parts[4] == "." else int(parts[4]),
                                    "score": None if parts[5] == "." else float(parts[5]),
                                    "strand": None if parts[6] == "." else urllib.parse.unquote(parts[6]),
                                    "phase": None if parts[7] == "." else urllib.parse.unquote(parts[7]),
                                 #   "attributes": parseGFFAttributes(parts[8])
                                }

                            local_dataframe = pd.DataFrame(normalizedInfo, index = [0])
                            global_dataframe = pd.concat([global_dataframe, local_dataframe])
    global_dataframe.to_excel(output_name)
