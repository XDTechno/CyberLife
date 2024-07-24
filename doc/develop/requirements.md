# how to create & update requirements.txt
```bash
python -m pip install --upgrade pip 
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
pip install pipreqs
pipreqs . 
```

# how to download requirement from requirements.txt
```bash
pip install -r requirements.txt
```