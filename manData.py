import os

def combine_csv_files(new_csv_file, csv_files):
    """
    Combine multiple csv files into a single csv file.
    Parameters:
    new_csv_file: str
        The name of the new csv file that will be created.
        If the file already exists, it will be overwritten.
    csv_files: list of tuples
        A list of tuples where each tuple contains the name of a csv file and the line numbers that will be copied to the new csv file.
        The line numbers are 0-based.
        Example:
        [('file1.csv', 0, 10), ('file2.csv', 5, 15, 2)]
    
    """
    if os.path.exists(new_csv_file):
        os.remove(new_csv_file)
    for csv_file in csv_files:
        csv_file_name = csv_file[0]
        line_start = csv_file[1]
        line_end = csv_file[2]
        if len(csv_file) == 4:
            line_step = csv_file[3]
        else:
            line_step = 1
        with open(csv_file_name, 'r') as f:
            lines = f.readlines()
            with open(new_csv_file, 'a') as file:
                if len(lines) < line_end:
                    line_end = len(lines)-1
                if line_step>1:
                    file.writelines(lines[line_start:line_end+1:line_step])
                else:
                    file.writelines(lines[line_start:line_end+1])
                
"""
# Example of using pd to get new data by subtracting two columns
df_new = pd.DataFrame()
df = pd.read_csv(new_csv_file)
df_sugar = pd.read_csv(new_csv_file_sugar)
df_new['Ii'] = df_sugar['SGLT1_BG | Ii (fA)']*-1e-6-df['SGLT1_BG | Ii (fA)']*-1e-6
df_new['V_E'] = df['SGLT1_BG | V0_Vm (volt)']*1e3
df_new.to_csv(path_+'fig5_BG_fast.csv', index=False)

"""