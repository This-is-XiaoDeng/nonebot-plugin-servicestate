<p align="center">
  <a href="https://v2.nonebot.dev/"><img src="https://v2.nonebot.dev/logo.png" width="200" height="200" alt="nonebot"></a>
</p>

<div align="center">

# NoneBot Plugin ServiceStatus

_✨ NoneBot 服务状态查询插件 ✨_

</div>

<p align="center">
  <a href="https://raw.githubusercontent.com/nonebot/plugin-apscheduler/master/LICENSE">
    <img src="https://img.shields.io/github/license/nonebot/plugin-apscheduler.svg" alt="license">
  </a>
  <a href="https://pypi.python.org/pypi/nonebot-plugin-apscheduler">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-apscheduler.svg" alt="pypi">
  </a>
  <img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">
</p>

## 简介

可通过 `服务状态` 查询当前服务器各功能 API 可用状态

例如：

```
O 可用 | 会战面板
O 可用 | SSH登录
X 故障 | 涩图
O 可用 | 画图
X 故障 | ChatGPT
```


## 特色

- 易于上手：所有配置项的增删查改都可通过文本交互实现，无需修改任何配置文件
- 异步支持：所有协议均通过异步实现，无需担心探测过程中造成堵塞
- 易于拓展：开发者只需继承内部抽象基类`BaseProtocol`并实现部分核心方法即可增添新协议支持


## 安装

使用 `nb-cli` 安装（推荐）：
```
nb plugin install nonebot-plugin-servicestate
```

使用 `git clone` 安装：
```
git clone https://github.com/OREOCODEDEV/nonebot-plugin-servicestate.git
```


## 使用

### 服务状态查询
可通过发送 `服务状态` 获取当前绑定的监控服务可用状态

### 新增监控服务
可通过发送 `添加监控服务 <协议> <名称> <地址>` 以新增需要监控的服务
```
添加监控服务 HTTP git截图 https://github.com
```

### 修改监控服务
可通过发送 `修改监控服务 <名称> <参数名> <参数内容>` 以修改监控服务的参数
* 不同协议支持修改的参数内容不同，具体请参考下方协议篇
```
修改监控服务 git截图 proxy http://127.0.0.1:10809
```

### 群组监控服务
**当前版本服务群组后暂不支持修改及解除群组，只能删除群组，请注意**

当多个API共同支持某项服务时，可通过 `群组监控服务 <名称1> <名称2> <群组名称>` 群组多个服务为一个显示

* 只有当群组中的所有服务都为可用状态时，群组才显示为可用，当有一个或多个服务为故障状态时，群组都显示为故障

例：假设当前已设置好 涩图信息API 和 涩图图床 两个监控服务，可通过下列命令组合为一个服务
```
群组监控服务 涩图信息API 涩图图床 涩图
```
群组命令前：
```
O 可用 | 涩图信息API
X 故障 | 涩图图床
```
群组命令后：
```
X 故障 | 涩图
```

### 群组监控服务
可通过发送 `删除监控服务 <名称>` 以不再监测该服务
```
删除监控服务 git截图
```


## 协议支持

以下是项目当前支持的协议，以及可被通过修改命令配置的字段

### HTTP GET
- [x] 状态查询：无关键字
- [x] 监测地址：`host`
- [x] 代理地址：`proxies`
- [x] 超时时间：`timeout`
- [ ] 请求头：暂未支持
- [ ] UA：暂未支持
- [ ] Cookie：暂未支持
- [ ] 有效响应码：暂未支持

### TCP
- [x] 状态查询：无关键字
- [x] 监测地址：`host`
- [x] 端口：`port`
- [ ] 代理地址：暂未支持
- [ ] 超时时间：暂未支持

### PING
- [ ] 状态查询：暂未支持
- [ ] 监测地址：暂未支持
- [ ] 代理地址：暂未支持
- [ ] 超时时间：暂未支持


## Todo
- [ ] 支持更多配置字段
- [ ] 协议拓展接口增强
- [ ] 解绑群组支持
- [ ] 群组编辑支持
