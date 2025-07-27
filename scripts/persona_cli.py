import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROMPT_FILES = [ROOT / 'AI_Persona_Prompts.md', ROOT / 'examples' / 'new_persona_prompts.md']
VOICE_FILE = ROOT / 'examples' / 'voice_dictation_prompts.md'

def parse_persona_md(path):
    prompts = {}
    name = None
    buf = []
    for line in open(path, encoding='utf-8'):
        if line.startswith('### '):
            if name:
                prompts[name] = ''.join(buf).strip()
                buf = []
            match = re.match(r'^###\s+\d+\.\s+(.*)$', line)
            if match:
                name = match.group(1).strip()
            else:
                name = None
        else:
            if name is not None:
                buf.append(line)
    if name:
        prompts[name] = ''.join(buf).strip()
    return prompts

def parse_voice_prompts(path):
    voice = {}
    name = None
    for line in open(path, encoding='utf-8'):
        if line.startswith('### '):
            match = re.match(r'^###\s+\d+\.\s+(.*)$', line)
            if match:
                name = match.group(1).strip()
        elif name and line.strip().startswith('"'):
            voice[name] = line.strip().strip('"')
            name = None
    return voice

def load_library():
    prompts = {}
    for path in PROMPT_FILES:
        prompts.update(parse_persona_md(path))
    voice = parse_voice_prompts(VOICE_FILE)
    return prompts, voice

def cmd_list(prompts):
    for i, name in enumerate(prompts, 1):
        print(f"{i}. {name}")

def cmd_use(prompts, name):
    text = prompts.get(name)
    if not text:
        print(f"Persona '{name}' not found.")
        return
    print(text)

def cmd_voice(voice, name):
    text = voice.get(name)
    if not text:
        print(f"Voice prompt for '{name}' not found.")
        return
    print(text)

def cmd_help():
    print("Commands: /list, /use <name>, /voice <name>, /help")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        cmd_help()
        sys.exit(0)
    command = sys.argv[1]
    prompts, voice = load_library()
    if command == '/list':
        cmd_list(prompts)
    elif command == '/use' and len(sys.argv) > 2:
        name = ' '.join(sys.argv[2:])
        cmd_use(prompts, name)
    elif command == '/voice' and len(sys.argv) > 2:
        name = ' '.join(sys.argv[2:])
        cmd_voice(voice, name)
    else:
        cmd_help()
