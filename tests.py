from unittest import TestCase
from DocumentConverter import DocumentConverter

class DocumentConverterTest(TestCase):

  def setUp(self):
    self.converter = DocumentConverter(listener=('localhost', 2002))