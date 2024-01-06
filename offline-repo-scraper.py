import os

def get_all_files(directory, ignore_patterns):
    """
    Yields the path of each file in a directory, excluding those that match the ignore patterns.
    """
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not any(pattern.lower() in file.lower() for pattern in ignore_patterns):
                yield os.path.join(root, file)

def combine_files(repo_dir, output_file, ignore_patterns):
    """
    Combines all files from a repository into a single text file, ignoring specified patterns.
    """
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for file in get_all_files(repo_dir, ignore_patterns):
            try:
                with open(file, 'r', encoding='utf-8') as infile:
                    outfile.write(infile.read())
                    outfile.write("\n\n")
            except Exception as e:
                print(f"Skipping file {file} due to error: {e}")

local_repo_dir = r"C:\Users\SomeRandomAssFolder\Downloads\YourDownloadedRepoFolder"
output_text_file = "scraped.txt"
ignore_files = ["readme", "license", "contributing"]

combine_files(local_repo_dir, output_text_file, ignore_files)

print(f"All files have been combined into {output_text_file}")
