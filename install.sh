#!/usr/bin/env bash
# WAKACK v6.0 ULTRA — Installer (Linux / Mac / Termux)
# Made by Raj
set -e

G="\033[92m"; R="\033[91m"; Y="\033[93m"; C="\033[96m"; B="\033[1m"; X="\033[0m"

echo -e "${R}${B}"
cat << "EOF"
 ██╗    ██╗ █████╗ ██╗  ██╗ █████╗  ██████╗██╗  ██╗
 ██║    ██║██╔══██╗██║  ██║██╔══██╗██╔════╝██║ ██╔╝
 ██║ █╗ ██║███████║███████║███████║██║     █████╔╝
 ██║███╗██║██╔══██║██╔══██║██╔══██║██║     ██╔═██╗
 ╚███╔███╔╝██║  ██║██║  ██║██║  ██║╚██████╗██║  ██╗
  ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
EOF
echo -e "${X}"
echo -e "${C}${B}WAKACK v6.0 ULTRA — Installer${X}"
echo -e "${Y}Made by Raj${X}"
echo ""

# --- 1. Check Python ---
echo -e "${C}[1/4]${X} Checking Python..."
if command -v python3 >/dev/null 2>&1; then
    PY=python3
elif command -v python >/dev/null 2>&1; then
    PY=python
else
    echo -e "${R}[!] Python not found. Please install Python 3.7+ and retry.${X}"
    exit 1
fi
PY_VER=$($PY --version 2>&1 | awk '{print $2}')
echo -e "${G}[✓]${X} Found Python $PY_VER"

# --- 2. Check git ---
echo -e "${C}[2/4]${X} Checking git..."
if command -v git >/dev/null 2>&1; then
    echo -e "${G}[✓]${X} git available"
else
    echo -e "${Y}[!] git not found — you can still download the .py file manually.${X}"
fi

# --- 3. Clone or update ---
echo -e "${C}[3/4]${X} Fetching WAKACK..."
INSTALL_DIR="$HOME/wakack"
if [ -d "$INSTALL_DIR/.git" ]; then
    cd "$INSTALL_DIR"
    git pull --quiet
    echo -e "${G}[✓]${X} Updated existing install at $INSTALL_DIR"
else
    if command -v git >/dev/null 2>&1; then
        git clone --quiet https://github.com/rg100152/wakack.git "$INSTALL_DIR"
        echo -e "${G}[✓]${X} Cloned to $INSTALL_DIR"
    else
        echo -e "${R}[!] Please install git or download wakack.py manually.${X}"
        exit 1
    fi
fi
cd "$INSTALL_DIR"

# --- 4. Make launcher ---
echo -e "${C}[4/4]${X} Creating launcher..."
chmod +x wakack.py 2>/dev/null || true

# Try to add a global command
if [ -w /usr/local/bin ] 2>/dev/null; then
    ln -sf "$INSTALL_DIR/wakack.py" /usr/local/bin/wakack
    echo -e "${G}[✓]${X} Installed global command: ${B}wakack${X}"
else
    echo -e "${Y}[!] No permission for /usr/local/bin — using local alias.${X}"
    SHELL_RC="$HOME/.bashrc"
    [ -n "$ZSH_VERSION" ] && SHELL_RC="$HOME/.zshrc"
    if ! grep -q "alias wakack=" "$SHELL_RC" 2>/dev/null; then
        echo "alias wakack='python3 $INSTALL_DIR/wakack.py'" >> "$SHELL_RC"
        echo -e "${G}[✓]${X} Added alias to $SHELL_RC (run: source $SHELL_RC)"
    fi
fi

echo ""
echo -e "${G}${B}════════════════════════════════════════${X}"
echo -e "${G}${B}  ✓ Installation complete!${X}"
echo -e "${G}${B}════════════════════════════════════════${X}"
echo ""
echo -e "${C}Run it with:${X}"
echo -e "  ${B}wakack${X}        (if installed globally)"
echo -e "  ${B}python3 $INSTALL_DIR/wakack.py${X}"
echo ""
echo -e "${Y}⚠  Simulation only. Real hacking is illegal.${X}"
echo ""
