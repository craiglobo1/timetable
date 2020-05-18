import pandas as pd


class xlsxParser:
    def __init__(self, filepath='databases\IGCSE-2-AS2019.xlsx'):
        self.filepath = filepath

    def postionToTuple(self, tag='A5'):
        column = 0
        for i in range(len(tag)):
            if tag[i].isdigit():
                index = i
                break

        for i, letter in enumerate(tag[:index]):
            column += (ord(letter)-ord('A')+1) * (26**(len(tag[:index])-i-1))            

        position = (column, int(tag[index:]))

        return position

    def getDatabase(self, initialPostion, finalPosition, sheetName, ):
        self.initialPosition = self.postionToTuple(initialPostion)
        self.finalPosition = self.postionToTuple(finalPosition)
        self.dfs = pd.read_excel(
            self.filepath, sheet_name=sheetName)
        self.dfs = self.dfs.iloc[self.initialPosition[1]-2:self.finalPosition[1]-1,
                                 self.initialPosition[0]-1:self.finalPosition[0]]

        return self.dfs.values.tolist()

    def printClass(self):
        print(self.initialPosition, self.finalPosition)
        print(self.dfs)