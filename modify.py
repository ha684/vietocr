# Define the function to replace the path
def replace_path(data):
    new_data = []
    for line in data:
        new_line = line.replace("D:\\Data\\image_random\\random\\", "InkData_line_processed/")
        new_data.append(new_line)
    return new_data

# Read the file, replace the paths, and write back to the file
input_file_path = r'D:\Data\image_random\train_annotation.txt'
output_file_path = r'D:\Data\image_random\train_annotation.txt'

with open(input_file_path, 'r', encoding='utf-8') as file:
    data = file.readlines()

# Replace the paths
updated_data = replace_path(data)

# Write the updated data to a new file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(updated_data)

print("Paths have been replaced and the updated file is saved as 'train_annotation_updated.txt'.")
