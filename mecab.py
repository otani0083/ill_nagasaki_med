#coding:utf-8
import MeCab
import nltk

#Python2.7.3で実行
#pymecabとNLTKを利用


def extractNouns(text):  # 文字列から名詞を取り出して配列で返す関数
    wdlist = []
    tagger = MeCab.Tagger('-Ochasen')
    encoded_text = text.encode('utf-8')
    node = tagger.parseToNode(encoded_text)
    stopwords = nltk.corpus.stopwords.words('english')
    while node:
        noun = unicode(node.surface, "utf-8")
        noun = noun.lower()
        np = node.posid
        if ((np >= 36 and np <= 47) or (np >= 49 and np <=67)) and (len(noun) > 1) and (noun not in stopwords):
            wdlist.append(noun)
        node = node.next
    return wdlist

wddict = {}

with open("log.txt", "r") as f:  # log.txtというファイルから雑誌タイトルを抽出。log.txtはタブ区切りで年度、NCID、雑誌タイトルを持つテキストデータ
    for i in f.readlines():
        a = i.split("\t")
        if True:
            b = a[1].rstrip()
            if wddict.has_key(b):
                wddict[b] += 1
            else:
                wddict[b] = 1
            wdl=extractNouns(a[2])
            for j in wdl:
                if wddict.has_key(j):
                    wddict[j] += 1
                else:
                    wddict[j] = 1

for k, v in sorted(wddict.items(), key=lambda x: x[1], reverse=True):
    print k + "\t" + str(v)

  