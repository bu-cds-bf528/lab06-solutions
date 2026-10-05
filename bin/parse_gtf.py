#!/usr/bin/env python3
"""Extract gene_id and gene_name from every line of a gzipped GTF into a CSV."""
import argparse
import csv
import gzip
import re


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-i", "--input", required=True, help="gzipped GTF file (.gtf.gz)")
    parser.add_argument("-o", "--output", required=True, help="CSV file to write")
    args = parser.parse_args()

    with gzip.open(args.input, "rt") as gtf, open(args.output, "w", newline="") as out:
        writer = csv.writer(out)
        writer.writerow(["gene_id", "gene_name"])
        for line in gtf:
            if line.startswith("#"):
                continue
            attributes = line.rstrip("\n").split("\t")[-1]
            gene_id = re.search(r'gene_id "([^"]*)"', attributes)
            gene_name = re.search(r'gene_name "([^"]*)"', attributes)
            writer.writerow([
                gene_id.group(1) if gene_id else "",
                gene_name.group(1) if gene_name else "",
            ])


if __name__ == "__main__":
    main()
