import glob

def insert_escape(to_fix):
    if '_' not in to_fix:
        return to_fix
    
    index_list = [i for i, char in enumerate(to_fix) if char == '_' or char == "_"]

    i = 0
    for index in index_list:
        to_fix = to_fix[:index + i] + "{backslash}".format(backslash = "\\") + to_fix[index + i:]
        print(to_fix)
        i+=1
        
    return to_fix

def main():
    with open("dsp_doc.tex", 'w') as tex_file:
        tex_file.write("\documentclass[a4paper, 12pt]{article}\n")
        tex_file.write("\\begin{document}\n")

        for file_string in glob.glob("*.txt"):
            with open(file_string) as txt_file:
                file_string_split = file_string.split('.')

                document_string = "\section{section_name}\n"
                document_string_formatted = document_string.format(section_name = "{" + file_string_split[0] + "}")
                tex_file.write(document_string_formatted)

                tex_file.write("\t \\begin{enumerate}\n")
                file_lines = txt_file.readlines()
                for line in file_lines:
                    line_split = line.split(',', 1)
                     #if line_split[0][0] is '_':
                    #     continue
                    line_to_fix_attribute = "\t\t \item {attribute_name}\n".format(attribute_name = line_split[0])

                    fixed_line_attribute = insert_escape(line_to_fix_attribute)
                    tex_file.write(fixed_line_attribute)
                    line_to_fix_type = "\t\t\t {attribute_type}".format(attribute_type=line_split[1])
                    fixed_line_type = insert_escape(line_to_fix_type)
                    tex_file.write(fixed_line_type)
                tex_file.write("\t \\end{enumerate}\n")
        tex_file.write("\end{document}")
                    

main()