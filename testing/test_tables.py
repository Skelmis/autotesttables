import io
import sys
import unittest

sys.path.insert(0, "..")
from autotesttables import Table


class TestTables(unittest.TestCase):
    """
    Test the functionality of the Table class
    """

    def test_init(self):
        """
        Tests the __init__ values for the Table class
        """
        cur = Table()
        self.assertEqual(cur.GetTitle(), None, msg="Title")
        self.assertEqual(cur.GetDescription(), None, msg="Description")
        self.assertEqual(cur.GetInput(), None, msg="Input")
        self.assertEqual(cur.GetOutput(), None, msg="Output")
        self.assertEqual(cur.GetStatus(), None, msg="Status")
        self.assertEqual(cur.GetStack(), None, msg="Stack")

    def test_str(self):
        """
        Tests str(Table Instance)
        """
        cur = Table("Title")
        self.assertEqual(str(cur), "Table(Title)")

    def test_repr(self):
        """
        Tests print(Table instance)
        """
        cur = Table("Title")
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        print(cur)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), "Table(Title)\n")

    def test_title(self):
        """
        Tests the title methods

        Input:
        SetTitle() & GetTitle()
        """
        cur = Table()
        cur.SetTitle("test")
        self.assertEqual(cur.GetTitle(), "test")

    def test_description(self):
        """
        Tests the description methods

        Input:
        SetDescription() & GetDescription()
        """
        cur = Table()
        cur.SetDescription("test")
        self.assertEqual(cur.GetDescription(), "test")

    def test_input(self):
        """
        Tests the input methods

        Input:
        SetInput() & GetInput()
        """
        cur = Table()
        cur.SetInput("test")
        self.assertEqual(cur.GetInput(), "test")

    def test_output(self):
        """
        Tests the output methods

        Input:
        SetOutput() & GetOutput()
        """
        cur = Table()
        cur.SetOutput("test")
        self.assertEqual(cur.GetOutput(), "test")

    def test_status(self):
        """
        Tests the status methods

        Input:
        SetStatus() & GetStatus()
        """
        cur = Table()
        cur.SetStatus("test")
        self.assertEqual(cur.GetStatus(), "test")

    def test_stack(self):
        """
        Tests the stack methods

        Input:
        SetStack() & GetStack()
        """
        cur = Table()
        cur.SetStack("test")
        self.assertEqual(cur.GetStack(), "test")

    def test_build(self):
        """
        Tests the table Build method

        Output:
        A Dictionary with relevant data
        """
        cur = Table()
        self.assertDictEqual(
            cur.Build(),
            {
                "title": "",
                "description": "",
                "input": "",
                "output": "",
                "status": "Fail",
                "stack": "",
            },
        )


if __name__ == "__main__":
    unittest.main()
