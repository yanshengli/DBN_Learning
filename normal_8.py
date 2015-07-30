__author__ = 'LiGe'
#encoding:utf-8
import numpy as np

#归一化train数据
def txt2mat_train():
    f=open("train.txt",'r')
    datas=f.readlines()
    train_mat=list()
    train_label=list()
    for data in datas:
        data=data.strip()
        if len(data)>0:
            data=data.split(',')
            row=list()
            for j in range(0,len(data)-1):
                row.append(float(data[j]))
            if len(row)!=8:
                print row
            train_mat.append(row)
            if data[-1]=='1':
                train_label.append([1,0])
            else:
                train_label.append([0,1])
    #print train_mat
    train_np=np.array(train_mat)
    train_label_np=np.array(train_label)
    for i in range(0,train_np.shape[1]):
        max=train_np[:,i].max()
        min=train_np[:,i].min()
        #print max,min
        print '_______________________________________'+str(i)+'__________________'
        for j in range(0,train_np.shape[0]):
            normal_value='%0.4f'%((train_np[j,i]-min)/(max-min))
            print normal_value
            if i==0:
                if float(normal_value) > 0.5:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==1:
                if float(normal_value) < 0.0001:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==2:
                if float(normal_value)>0.05:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==3:
                if float(normal_value)>0.02:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==4:
                if float(normal_value)>0.4:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==5:
                if float(normal_value)<0.02:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==6:
                if float(normal_value)>0.80:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==7:
                if float(normal_value)>0.09:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
    print train_np
    #print train_label_np
    return train_np,train_label_np


#归一化测试数据
def txt2mat_text():
    f=open("test.txt",'r')
    datas=f.readlines()
    train_mat=list()
    train_label=list()
    for data in datas:
        data=data.strip()
        if len(data)>0:
            data=data.split(',')
            row=list()
            for j in range(0,len(data)-1):
                row.append(float(data[j]))
            if len(row)!=8:
                print row
            train_mat.append(row)
            if data[-1]=='1':
                train_label.append([1,0])
            else:
                train_label.append([0,1])
    #print train_mat
    train_np=np.array(train_mat)
    train_label_np=np.array(train_label)
    for i in range(0,train_np.shape[1]):
        max=train_np[:,i].max()
        min=train_np[:,i].min()
        #print max,min
        for j in range(0,train_np.shape[0]):
            normal_value='%0.4f'%((train_np[j,i]-min)/(max-min))
            print normal_value
            if i==0:
                if float(normal_value) > 0.5:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==1:
                if float(normal_value) < 0.0001:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==2:
                if float(normal_value)>0.05:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==3:
                if float(normal_value)>0.02:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==4:
                if float(normal_value)>0.4:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==5:
                if float(normal_value)<0.02:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==6:
                if float(normal_value)>0.80:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
            if i==7:
                if float(normal_value)>0.09:
                    train_np[j,i]=1
                else:
                    train_np[j,i]=0
    #print train_np
    #print train_label_np
    return train_np,train_label_np


if __name__=='__main__':
    txt2mat_train()