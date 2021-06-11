########### Installing Packages ###########
paru -S alacritty qtile vim nvim rofi zsh shell-color-scripts starship emacs


########### Taking Backups of Files if They Exist ###########
cd
mkdir backups
mv .config/alacritty backups
mv .config/qtile backups
mv .config/nvim backups
mv .config/rofi backups
mv .config/starship.toml backups
mv .doom.d backups
mv .vim backups
mv .vimrc backups
mv .zshrc backups


########### CLoning the Directory ###########
cd
git clone --branch=Beta https://github.com/StudGaming/dotfiles


########### Getting Vim Plugged for Both NeoVim and Vim ###########
#### Vim ####
curl -fLo ~/.vim/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
#### NeoVim ####
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'


########### Creating Directories ###########
cd
mkdir -p .config/alacritty
mkdir -p .config/qtile
mkdir -p .config/nvim
mkdir -p .config/rofi
mkdir -p .doom.d


########### Moving Files ###########
cd
mv dotfiles/.config/alacritty/alacritty.yml .config/alacritty
mv dotfiles/.config/qtile/* .config/qtile
mv dotfiles/.config/rofi/* .config/rofi
mv dotfiles/.config/nvim/init.vim .config/nvim
mv dotfiles/.config/starship.toml .config/
mv dotfiles/.zshrc .
mv dotfiles/.vimrc .


########### Removing the Cloned Directory ###########
cd
rm -rf dotfiles
