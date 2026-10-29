"""Check all relative Markdown links without making network requests."""
from pathlib import Path
from urllib.parse import unquote
import re


def check(root):
    errors=[];count=0
    for file in root.rglob('*.md'):
        for link in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',file.read_text(encoding='utf-8')):
            destination=link.split('#',1)[0]
            if not destination or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:',destination):continue
            count+=1
            if not (file.parent/unquote(destination)).exists():errors.append(f'{file.relative_to(root)}: {destination}')
    return count,errors


if __name__=='__main__':
    root=Path(__file__).resolve().parents[1];count,errors=check(root)
    if errors:raise SystemExit('\n'.join(errors))
    print(f'Проверено относительных ссылок: {count}. Ошибок нет.')
