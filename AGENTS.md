# 分发仓库同步清单

本仓库是 `E:/ok-wuthering-waves` 的声骸评分 OK Script 分发产物。每次上游实现或模板变化后：

- [ ] 从主项目重新构建 `dist/echo-score`，同步到本仓库 `echo-score/` 和 `D:/ok-ww/data/apps/ok-ww/working/ok_import/echo-score/`，核对文件内容一致。
- [ ] 将本仓库 `echo-score/` 重新打包为 `echo-score.zip`（ZIP 内保留顶层 `echo-score/`），排除缓存文件并校验归档内容。
- [ ] 必要时更新 README；确认主项目测试通过、版本号一致、两个仓库 diff 合理，然后分别 commit & push。不要只更新 D 盘安装目录。

仅同步 XW-UID 评分模板时，在主项目运行
`.venv/Scripts/python.exe scripts/update_xwuid_echo_templates.py --publish --commit-push`。
该脚本全量拉取角色和模态权重，自动执行测试、目录同步、ZIP 校验和两个仓库的提交推送；
两个仓库必须先保持干净。用 `--check` 可先查看差异，无变化时不会重复发布。
