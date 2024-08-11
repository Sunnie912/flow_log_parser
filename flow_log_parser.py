import csv
from collections import defaultdict
import io
import sys

def load_lookup_table(lookup_file):
    lookup = {}
    with open(lookup_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            key = (int(row['dstport']), row['protocol'].lower())
            lookup[key] = row['tag']
    return lookup

def process_flow_log(input_file, lookup_table, output_file):
    tag_counts = defaultdict(int)
    port_protocol_counts = defaultdict(int)

    with io.open(input_file, 'r', encoding='ascii') as infile, \
         io.open(output_file, 'w', encoding='ascii') as outfile:
        
        for line in infile:
            fields = line.strip().split()
            if len(fields) < 14:  # Ensure we have at least the required fields
                continue

            # Extract relevant fields
            dstport = int(fields[6])  # dstport is the 7th field (0-indexed)
            protocol = fields[7].lower()  # protocol is the 8th field

            key = (dstport, protocol)
            tag = lookup_table.get(key, 'Untagged')
            
            tag_counts[tag] += 1
            port_protocol_counts[key] += 1

        # Write tag counts
        outfile.write("Tag Counts:\n")
        outfile.write("Tag             Count\n")
        for tag, count in sorted(tag_counts.items()):
            outfile.write(f"{tag:<15} {count}\n")
        
        outfile.write("\nPort/Protocol Combination Counts:\n")
        outfile.write("Port    Protocol    Count\n")
        for (port, protocol), count in sorted(port_protocol_counts.items()):
            outfile.write(f"{port:<8} {protocol:<12} {count}\n")

def main(input_file, lookup_file, output_file):
    lookup_table = load_lookup_table(lookup_file)
    process_flow_log(input_file, lookup_table, output_file)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input_file> <lookup_file> <output_file>")
        sys.exit(1)

    main(sys.argv[1], sys.argv[2], sys.argv[3])