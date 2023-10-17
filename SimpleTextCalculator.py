def delete(lst, index_num):  # This function deletes the selected index
    del lst[index_num]
    del lst[index_num]


counter = 0
listedTextFile = ""
try:
    FILE_INPUT = open("input.txt", "r", encoding="utf8")  # Opening the input file and adding text file to a list line by line
    contents = FILE_INPUT.read()
    listedTextFile = contents.split("\n")
    FILE_INPUT.close()
    for i in listedTextFile:
        counter += 1
except FileNotFoundError:
    print("File not found")
except ValueError:
    print("Value error")

try:
    FILE_OUTPUT = open("output.txt", "w", encoding="utf8")
    count = 0
    newList = list()
    while True:
        flag = True
        output = 0
        if count == counter:  # If the number of lines in the input file is equal to the output file, get out of while
            break
        elif listedTextFile[count] == '':  # Checking for empty lines
            FILE_OUTPUT.write("\n")
            flag = False
        else:
            numbers = "0123456789"
            operators = "*+/-%<>!="
            sign = "-"
            listToStr = listedTextFile[count]  # Assigning the current index of the listedTextFile list to a variable which is string
            listToStr.strip()  # Erasing the white spaces before and after the string
            if flag:
                tempStr = " ".join(listToStr.split())  # Here I turned every space which is more than one into one space
                k = 0
                while k < len(tempStr) and flag:
                    if k + 2 <= len(tempStr):
                        if tempStr[k] in numbers and tempStr[k + 1] == " " and tempStr[k + 2] in numbers:
                            FILE_OUTPUT.write("Error" + "\n")  # If there was a space Between two numbers an error occurs
                            flag = False
                        elif tempStr[k] in operators and tempStr[k + 1] == " " and tempStr[k + 2] in sign:
                            pass
                        elif tempStr[k] in operators and tempStr[k + 1] == " " and tempStr[k + 2] in operators:
                            FILE_OUTPUT.write("Error" + "\n")  # If there was a space Between two operators an error occurs
                            flag = False
                        elif tempStr[-1] in operators:  # If the last index is an operator an error occurs
                            FILE_OUTPUT.write("Error" + "\n")
                            flag = False
                    k += 1
            if flag:
                for i in listToStr:  # Erasing all the spaces
                    if i == " ":
                        listToStr = listToStr.replace(" ", "")
                        break
                for i in listToStr:  # If there exists an element which is nighter a number nor operator, an error occurs
                    if i not in numbers:
                        if i not in operators:
                            FILE_OUTPUT.write("Error" + "\n")
                            flag = False
                            break
            if flag:
                if listToStr[0] in operators and listToStr[0] not in sign:  # If the first index of the string isn't a number or minus sign, an error occurs
                    FILE_OUTPUT.write("Error" + "\n")
                    flag = False
            if flag:
                if listToStr[-1] in operators:   # If the last index of the string is operator, an error occurs
                    FILE_OUTPUT.write("Error" + "\n")
                    flag = False
            chars_size = 0
            chars = list()
            if flag:
                listToStr = " ".join(listToStr)  # Adding a space between each element
                chars = listToStr.split(" ")  # Adding each element to an individual index in chars named list
                j = 0
                chars_size = len(chars)
                while j < chars_size:
                    chars_size = len(chars)
                    control = True
                    if j + 2 <= chars_size:
                        if j == 0:                                             # This parts conditions are just for the beginning, j == 0
                            if chars[j] in sign and chars[j + 1] in numbers:
                                chars[j: j + 2] = [''.join(chars[j: j + 2])]  # Merging current and next indexes if the current index is negative sign and next index is number
                                control = False
                            elif chars[j] in numbers and chars[j + 1] in numbers:
                                chars[j: j + 2] = [''.join(chars[j: j + 2])]  # Merging current and next indexes if the current and next indexes are numbers
                                control = False
                            elif chars[j + 1] in numbers:
                                chars[j: j + 2] = [''.join(chars[j: j + 2])]  # Merging current and next indexes if the next index is number
                                control = False
                        else:
                            if chars[j - 1] in numbers and chars[j] in sign and chars[j + 1] in numbers:
                                pass  # If previous and next indexes are number and current index is negative sign
                            elif chars[j - 1] in operators and chars[j] in sign and chars[j + 1] in numbers:
                                chars[j: j + 2] = [''.join(chars[j: j + 2])]  # Merging Current and next indexes if the previous index is an operator and current index is negative sign and next index is a number
                                control = False
                            elif chars[j] not in operators and chars[j + 1] in numbers:
                                chars[j: j + 2] = [''.join(chars[j: j + 2])]  # Merging current and next indexes if the next index is number
                                control = False
                    if control:  # If flag was false it won't count up j because false control means a merge operation has occurred and the size of the has been changed
                        j += 1   # So there is no way to miss an index
                p = 1
                while p < chars_size:
                    chars_size = len(chars)
                    if p + 2 <= chars_size:
                        if chars[p] in operators and chars[p + 1] in operators:
                            chars[p: p + 2] = [''.join(chars[p: p + 2])]  # Merging current and next indexes if they're operators
                    p += 2
                while chars[-1] == "":
                    del chars[-1]  # Erasing empty indexes from end of the list if there is any
            if flag:
                w = 1
                comparisonCount = 0
                while w < chars_size and flag:
                    if str(chars[w]) != "==" and str(chars[w]) != "!=" and str(chars[w]) != ">=" \
                            and str(chars[w]) != "<=" and str(chars[w]) != "**" and str(chars[w]) != "//" \
                            and str(chars[w]) != "/" and str(chars[w]) != "%" and str(chars[w]) != "*" \
                            and str(chars[w]) != "+" and str(chars[w]) != "-" and str(chars[w]) != ">" \
                            and str(chars[w]) != "<":
                        FILE_OUTPUT.write("Error" + "\n")  # If any combination of operators other than combinations above an error occurs
                        flag = False
                    elif str(chars[w]) == "==" or str(chars[w]) == "!=" or str(chars[w]) == ">=" \
                            or str(chars[w]) == "<=" or str(chars[w]) == ">" or str(chars[w]) == "<":
                        comparisonCount += 1  # If there is an operator for comparing count up
                    if comparisonCount > 1:
                        FILE_OUTPUT.write("Error" + "\n")  # If there exists more than one comparison operator an error occurs
                        flag = False
                    w += 2
            if flag:
                y = 1
                while y < chars_size:  # Calculating the power operations because they're prior than others
                    chars_size = len(chars)
                    if chars_size >= 3:
                        if str(chars[y]) == "**":
                            chars[y + 1] = str(float(chars[y - 1]) ** float(chars[y + 1]))
                            delete(chars, y - 1)
                            y = 0
                        y += 1
                y = 1
                while y < chars_size and flag:  # Calculating the second prior calculations
                    chars_size = len(chars)
                    if chars_size >= 3:
                        if str(chars[y]) == "*":
                            chars[y + 1] = str(float(chars[y - 1]) * float(chars[y + 1]))
                            delete(chars, y - 1)
                            y = 0
                        elif str(chars[y]) == "/":
                            if float(chars[y + 1]) != 0:  # Checking for division by zero
                                chars[y + 1] = str(float(chars[y - 1]) / float(chars[y + 1]))
                                delete(chars, y - 1)
                                y = 0
                            else:
                                FILE_OUTPUT.write("Error" + "\n")
                                flag = False
                        elif str(chars[y]) == "//":
                            if float(chars[y + 1]) != 0:  # Checking for division by zero
                                chars[y + 1] = str(float(chars[y - 1]) // float(chars[y + 1]))
                                delete(chars, y - 1)
                                y = 0
                            else:
                                FILE_OUTPUT.write("Error" + "\n")
                                flag = False
                        elif str(chars[y]) == "%":
                            if float(chars[y + 1]) != 0:  # Checking for division by zero
                                chars[y + 1] = str(float(chars[y - 1]) % float(chars[y + 1]))
                                delete(chars, y - 1)
                                y = 0
                            else:
                                FILE_OUTPUT.write("Error" + "\n")
                                flag = False
                    y += 1
                y = 1
                while y < chars_size and flag:  # Calculating the third prior calculations
                    chars_size = len(chars)
                    if chars_size >= 3:
                        if str(chars[y]) == "+":
                            chars[y + 1] = str(float(chars[y - 1]) + float(chars[y + 1]))
                            delete(chars, y - 1)
                            y = 0
                        elif str(chars[y]) == "-":
                            chars[y + 1] = str(float(chars[y - 1]) - float(chars[y + 1]))
                            delete(chars, y - 1)
                            y = 0
                    y += 1
                if chars_size >= 3:  # Comparison operations
                    if str(chars[1]) == "==":
                        if float(chars[0]) == float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
                    elif str(chars[1]) == ">=":
                        if float(chars[0]) >= float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
                    elif str(chars[1]) == "<=":
                        if float(chars[0]) <= float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
                    elif str(chars[1]) == "<":
                        if float(chars[0]) < float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
                    elif str(chars[1]) == ">":
                        if float(chars[0]) > float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
                    elif str(chars[1]) == "!=":
                        if float(chars[0]) != float(chars[2]):
                            chars[2] = "True"
                            delete(chars, 0)
                        else:
                            FILE_OUTPUT.write("False" + "\n")
                            flag = False
            output = " ".join(chars)
        if flag:
            FILE_OUTPUT.write(output.strip() + "\n")
        count += 1
    FILE_OUTPUT.close()
except FileExistsError:
    print("File does not exist")
except ValueError:
    print("Value error")
