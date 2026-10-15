# 个人主页维护指南

网站：https://circlelzy.github.io/  
仓库：`circleLZY/circleLZY.github.io`，主分支：`main`。

## 技术结构

这是基于 AcadHomepage / Minimal Mistakes 的 Jekyll 静态单页站点，使用 Liquid 模板、Kramdown Markdown、SCSS 和 jQuery，没有独立后端或 Node 应用。

渲染入口为 `_pages/about.md`，通过 `include_relative` 依次拼入正文片段，再由 `_layouts/default.html` 添加导航、侧栏、样式和脚本。`/about/` 与 `/about.html` 重定向到 `/`。

`_config.yml` 维护站点地址、作者信息、构建配置及插件；`_data/navigation.yml` 维护顶栏链接。GitHub Pages 发布站点，仓库中唯一的自定义 Actions 工作流用于抓取 Google Scholar 引用数据。

## 更新内容的位置

- `_pages/includes/intro.md`：个人简介、研究方向。
- `_pages/includes/news.md`：动态，按月份倒序。
- `_pages/includes/experience.md`：教育和工作／实习经历。
- `_pages/includes/pub.md`：精选论文，按遥感变化检测、SAR 图像处理和其他研究分类。
- `_pages/includes/project.md`：项目经历。
- `_pages/includes/contest.md`：竞赛成绩。
- `_pages/includes/honers.md`：荣誉、奖学金及体育经历。文件名沿用现有拼写，改名时需同步修改入口引用。
- `_pages/includes/service.md`：学术服务。
- `_config.yml` 的 `author`：姓名、头像、邮箱、机构、社交与学术链接。
- `images/`：头像、论文配图和站点图标。

新增普通条目只需编辑相应片段。新增一级栏目还需在 `_pages/about.md` 中引入，并按需要更新 `_data/navigation.yml`。顶栏锚点对应 Kramdown 生成的标题 ID；修改标题后应检查导航跳转。

正文片段不带 YAML front matter，并在 `_config.yml` 的 `exclude` 中排除独立发布。Jekyll 的 `include_relative` 仍可读取它们。这样可避免把片段生成重复页面并加入 sitemap。

论文卡片混用 HTML 和 Markdown，内部的 `markdown="1"` 使论文链接、作者加粗和列表得以解析。添加论文时可复制相邻卡片，替换标题、作者、会议／期刊标记、图片、链接和描述。

## 样式与交互

- `assets/css/main.scss` 汇总 `_sass/` 并定义论文卡片、锚点偏移和期刊标记。
- `_sass/_variables.scss` 定义字体、颜色和布局断点。
- `_sass/_sidebar.scss`、`_masthead.scss`、`_navigation.scss` 控制侧栏和顶栏布局。
- 页面加载的 JS 是 `assets/js/main.min.js`，包含 jQuery、响应式导航、平滑滚动和图片弹窗。
- `assets/js/_main.js` 和 `assets/js/plugins/` 是相关源码，当前仓库没有 JS 打包脚本；只修改这些源码不会更新线上实际加载的 bundle。
- `assets/js/collapse.js` 与 `assets/css/collapse.css` 当前未被页面引用。
- `_includes/head/custom.html` 配置 MathJax 和图标。MathJax 使用 2.x 的配置格式，应直接加载对应版本的 `MathJax.js`。
- 页面保留 `<base target="_blank">`，普通外链默认在新标签打开；同页导航由平滑滚动脚本处理。

## 引用数据与外部服务

`.github/workflows/google_scholar_crawler.yaml` 在推送 `main` 后及每天 08:00 UTC（北京时间 16:00）计划运行，也支持在 Actions 页面手动运行，实际启动时间可能延迟。使用 Python 3.12，脚本读取仓库 Secret `GOOGLE_SCHOLAR_ID`，调用 `google_scholar_crawler/main.py`，将 JSON 写入 `google-scholar-stats` 分支。工作流显式配置写入权限及机器人提交身份，按顺序运行，保留数据分支提交历史；抓取或校验失败时不会发布数据。

`_includes/fetch_google_scholar_stats.html` 从 jsDelivr 或 GitHub Raw 读取 JSON，只在页面存在引用数元素时发起请求。总引用数元素为 `id="total_cit"`；单篇引用数示例：

```html
<span class="show_paper_citations" data="SCHOLAR_ID:PUBLICATION_ID"></span>
```

