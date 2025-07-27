"""Load persona prompts from markdown."""

from pathlib import Path
from typing import Dict

from .persona import Persona


def _parse_persona_md(path: Path) -> Dict[str, str]:
    prompts: Dict[str, str] = {}
    name: str | None = None
    buf: list[str] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            if name:
                prompts[name] = "\n".join(buf).strip()
                buf = []
            parts = line.split(" ", 2)
            name = parts[2] if len(parts) > 2 else parts[-1]
        else:
            if name:
                buf.append(line)
    if name:
        prompts[name] = "\n".join(buf).strip()
    return prompts


def load_personas() -> Dict[str, Persona]:
    root = Path(__file__).resolve().parents[1]
    files = [root / "AI_Persona_Prompts.md", root / "examples" / "new_persona_prompts.md"]
    voice = root / "examples" / "voice_dictation_prompts.md"
    personas: Dict[str, Persona] = {}
    for file in files:
        for name, prompt in _parse_persona_md(file).items():
            personas[name] = Persona(name=name, prompt=prompt)
    voice_prompts = _parse_persona_md(voice)
    for name, vp in voice_prompts.items():
        if name in personas:
            personas[name].voice_prompt = vp
    return personas
