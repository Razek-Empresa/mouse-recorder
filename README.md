# Mouse Recorder

Gravador e reprodutor de movimentos, cliques e rolagem do mouse, pensado para automatizar tarefas repetitivas no computador.  
Este projeto utiliza a biblioteca `pynput` para capturar e simular eventos de mouse e teclado.

## Pré-requisitos

- **Python**: versão 3.8 ou superior recomendada.
- **pip**: gerenciador de pacotes do Python.
- **Sistema operacional**: focado em Windows, mas pode funcionar em outros sistemas suportados pelo `pynput`.
- **Permissões**:
  - Em alguns casos, pode ser necessário executar o terminal como **Administrador** (no Windows) para que a captura global de mouse/teclado funcione corretamente.

## Instalação

1. **Clonar o repositório**

   ```bash
   git clone https://seu-servidor-ou-github/mouse-recorder.git
   cd mouse-recorder
   ```

2. **(Opcional, mas recomendado) Criar um ambiente virtual**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   # ou, em sistemas Unix-like:
   # source .venv/bin/activate
   ```

3. **Instalar dependências**

   As dependências estão listadas em `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. **Executar o script principal**

   A partir da raiz do projeto:

   ```bash
   python mouse_recorder.py
   ```

2. **Controles por teclado**

   Após iniciar o script, use as seguintes teclas:

   - **G** → Iniciar/Parar **gravação** de eventos do mouse.
   - **P** → Iniciar/Parar **reprodução em loop** dos eventos gravados.
   - **Ctrl+C** → Encerrar o programa no terminal.

3. **Fluxo típico de uso**

   1. Execute `python mouse_recorder.py`.
   2. Pressione **G** para começar a gravar os movimentos, cliques e rolagens do mouse.
   3. Execute normalmente a sequência de ações que você deseja automatizar.
   4. Pressione novamente **G** para encerrar a gravação.
   5. Pressione **P** para iniciar a reprodução em **loop contínuo** da sequência gravada.
   6. Quando quiser parar a reprodução, pressione **P** novamente.
   7. Para encerrar o programa, use **Ctrl+C** no terminal.

   > **Importante**: é necessário ter gravado pelo menos uma sequência (com a tecla **G**) antes de tentar reproduzir com **P**.

## Limitações e considerações

- **Eventos em memória**: os eventos de mouse são armazenados apenas em memória, não sendo salvos em arquivo. Ao encerrar o programa, a gravação é perdida.
- **Loop contínuo**: a reprodução ocorre em loop até que a tecla **P** seja pressionada novamente.
- **Compatibilidade**: o comportamento pode variar entre sistemas operacionais, dependendo do suporte da biblioteca `pynput`.
- **Segurança**: evite usar o gravador para automatizar ações sensíveis, como operações bancárias, digitação de senhas ou acesso a dados confidenciais.

## Possíveis extensões futuras

Algumas ideias de melhorias que podem ser implementadas posteriormente:

- Salvar e carregar gravações a partir de arquivos.
- Definir um número fixo de repetições em vez de loop infinito.
- Permitir configuração de teclas de atalho personalizadas.
- Interface gráfica simples para iniciar/parar gravação e reprodução.

