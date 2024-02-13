import unittest
from unittest.mock import patch
from io import StringIO
import simplePortScanner

class TestPortScanner(unittest.TestCase):
    def setUp(self):
        self.host = "127.0.0.1"
        self.ports = [80, 443, 22]
        self.timeout = 1
        self.num_threads = 10

    @patch('sys.stdout', new_callable=StringIO)
    def test_scan_ports(self, mock_stdout):
        expected_output = "\nOpen ports on 127.0.0.1:\n    Port 80 (HTTP) is open\n    Port 22 (SSH) is open\n"
        simplePortScanner.scan_ports(self.host, self.ports, self.timeout, self.num_threads, verbose=True)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_parse_ports(self):
        port_str = "80,22,443"
        expected_ports = [80, 22, 443]
        parsed_ports = simplePortScanner.parse_ports(port_str)
        self.assertEqual(parsed_ports, expected_ports)

        port_str = "1-100"
        expected_ports = list(range(1, 101))
        parsed_ports = simplePortScanner.parse_ports(port_str)
        self.assertEqual(parsed_ports, expected_ports)

    def test_scan_port(self):
        # Test with an open port
        open_port = simplePortScanner.scan_port(self.host, 80, self.timeout)
        self.assertEqual(open_port, 80)

        # Test with a closed port
        closed_port = simplePortScanner.scan_port(self.host, 9999, self.timeout)
        self.assertIsNone(closed_port)

if __name__ == '__main__':
    unittest.main()
