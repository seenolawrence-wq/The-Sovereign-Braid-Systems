import os
import time
import subprocess
from datetime import datetime

VAULT_LOG = os.path.expanduser("~/Desktop/SOVEREIGN_VAULT/Braid_Docs/night_log.md")

def log(msg):
    os.makedirs(os.path.dirname(VAULT_LOG), exist_ok=True)
    with open(VAULT_LOG, "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")

def check_and_process():
    # 1. Check Hardware Health
    temp = subprocess.check_output(['cat', '/sys/class/thermal/thermal_zone0/temp'], text=True).strip()
    joules = f"{int(temp)/1000}°C"
    
    # 2. Log the Pulse
    output = f"PULSE: System Stable at {joules}. Engine idling."
    print(output)
    log(output)

print("--- NIGHT SHIFT ACTIVE: ARCHITECT RESTING ---")
# Initial log to verify path
log("SYSTEM SECURED. ARCHITECT ENGAGED SLEEP MODE.")

while True:
    try:
        check_and_process()
        time.sleep(1800) # 30 Minute Cycles
    except KeyboardInterrupt:
        print("\n--- NIGHT SHIFT TERMINATED BY ARCHITECT ---")
        break
