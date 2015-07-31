__author__ = 'lige'
#encoding:Utf-8
import numpy as np
from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer

from graph_feature import build_graph


def file():
    cats = ['alt.atheism','sci.electronics']

    newsgroups_train = fetch_20newsgroups(subset='train', categories=cats)

    newsgroups_test = fetch_20newsgroups(subset='test', categories=cats)
    vectorizer = TfidfVectorizer()#把所有文档都切词,统计了

    vectors_train = vectorizer.fit_transform(newsgroups_train.data)
    vectors = vectorizer.transform(newsgroups_test.data)
    print vectors.shape[1]
    #f=open('test_all.txt','wb')
    for j in range(0,vectors.shape[0]):
        item_id=list()
        tokens=vectorizer.build_tokenizer()(newsgroups_test.data[j])#提取分词结果
        #print tokens

        word_sort=np.argsort(-vectors[j].data)
        print '顶点'+str(j)
        for i in range(0,len(word_sort)):
            word=vectorizer.get_feature_names()[vectors[j].indices[word_sort[i]]]#这个是tf-idf詞
            for line in range(0,len(tokens)):
                if tokens[line].lower()==word:
                     item_id.append((line,word_sort[i]))

        pos_item=sorted(item_id,key=lambda jj:jj[0],reverse=True)#抽取ｔｆ-ｉｄｆ词

        word_word=np.zeros([len(word_sort),len(word_sort)])
        for p in range(0,len(pos_item)):
            if p <(len(pos_item)-1):
                ki=word_sort[pos_item[p][1]]
                kj=word_sort[pos_item[p+1][1]]
                word_word[ki, kj]= word_word[ki,kj]+1

        #调用图分析函数
        #build_graph(word_word,word_sort,vectors,j)
    #f.close()



if __name__=='__main__':
    file()
