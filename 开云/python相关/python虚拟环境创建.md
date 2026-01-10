# 虚拟环境创建
```
python -m venv .venv
conda create -n handllm python=3.11

pip install --upgrade pip
pip install ipykernel -i https://pypi.tuna.tsinghua.edu.cn/simple/
python -m ipykernel install --user --name llm_learn --display-name "Python (llm_learn)"
```  
结果如下：  
```
your_project/
├── .venv/
├── main.py
└── ...
```  
cursor里面可能不显示`activate`,执行`ls .venv/bin`，一般就会出现。  
IDE把`activate`隐藏了。