论文区已启用 Google Scholar 总引用数徽章，点击可进入作者主页。Shields.io 读取数据分支的 `gs_data_shieldsio.json`，直接使用 Google Scholar 返回的总引用数，不累加单篇引用数。徽章直接从 GitHub Raw 读取，避免额外的 jsDelivr 缓存层；Shields.io 和浏览器仍可能有数分钟缓存。当前正文未启用上述 JS 引用数元素。GitHub Stars badge 为另一张独立的 Shields.io 图片。

爬虫保留 `scholarly==1.5.1`，并固定兼容依赖 `bibtexparser==1.4.4`。不要直接升级到 bibtexparser 2.x：它移除了 scholarly 依赖的 `bibtexparser.bibdatabase` 模块。更新依赖时需实际检查 scholarly 导入和数据抓取。

爬虫的离线测试可使用 `python -m unittest discover -s google_scholar_crawler -p 'test_*.py' -v` 运行，覆盖总引用数、零引用、单篇 ID、异常数据不覆盖已有文件、缺失 Secret 的报错。真实抓取完成前不会将错误或空值替换成零引用数。

Google Analytics 只在 `_config.yml` 配置非空 `google_analytics_id` 后加载。页面底部还引用了 RevolverMaps 脚本。

## 本地运行与验证

依赖版本由 `Gemfile.lock` 锁定，目前为 GitHub Pages 215、Jekyll 3.9.0、Bundler 2.2.19。准备兼容的 Ruby、RubyGems 和编译工具后：

```sh
gem install bundler -v 2.2.19
bundle install
bash run_server.sh
```

默认访问 http://127.0.0.1:4000/。`run_server.sh` 使用 Hawkins 提供的 `jekyll liveserve`；修改 `_config.yml` 后需重启。

构建检查：

```sh
JEKYLL_ENV=production bundle exec jekyll build --safe
git diff --check
```

现有锁文件仅列出 `universal-darwin-19` 与 `x86_64-linux`。其他平台可能需要补充平台记录；本轮验证使用临时 Gemfile/锁文件副本安装依赖，未修改仓库锁文件或系统 Ruby。

更新后重点检查：完整正文、桌面和手机布局、顶栏锚点、论文图片与公式、浏览器错误、旧地址重定向，以及 sitemap 只包含正式页面。

## 提交与发布约定

每轮修改完成并通过本地验证后，提交到 Git 并推送远端 `main`，随后检查 GitHub Pages 的部署结果和实际线上页面。此流程已获站点所有者授权；提交前先同步远端状态，保留他人的改动。若线上出现新的问题，修复、验证后再提交发布。

## 2026-10-15 检查记录

已修复：引用统计访问空元素／缺失论文时报错；MathJax 的旧 `latest.js` 加载器无法处理接口返回的 4.x 版本；manifest 图标地址错误及不存在的 Windows 图标配置；重复的 `<head>`；不存在的 `compress` 父布局；未配置 ID 仍加载 Analytics；8 个正文片段被作为独立网页发布并写入 sitemap。另修正 `anovel` 为 `a novel`，显式配置正式站点 URL。

首次本地检查通过：Jekyll 生产模式安全构建、全部导航锚点及本地资源检查、manifest 图标与 sitemap 检查、引用脚本的空元素／缺失数据／零引用数场景；浏览器确认桌面与 390px 手机布局、菜单跳转、8 张图片加载和 2 处数学公式渲染，未捕获 JS 错误。该次构建提示未提供 GitHub API 认证，当时尚未提交或触发远端 Actions。

引用任务后续排查：在干净的 Python 3.12 环境中复现 `ModuleNotFoundError: No module named 'bibtexparser.bibdatabase'`，锁定 bibtexparser 1.4.4 后实际抓取成功。2026-10-15 返回总引用数 232、论文 19 篇；该数值为排查时快照，线上以数据分支为准。参考站点 likyoo.github.io 使用相同爬虫与 Shields.io 方案，其当时的最新抓取也失败，JSON 停留在 2026-09-06。

其他待后续处理：

- 本轮环境无法解析 `rf.revolvermaps.com`；尚不能确认是服务还是网络问题，保留现有引用。
- 内容更新时复核简介中的 `fourth-year`、仍标记为 `Now` 的经历，以及最新动态。目前 News 最新条目为 2026.06，体育经历最新条目为 2026.03；本轮没有推断或补写个人近况。
