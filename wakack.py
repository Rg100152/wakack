#!/usr/bin/env python3
"""
WAKACK v5.0 — Prank Terminal Framework
------------------------------------------------
All outputs are SIMULATED. No network calls. No real target.
For entertainment / educational demonstration only.
"""

import os
import sys
import time
import random
import shutil
from datetime import datetime

# ---------------- ANSI COLORS ----------------
G   = "\033[92m"
DG  = "\033[32m"
R   = "\033[91m"
Y   = "\033[93m"
C   = "\033[96m"
M   = "\033[95m"
W   = "\033[97m"
B   = "\033[1m"
DIM = "\033[2m"
X   = "\033[0m"

# ---------------- GLOBALS ----------------
TARGET = {"value": "unknown", "set": False}
REPORT = []

# ---------------- HELPERS ----------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def term_w():
    return min(shutil.get_terminal_size((110, 30)).columns - 2, 104)

def ts():
    return datetime.now().strftime("%H:%M:%S")

def log(tag, msg, color=G, save=True):
    tc = {"INFO": C, "OK": G, "WARN": Y, "ERR": R, "DBG": M, "EXEC": W}.get(tag, G)
    line = f"[{ts()}] [{tag:<4}] {msg}"
    print(f"{DIM}[{ts()}]{X} {tc}{B}[{tag:<4}]{X} {color}{msg}{X}")
    if save:
        REPORT.append(line)

def progress(label, total=100, speed=0.006, color=G, width=28):
    for i in range(total + 1):
        f = int(width * i / total)
        bar = "█" * f + "░" * (width - f)
        sys.stdout.write(
            f"\r{DIM}[{ts()}]{X} {color}[>]{X} {label:<38} "
            f"{color}[{bar}] {i:3d}%{X}"
        )
        sys.stdout.flush()
        time.sleep(speed)
    print()

def hr(c="─", col=DG, w=None):
    print(col + c * (w or term_w()) + X)

def ttl(text, col=G, w=None):
    w = w or term_w()
    t = f" {text} "
    pad = max(0, w - len(t) - 2)
    print(col + B + "┌" + t + "─" * pad + "┐" + X)

def row(text, col=G, w=None):
    w = w or term_w()
    inner = w - 4
    print(G + "│ " + col + text[:inner].ljust(inner) + G + " │" + X)
    REPORT.append(text)

def end(w=None):
    print(G + "└" + "─" * ((w or term_w()) - 2) + "┘" + X)

def prompt_enter(msg="press ENTER to continue..."):
    input(DIM + f"\n  {msg}" + X)

# ---------------- FAKE DATA ----------------
def f_ip():
    return f"{random.randint(10,220)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,254)}"

def f_mac():
    return ":".join(f"{random.randint(0,255):02x}" for _ in range(6))

def f_hash(n=40):
    return "".join(random.choice("0123456789abcdef") for _ in range(n))

def f_port():
    return random.choice([21, 22, 23, 25, 53, 80, 110, 143, 443, 445,
                          993, 995, 1433, 1521, 3306, 3389, 5432, 5900,
                          6379, 8080, 8443, 27017])

def f_user():
    return random.choice(["admin", "root", "wa_service", "chatd", "msgrouter",
                          "syncd", "notifyd", "media_proc", "session_mgr"])

def f_proc():
    return random.choice(["wa_sync", "chatd", "msgrouter", "enclave_srv",
                          "session_mgr", "otp_verify", "key_exchange"])

def f_domain():
    return random.choice(["wa-edge-07.internal", "c2-node.darknet",
                          "msg-gw-12.wa.net", "sync-cluster.aws"])

# ---------------- BANNER (SKULL) ----------------
SKULL = r"""
⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣶⣶⣶⣶⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀
⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣿⡿⠟⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀
⠀⣾⣿⣿⣿⣿⡟⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
⢠⣿⣿⣿⣿⣿⣧⠀⠀⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
⢸⣿⣿⣿⣿⣿⣿⣦⠀⠀⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
⠘⣿⣿⣿⣿⣿⣿⣿⣷⣄⠀⠈⠻⢿⣿⠟⠉⠛⠿⣿⣿⣿⣿⣿⣿⠃
⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⡿⠀
⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣤⣤⣴⣾⣿⣿⣿⣿⡿⠁⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠀⠀⠀
⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠁⠀⠀⠀⠀
⠠⠛⠛⠛⠉⠁⠀⠈⠙⠛⠛⠿⠿⠿⠿⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀
"""

