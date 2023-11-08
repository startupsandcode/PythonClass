def read_input_file():
    results = []
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        lines = [x.strip() for x in lines]
        for index, line in enumerate(lines):
            curLine = line
            if len(curLine) > 0 and curLine[0] == ":":
                results.append(curLine)
            elif curLine == "":
                results.append(lines[index+1])
            else:
                results.append(curLine)
    with open('output.txt', 'w') as f:
        for index, line in enumerate(results):
            if line.startswith(":"):
                f.write(line + ",")
                f.write(results[index+1] + "\n")

read_input_file()