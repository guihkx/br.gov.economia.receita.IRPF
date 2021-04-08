# IRPF 2021 via Flatpak 📦

Este repositório contém os arquivos metadados necessários para criar e rodar o programa de declaração de imposto de renda [IRPF 2021](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/download/pgd/dirpf) via [Flatpak](https://flatpak.org/).

Versões prontas estão disponíveis para download na página [*Releases*](https://github.com/guihkx/br.gov.economia.receita.IRPF/releases).

## Instalação

1. Navegue até a página [*Releases*](https://github.com/guihkx/br.gov.economia.receita.IRPF/releases)
2. Baixe a versão apropriada para seu computador (na dúvida, baixe a versão `x86_64`)
3. Supondo que você baixou o arquivo para a pasta `~/Downloads`, execute os seguintes comandos para instalar:

    ```bash
    cd ~/Downloads
    flatpak install IRPF_v2021-1.2-x86_64.flatpak
    ```

4. Digite sua senha e confirme a instalação
5. Pronto! Você irá encontrar o programa `IRPF 2021` na categoria `Internet`.

## O que não funciona?

* Alguns menus e botões que abrem o navegador web ao serem clicados, não funcionam. (Problema será resolvido quando [esta PR](https://github.com/flathub/org.freedesktop.Sdk.Extension.openjdk11/pull/16) for aceita)
* ... Algo mais? [Me avise aqui!](https://github.com/guihkx/br.gov.economia.receita.IRPF/issues/new)
