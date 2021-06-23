#!/usr/bin/env bash

## Author  : Aditya Shakya
## Mail    : adi1090x@gmail.com
## Github  : @adi1090x
## Twitter : @adi1090x

# Available Styles
# >> Created and tested on : rofi 1.6.0-1
#
# style_1     style_2     style_3     style_4     style_5     style_6
# style_7     style_8     style_9     style_10    style_11    style_12

theme="theme"
dir="$HOME/.config/rofi/Launcher"

# dark
ALPHA="#00000000"
BG="#000000ff"
FG="#FFFFFFff"
SELECT="#101010ff"

# light
#ALPHA="#00000000"
#BG="#FFFFFFff"
#FG="#000000ff"
#SELECT="#f3f3f3ff"

# accent colors
COLORS=('#FDD835' '#4DD0E1')
ACCENT="${COLORS[$(( $RANDOM % 2 ))]}ff"

# overwrite colors file
cat > $dir/colors.rasi <<- EOF
	/* colors */
	* {
	  al:  $ALPHA;
	  bg:  $BG;
	  se:  $SELECT;
	  fg:  $FG;
	  ac:  $ACCENT;
	}
EOF

rofi -no-lazy-grab -show drun -modi drun -theme $dir/"$theme"
