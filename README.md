# FastProxy

## What?

你是否有以下苦恼：

-   打点之后的垃圾终端，命令难输的一批，稍有错误就要重新输入命令，甚至手贱断开shell又得再重新打一遍点
-   打点后要上传frp、fscan等工具，又要在vps中开代理，开httpserver，又要编辑frpc配置文件，又要连接到vps

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

![image-20230301123126817](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011231862.png)

假设成功打点获得了shell，将上方红色方框的命令放在打点的机器上执行

![image-20230301122640167](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011226239.png)

执行后，等待下载即可，不出意外的话就能挂上代理了

![image-20230301123408832](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011234871.png)

socks代理信息在vps端

-   socks认证：admin、password
-   frps的token默认为admin888，可以自行到tools目录下修改frpc.ini和frps.ini

![image-20230301123502389](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011235433.png)

给proxychains配置好代理信息，就可以愉快的梭内网了

![image-20230301123617341](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011236394.png)

打点后的工具和脚本都在/tmp目录下

![image-20230301123910341](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011239395.png)

## Notice

请注意，该脚本仅建议在打靶场时使用

使用完成后，自行擦屁股（本工具没有擦屁股功能）

![image-20230301124042839](https://lxxx-markdown.oss-cn-beijing.aliyuncs.com/pictures/202303011240881.png)