# Problema: Avisos do Qt (Wayland e QFontDatabase) ao executar OpenCV no Linux

Ao executar scripts com interface gráfica do OpenCV (`cv2.imshow`), podem surgir no terminal avisos como:

```text
qt.qpa.plugin: Could not find the Qt platform plugin "wayland" in ".../cv2/qt/plugins"
QFontDatabase: Cannot find font directory .../cv2/qt/fonts.
Note that Qt no longer ships fonts. Deploy some (from https://dejavu-fonts.github.io/ for example) or switch to fontconfig.
```

---

## 🔍 Causas

1. **Plugin Wayland ausente no pacote pip do OpenCV (`qt.qpa.plugin`)**:
   - Em distribuições Linux modernas rodando sessão Wayland, o Qt tenta utilizar o plugin nativo de Wayland.
   - Porém, a biblioteca pré-compilada `opencv-python` inclui apenas o plugin X11 (`xcb`), gerando o aviso antes de recorrer ao XWayland.

2. **Pasta de fontes interna ausente (`QFontDatabase`)**:
   - As versões mais recentes do Qt embutidas no OpenCV esperam encontrar fontes na pasta interna `cv2/qt/fonts`, que não vem preenchida por padrão no wheel do pip.

---

## 🛠️ Soluções Aplicadas

### 1. Forçar a plataforma Qt para `xcb` no código Python
Adicione no início do script, **antes** de importar o `cv2`:

```python
import os
os.environ.setdefault("QT_QPA_PLATFORM", "xcb")

import cv2
```

> Alternativamente, pode ser exportado no terminal ou no `activate` do venv:
> ```bash
> export QT_QPA_PLATFORM=xcb
> ```

### 2. Criar link simbólico para as fontes do sistema no venv
Para eliminar o aviso de `QFontDatabase`, basta vincular as fontes TrueType do sistema (DejaVu) à pasta de fontes do Qt do OpenCV no venv:

```bash
ln -s /usr/share/fonts/truetype/dejavu venv/lib/python3.*/site-packages/cv2/qt/fonts
```
