import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
import PyPDF2, pdfplumber
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class DocService():
    def __init__(self, cv, requirements):
        self.cv=cv
        self.requirement = requirements
    
    def compare(self):
        CV_File=open(self.cv,'rb')
        Script=PyPDF2.PdfFileReader(CV_File)
        pages=Script.numPages

        Script = []
        with pdfplumber.open(CV_File) as pdf:
            for i in range (0,pages):
                page=pdf.pages[i]
                text=page.extract_text()
                # print (text)
                Script.append(text)

        Script=''.join(Script)
        CV_Clear=Script.replace("\n","")
        CV_Clear

        Req_File=open(self.requirement,'rb')
        Script_Req=PyPDF2.PdfFileReader(Req_File)
        pages=Script_Req.numPages

        Script_Req = []
        with pdfplumber.open(Req_File) as pdf:
            for i in range (0,pages):
                page=pdf.pages[i]
                text=page.extract_text()
                # print (text)
                Script_Req.append(text)

        Script_Req=''.join(Script_Req)
        Req_Clear=Script_Req.replace("\n","")
        Req_Clear

        Match_Test=[CV_Clear,Req_Clear]

        cv=CountVectorizer()
        count_matrix=cv.fit_transform(Match_Test)
 
        print('Similarity is :',cosine_similarity(count_matrix))

        MatchPercentage=cosine_similarity(count_matrix)[0][1]*100
        MatchPercentage=round(MatchPercentage,2)
        # print('Match Percentage is :'+ str(MatchPercentage)+'% to Requirement')
        return MatchPercentage

def main():
    document = DocService("./input/sample_1.pdf","./input/sample_2.pdf")
    per = document.compare()
    print('Match Percentage is :'+ str(per)+'%')

if __name__ == "__main__":
    main( )