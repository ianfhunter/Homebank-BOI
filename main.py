# Define your own replacements here
def reg_match(word):
    return word

# Open Exported Transaction Document
with open("transaction.csv", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

array.pop(0) # We don't need the first line.
translated_array = []
for line in array:
    translated_line = ""
    cols = line.split(",")
    translated_line += cols[0]
    translated_line += ";;;;"
    translated_line += reg_match(cols[1])
    translated_line += ";"
    if(cols[2]): # Expenditure
        translated_line += "-" + cols[2]
    if(cols[3]): # Income
        translated_line += cols[3]
    translated_line += ";;"
    translated_line += "ATAG" # Some tag, I don't use these personally
    translated_array.append(translated_line)

# Write back your new, formatted document
with open("transaction_formatted.csv", "w") as ins:
    for line in translated_array:
        ins.write(line + "\n")