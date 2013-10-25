from unittest import TestCase
from DocumentConverter import DocumentConverter, DocumentConversionException

class DocumentConverterTest(TestCase):

  def setUp(self):
    self.converter = DocumentConverter(listener=('localhost', 2002))

  def test_failed_to_connect(self):
    with self.assertRaises(DocumentConversionException):
      DocumentConverter(listener=('localhost', 1337))
