import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents" / "skills" / "research-design-evidence"
WORKFLOWS = ("closest-work-gap.md", "claim-experiment-design.md")


class ResearchDesignPackageTests(unittest.TestCase):
    def test_standalone_prompts_match_bundled_workflows(self):
        for name in WORKFLOWS:
            with self.subTest(name=name):
                prompt = (ROOT / "prompts" / name).read_bytes()
                self.assertTrue(prompt.strip())
                self.assertEqual(prompt, (SKILL / "references" / name).read_bytes())

    def test_skill_links_to_its_bundled_workflows(self):
        entry = (SKILL / "SKILL.md").read_text(encoding="utf-8")
        links = set(re.findall(r"\]\((references/[^)]+)\)", entry))
        self.assertEqual(links, {f"references/{name}" for name in WORKFLOWS})
        for link in links:
            self.assertTrue((SKILL / link).is_file(), link)

    def test_readme_links_to_the_public_entries(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        links = set(re.findall(r"\]\(([^)]+)\)", readme))
        entries = {
            (SKILL / "SKILL.md").relative_to(ROOT).as_posix(),
            "tests/research-design-evidence.md",
            *(f"prompts/{name}" for name in WORKFLOWS),
        }
        for entry in entries:
            with self.subTest(entry=entry):
                self.assertIn(entry, links)
                self.assertTrue((ROOT / entry).is_file(), entry)
