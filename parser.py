import json, glob

def main():
    for  json_file_string in glob.glob('*.json'):
        with open(json_file_string) as json_file:
            file_as_json = json.load(json_file)
            file_name = json_file_string.split(".")
            with open(file_name[0] + ".txt", "w") as output_file:
                dict_items = file_as_json[file_name[0]].items()
                for pair in dict_items:
                    output_file.write(pair[0] + "," + pair[1] + "\n")

main()
