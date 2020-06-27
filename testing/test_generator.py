import io
import sys
import unittest

sys.path.insert(0, "..")
from autotesttables import Generator, Table


class TestGenerator(unittest.TestCase):
    """
    A class used to test the Generator methods
    """

    def test_generatorInit(self):
        """
        Test __init__ values
        """
        cur = Generator()
        self.assertEqual(cur.GetReportTitle(), "Test Tables", msg="Report Title")
        self.assertEqual(cur.GetReportDescription(), "", msg="Report Description")
        self.assertEqual(cur.GetSuccessCount(), 0, msg="Success count")
        self.assertEqual(cur.GetFailureCount(), 0, msg="Failure count")
        self.assertEqual(cur.GetErrorCount(), 0, msg="Error count")
        self.assertEqual(cur.tables, {}, msg="Tables")

    def test_reportTitle(self):
        """
        Test the methods handling report titles

        Input:
        SetReportTitle() & GetReportTitle()
        """
        cur = Generator()
        cur.SetReportTitle("test")
        self.assertEqual(cur.GetReportTitle(), "test")

    def test_reportDescription(self):
        """
        Test the methods handling report descriptions

        Input:
        SetReportDescription() & GetReportDescription()
        """
        cur = Generator()
        cur.SetReportDescription("test")
        self.assertEqual(cur.GetReportDescription(), "test")

    def test_mode(self):
        """
        Test the methods handling report modes

        Input:
        SetReportTitle() & GetMode()
        """
        cur = Generator()
        cur.SetReportTitle("test")
        self.assertEqual(cur.GetReportTitle(), "test")

    def test_invalidMode(self):
        """
        Sets the mode, but with an invalid input
        """
        cur = Generator()
        with self.assertRaises(Exception):
            cur.SetMode("Test")

    def test_reportSuccessCount(self):
        """
        Test the methods handling report sucess counts

        Input:
        SetSuccessCount() & GetSuccessCount()
        """
        cur = Generator()
        cur.SetSuccessCount(2)
        self.assertEqual(cur.GetSuccessCount(), 2)

    def test_reportInvalidSucess(self):
        """
        Test the methods handling report sucess counts with invalid input

        Input:
        SetSuccessCount() & GetSuccessCount()
        """
        cur = Generator()
        with self.assertRaises(ValueError):
            cur.SetSuccessCount("test")
        self.assertEqual(cur.GetSuccessCount(), 0)

    def test_reportFailureCount(self):
        """
        Test the methods handling report failure counts

        Input:
        SetFailureCount() & GetFailureCount()
        """
        cur = Generator()
        cur.SetFailureCount(2)
        self.assertEqual(cur.GetFailureCount(), 2)

    def test_reportInvalidFailure(self):
        """
        Test the methods handling report failure counts with invalid input

        Input:
        SetFailureCount() & GetFailureCount()
        """
        cur = Generator()
        with self.assertRaises(ValueError):
            cur.SetFailureCount("test")
        self.assertEqual(cur.GetFailureCount(), 0)

    def test_reportErrorCount(self):
        """
        Test the methods handling report error counts

        Input:
        SetErrorCount() & GetErrorCount()
        """
        cur = Generator()
        cur.SetErrorCount(2)
        self.assertEqual(cur.GetErrorCount(), 2)

    def test_reportInvalidError(self):
        """
        Test the methods handling report error counts with invalid input

        Input:
        SetErrorCount() & GetErrorCount()
        """
        cur = Generator()
        with self.assertRaises(ValueError):
            cur.SetErrorCount("test")
        self.assertEqual(cur.GetErrorCount(), 0)

    def test_filename(self):
        """
        Test the methods handling filenames

        Input:
        SetFilename() & GetFilename()
        """
        cur = Generator()
        cur.SetFilename("test")
        self.assertEqual(cur.GetFilename(), "test")

    def test_addTable(self):
        """
        Tests the ability to add tables to our generator

        Input:
        Table instance
        """
        cur = Generator()
        table = Table()
        cur.AddTable(table)
        self.assertEqual(len(cur.tables), 1)

    def test_invalidAddTable(self):
        """
        Tests the ability to add tables to our generator
        but with incorrect input types

        Input:
        Table instance
        """
        cur = Generator()
        with self.assertRaises(Exception):
            cur.AddTable(Generator())

    def test_addDuplicateTable(self):
        """
        Tests the ability to add tables to our generator
        but with duplicate table titles

        Input:
        Table instance
        """
        cur = Generator()
        cur.AddTable(Table("Test"))
        with self.assertRaises(KeyError):
            cur.AddTable(Table("Test"))

    def test_getTable(self):
        """
        Tests the abilty to get tables back out

        Output:
        Table instance
        """
        cur = Generator()
        t = Table("Test")
        cur.AddTable(t)
        data = cur.GetTable("Test")
        self.assertEqual(data, t)


if __name__ == "__main__":
    unittest.main()
