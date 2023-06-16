# WYN LLM

This is the official research package from [W.Y.N. Associates](https://wyn-associates.com/), led by [Yiqiao Yin](https://www.y-yin.io/).

![main](./docs/main.jpg)


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

## Examples of API Calls

We demonstrate efficient way of making API calls using this package. Large Language Models such as `openai.completion` and `palm.generate_text` are at the tip of your finger. For OpenAI's GPT related models, you will need to acquire your own API Key, which you can go to their official [site](https://platform.openai.com/) to create your own key. It is the same with Google's Palm. You can go to their [site](https://developers.generativeai.google/tutorials/setup) to apply for API Key. You will need both keys for the following code. 

```py
from src.explain.similarity import *
str1 = "hello world"
str2 = "hi world"
print(wyn_explain_sim.calculate_cosine_similarity(str1, str2))
print(wyn_explain_sim.calculate_sts_score(str1, str2))
print(wyn_explain_sim.calculate_sts_openai_score(str1, str2, YOUR_OPENAI_API_KEY))
# 0.5
# 0.8213709592819214
# 0.9113127745099068
```

```py
from src.models.msft import call_chatgpt
ans = call_chatgpt("tell me a joke", key)
ans
# \n\nQ: What did the fish say when it hit the wall?\nA: Dam!
```

```py
from src.models.googl import call_palm
call_palm("tell me a joke", key)
ans = call_palm("who is yiqiao", key)
ans
# Why did the scarecrow win an award?\n\nBecause he was outstanding in his field!
```