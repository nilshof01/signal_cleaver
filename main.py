import requests as r

from Bio import SeqIO

from io import StringIO

import mechanize
from os.path import normpath
import re

import time

from six.moves import urllib

from bs4 import BeautifulSoup

myList = ['P23028']

for x in myList:

    cID = x

    url = 'https://services.healthtech.dtu.dk/services/SignalP-6.0/1-Submission.php'

    pattern = re.compile("\d+")

    baseUrl = "http://www.uniprot.org/uniprot/"

    currentUrl = baseUrl + cID + ".fasta"

    response = r.post(currentUrl)

    cData = ''.join(response.text)

    Seq = StringIO(cData)

    pSeq = list(SeqIO.parse(Seq, 'fasta'))

    print(pSeq[0].id)

    fas = pSeq[0].seq

    br = mechanize.Browser()

    br.set_handle_robots(False)  # ignore robots

    br.open(url)


    # here I don't know yet how to handle the form

    def select_form(form):

        return form.attrs.get('action', None) == '/cgi-bin/webface2.fcgi'


    br.select_form('')

    br.form[''] = str(fas)

    res = br.submit()

    content = res.read()

    # stuff below here depend on how I can handle the previous form

    soup = BeautifulSoup(content, "html.parser")

    one_a_tag = soup.findAll('a')[0]

    link = one_a_tag['href']

    # print(link)

    time.sleep(8)

    urllib.request.urlretrieve(link, '%s.html' % cID)

    for i, line in enumerate(open('%s.html' % cID)):

        for match in re.finditer(pattern, line):
            print
            '%s' % (match.group()), cID