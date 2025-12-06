import os
import pandas as pd

data = {
  'Name': ['Alice', 'Bob', 'Charlie'],
  'Age': [25, 30, 35],
  'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# # Adding a new row to df for V2
# new_row_loc = {
#   'Name': 'V2',
#   'Age': 20,
#   'City': 'City1'
# }
# df.loc(len(df.index)) = new_row_loc

# # Adding a new row to df for V3
# new_row_loc2 = {
#   'Name': 'V3',
#   'Age': 30,
#   'City': 'City2'
# }
# df.loc(len(df.index)) = new_row_loc2

# Ensure that the "data" directory exists at root level
data_dir = "data"
os.makedirs(data_dir, exist_ok=True)

# Define File path
file_path = os.path.join(data_dir, 'sample_data.csv')

# Save the dataframe to CSV file, including column names
df.to_csv(file_path, index=False)
print(f"CSV file saved to {file_path}")
