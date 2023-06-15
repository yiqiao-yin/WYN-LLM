# WYN LLM

This is the official research package from [W.Y.N. Associates](https://wyn-associates.com/), led by [Yiqiao Yin](https://www.y-yin.io/).


## Installation

Use `git` to clone the repo. 

```git
git clone https://github.com/yiqiao-yin/WYN-LLM.git
```

We recommend to do this in a virtual environment. In `Linux` system, you can use the following

```git
python3 -m venv myenv
source myenv/bin/activate
```

In a Windows terminal, you can use the following code

```git
python -m virtualenv .venv_my_env
.venv_my_env\scripts\act
```

Then install the dependencies which are saved in `requirements.txt` file

```git
pip install -r requirements.txt
```

Last, install our package

```git
pip install .
```

## Sample

```py
from src.explain.similarity import *
str1 = "hello world"
str2 = "hi world"
calculate_cosine_similarity(str1, str2)
# 0.5
```