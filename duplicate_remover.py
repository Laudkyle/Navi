def remove_duplicates(input_file, output_file):
    # Keep track of encountered lines using a set
    encountered_lines = set()

    # Read all lines from the file, convert to lowercase, and add to the set
    with open(input_file, 'r', encoding='utf-8') as file:
        for line in file:
            lower_line = line.strip().lower()
            encountered_lines.add(lower_line)

    # Write unique lines back to the file
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(encountered_lines))



remove_duplicates("objects.txt", "objects_cleansed.txt")
