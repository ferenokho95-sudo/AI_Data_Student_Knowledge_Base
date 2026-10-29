from pathlib import Path
import importlib.util
import json
import os
import contextlib
import io


root=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('example',root/'examples/first_analysis.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
data,result=module.analyze()
notebook=json.loads((root/'examples/first_analysis.ipynb').read_text(encoding='utf-8'))
assert notebook['nbformat']==4
assert any(cell['cell_type']=='code' for cell in notebook['cells'])
assert all(cell.get('cell_type') in ['code','markdown'] for cell in notebook['cells'])
previous=Path.cwd()
try:
    os.chdir(root/'examples')
    namespace={}
    with contextlib.redirect_stdout(io.StringIO()):
        for cell in notebook['cells']:
            if cell['cell_type']=='code':
                exec(compile(''.join(cell['source']),'first_analysis.ipynb','exec'),namespace)
    assert namespace['total']==4100
finally:
    os.chdir(previous)
print('Пример Python и все кодовые ячейки ноутбука проверены. Выручка:',int(data.revenue.sum()))
