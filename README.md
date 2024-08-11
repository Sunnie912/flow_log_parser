# Flow Log Parser

This project contains a Python script that parses Amazon VPC Flow Logs and maps each entry to a tag based on a lookup table. It also provides functionality to count occurrences of each tag and port/protocol combination.

## Requirements

- Python 3.6 or higher

No additional libraries are required as the script only uses Python standard libraries.

## Files

- `flow_log_parser.py`: The main script that parses flow logs and generates output.
- `test_flow_log_parser.py`: A test script to validate the functionality of the main script.
- `test_flow_log.txt`: A sample flow log file used for testing.
- `test_lookup_table.csv`: A sample lookup table used for testing.
- `test_expected_output.txt`: The expected output file used to validate test results.

## Usage

To use the flow log parser, run the following command:

```
python flow_log_parser.py <input_file> <lookup_file> <output_file>
```

Where:
- `<input_file>` is the path to your VPC Flow Log file
- `<lookup_file>` is the path to your CSV lookup table
- `<output_file>` is the path where you want the output to be written

Example:
```
python flow_log_parser.py flow_log.txt lookup_table.csv output.txt
```

## Lookup Table Format

The lookup table should be a CSV file with the following columns:
```
dstport,protocol,tag
```

Example:
```
dstport,protocol,tag
22,tcp,sv_P1
3389,tcp,sv_P2
80,tcp,sv_P1
68,udp,sv_P2
443,tcp,sv_P2
53,udp,sv_P3
```

## Output Format

The script generates an output file with two sections:

1. Tag Counts: Shows the count of each tag found in the flow log.
2. Port/Protocol Combination Counts: Shows the count of each unique port and protocol combination found in the flow log.

## Running Tests

To run the tests, execute the following command:

```
python test_flow_log_parser.py
```

This will run the test script, which uses the sample input files (`test_flow_log.txt` and `test_lookup_table.csv`) and compares the output with the expected output (`test_expected_output.txt`).

If the test passes, you will see the message "Test passed! The output matches the expected result." If it fails, the script will show the differences between the expected and actual output.

## Modifying Tests

If you want to modify the tests:

1. Edit `test_flow_log.txt` to change the input flow log entries.
2. Edit `test_lookup_table.csv` to change the lookup table entries.
3. Edit `test_expected_output.txt` to reflect the expected output based on your changes to the input files.

After making changes, run the test script again to validate the results.
