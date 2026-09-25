# OKWW 声骸实时评分

这是一个通过 OKWW（ok-script 机制）加载的《鸣潮》声骸实时评分功能。它复用 OKWW 的 OCR 图像识别能力，评分逻辑参考 [XutheringWavesUID（小维）](https://github.com/Loping151/XutheringWavesUID)。

> 当前版本为玩票性质的 BETA 版。请在了解相关风险后按需使用。项目不会修改 OKWW 宿主程序源码。

## 功能

在查看或调谐单个声骸时，工具会显示：

- 主词条及其分数贡献（红框区域）；
- 已解锁副词条及其分数贡献（白框区域）；
- 当前总分：主词条加已解锁副词条；
- 理论最高分：剩余副词条均出现最有效词条、且数值达到最高档位时的分数。

这些信息可以帮助你判断声骸是否值得继续开启副词条。

## 游戏语言

目前经过测试，支持游戏设置为**简体中文**或**繁体中文**时识别单个声骸的主词条、副词条及数值，并进行评分。繁体中文词条和“角色名裝配中”会在匹配前转换为评分模板使用的简体名称。其他游戏语言尚未测试。

## 安装

### 1. 安装 OKWW

本功能依赖 OKWW 的 OKScript 机制和 OCR 能力。请先从 [ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves) 了解并安装 OKWW；使用前请阅读其说明并自行评估风险。

### 2. 安装声骸评分脚本

本仓库提供可直接复制的 [`echo-score/`](echo-score/) 目录和同内容的 [`echo-score.zip`](echo-score.zip)。安装步骤：

1. 解压 `echo-score.zip`，或直接使用仓库中的 `echo-score` 文件夹；
2. 将整个文件夹复制到 OKWW 安装目录下的：

   ```text
   data/apps/ok-ww/working/ok_import/echo-score
   ```

   例如：

   ```text
   D:\ok-ww\data\apps\ok-ww\working\ok_import\echo-score
   ```

3. 重启 OKWW；
4. 在 OKWW 的“截图方式”页面选择鸣潮窗口并开始捕获，然后到“声骸评分”页面使用右上角的开/关按钮启用功能。评分设置修改后即时生效，无需点击任务“开始”。

### 3. 选择评分模板

打开“自动匹配评分模板”后，工具会根据单个声骸查看界面的“角色名装配中”选择模板，并在调谐界面沿用上一次识别结果；也可以在可输入搜索的下拉框中手动选择模板。

## 构建与目录结构

源码位于 [`echo-score/`](echo-score/)，其中包含设置页面、后台识别任务、繁简文字规范化、评分逻辑和角色模板数据。`echo-score.zip` 是该目录的打包副本，包含顶层 `echo-score/` 文件夹。

## 致谢与许可

- 感谢 [老王同学 OK](https://github.com/ok-oldking/ok-wuthering-waves) 开发 OKWW 及其 OKScript 机制；OKWW 使用 GNU Affero General Public License v3（AGPL-3.0）。
- 感谢 [Loping151（小维）](https://github.com/Loping151/XutheringWavesUID) 开源 XW-UID；其项目使用 GNU General Public License v3（GPL-3.0）。本项目的评分逻辑参考该项目。
- 本项目代码按 GNU GPL v3 发布，详见 [`LICENSE`](LICENSE)。第三方项目及其代码仍分别受各自许可证约束。

问题反馈和改进建议欢迎通过仓库 Issue 提交。
