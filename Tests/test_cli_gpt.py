import unittest
from unittest.mock import patch, MagicMock, mock_open
import os 
from cli_agent import read_file, ask_llm, format_llm_answer

class TestCliGpt(unittest.TestCase):

    def test_read_file(self):
        m = mock_open(read_data="file's content")
        with patch("builtins.open", m):
            res = read_file("path")
            self.assertEqual(res, "file's content")
            m.assert_called_once_with("path", 'r')
    
    def test_format_llm_answer(self):

        input_str = "Hy \\033[913ab\\033[0m"
        expected_str = "Hy \033[91ab\033[0m"
        self.assertEqual(format_llm_answer(input_str), expected_str)

        # Test replacing double backslash escaped codes
        input_str_2 = "Hy \\\\033[mock\\\\033[77"
        expected_str_2 = "Hy \033[mock\033[77"
        self.assertEqual(format_llm_answer(input_str_2), expected_str_2)

        # Test no changes
        input_str_3 = "Mock Testing"
        self.assertEqual(format_llm_answer(input_str_3), "Mock Testing")