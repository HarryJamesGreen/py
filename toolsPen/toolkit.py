import argparse
import sys
from simplePortScanner import main as simple_port_scanner_main

def main():
    print("Welcome to the Penetration Testing Toolkit!")
    print("This toolkit allows you to perform various penetration testing tasks.")

    parser = argparse.ArgumentParser(description="Penetration Testing Toolkit CLI", formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers(dest='tool', help='Select the tool to use')

    # Add subparser for each tool
    simple_port_scanner_parser = subparsers.add_parser('port-scan', help='Port Scanner Tool')
    simple_port_scanner_parser.add_argument("host", help="Target IP address or hostname")
    simple_port_scanner_parser.add_argument("-p", "--ports", default="1-1024", help="Port range to scan (default: 1-1024)")
    simple_port_scanner_parser.add_argument("-t", "--timeout", type=float, default=1, help="Timeout for port connection (default: 1 second)")
    simple_port_scanner_parser.add_argument("-T", "--threads", type=int, default=10, help="Number of threads for scanning (default: 10)")
    simple_port_scanner_parser.add_argument("-v", "--verbose", action="store_true", help="Verbose output")
    simple_port_scanner_parser.add_argument("-L", "--logfile", help="Path to logfile")

    # Add subparser for other tools as needed

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    try:
        args = parser.parse_args()
    except TypeError:
        print("Error: Incorrect number of arguments provided.")
        parser.print_help(sys.stderr)
        sys.exit(1)

    if args.tool == "port-scan":
        simple_port_scanner_main(args)
    # Add other tool handlers here
    else:
        print("Error: Invalid tool selected.")
        parser.print_help(sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
