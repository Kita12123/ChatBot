#source ~/.zshrc で実行
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)" # これを追記
eval "$(pyenv init -)"