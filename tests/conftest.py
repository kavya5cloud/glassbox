from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ROOT_STR = str(ROOT)
if ROOT_STR in sys.path:
    sys.path.remove(ROOT_STR)
sys.path.insert(0, ROOT_STR)

for module_name in list(sys.modules):
    if module_name == "glassbox" or module_name.startswith("glassbox."):
        del sys.modules[module_name]
