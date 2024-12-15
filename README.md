# some SZU $\LaTeX$ templates

$\LaTeX$ versions of some Word documents templates of SZU

一些（我自己用的）深大的照着Word版本抄的$\LaTeX$模板

---

学校的很多文档都只提供Word格式的模板，写起来不习惯，就使用$\LaTeX$复刻了一部分，并分享在这个仓库中，供能找到的人自取。

大多数都是编译起来和原来的文件长得差不多就行，所以不保证没有奇奇怪怪的小bug，不保证样式与原文档完全相同。~~没关系反正本来每个人打开同样的Word文档样式也不相同。~~

目前已有：

- [some SZU $\\LaTeX$ templates](#some-szu-latex-templates)
- [各个模板使用说明](#各个模板使用说明)
  - [大学物理实验报告](#大学物理实验报告)
    - [建议流程：](#建议流程)
    - [原理说明](#原理说明)
    - [修改默认配置](#修改默认配置)
      - [修改封面样式](#修改封面样式)
      - [修改个人信息](#修改个人信息)
      - [\[ 可选 \] 增加你需要的修改信息](#-可选--增加你需要的修改信息)
    - [其它](#其它)
  - [大学物理实验实验论文](#大学物理实验实验论文)
  - [大学物理实验调研报告](#大学物理实验调研报告)
    - [需要注意的地方：](#需要注意的地方)
  - [深圳大学考试答题纸](#深圳大学考试答题纸)
  - [大学生创新训练项目申报书](#大学生创新训练项目申报书)
    - [注意事项](#注意事项)
- [登陆校园网Python脚本](#登陆校园网python脚本)
- [如果你的老师只允许提交.docx文件……](#如果你的老师只允许提交docx文件)
  - [方案1](#方案1)
  - [方案2](#方案2)

# 各个模板使用说明

## 大学物理实验报告

本仓库模板和[jinqKing的这个仓库的](https://github.com/jinqKing/SZU-Physics-Experiment-Report-LaTeX-Module)是同源的（但是他抢先一步上传到了GitHub），但根据我两需求不同所以有了两branch。图省事所以本说明有些内容直接从jinqKing那里复制修改来。

文档包括`大物实验报告模板.tex`和`phyreport.cls`

### 建议流程：

文档结构：

```
.
├──── ReadMe.md
├──── phyreport.cls
├──── 空白
│       └── 模版.tex
├──── 电感
│       ├── 电感的测量.tex
│       ├── 电感的测量.pdf
│       ├── fig
│       │    └── p1.png
│       └── data
│            └── pd.csv
```

0. 修改 `phyreport.cls` 文件，填写个人信息。
1. 复制 `空白` 文件夹，重命名为实验文件夹。
2. 重命名 `模版.tex` 文件，编辑内容，补充实验细节。
3. 编译 `实验.tex` 文件，生成 `实验.pdf` 文件。

这样安排可以方便管理实验报告，一个文件夹记录一次实验，统一模板文件。

### 原理说明

编写了一个 `phyreport.cls` 类文件（就像article、ctexart），定义了实验报告的格式，通过控制页边距等使得像官方提供的 Word 模版。于是每次文档直接使用这个类文件即可得到一份“普通的”实验报告。

基于 ctexart 类，预先一些常用包和需要的功能，如我们使用 `tikz` 绘制了封面以及各种打分方格。

细节说明: 
- 使用 fancypage 和页边指令控制页边距，清除页眉页脚，让页码只在右下；
- 改了一般的节 section、subsection 标题格式，变成汉字数字且左对齐
- 使用新命令定义变量，方便修改，如实验名称、实验地点、实验日期等；

正文使用的命令
1. `\phyExpCover` : 生成封面，里面的日期
2. `\SmartLongLine` : 生成一条长横线，用于分隔不同部分；（这条线会尝试在它自己该出现的时候出现，不该出现的时候消失，但是有时会错误地干扰文档布局，如果你遇到了这个问题，可以在对应位置删除这条命令或使用`\LoneLine`代替，这个函数会在你调用它的地方直接画出线来）
3. `\endBox` : 用于绘制结尾教师评价和打分表格。

### 修改默认配置

#### 修改封面样式

报告默认封面是大物三的格式，一和二以及各个老师的模板可能不完全相同，你大概率需要自行修改一次。


为保证效果和原有的Word模板相近，使用了TikZ库直接在指定位置画上文字。如果不了解TikZ，可参照下面不是很详细的说明并自己摸索修改封面。

封面定义在

```LaTeX
% phyreport.cls
\NewDocumentCommand\phyExpCover{}{
   ...
}
```
语句内，每行文字使用了一个或多个TikZ语句绘制，表格使用TikZ线条绘制。

TikZ绘制文字语句介绍：

```latex
%这是一行示例语句
\node[right] at (1.8,-9.8) % TiKZ语句以 ; 作为语句结束，换行不会中断
{\textbf{学　　院：}\rule[-5pt]{8.7cm}{1pt}}; % <-这个 ; 是必需的
```

在上面这行示例语句中， 
- `\node[] {}`：表示绘制一个节点，`{ }`内为节点内容，基本可以放任何东西
- `[...]`： `[ ]`内的内容是提供给 node 的可选参数，`right`表示文字在指定位置的右边（即向左对齐），同理，使用`center`即可居中对齐，使用`left`可以向右对齐。
- `at (1.8, -9.8)` 指定了 node 的位置，格式为`at (x, y)`，默认单位是厘米，方向如下图
```
↑ y
│
└───→ x
```
- `\rule[-5pt]{8.7cm}{1pt}` 是一条下划线，`[-5pt]`是y方向上偏移长度5pt，`{8.7cm}`是线段长度，`{1pt}`是线段宽度。

Tips: 你不用在意将线段细致长度，设置得过长不会有大问题，因为在封面语句定义中大概在位置*处有一个白色矩形，会将多余的线条遮挡住。

```
┌───────────────┐
│               │
│     cover     │
│           ┌───┤
│     i__   │   │
│     n__   │   │
│     f__   │ * │
│     o__   │   │
│           └───┤
│               │
└───────────────┘
```


#### 修改个人信息

进入 `phyreport.cls` 文件，修改 `\NewDocumentCommand\phyExpCover{}` 内容，填上你的课程编号、学院、老师、名字、学号、组号等不会变的信息。

#### [ 可选 ] 增加你需要的修改信息

格式请自行参照cls内已有信息，如
```latex
\newcommand{\expName}[1]{\newcommand{\phyExpName}{#1}}
    ...
\node[above] at (8.5,-7.9) {\textbf{\phyExpName}};
```


### 其它
- 插入一页预习报告：
  - 文档类定义了`\includeFullPageGraphicsBeta`函数，可以调用它来插入（注意：插入的图片可能需要第二次编译后才能显示）
- 同一目录操作:
     ```latex
    \documentclass[a4paper]{../phyreport}
    ```
    `../` 代表上一级目录，可以直接在`实验`文件夹中使用上一级`样版`中`phyreport.cls` 文件。如果不习惯,可以将 `phyreport.cls` 文件相应 .tex 同文件夹下删掉 `../`。
- 默认载入包：尽量覆盖一般使用，但比如处理多图并排时不够，细节自行查看`\RequirePackage` 部分。
- 本模板为学习交流使用，不保证完全符合实验报告要求。
- 最大优势: ~~方便抄别人的报告+Copolit自动补全~~

## 大学物理实验实验论文

文件包括`大物实验论文.tex`

这个文档没有什么需要注意的地方，因为只需要用到一次所以比较简陋，没有使用cls等东西，可以直接编译，只需要在71-84行修改对应位置的文字信息即可。

你可能需要了解一些$\LaTeX$的双栏排版样式代码才能愉快地使用它。

## 大学物理实验调研报告

文件包括`大物调研报告.tex`

这个文档同样因为只需要用到一次所以比较简陋，没有使用cls等东西，可以直接编译，只需要在129-139行修改对应位置的文字信息即可。

如果需要修改封面样式可以参考大物实验模板中的[修改封面样式](#修改封面样式)段

### 需要注意的地方：

- 四个章节不是使用`\section{ }`实现的，所以section需要手动编号，但是章节应该都是定死的所以也不用改。
- `\SectionSearator`产生的章节包括上下两条分割线，但它不是很智能：当章节刚好在页面顶端时可能会出现上面的线段与页面顶端的线段重合的问题，这时候可以使用`\SectionSearatorb`命令代替，这个命令只会生成包含下端的分割线的章节分割。
- 新加页面的边框需要第二次编译后才能显示

## 深圳大学考试答题纸

修改内容直接编译即可

你可能需要在下划线的两端添加`\quad`、`\ `、全角空格“　”或别的什么来控制间距。

## 大学生创新训练项目申报书

文件包括`大学生创新训练项目申报书.tex`和`附件2.大学生创新训练项目申报书.pdf`

> 为什么他们总是喜欢用整页的长表格然后里面表格套表格

### 注意事项

`大学生创新训练项目申报书.tex`，需要配合`附件2.大学生创新训练项目申报书.pdf`使用，因为前三页没什么需要修改的地方，所以直接把附件2转成pdf插进去。

需要修改的基础信息在71行以后。那个大表格使用单独的一页空间，如果你的“指导教师主要研究方向与成果”不够长就拿空白填充，如果太长了就在`\projProfInfo`的第二个 `{ }` 内插入第二页的内容，需要自行控制 `}{` 两端的内容分页。如果两页纸也写不完就需要修改模板了。

因为文档要求仿宋，需要自行设置字体，字体配置方式在59行。注意不同系统可用的字体名称不一样。

可以调用`\tableSeparator`命令绘制一条横线。

# 登陆校园网Python脚本

[`loginSZUnetwork.py`](loginSZUnetwork.py)

在文件里修改你的校园卡号和密码后使用Python运行此脚本便可以一键登陆深圳大学校园网。

不知道扔哪里就一并放到这个库了。

若使用请注意卡号和密码被明文储存在脚本中，需留心保管你的脚本文件以免密码泄漏。

# 如果你的老师只允许提交.docx文件……

## 方案1

Microsoft Word、[Smallpdf](https://smallpdf.com/cn/pdf-to-word) 和 Acrobat PDF（他有一个[免费的网页版](https://www.adobe.com/acrobat/online/pdf-to-word.html)）可以将.pdf转为.docx文件。

当然，pdf的样式不能完美保留下来，但你可以尝试一下，看是否能接受。

## 方案2

将每一页生成pdf转为图片再插入到word中。不能编辑，但长得和原来的pdf几乎一模一样！

1. 在$\LaTeX$文档的导言区插入
```LaTeX
\geometry{paperwidth=6.268in, paperheight=9.693in, margin=0.1in}
```
将边距设为几乎为0，重新编译得到一个无边距的pdf文件。
（注：a4纸的尺寸为8.268 x 11.693 inch）

2. 使用你喜欢的工具将这个pdf文件导出为图片，例如：
    - Smallpdf（没错又是他）提供了一个转jpg的[网页工具](https://smallpdf.com/cn/pdf-to-jpg)
    - Acrobat PDF 可以直接导出pdf为图片
    - 学校提供的[免费教育版福昕pdf](http://ms.szu.edu.cn/)导出
    - 本仓库下的[`pdf2svg.py`](pdf2svg.py)脚本（感谢PyMuPDF，它可以将pdf转为矢量的svg）

3. 将生成的pdf一股脑插入word文档中。