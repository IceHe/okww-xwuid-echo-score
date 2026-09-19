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

## 安装

### 1. 安装 OKWW

本功能依赖 OKWW 的 OKScript 机制和 OCR 能力。请先从 [ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves) 了解并安装 OKWW；使用前请阅读其说明并自行评估风险。

### 2. 安装声骸评分脚本

推荐使用 OKWW 的“脚本”页面导入仓库发布的 `echo-score.okscript` 文件。导入后，在“声骸评分设置”任务卡中启用功能。

如果需要手动复制文件：

1. 解压本项目发布包中的 `echo-score` 文件夹；
2. 将整个文件夹复制到 OKWW 安装目录下的：

   ```text
   data/apps/ok-ww/working/ok_import/echo-score
   ```

   例如：

   ```text
   D:\ok-ww\data\apps\ok-ww\working\ok_import\echo-score
   ```

3. 重启 OKWW；
4. 在首页点击“开始”，进入“声骸评分”页面并开启功能。

### 3. 选择评分模板

可以保持“自动识别”，让工具根据当前角色自动选择模板；也可以在设置中搜索或下拉选择指定角色的评分模板。

## 构建与目录结构

源码位于 [`echo-score/`](echo-score/)，其中包含设置页面、后台识别任务、评分逻辑和角色数据。若本地已有构建脚本，可生成 OKWW 导入包：

```powershell
.\\.venv\\Scripts\\python.exe scripts\\build_echo_score_okscript.py
```

生成的导入包位于 `dist/echo-score.okscript`，手动复制目录时使用 `dist/echo-score/`。

## 致谢与许可

- 感谢 [老王同学 OK](https://github.com/ok-oldking/ok-wuthering-waves) 开发 OKWW 及其 OKScript 机制；OKWW 使用 GNU Affero General Public License v3（AGPL-3.0）。
- 感谢 [Loping151（小维）](https://github.com/Loping151/XutheringWavesUID) 开源 XW-UID；其项目使用 GNU General Public License v3（GPL-3.0）。本项目的评分逻辑参考该项目。
- 本项目代码按 GNU GPL v3 发布，详见 [`LICENSE`](LICENSE)。第三方项目及其代码仍分别受各自许可证约束。

问题反馈和改进建议欢迎通过仓库 Issue 提交。
