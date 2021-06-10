cd
mkdir backups
mv .config/alacritty backups
mv .config/nvim backups
mv .config/starship.toml backups
mv .zshrc backups
mv .vimrc backups
mv .doom.d backups
mv .vim backups
git clone --branch=Main https://github.com/StudGaming/dotfiles
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
mkdir -p .config/alacritty
mkdir -p .config/nvim
mkdir .doom.d
mv dotfiles/.config/alacritty/alacritty.yml .config/alacritty
mv dotfiles/.config/nvim/init.vim .config/nvim
mv dotfiles/.config/starship.toml .config/
mv dotfiles/.zshrc ~
mv dotfiles/.vimrc ~
