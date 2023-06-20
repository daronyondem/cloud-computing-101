# pip install pypandoc

import pypandoc

input_file = 'Week-12-Case-Study-Discussions/Grading-Paper.md'
output_file = 'Week-12-Case-Study-Discussions/Grading-Paper.pdf'
pdf_engine = 'xelatex'
geometry_options = 'top=0.5in, bottom=0.5in, left=0.5in, right=0.5in'

output = pypandoc.convert_file(
    input_file,
    'pdf',
    outputfile=output_file,
    extra_args=['--pdf-engine=' + pdf_engine, f'--variable=geometry:{geometry_options}']
)

assert output == ""