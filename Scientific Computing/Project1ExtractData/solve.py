import pandas as pd
import numpy as np
from typing import List,Dict,Set
import re as regex
from random import choice
import string
if __name__ == "__main__":
    text : str 
    with open("captions_text.vtt","r") as fuf:
        text = fuf.read()
    print(type(text))

    sampletext : str = "prim suka sama prim sama prim sama kodingprim ngab"
    regexSample  = regex.compile("prim")

    print(type(regexSample))
    print(regexSample.findall(sampletext))
    print(regexSample.sub("PRAM",sampletext))
    
    pattern :str = r'\n\n\d{1,3}\n\d\d:\d\d.\d\d\d --> \d\d:\d\d.\d\d\d\n'
    regexObj = regex.compile(pattern=pattern)
    print(regexObj.findall(text))

    cleanText : str = regexObj.sub("",text)
    cleanText= cleanText[9:-1]
    print(cleanText)

    pattern : str = r"\b(\w{4})\b"
    words : List[str] 
    regexObj = regex.compile(pattern)
    words  = regexObj.findall(cleanText)
    print(words)
    cleanTexts = " ".join([text.replace(text[1:],"***") if text in words else text for text in cleanText.split()  ]  ) 
    print(cleanTexts)

    with open("cleantext.txt","w+") as fuf:
        fuf.write(cleanTexts)

    sampleScramble : str= "Mr. Robot is an American drama thriller television series created by Sam Esmail for USA Network. It stars Rami Malek as Elliot Alderson, \
        a cybersecurity engineer and hacker with social anxiety disorder and clinical depression."
    
    pattern = r"\b(\w{3,13})\b"
    regexObj = regex.compile(pattern) 
    ScrambledtextList = regexObj.findall(sampleScramble)
    def getpermutationText(text : str) :
        return "".join(text[indx] for indx in np.random.permutation(len(text) -2))
    def randStr(chars = string.ascii_lowercase, N=10):
	    return ''.join(choice(chars) for _ in range(N))
    Scrambledtext = [text.replace(text[1:-1],getpermutationText(text)) if text in ScrambledtextList else text for text in sampleScramble.split()]
    print(Scrambledtext)  