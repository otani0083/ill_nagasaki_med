#coding:utf-8
import MeCab
import nltk
import re

stopwords = nltk.corpus.stopwords.words('english')
symbols = ["'", '"', '`', '.', ',', '-', '!', '?', ':', ';', '(', ')']
stopwords=set(stopwords+symbols)


def extractNouns(text):#文字列から名詞を取り出して配列で返す関数
    wdlist=[]
    symbol=["--",'-"',"].",']-"',".,",')"',"],","?",']"','"',"-.",'."',"?","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","1999","1998"]
    tagger = MeCab.Tagger('-Ochasen')
    encoded_text = text.encode('utf-8')
    node = tagger.parseToNode(encoded_text)
    stopwords = symbol+nltk.corpus.stopwords.words('english')+nltk.corpus.stopwords.words('german')+nltk.corpus.stopwords.words('french')+nltk.corpus.stopwords.words('italian')+nltk.corpus.stopwords.words('spanish')
    while node:
        noun=unicode(node.surface,"utf-8")
        noun=noun.lower()
        # if (node.posid >=36 and node.posid <=67) and (len(noun)>1) and (noun not in stopwords) and re.match("\d{4}", noun)==None:
        if ((node.posid >=36 and node.posid<=47) or (node.posid>=49 and node.posid <=67)) and (len(noun)>1) and (noun not in stopwords):
            wdlist.append(noun)
        # wdlist.append(noun)
        node = node.next
    return wdlist

wddict={}

with open("log.txt","r") as f: #log.txtというファイルから雑誌タイトルを抽出。log.txtはタブ区切りで年度、NCID、雑誌タイトルを持つテキストデータ
    for i in f.readlines():
        a=i.split("\t")
        if True:
            b=a[1].rstrip()
            if wddict.has_key(b):
                wddict[b]+=1
            else:
                wddict[b]=1
            wdl=extractNouns(a[2])
            for j in wdl:
                if wddict.has_key(j):
                    wddict[j]+=1
                else:
                    wddict[j]=1

for k,v in sorted(wddict.items(),key=lambda x:x[1],reverse=True):
    print k+"\t"+str(v)

  