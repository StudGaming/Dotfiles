########### Taking Backups of Files if They Exist ###########
cd
mkdir backups
mv -rf .config/alacritty backups
mv -rf .config/qtile backups
mv -rf .config/nvim backups
mv -rf .config/rofi backups
mv -rf .config/starship.toml backups
mv -rf .doom.d/ backups
mv -rf .vim/ backups
mv -rf .vimrc backups
mv -rf .zshrc backups
mv -rf .icons/ backups
mv -rf .themes/ backups


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
mkdir -p .config/alacritty/
mkdir -p .config/qtile/
mkdir -p .config/nvim/
mkdir -p .config/rofi/
mkdir -p .doom.d/
mkdir -p .icons/
mkdir -p .themes/


########### Moving Files ###########
cd
mv dotfiles/.config/alacritty/alacritty.yml .config/alacritty/
mv dotfiles/.config/qtile/* .config/qtile/
mv dotfiles/.config/rofi/* .config/rofi/
mv dotfiles/.config/nvim/init.vim .config/nvim/
mv dotfiles/.config/starship.toml .config/
mv dotfiles/.doom.d/* .doom.d/
mv dotfiles/.icons/* .icons/
mv dotfiles/.themes/* .themes/
mv dotfiles/.vimrc .
mv dotfiles/.zshrc .


########### Removing the Cloned Directory ###########
cd
rm -rf dotfiles
