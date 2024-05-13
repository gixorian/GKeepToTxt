import json
import os

inputDir = os.path.join(os.path.dirname(__file__), "input")
outputDir = os.path.join(os.path.dirname(__file__), "output")

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

os.chdir(inputDir)

fileList = []
keywordList = []

for filename in os.listdir(inputDir):
    if filename.endswith(".json"):
        with open(os.path.join(inputDir, filename), encoding="utf8") as input:
            data = json.load(input)
            txtFile = filename.replace("json", "txt")
            fileName = txtFile.replace(" ", "_")
            
            if "labels" in data:
                labelsPrefix = ""
                for label in data["labels"]:
                    labelsPrefix += "[" + label["name"] + "]"
                fileName = labelsPrefix+fileName
            
            output = open(
                os.path.join(outputDir, fileName),
                mode="w",
                encoding="utf8",
            )
            
            print(fileName)

            if "textContent" in data:
                content = data["textContent"]
                output.write(content)
                output.close()
                
        input.close()
