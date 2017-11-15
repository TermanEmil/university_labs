INSTALL_DIR=/usr/share/texlive/texmf-dist/tex/latex/

cd $INSTALL_DIR
sudo git clone "https://github.com/2pi/karnaugh-map.git"
cd $INSTALL_DIR/karnaugh-map

sudo latex *.ins
sudo rm -rf `find . -not -path . -not -name "*.sty" -not -name "." -not -name ".."`
sudo texhash