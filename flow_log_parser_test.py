import os
import tempfile
from flow_log_parser import main as process_flow_log

def run_test():
    # Paths to test input and expected output files
    flow_log_file = 'test_flow_log.txt'
    lookup_table_file = 'test_lookup_table.csv'
    expected_output_file = 'test_expected_output.txt'
    
    # Create a temporary output file
    fd, output_file = tempfile.mkstemp()
    os.close(fd)

    try:
        # Check if input files exist
        for file in [flow_log_file, lookup_table_file, expected_output_file]:
            if not os.path.exists(file):
                raise FileNotFoundError(f"Test file not found: {file}")

        # Run the main function
        process_flow_log(flow_log_file, lookup_table_file, output_file)

        # Read the actual output
        with open(output_file, 'r') as f:
            actual_output = f.read().strip()

        # Read the expected output
        with open(expected_output_file, 'r') as f:
            expected_output = f.read().strip()

        # Compare actual output with expected output
        if actual_output == expected_output:
            print("Test passed! The output matches the expected result.")
        else:
            print("Test failed! The output does not match the expected result.")
            print("\nExpected output:")
            print(expected_output)
            print("\nActual output:")
            print(actual_output)
            print("\nDifferences:")
            for i, (expected_line, actual_line) in enumerate(zip(expected_output.split('\n'), actual_output.split('\n'))):
                if expected_line != actual_line:
                    print(f"Line {i+1}:")
                    print(f"  Expected: {expected_line}")
                    print(f"  Actual:   {actual_line}")

    finally:
        # Clean up temporary output file
        os.remove(output_file)

if __name__ == "__main__":
    run_test()