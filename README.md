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
	

后续工作：
	
	后续需要研究的是在特征多而稀疏时，利用dA模型来进行训练，然后与RBM模型对比。
	

参考资料：
	https://github.com/lisa-lab/DeepLearningTutorials
	Y. Bengio, P. Lamblin, D. Popovici, H. Larochelle: Greedy Layer-Wise Training of Deep Networks, Advances in Neural Information Processing Systems 19, 2007