# FastProxy

## What?

你是否有以下苦恼：

-   打点之后的垃圾终端，命令难输的一批，稍有错误就要重新输入命令，甚至手贱断开shell又得再打一遍
-   打点后要上传frp、fscan等工具，又要在vps中开代理，又要编辑frpc配置文件，又要连接到vps

FastProxy目标：在vps启动一次，仅在打点机上执行一条命令就完成代理等动作

## How to use？

clone项目：

```sh
git clone https://github.com/LxxxSec/FastProxy
cd FastProxy/
```

![image-20230301122052896](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011220090.png)

pip3安装flask：

```sh
pip3 install --upgrade flask
```

在远程vps中启动app.py脚本：

-   第一个参数是远程vps的IP
-   第二个参数为端口，填写任意空闲端口即可

```sh
python3 app.py 121.40.253.177 12345
```

![image-20230301122146806](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011221857.png)

将上方红色方框的命令放在打点的机器上执行

![image-20230301122640167](../../../Library/Application%20Support/typora-user-images/image-20230301122640167.png)