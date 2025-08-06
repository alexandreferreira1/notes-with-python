#!/bin/bash
set -e

echo "Instalando oh-my-zsh..."
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

echo "Clonando plugins extras..."
ZSH_CUSTOM=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
git clone https://github.com/zsh-users/zsh-completions $ZSH_CUSTOM/plugins/zsh-completions

echo "Configurando plugins no .zshrc..."
sed -i '/^plugins=/c\plugins=(git zsh-autosuggestions zsh-syntax-highlighting zsh-completions)' ~/.zshrc

# Garante que os plugins fiquem ao final do .zshrc para evitar conflito
echo "" >> ~/.zshrc
echo "# Ativar zsh-completions manualmente (evita conflito com built-in)" >> ~/.zshrc
echo "fpath+=${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-completions/src" >> ~/.zshrc
echo "autoload -Uz compinit && compinit" >> ~/.zshrc

echo "Setup completo. Abra uma nova aba ou digite 'zsh' para ativar."
