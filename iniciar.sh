#!/bin/bash

# Garante que estamos na pasta correta do Gotoh
cd "$(dirname "$0")"

# Exibe mensagem no terminal
echo "================================="
echo "   Inicializando o Gotoh...     "
echo "================================="

# Executa o painel principal
python3 app.py
