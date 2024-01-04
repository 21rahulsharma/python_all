from turtle import update


myDict = {"fast": "In a quick manner ","harry":"A Coder",
"marks":[21,42,67],
1:23
}
print(myDict['fast'])
print(myDict['harry'])
myDict['marks']=[45,99]
print(myDict['marks'])
updateDict={"Rahul":"A great coder"}
myDict.update(updateDict)
print(myDict.items())
print(myDict.keys())
