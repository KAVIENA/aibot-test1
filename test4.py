import pandas as pd
import json

# Read the CSV file
csv_file = r'C:\FYP1\test\ipc_sections_Data - ipc_sections.csv'
data = pd.read_csv(csv_file)

# Convert CSV data to JSON format
intents = []
for index, row in data.iterrows():
    intent = {
        "tag": row['Section'],
        "patterns": [
            row['Offense'],
            row['Description']
        ],
        "responses": [
            row['Punishment'],
            row['Description'],
            row['Section']
        ],
        "context_set": ""
    }
    intents.append(intent)

# Save the JSON data to a file
json_file = 'intents.json'
with open(json_file, 'w') as f:
    json.dump(intents, f, indent=4)

print("Conversion complete. JSON file saved as 'intents.json'.")
