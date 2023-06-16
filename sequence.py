#!/usr/bin/python

# run all:  pytest -v sequence.py
# run one:  pytest -v sequence.py -m apitest

import pytest



# pytestmark = [pytest.mark.ABC]



class SeqUtils:

   def getSeqs(self):
      """ Set and return sequences (Get from database or files usually; here hard-coded) """ 
      seqA = 'gggaccagat ggattgtagg gagtagggta caatacagtc tgttctcctc cagctccttc tttctgcaac \
         atggggaaga acaaactcct tcatccaagt ctggttcttc tcctcttggt cctcctgccc acagacgcct \
         cagtctctgg aaaaccgcag tatatggttc tggtcccctc cctgctccac actgagacca ctgagaaggg'

      seqB = 'ctgtgtcctt ctgagctacc tgaatgagac agtgactgta agtgcttcct tggagtctgt caggggaaac \
         aggagcctct tcactgacct ggaggcggag aatgacgtac tccactgtgt cgccttcgct gtcccaaagt \
         cttcatccaa tgaggaggta atgttcctca ctgtccaagt gaaaggacca acccaagaat ttaagaagcg'

      return (seqA, seqB)


   def __init__(self):
      """ Set sequence information """
      self.seqA, self.seqB = self.getSeqs()


   def getManipulatedList(self):
      """Change sequence from string to list and alter it"""
      seqA = self.seqA.translate(str.maketrans('', '', ' \n\t\r'))
      seqB = self.seqB.translate(str.maketrans('', '', ' \n\t\r'))
      seq = seqA + seqB
      seqL = list(seq)
      seqL.sort(reverse=True)

      return seqL


   def getChromSet(self):
      """From a large list of chromosomes, filter out the unique ones"""
      seqL = self.getManipulatedList()
      return set(seqL)




@pytest.mark.apitest
def test_alter_sequence():
   """Unit Test marked as an API test."""

   su = SeqUtils()

   manList = su.getManipulatedList()

   assert manList[0] == 't'


@pytest.mark.webtest
def test_bases():
   """Unit Test marked as a Web test."""

   expected = {'a', 'c', 't', 'g'}

   su = SeqUtils()
   uniqBases = su.getChromSet()

   assert uniqBases == expected


@pytest.mark.webtest
def test_len_bases():
   """Unit Test marked as a Web test."""

   su = SeqUtils()
   uniqBases = su.getChromSet()

   assert len(uniqBases) == 4

