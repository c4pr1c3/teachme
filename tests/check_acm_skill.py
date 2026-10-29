#!/usr/bin/env python3
"""Zero-dependency structural checks for the TeachMe ACM skill branch."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "SKILL.md",
    "README.md",
    "references/acm/coaching.md",
    "references/acm/topic-cards.md",
    "references/acm/context-and-review.md",
    "references/acm/style-and-templates.md",
    "references/acm/verification.md",
    "references/acm/sources.md",
    "references/acm/quality-checklist.md",
    "tests/acm-scenarios.md",
]

REQUIRED_TOKENS = {
    "SKILL.md": [
        "name: teachme",
        "ACM/CCPC/ICPC 专项快速路由（优先）",
        "references/acm/coaching.md",
        "非 ACM 教学继续使用原三阶段流程",
    ],
    "references/acm/coaching.md": [
        "L1 观察",
        "L5 完整解答",
        "solution_viewed",
        ".teachme/acm/",
        "最小充分提示",
    ],
    "references/acm/context-and-review.md": [
        "完整程序",
        "核心片段",
        "已确认",
        "候选",
        "未匹配",
        "编译与正确性",
    ],
    "references/acm/style-and-templates.md": [
        "T1 直接套用",
        "T2 变式适配",
        "T3 组合建模",
        "T4 核心观察优先",
        "不能可靠证明代码由 AI 或人类编写",
    ],
    "references/acm/verification.md": [
        "用户声明 AC",
        "样例通过",
        "静态审查完成",
        "暴力对拍通过",
        "性能实测完成",
        "交互题",
    ],
    "references/acm/sources.md": [
        "CC BY-SA 4.0",
        "CC BY-NC-SA 4.0",
        "MIT",
        "stars/forks 只表示公开采用信号",
    ],
}

EXPECTED_SCENARIOS = {f"ACM-{i:02d}" for i in range(1, 13)} | {"GEN-01", "GEN-02"}
BACKTICK_PATH = re.compile(r"`((?:references|tests)/[^`\n]+?\.(?:md|py))`")
SCENARIO_HEADING = re.compile(r"^## ((?:ACM|GEN)-\d{2})：", re.MULTILINE)


def main() -> int:
    errors = []

    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or not path.read_text(encoding="utf-8").strip():
            errors.append(f"missing or empty: {relative}")

    for relative, tokens in REQUIRED_TOKENS.items():
        path = ROOT / relative
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for token in tokens:
            if token not in text:
                errors.append(f"{relative}: missing required token: {token}")

    markdown_files = [ROOT / "SKILL.md", ROOT / "README.md"]
    markdown_files.extend((ROOT / "references").rglob("*.md"))
    for path in markdown_files:
        text = path.read_text(encoding="utf-8")
        for relative in BACKTICK_PATH.findall(text):
            if not (ROOT / relative).is_file():
                errors.append(f"{path.relative_to(ROOT)}: broken path pointer: {relative}")

    scenarios_path = ROOT / "tests/acm-scenarios.md"
    if scenarios_path.is_file():
        scenarios = set(SCENARIO_HEADING.findall(scenarios_path.read_text(encoding="utf-8")))
        missing = sorted(EXPECTED_SCENARIOS - scenarios)
        extra = sorted(scenarios - EXPECTED_SCENARIOS)
        if missing:
            errors.append(f"tests/acm-scenarios.md: missing scenarios: {', '.join(missing)}")
        if extra:
            errors.append(f"tests/acm-scenarios.md: unexpected scenarios: {', '.join(extra)}")

    if errors:
        print("ACM skill structural checks FAILED:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"ACM skill structural checks passed: {len(REQUIRED_FILES)} required files, "
          f"{len(EXPECTED_SCENARIOS)} behavior scenarios, local pointers valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
