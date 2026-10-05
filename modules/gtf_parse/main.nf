nextflow.enable.types = true

process GTF_PARSE {
    label 'process_single'
    conda 'conda-forge::python=3.12'

    input:
    gtf: Path

    output:
    file('gene_names.csv')

    script:
    """
    parse_gtf.py -i ${gtf} -o gene_names.csv
    """

    stub:
    """
    touch gene_names.csv
    """
}
