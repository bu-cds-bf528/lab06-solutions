nextflow.enable.types = true

process GTF_DOWNLOAD {
    label 'process_single'
    conda 'conda-forge::wget=1.25.0'

    input:
    url: String

    output:
    file(url.tokenize('/')[-1])

    script:
    """
    wget -O ${url.tokenize('/')[-1]} '${url}'
    """
}
