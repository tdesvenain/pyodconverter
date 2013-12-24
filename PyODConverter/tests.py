import os
from unittest import TestCase
from PyODConverter import DocumentConverter, DocumentConversionException

TEST_DATA_PATH = os.path.normpath(os.path.join(os.path.dirname(__file__),
                                               os.path.pardir,
                                               'test_data'))
ODT_FILE_PATH = os.path.join(TEST_DATA_PATH, 'document.odt')
DOCX_FILE_PATH = os.path.join(TEST_DATA_PATH, 'document.docx')
PDF_FILE_PATH = os.path.join(TEST_DATA_PATH, 'document.pdf')


class DocumentConverterTest(TestCase):

    def setUp(self):
        self.converter = DocumentConverter(listener=('localhost', 2002))

    def test_fail_connect(self):
        with self.assertRaises(DocumentConversionException):
            DocumentConverter(listener=('localhost', 1337))

    def test_not_existing_document(self):
        with self.assertRaises(DocumentConversionException):
            self.converter.convert("kittens.docx", "docs.pdf")

    def test_convert_docx_to_pdf(self):
        self.converter.convert(DOCX_FILE_PATH, PDF_FILE_PATH)
        self.assertTrue(os.path.exists(PDF_FILE_PATH))

    def test_convert_odt_to_pdf(self):
        self.converter.convert(ODT_FILE_PATH, PDF_FILE_PATH)
        self.assertTrue(os.path.exists(PDF_FILE_PATH))

    def tearDown(self):
        """
        Cleanup
        """
        if os.path.exists(PDF_FILE_PATH):
            os.remove(PDF_FILE_PATH)
