# 多线程C/S模型（Socket）
## 一、基本模型
```text
Server
├─ Client1
├─ Client2
└─ ...
```
## 二、启动步骤
1. 启动server，设置ip与port，默认本机回调
2. 启动client，设置目标服务器的ip与port，默认本机回调
3. 启动更多的client
## 三、展示效果
Server:
```text
我在MainThread线程中 
waiting for connecting...
connected from: ('127.0.0.1', 14054)
connected from: ('127.0.0.1', 14055)
[Thu May 13 17:12:41 2021][('127.0.0.1', 14054)]: b'11'
[Thu May 13 17:12:46 2021][('127.0.0.1', 14055)]: b'23'
```
Client1:
```text
>11
>
```
Client2:
```text
>23
>
```