def banner():
    w = term_w()
    print(G + B + SKULL + X)
    print(R + B + "WAKACK v5.0 // WhatsApp Session Exploit Kit".center(w) + X)
    print(DIM + G + "[ Raj] paid.Persistent TCP / WebSocket,XMPP ( . contain  web link click https://rg100152.github.io/wakack/ .".center(w) + X)
    print()

# ---------------- MATRIX ----------------
def matrix_burst(seconds=0.8, w=None, h=6):
    w = w or term_w()
    chars = "01アイウエオカキクケコ#$%&@"
    et = time.time() + seconds
    while time.time() < et:
        for _ in range(h):
            print(G + "".join(random.choice(chars) if random.random() > 0.2 else " "
                              for _ in range(w)) + X)
        time.sleep(0.05)
        clear()

# ---------------- MODULES ----------------
def mod_target():
    clear(); banner()
    ttl("SET TARGET", C)
    print(G + "│ " + W + "Enter target phone number / username:".ljust(term_w() - 4) + G + " │" + X)
    end()
    t = input(Y + B + "\n  target > " + X).strip()
    if t:
        TARGET["value"] = t
        TARGET["set"] = True
        log("OK", f"target set: {t}")
    else:
        log("WARN", "no target entered")

def mod_recon():
    print()
    ttl("RECON  //  Port Scan", C)
    row(f"{'HOST':<16} {'PORT':<7} {'STATE':<10} {'SERVICE':<14} {'BANNER'}", W)
    hr("┄", DG, term_w() - 2)
    progress("Scanning target range", 100, 0.005, G)
    for _ in range(8):
        st = random.choice(["OPEN", "OPEN", "FILTERED", "CLOSED"])
        col = G if st == "OPEN" else (Y if st == "FILTERED" else R)
        row(f"{f_ip():<16} {f_port():<7} {st:<10} {f_proc():<14} v{random.randint(1,9)}.{random.randint(0,9)}", col)
        time.sleep(0.18)
    end()
    log("OK", "recon complete (simulated)")

def mod_exploit():
    print()
    ttl("EXPLOIT  //  Payload Delivery (Simulated)", Y)
    log("EXEC", "generating shellcode buffer (fake)")
    progress("Encoding payload", 100, 0.006, Y)
    progress("Sending crafted packet", 100, 0.006, Y)
    progress("Triggering buffer overflow", 100, 0.006, R)
    time.sleep(0.2)
    log("ERR", "retry with ROP chain... (nothing happened)", R)
    log("OK", "shell returned: wa-edge-07$ (simulated)", G)
    end()
    log("OK", "exploit chain finished (simulated)")

def mod_hash():
    print()
    ttl("CRACKER  //  Dictionary Attack (Simulated)", Y)
    row(f"{'HASH':<26} {'ALGO':<6} {'PROGRESS':<10} {'STATUS'}", W)
    hr("┄", DG, term_w() - 2)
    for _ in range(6):
        p = random.randint(20, 99)
        st = "CRACKED" if p >= 90 else "RUNNING"
        col = G if st == "CRACKED" else Y
        row(f"{f_hash(24):<26} {'SHA1':<6} {str(p)+'%':<10} {st}", col)
        time.sleep(0.2)
    end()
    log("OK", "hash cracking finished (simulated)")

def mod_session():
    print()
    ttl("SESSION HIJACK  //  Active Sessions (Fake)", M)
    row(f"{'USER':<14} {'IP':<16} {'MAC':<18} {'TTL':<6} {'STATE'}", W)
    hr("┄", DG, term_w() - 2)
    for _ in range(6):
        row(f"{f_user():<14} {f_ip():<16} {f_mac():<18} {random.randint(60,3600):<6} ESTABLISHED", C)
        time.sleep(0.18)
    end()
    log("OK", "session dump complete (simulated)")

def mod_exfil():
    print()
    ttl("EXFIL  //  Data Transfer (0 bytes actually sent)", R)
    progress("Compressing chat metadata", 100, 0.006, M)
    progress("Encrypting archive (AES-256)", 100, 0.006, M)
    progress("Uploading to c2-node", 100, 0.006, R)
    time.sleep(0.25)
    log("WARN", "0 bytes transferred — nothing left the machine", Y)
    end()

