import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
import PyPDF2, pdfplumber

CV="./input/sample_1.pdf"
Req="./input/sample_2.pdf"

CV_File=open(CV,'rb')
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

Req_File=open(Req,'rb')
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

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
count_matrix=cv.fit_transform(Match_Test)

from sklearn.metrics.pairwise import cosine_similarity
print('Similarity is :',cosine_similarity(count_matrix))

MatchPercentage=cosine_similarity(count_matrix)[0][1]*100
MatchPercentage=round(MatchPercentage,2)
print('Match Percentage is :'+ str(MatchPercentage)+'% to Requirement')