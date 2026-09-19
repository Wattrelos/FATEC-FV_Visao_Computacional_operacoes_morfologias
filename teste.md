# Issue de encoding no Windows

### 🔍 Por que o erro acontece no Windows?

1. **Acentos nos comentários + Codificação ANSI/CP1252**:
   - No Windows, muitos arquivos são salvos por padrão em **Windows-1252 (ANSI)**.
   - O Python 3 espera que arquivos de código estejam em **UTF-8**. Ao encontrar caracteres como `ç` (`0xe7`) ou `ã` (`0xe3`) na primeira linha (`#importação...`), o interpretador dispara o erro:
     ```text
     SyntaxError: Non-UTF-8 code starting with '\xe7' in file teste.py on line 1, but no encoding declared
     ```

2. **Falta de extensão no `imwrite` (outro erro que ocorreria)**:
   - Na linha 15 estava `cv2.imwrite("Imagem processada", imProc)` sem a extensão (`.bmp`). O OpenCV precisa da extensão para saber o formato de gravação.

---

### 🛠️ O que foi corrigido no arquivo [teste.py](file:///var/www/html/AndroidStudioProjects/Visão Computacional/FATEC-FV_VC_BGR2GRAY/teste.py):

1. **Declaração de codificação UTF-8**:
   - Adicionado `# -*- coding: utf-8 -*-` na primeira linha.
2. **Remoção de acentos nos comentários**:
   - Trocado `importação` por `importacao`, `função` por `funcao`, `morfológico` por `morfologico` e `método` por `metodo`. Isso garante compatibilidade universal, mesmo se o Windows abrir em CP1252/ANSI.
3. **Extensão do arquivo no `cv2.imwrite`**:
   - Alterado para `cv2.imwrite("Imagem_processada.bmp", imProc)`.
4. **Proteção contra imagem não encontrada**:
   - Adicionada verificação `if imOriginal is None:` para exibir uma mensagem clara se o caminho no Desktop estiver incorreto ou o arquivo não existir.

---

### 💡 Dica no VS Code do Windows:
Se ainda quiser usar acentos em scripts Python no Windows:
1. Olhe no **canto inferior direito da barra de status do VS Code**.
2. Se estiver mostrando `Windows 1252` ou `CP1252`, clique nele.
3. Selecione **"Salvar com codificação" (Save with Encoding)** e escolha **`UTF-8`**.