def mod_cred():
    print()
    ttl("CREDENTIALS  //  Dump (Fake)", R)
    row(f"{'USER':<14} {'PASSWORD':<20} {'HASH':<16}", W)
    hr("┄", DG, term_w() - 2)
    for _ in range(6):
        row(f"{f_user():<14} {'prank_'+f_hash(6):<20} {f_hash(14)}", R)
        time.sleep(0.18)
    end()
    log("OK", "credential dump finished (simulated)")

def mod_keylogger():
    print()
    ttl("KEYLOGGER  //  Keystroke Capture (Simulated)", M)
    keys = "asdfghjklqwertyuiop1234567890"
    progress("Installing hook", 100, 0.008, M)
    for i in range(6):
        captured = "".join(random.choice(keys) for _ in range(random.randint(8, 16)))
        row(f"session_{i+1}  captured: {captured}", M)
        time.sleep(0.25)
    end()
    log("WARN", "no keys were actually logged", Y)

def mod_ransom():
    print()
    ttl("RANSOMWARE  //  Encryption (Simulated)", R)
    progress("Enumerating files", 100, 0.006, Y)
    progress("Encrypting files (AES-256)", 100, 0.006, R)
    progress("Dropping ransom note", 100, 0.006, R)
    time.sleep(0.2)
    log("WARN", "0 files touched — simulation only", Y)
    end()

def mod_ddos():
    print()
    ttl("DDOS  //  Botnet Flood (Simulated)", R)
    progress("Loading botnet list", 100, 0.006, Y)
    progress("Sending SYN flood", 100, 0.006, R)
    time.sleep(0.2)
    for _ in range(5):
        row(f"bot {f_ip():<16} -> target  pkts/s={random.randint(1000,9999)}", R)
        time.sleep(0.15)
    end()
    log("WARN", "0 packets sent — simulation only", Y)

def mod_sqli():
    print()
    ttl("SQL INJECTION  //  Database Dump (Simulated)", Y)
    payloads = ["' OR '1'='1", "'; DROP TABLE users;--", "' UNION SELECT * FROM sessions--"]
    for p in payloads:
        row(f"payload: {p}", Y)
        time.sleep(0.2)
    progress("Injecting payload", 100, 0.006, Y)
    row(f"table: users   rows: {random.randint(100,9999)}  status: DUMPED", G)
    row(f"table: sessions rows: {random.randint(100,9999)}  status: DUMPED", G)
    end()
    log("WARN", "0 rows actually fetched", Y)

def mod_xss():
    print()
    ttl("XSS  //  Payload Injection (Simulated)", Y)
    payload = "<script>alert('prank')</script>"
    row(f"injecting: {payload}", Y)
    progress("Reflecting payload", 100, 0.006, Y)
    row("cookie stealer loaded (fake)  ->  " + f_hash(16), R)
    end()
    log("WARN", "no cookies were stolen", Y)

def mod_phish():
    print()
    ttl("PHISHING  //  Page Generator (Simulated)", M)
    progress("Cloning login page", 100, 0.006, M)
    progress("Deploying to " + f_domain(), 100, 0.006, M)
    row(f"phish URL: https://{f_domain()}/login", C)
    row("0 credentials captured (simulation only)", Y)
    end()
    log("WARN", "page was not actually deployed", Y)

def mod_logs():
    print()
    ttl("LOG EXFIL  //  Chat Metadata (Simulated)", C)
    row(f"{'TIMESTAMP':<20} {'FROM':<16} {'TYPE':<10} {'SIZE'}", W)
    hr("┄", DG, term_w() - 2)
    for _ in range(6):
        row(f"{datetime.now().strftime('%Y-%m-%d %H:%M'):<20} {f_user():<16} {'text':<10} {random.randint(10,999)}B", C)
        time.sleep(0.18)
    end()
    log("WARN", "0 bytes actually exfiltrated", Y)

def mod_persist():
    print()
    ttl("PERSISTENCE  //  Backdoor Install (Simulated)", M)
    progress("Creating startup entry", 100, 0.006, M)
    progress("Registering service", 100, 0.006, M)
    progress("Setting cron job", 100, 0.006, M)
    time.sleep(0.2)
    row(f"backdoor: /tmp/.wa_{f_hash(6)} (fake)", R)
    end()
    log("WARN", "nothing was written to disk", Y)

def mod_full():
    for fn in (mod_recon, mod_exploit, mod_hash, mod_session,
               mod_exfil, mod_cred, mod_keylogger, mod_ransom,
               mod_ddos, mod_sqli, mod_xss, mod_phish,
               mod_logs, mod_persist):
        fn()
        time.sleep(0.25)
    log("OK", "full chain finished (simulated)")

