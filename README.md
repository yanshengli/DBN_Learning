基于RBM的深度学习算法
========

基于多层RBM模型，实现二分类学习算法，目前针对该问题是采用2层RBM,特征输入只有8维，效果并不理想。



功能框架：

	DBN.py：深度学习主框架，包括数据输入、输入sigmoid转换，RBM层堆叠，softmax层输出。

	RBM.py：RBM层框架，包括gibss采样、交叉熵误差验证
	
	dA.py:这个是降噪自动编码器，目前还在研究
	
	SdA.py:，堆叠降噪自动编码器，目前仍在研究
	
	HiddenLayer.py:隐层主要是权值计算与更新
	
	util.py：这主要是最后的softmax函数计算及输出
	
	normal_8.py：输入数据归一化到[0,1]
	
	train.txt:训练数据
	
	text.txt:测试数据
	

基于复杂语言网络的文本分类：
	
	这里面主要包括两部分，一部分是语言网络的生成，另一部分是语言网络的特征抽取。
	
	第一部分采用的数据是twenty-news-group，根据词语序列生成语言网络。

	另一部分是特征抽取，由于课题没有结题，所以这里只展示了提取了结点度特征，并采用SVM作为训练器，
	
	最终效果和采用普通的词袋模型相当。所以需要抽取	语义特征加上深度模型训练。深度模型训练目前
	
	已经有几个模型结果，效果有大幅提升，目前还在继续优化中。
	
后续工作：
	
	后续需要研究的是在特征多而稀疏时，利用dA模型来进行训练，然后与RBM模型对比。
	

参考资料：
	https://github.com/lisa-lab/DeepLearningTutorials
	
	Y. Bengio, P. Lamblin, D. Popovici, H. Larochelle: Greedy Layer-Wise Training of Deep Networks, Advances in Neural Information Processing Systems 19, 2007