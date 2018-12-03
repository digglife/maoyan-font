## maoyan-font

### 简介

将猫眼电影网页中票房、评分等数据的乱码转化成正常数字。

### 用法

```python

from maoyan_font import MaoyanFontParser
parser = MaoyanFontParser()
font = parser.load('http://vfile.meituan.net/colorstone/00b9347ca891bde9d2716c49b7e07fd92080.woff')
font.normalize('\ue871.\ue829')
# '9.1'

```

### 原理

猫眼为了保护重要数据，对评分和票房数据采用了 网络字体反爬机制。概括而言，就是 HTML 中的数据返回无对应字符的 UNICODE 代码（UNICODE 私人使用区），
然后使用网络字体在浏览器中渲染出代码对应的数字。

每次请求电影页面，下载的 woff 都不同，每个 woff 中的代码对应的数字也都不同。比如，网络字体 A 中，`\uE851` 对应的是 数字 0， 网络字体 B 中 数字0 对应的代码可能是 `\uE748`，没有规律。
但是字体的字形数据 (glyphs) 是不变的，我们只要获取猫眼的任一 woff，找出字形和数字的对应关系，保存为字典，然后每次抓取时，解析出新字体中的字形，在字典中查询即可获取真正的数字。