def mod_report():
    print()
    ttl("REPORT  //  Save Session Log", G)
    fname = f"wakack_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(fname, "w", encoding="utf-8") as f:
            f.write("WAKACK v5.0 — Prank Report\n")
            f.write("=" * 60 + "\n")
            f.write(f"Target: {TARGET['value']}\n")
            f.write(f"Generated: {datetime.now()}\n")
            f.write("=" * 60 + "\n\n")
            for line in REPORT:
                f.write(line + "\n")
        log("OK", f"report saved: {fname}")
    except Exception as e:
        log("ERR", f"could not save report: {e}")
    end()

def mod_prank():
    clear()
    tw = r"""
 ██╗   ██╗ ██████╗ ██╗   ██╗    ██████╗  █████╗ ███╗   ███╗███████╗
 ╚██╗ ██╔╝██╔═══██╗██║   ██║   ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
  ╚████╔╝ ██║   ██║██║   ██║   ██║  ███╗███████║██╔████╔██║█████╗
   ╚██╔╝  ██║   ██║██║   ██║   ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
    ██║   ╚██████╔╝╚██████╔╝   ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
    ╚═╝    ╚═════╝  ╚═════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                        YOU GOT PRANKED
"""
    print(G + B + tw + X)
    print(Y + "\nThis was a prank. Nothing was hacked. No data was touched." + X)
    print(C + f"Target: {TARGET['value']}" + X)
    print(C + "Screenshot lo aur doston ko bhejo.\n" + X)

# ---------------- MENU ----------------
MENU = [
    ("1",  "Set target (phone / username)",       mod_target),
    ("2",  "Reconnaissance — Port Scan",          mod_recon),
    ("3",  "Exploitation — Payload Delivery",     mod_exploit),
    ("4",  "Cracker — Hash Dictionary",           mod_hash),
    ("5",  "Hijack — Session Dump",               mod_session),
    ("6",  "Exfiltration — Data Transfer",        mod_exfil),
    ("7",  "Credentials — Dump (fake)",           mod_cred),
    ("8",  "Keylogger — Keystroke Capture",       mod_keylogger),
    ("9",  "Ransomware — Encryption",             mod_ransom),
    ("10", "DDoS — Botnet Flood",                 mod_ddos),
    ("11", "SQL Injection — DB Dump",             mod_sqli),
    ("12", "XSS — Payload Injection",             mod_xss),
    ("13", "Phishing — Page Generator",           mod_phish),
    ("14", "Log Exfil — Chat Metadata",           mod_logs),
    ("15", "Persistence — Backdoor Install",      mod_persist),
    ("16", "FULL CHAIN — Run all modules",        mod_full),
    ("17", "Save report to file",                 mod_report),
    ("18", "REVEAL — Prank reveal",               mod_prank),
    ("0",  "Exit",                                None),
]

def menu():
    w = term_w()
    print()
    print(C + B + "┌─ MAIN MENU " + "─" * (w - 14) + "┐" + X)
    print(G + "│ " + W + f"target: {TARGET['value']}".ljust(w - 4) + G + " │" + X)
    print(C + "├" + "─" * (w - 2) + "┤" + X)
    for key, label, _ in MENU:
        col = R if key == "0" else (G if key == "18" else W)
        print(G + "│ " + col + B + f"[{key:>2}]" + X + " " + W + label.ljust(w - 9) + G + "│" + X)
    print(C + B + "└" + "─" * (w - 2) + "┘" + X)
    print()

# ---------------- MAIN ----------------
def main():
    clear(); banner(); time.sleep(0.8)
    log("INFO", "Initializing WAKACK framework...", C); time.sleep(0.3)
    for m in ["network_scanner", "crypto_breaker", "session_hijack",
              "wa_protocol", "payload_gen", "log_exfil", "phish_gen"]:
        log("OK", f"{m:<18} loaded"); time.sleep(0.1)
    matrix_burst(0.8, term_w(), 6)

    while True:
        menu()
        try:
            ch = input(Y + B + "  wakack > " + X).strip()
        except (EOFError, KeyboardInterrupt):
            break
        if ch == "0":
            print(R + "\n[!] Exiting. Stay ethical.\n" + X)
            break
        found = False
        for key, _, fn in MENU:
            if ch == key and fn:
                fn(); found = True
                prompt_enter()
                break
        if not found:
            print(R + "[!] Invalid option." + X)
            time.sleep(0.8)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + R + "Interrupted." + X)
