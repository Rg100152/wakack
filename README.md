
<!-- ============================================================ -->
<!--  WAKACK v6.0 ULTRA — README                                    -->
<!--  Made by Raj                                                  -->
<!-- ============================================================ -->

<div align="center">

<!-- Hero Skull GIF (Tenor) -->
<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="WAKACK Skull" width="180" />

# ☠️ WAKACK v6.0 ULTRA

**Dark Skull Cyber Terminal & Suite**

*A fake hacking simulator for pranks, demos, and learning — 100% safe, 100% fake.*

[![Made with Python](https://img.shields.io/badge/Python-3.7%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Version](https://img.shields.io/badge/Version-6.0%20ULTRA-red?style=for-the-badge)](https://github.com/Rg100152/wakack)
[![Status](https://img.shields.io/badge/Status-Simulation%20Only-green?style=for-the-badge)](#-legal-disclaimer)

[🌐 Live Demo](https://rg100152.github.io/wakack/) •
[💻 CLI Version](#-cli-version) •
[⚡ Install](#-quick-install) •
[📖 Commands](#-commands) •
[⚠️ Disclaimer](#-legal-disclaimer)

</div>

---

<div align="center">

<!-- Glitch Skull (Blue) -->
<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="Blue Skull Glitch" width="120" />

</div>

## 🌑 What is WAKACK?

**WAKACK** is a **dark-web styled cyber terminal** available in two flavours:

| 🖥️ Platform | 📁 File | 🎯 Purpose |
|:-------------|:--------|:-----------|
| 🌐 **Web** | `index.html` | Blog + fake terminal UI in the browser |
| 💻 **CLI** | `wakack.py` | Python terminal framework with 20+ fake modules |

Both versions are **pure simulation**:
- ❌ No network calls
- ❌ No data access
- ❌ No real hacking
- ✅ Just cool visuals + fake outputs

Perfect for **pranks, demos, videos, or learning how security tools *look***.

---

## ⚡ Quick Install

### 🐧 Linux / 🍎 macOS / 📱 Termux

**One-liner install:**

```bash
bash <(curl -s https://raw.githubusercontent.com/Rg100152/wakack/main/install.sh)
```

**Or manually:**

```bash
git clone https://github.com/Rg100152/wakack.git
cd wakack
chmod +x install.sh
./install.sh
```

After install, just type:

```bash
wakack
```

### 🪟 Windows

**Option A — Auto installer:**

1. Download [`install.bat`](install.bat)
2. **Double-click** it
3. A **`WAKACK.bat`** shortcut appears on your Desktop — double-click to run

**Option B — Manual:**

```cmd
git clone https://github.com/Rg100152/wakack.git
cd wakack
python wakack.py
```

### 📦 Manual (no installer, no git)

1. Download [`wakack.py`](wakack.py) directly
2. Open a terminal in that folder
3. Run:

```bash
python3 wakack.py
```

### 🔧 Requirements

- **Python 3.7+** — [download here](https://www.python.org/downloads/)
  - Windows: ✅ tick **"Add Python to PATH"** during install
- **Git** *(optional — only for one-liner install)*
- **Terminal** with Unicode support *(optional — auto-falls back to ASCII)*

**No external pip packages required.** Pure standard library.

---

## 🌐 Web Version

<div align="center">

<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="Skull animation" width="80" />

</div>

The web version is a **single self-contained HTML file** — no server, no dependencies.

### Run it

1. Download [`index.html`](index.html)
2. **Double-click** — opens in any modern browser
3. Works **offline**

### Live Demo

👉 **[https://rg100152.github.io/wakack/](https://rg100152.github.io/wakack/)**

### Features

- ☠️ Animated skull hero with flame particles
- 📝 Blog post grid with tags & sidebar
- 🌧️ Matrix rain canvas background
- 💀 CRT scanline + flicker effect
- 🖥️ Fake terminal menu (18 modules)
- 🎨 Responsive — works on mobile

---

## 💻 CLI Version

<div align="center">

<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="Skull CLI" width="80" />

</div>

### Run

```bash
# After install
wakack

# Or directly
python3 wakack.py

# On Windows
python wakack.py
```

### Preview

```text
        ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
     ▄███████████████████████████████████▄
    ███████████████████████████████████████
   ██████████████▀▀▀▀▀▀▀▀▀▀▀▀██████████████
   ████████████▀             ▀█████████████
   ████████████    ▄▄     ▄▄    ████████████
   ████████████   ████   ████   ████████████
   █████████████▄▄▄███▄▄▄███▄▄▄█████████████
    ███████████████████████████████████████
     ▀████████████▄▄▄▄▄▄▄▄▄▄▄▄████████████▀
       ▀████████████████████████████████▀
          ▀▀████████████████████████▀▀

WAKACK v6.0 ULTRA // DARK SKULL CYBER SUITE
Safe simulation • Made by Raj • Type 'help' to begin

┌──────────────────────────────────────────────────────────────────────┐
│ wakack-shell v6.0 | IP: 192.168.1.104 | CPU: 12% | MEM: 410MB       │
└──────────────────────────────────────────────────────────────────────┘

wakack@dark-skull:~# help
```

### Status Bar

Live-updating bar at the top of every prompt:

```
wakack-shell v6.0 | IP: 192.168.1.104 | CPU: 12% | MEM: 410MB | UP: 42s
```

All values are **randomly generated** — nothing real is measured.

---

## 📖 Commands

Once inside the CLI, use these commands:

| Command | Description |
|:--------|:------------|
| `help` | Show all commands |
| `tools` | List exploit modules |
| `target` | Set target phone / IP / username |
| `scan` | Run recon / port scan |
| `map` | Show live network map |
| `exploit` | Run payload delivery |
| `payload` | Generate custom shell payload |
| `crack` | Run hash dictionary attack |
| `session` | Dump active sessions |
| `exfil` | Simulate data exfiltration |
| `cred` | Dump credentials |
| `keylog` | Simulate keylogger |
| `ransom` | Simulate ransomware |
| `ddos` | Simulate DDoS flood |
| `sqli` | Simulate SQL injection |
| `xss` | Simulate XSS payload |
| `phish` | Simulate phishing page |
| `logs` | Simulate log exfil |
| `persist` | Simulate backdoor persistence |
| `full` | Run **full chain** (all modules) |
| `report` | Save session report to `.txt` |
| `sysinfo` | Show system information |
| `whoami` | Show current identity |
| `knowledge` | Knowledge hub index |
| `prank` | **Reveal the prank** |
| `clear` | Clear terminal |
| `exit` | Exit WAKACK |

**Tip:** You can chain them. Try `target` → `map` → `full` → `prank` for the full experience.

---

## 🎨 Tech Stack

| Layer | Technology |
|:------|:-----------|
| CLI | Python 3 (standard library only) |
| Web | HTML5 + CSS3 + vanilla JavaScript |
| Effects | ANSI colors, Canvas 2D, CSS animations |
| Fonts | System monospace (`Courier New`) |

No frameworks. No CDNs. No external dependencies.

---

## 📂 Project Structure

```
wakack/
├── wakack.py          ← Main CLI tool
├── index.html         ← Web version (single file)
├── install.sh         ← Linux/macOS installer
├── install.bat        ← Windows installer
├── setup.py           ← Optional pip packaging
├── README.md          ← This file
├── LICENSE            ← MIT license
└── .gitignore
```

---

## 🖼️ Screenshots

<div align="center">

### Web Version
<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="Web preview" width="90" />

> *(Add your own screenshot: `screenshot-web.png` in the repo root)*

### CLI Version
<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="CLI preview" width="90" />

> *(Add your own screenshot: `screenshot-cli.png` in the repo root)*

</div>

**Want to add screenshots?**

1. Take a screenshot of the tool
2. Save it as `screenshot-web.png` / `screenshot-cli.png` in the repo root
3. Replace the `<img>` tags above with:

```html
<img src="screenshot-web.png" alt="Web preview" />
```

---

## ⚠️ Legal Disclaimer

<div align="center">

<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="Warning skull" width="70" />

</div>

> **WAKACK is a SIMULATOR for entertainment and education.**
>
> - It makes **zero network calls**
> - It does **not** access, modify, or steal any data
> - All "attacks" are **visual animations only**
> - Any attempt to modify this tool for real hacking is **illegal** under:
>   - 🇮🇳 **IT Act 2000** (India) — up to 3 years imprisonment + fine
>   - 🇺🇸 **CFAA** (USA)
>   - 🇬🇧 **Computer Misuse Act** (UK)
>   - and similar laws worldwide
>
> **The author is not responsible for any misuse.**

---

## 🤝 Contributing

Found a bug? Want to add a new fake module?

1. Fork the repo
2. Create a branch: `git checkout -b feature/my-module`
3. Commit: `git commit -m "Add new module"`
4. Push: `git push origin feature/my-module`
5. Open a Pull Request

All contributions must keep the **simulation-only** rule.

---

## 📜 License

**MIT License** — see [LICENSE](LICENSE) for full text.

You are free to:
- ✅ Use commercially
- ✅ Modify
- ✅ Distribute
- ✅ Private use

Just keep the copyright notice and disclaimer.

---

## ⭐ Credits

<div align="center">

**Made with ☠️ by [Raj](https://github.com/Rg100152)**

[![GitHub](https://img.shields.io/badge/GitHub-Rg100152-181717?style=for-the-badge&logo=github)](https://github.com/Rg100152)
[![Website](https://img.shields.io/badge/Live-rg100152.github.io%2Fwakack-00ff41?style=for-the-badge&logo=githubpages)](https://rg100152.github.io/wakack/)

*If you found this fun, give it a ⭐!*

</div>

---

<div align="center">

<img src="https://media.tenor.com/pPYo24y8Zc4AAAAM/skull-head.gif" alt="End skull" width="60" />

**"It's not hacking — it's theatre."**

</div>
```

---

