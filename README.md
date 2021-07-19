# proguardRate
## 计算代码混淆率

计算代码混淆率

一个被忽略的维度：代码混淆率

## 背景
Android开发，都会关注包体、崩溃率、anr率，其实还有一个一直被忽略的维度，就是**混淆率**，为此，专门写了一个python脚本，用于**计算代码混淆率**

> 这个脚本已上传到了`PyPI`，使用非常方便

## 脚本使用方式
使用步骤（这个是针对Mac系统，其他系统其实也差不多）
1. 先安排python3，如果没有安装，建议用homebrew一键安装

```
brew install python3
```
2. 使用pip拉取脚本

```
pip install proguard-rate
```
3. 拉取成功后，打开terminal直接输入`calRate`命令，enter键，根据提示传入mapping文件地址，就可以计算出混淆率了

```
weigan@weigandeMacBook-Pro ~ % calRate                                         
请输入mapping文件地址：/Users/weigan/Downloads/104-mapping.txt 
总的有效行数: 186001 已混淆的行数 120641 混淆率 0.6486040397632271
```
上面传入的这个mappin可以知道，混淆率是64.8%

**使用非常方便，后续每次使用，直接调用`calRate`命令即可**


## 技术实现
关于混淆率的计算规则，我们先看下mapping文件截图

![](https://files.mdnice.com/user/3236/4d800e1f-3904-4ad0-8c52-e9af1e2ccfbe.png)

一共有三种类型的混淆
* 类名混淆
* 变量混淆
* 方法混淆

上面三种混淆都会参与计算，最终得到一个总的混淆率，计算思路如下

1. 取出箭头`->`左边跟右边的内容
2. 左边跟右边内容移除空格
3. 左边内容如果有方法的括号，就移除包括括号后面的内容
4. 如果左边内容以右边的内容是结尾，代表没有混淆，反之就是有混淆

