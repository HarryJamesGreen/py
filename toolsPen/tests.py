import unittest
from unittest.mock import patch
from io import StringIO
import sys
import toolsPen.portScannerSynScan as portScannerSynScan

class TestPortScanner(unittest.TestCase):

    @patch('sys.argv', ['portScanner.py', 'example.com'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_scan_successful(self, mock_stdout):
        # Mock the behavior of the scan_ports function
        with patch('portScanner.scan_ports') as mock_scan_ports:
            mock_scan_ports.return_value = [80, 443]  # Mocking open ports

            # Call the main function
            portScannerSynScan.main()

            # Check the output
            expected_output = "Scanning ports 1-1024 on example.com...\nOpen ports on example.com:\n    Port 80 is open\n    Port 443 is open\nScan completed in 0.00 seconds\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.argv', ['portScanner.py', 'example.com'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_scan_no_open_ports(self, mock_stdout):
        # Mock the behavior of the scan_ports function
        with patch('portScanner.scan_ports') as mock_scan_ports:
            mock_scan_ports.return_value = []  # Mocking no open ports

            # Call the main function
            portScannerSynScan.main()

            # Check the output
            expected_output = "Scanning ports 1-1024 on example.com...\nOpen ports on example.com:\n    No open ports found\nScan completed in 0.00 seconds\n"
            self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
