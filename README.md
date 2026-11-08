# cs-prompt-skill

可复用的学术写作 Skill 与 Prompt。当前提供 **论文发布会原则**，用于英文论文的审查、改写和信息保真的压缩。

围绕证据最充分的优势组织“问题 → 缺口 → 方法 → 证据”主线，主动解释贡献，精简失败尝试和重复辩解。对影响结论的弱项，根据已有证据说明目标、约束或权衡，必要时收缩主张。保留技术事实、实验数值、LaTeX 公式、标签及引用。

## 选择使用方式

| 方式 | 适用场景 | 入口 |
| --- | --- | --- |
| Skill 调用 | 在支持 Agent Skills 的工具中重复使用 | [论文发布会原则 Skill](.agents/skills/paper-launch-principles/SKILL.md) |
| Prompt 复制 | 在聊天界面粘贴规则并处理论文 | [完整 Prompt](prompts/paper-launch-principles.md) |

## 方式一 · Skill 调用

### 在本仓库中使用 Codex

```bash
git clone https://github.com/Lccs02/cs-prompt-skill.git
cd cs-prompt-skill
```

在这个仓库目录打开 Codex。Skill 位于 `.agents/skills/paper-launch-principles/`，可通过 `/skills` 查看，或在任务中输入 `$paper-launch-principles` 调用。

### 安装到其他论文项目

将整个 `.agents/skills/paper-launch-principles` 文件夹复制到论文项目的 `.agents/skills/` 下。安装后的入口应为 `<论文项目>/.agents/skills/paper-launch-principles/SKILL.md`。

### 在 Windows 上供所有项目使用

在克隆后的仓库根目录运行 PowerShell。首次安装会复制到当前用户的 `~/.agents/skills/`。

```powershell
$skillSource = Join-Path (Get-Location) '.agents/skills/paper-launch-principles'
$skillsDirectory = Join-Path $HOME '.agents/skills'
$skillDestination = Join-Path $skillsDirectory 'paper-launch-principles'
if (Test-Path $skillDestination) {
    throw '目标技能已存在，请先核对已有版本，再决定是否替换。'
}
New-Item -ItemType Directory -Force -Path $skillsDirectory | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillDestination -Recurse
```

macOS / Linux 用户可在仓库根目录运行以下命令完成首次安装。

```bash
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/paper-launch-principles" ]; then
  echo '目标技能已存在，请先核对已有版本，再决定是否替换。'
else
  cp -R .agents/skills/paper-launch-principles "$HOME/.agents/skills/"
fi
```

在 ChatGPT 中已安装此技能时，可通过输入框的 `@` 选择“论文发布会原则”。本地安装路径与调用方式参见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

### 调用示例

**审查**

```text
用 $paper-launch-principles 审查下面的实验分析。
按影响排序指出防御性措辞、过程性叙事和缺乏证据的主张，并提供英文替换建议。

〔粘贴原文〕
```

**改写**

```text
用 $paper-launch-principles 改写下面的引言。
突出最有证据支持的贡献，保留技术事实与引用键，给出可直接替换的完整英文 LaTeX。

〔粘贴原文〕
```

**压缩**

```text
用 $paper-launch-principles 将下面的实验设置压缩约 20%。
保留全部实验参数、数值、公式、标签和引用，优先通过句法优化与消除冗余压缩。
只输出可直接替换的英文 LaTeX。

〔粘贴原文〕
```

## 方式二 · Prompt 复制

打开 [完整 Prompt](prompts/paper-launch-principles.md)，复制全部内容到聊天输入框，填写文末的任务类型、修改范围、压缩目标和输出形式，然后粘贴论文原文。两种方式使用相同的核心规则。

Prompt 默认提供简短中文修改说明和英文 LaTeX。任务可指定“仅审查”“只输出代码”或“减少 5–15 个英文单词”等细化要求。

## 文件与维护

| 文件 | 用途 |
| --- | --- |
| `.agents/skills/paper-launch-principles/SKILL.md` | 技能元数据及完整写作规则 |
| `.agents/skills/paper-launch-principles/agents/openai.yaml` | 显示名称、默认调用提示及自动匹配设置 |
| `prompts/paper-launch-principles.md` | 独立可复制的提示词与任务填写区 |

更新写作规则时，同步修改 Skill 与 Prompt 中对应的规则。Skill 的 YAML 元数据用于发现技能，Prompt 的任务填写区用于单次输入。
