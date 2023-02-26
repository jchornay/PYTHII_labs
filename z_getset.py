#generates getter and setter code for a list of attributes
import pyperclip

attrList = input("List class attributes, separated by commas (,): ")

stringList = attrList.split(',')

for i in range(len(stringList)):
    stringList[i] = stringList[i].strip()

print("#getters and setters")

output = ""

for i in range(len(stringList)):

    output += f"\n" \
              f"def get_{stringList[i]}(self):\n" \
              f"\treturn self.__{stringList[i]}\n"
    output += f"def set_{stringList[i]}(self, {stringList[i]}):\n" \
              f"\tself.__{stringList[i]} = {stringList[i]}\n"

print(output)
pyperclip.copy(output)

print("COPIED TO CLIPBOARD")