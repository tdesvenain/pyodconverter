from unittest import TestCase
from DocumentConverter import DocumentConverter, DocumentConversionException

class DocumentConverterTest(TestCase):

  def setUp(self):
    self.converter = DocumentConverter(listener=('localhost', 2002))

  def test_fail_connect(self):
    with self.assertRaises(DocumentConversionException):
      DocumentConverter(listener=('localhost', 1337))

  def test_not_existing_document(self):
    input = "kittens.docx"
    output = "docs.pdf"
    with self.assertRaises(DocumentConversionException):
      self.converter.convert(input, output)
