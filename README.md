# weibospider
微博爬虫，爬取目标用户的微博
# 输入
所要爬取用户的id
# 输出
用户的昵称、微博数目、粉丝数、关注数以及内容
# 环境
系统：windows
开发语言：python3.6
# 安装说明
在使用之前，要先下载selenium库，命令如下：
> $pip install selenium
由于本程序使用谷歌浏览器，所以需要到http://npm.taobao.org/mirrors/chromedriver/ 中下载谷歌浏览器所需要的driver，解压后粘贴到谷歌浏览器exe文件所在目录即可
# 使用说明
1. 下载脚本
> $git clone https://github.com/nangongtianyi/weibospider.git
运行上述命令，将本项目下载到本地，会出现一个名为webospider.py的文件
2. 用文本编辑器打开上述文件，将文件最后的weibospyder(XXXXXX)更改为想要爬取的用户id，用户id获取如下，打开网址https://weibo.cn
,搜索我们想要找的人，如刘明月阿，其网址变为https://weibo.cn/u/2441045042 其中2441045042即为用户id，如果用户的id不显示，例如胡歌，其网址显示https://weibo.cn/hu_ge 此时可以点击资料，页面跳转后地址中会出现用户id
3. 运行脚本
> $python your_path/weibospider1.py
此时即可自动爬取微博，内容存储在当前目录下，文件名为weibo.txt
