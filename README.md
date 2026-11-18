# cs-prompt-skill

两套可复用的科研 Skill 和三个独立 Prompt，覆盖研究设计、实验论证与英文论文写作。

## 选择使用方式

| 你要做的决定 | Skill | 可直接复制的 Prompt |
| --- | --- | --- |
| 比较最接近工作，判断哪个机制差异值得研究 | [科研设计与实验证据](.agents/skills/research-design-evidence/SKILL.md) | [A · 最接近工作与研究缺口核查](prompts/closest-work-gap.md) |
| 判断已有证据能支持哪句主张，决定是否补实验 | [科研设计与实验证据](.agents/skills/research-design-evidence/SKILL.md) | [B · 核心主张与实验设计](prompts/claim-experiment-design.md) |
| 审查、改写或压缩英文稿，保留数值、LaTeX 和引用 | [论文发布会原则](.agents/skills/paper-launch-principles/SKILL.md) | [写作 · 论文发布会原则](prompts/paper-launch-principles.md) |

选题时把候选机制和原文交给 A。准备做实验时，把可检验的假设和已有结果交给 B。手头已经有实验表，可以直接从 B 开始。写论文时，把核实过的主张、证据位置和适用条件交给写作入口。

## 方式一 · Skill 调用

### 在本仓库中使用 Codex

```bash
git clone https://github.com/Lccs02/cs-prompt-skill.git
cd cs-prompt-skill
```

在仓库目录打开 Codex，通过 `/skills` 查看两个 Skill。也可以在任务中输入 `$research-design-evidence` 或 `$paper-launch-principles`。

### 安装到其他论文项目

将所需 Skill 的整个文件夹从本仓库的 `.agents/skills/` 复制到论文项目的 `.agents/skills/`。例如，科研设计入口为 `<论文项目>/.agents/skills/research-design-evidence/SKILL.md`，其 `references/` 子目录随文件夹一起复制。

### 在当前用户的所有项目中使用

Windows 用户在克隆后的仓库根目录运行 PowerShell。下面以科研设计为例。安装写作 Skill 时，将第一行的名称改为 `paper-launch-principles`。

```powershell
$skillName = 'research-design-evidence'
$skillSource = Join-Path (Get-Location) ".agents/skills/$skillName"
$skillsDirectory = Join-Path $HOME '.agents/skills'
$skillDestination = Join-Path $skillsDirectory $skillName
if (Test-Path $skillDestination) {
    throw '目标技能已存在，请先核对已有版本，再决定是否替换。'
}
New-Item -ItemType Directory -Force -Path $skillsDirectory | Out-Null
Copy-Item -LiteralPath $skillSource -Destination $skillDestination -Recurse
```

macOS / Linux 用户可在仓库根目录运行以下命令完成首次安装。

```bash
skill_name=research-design-evidence
mkdir -p "$HOME/.agents/skills"
if [ -e "$HOME/.agents/skills/$skill_name" ]; then
  echo '目标技能已存在，请先核对已有版本，再决定是否替换。'
else
  cp -R ".agents/skills/$skill_name" "$HOME/.agents/skills/"
fi
```

在 ChatGPT 中已安装相应 Skill 时，可通过输入框的 `@` 选择其显示名称。安装路径和调用方式参见 [OpenAI 官方技能文档](https://learn.chatgpt.com/docs/build-skills)。

### 调用示例

**判断研究缺口**

```text
用 $research-design-evidence 比较下面两篇方法的训练目标和推理输出。
给出能定位到原文的机制差异，以及一个会推翻我的判断的例子。
〔粘贴候选机制、原文或公式〕
```

**决定是否补实验**

```text
用 $research-design-evidence 判断这张表能否支持我的主张。
考虑已经做过的对照和已有预测。如果仍有缺口，只给一项最值得做的实验。
〔粘贴一句主张、实验协议、结果和可复用的产物〕
```

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

从页首表格打开所需 Prompt，复制全文到新对话。研究 Prompt 提供“我的输入”填写区，只有一段原文或一张实验表也可以开始。写作 Prompt 在文末填写任务类型、修改范围、压缩目标和输出形式。

写作 Prompt 默认提供简短中文修改说明和英文 LaTeX。任务可指定“仅审查”“只输出代码”或“减少 5–15 个英文单词”等细化要求。

## 维护与复测

研究 Prompt 的原件位于 `.agents/skills/research-design-evidence/references/`。修改后将同名文件复制到 `prompts/`，使单独安装 Skill 和复制 Prompt 的用户获得同一套规则。更新写作规则时，也应同步更新写作 Skill 和写作 Prompt。

在仓库根目录运行 `python -m unittest discover -s tests` 可检查研究 Prompt 的内容和相对链接。要复核模型能否识别证据缺口、按预设门槛作决定，可使用[三个公开测试用例](tests/research-design-evidence.md)。
