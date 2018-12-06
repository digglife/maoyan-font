## maoyan-font

### 简介

将猫眼电影网页中票房、评分等数据的乱码转化成正常数字。

### 安装

```bash
pip install maoyan-font
```
或者

```bash
git clone https://github.com/digglife/maoyan-font
cd maoyan-font
python setup.py install
```

### 用法

```python

from maoyan_font import MaoyanFontParser

parser = MaoyanFontParser()
font = parser.load('http://vfile.meituan.net/colorstone/294024cb386679d8e940022d5e3b6a162088.woff')
font.normalize('\uf8bc.\ueb54')
# '9.1'

```

本模块附带了一个命令行工具 `mybox`, 用于展示模块的用法。

```bash

$ mybox https://maoyan.com/films/249342
{'name': '海王', 'box': '468万'}

$ mybox -h

usage: mybox [-h] url

get box office info via url

positional arguments:
  url         movie url to parse

optional arguments:
  -h, --help  show this help message and exit

```


### 原理

猫眼为了保护重要数据，对评分和票房数据采用了 网络字体反爬机制。概括而言，就是 HTML 中的返回无对应字符的 Unicode 代码（[Unicode 私人使用区](https://zh.wikipedia.org/wiki/%E7%A7%81%E4%BA%BA%E4%BD%BF%E7%94%A8%E5%8C%BA)），
然后使用网络字体在浏览器中渲染出代码对应的数字。

每次请求电影页面，下载的 woff 都不同，每个 woff 中的 Unicode 代码对应的数字也都不同。比如，woff A 中，`\uE851` 对应的是 数字 0， woff B 中 数字0 对应的代码可能是 `\uE748`，没有规律可言。
但是字体的字形数据 (Glyphs) 是不变的，我们只要获取猫眼的任一 woff，找出字形和数字的对应关系，保存为字典，然后每次抓取时，解析出新字体中的字形，在字典中查询即可获取真正的数字。

### 许可证

[MIT](LICENSE)
