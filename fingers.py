import os
import shutil

def purge():
    print("\n--- DEEP HOUSE CLEANING: START ---")
    
    # Target 1: The Ollama Junk we found earlier
    # Target 2: The accidental 'fingers.py' folder
    # Target 3: The Steam Shader Cache (Temporary game data)
    targets = [
        "/home/deck/Documents/ollama_junk",
        "/home/deck/.continue/fingers.py",
        "/home/deck/.local/share/Steam/steamapps/shadercache"
    ]

    for path in targets:
        if os.path.exists(path):
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                else:
                    os.remove(path)
                print(f"REMOVED BLOAT: {path}")
            except Exception as e:
                print(f"SKIPPED {path}: {e}")
    
    print("\n--- PURGE COMPLETE ---")
    print("PROTECTED: All Music, Audios, Photos, and Google/Chrome data.")

if __name__ == "__main__":
    purge()