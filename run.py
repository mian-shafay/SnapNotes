"""
SnapNotes Launcher
Automatically patches the Streamlit default title and starts the app.
Usage: python run.py  (from the venv)
"""
import subprocess
import sys
import os
import re

APP_TITLE = "SnapNotes"

def patch_streamlit_title():
    """Patch Streamlit's index.html so the browser tab never flashes 'Streamlit'."""
    try:
        import streamlit
        index_path = os.path.join(os.path.dirname(streamlit.__file__), "static", "index.html")

        if not os.path.exists(index_path):
            print("[patch] Streamlit index.html not found, skipping patch.")
            return

        with open(index_path, "r", encoding="utf-8") as f:
            content = f.read()

        patched = content

        # 1. Patch the <title> tag
        patched = re.sub(r"<title>.*?</title>", f"<title>{APP_TITLE}</title>", patched)

        # 2. Inject MutationObserver to block JS from resetting title (if not already present)
        observer_marker = "// Prevent Streamlit JS from flashing"
        if observer_marker not in patched:
            observer_script = (
                f'      // Prevent Streamlit JS from flashing "Streamlit" in the tab title\n'
                f'      new MutationObserver(function(mutations) {{\n'
                f'        mutations.forEach(function(m) {{\n'
                f'          if (document.title === "Streamlit") {{\n'
                f'            document.title = "{APP_TITLE}";\n'
                f'          }}\n'
                f'        }});\n'
                f'      }}).observe(document.querySelector(\'title\'), {{ childList: true }});\n'
            )
            patched = patched.replace(
                "window.prerenderReady = false",
                "window.prerenderReady = false;\n" + observer_script,
            )

        if patched != content:
            with open(index_path, "w", encoding="utf-8") as f:
                f.write(patched)
            print(f"[patch] Browser tab title locked to '{APP_TITLE}'.")
        else:
            print(f"[patch] Already patched.")

    except Exception as e:
        print(f"[patch] Warning: Could not patch title: {e}")

if __name__ == "__main__":
    patch_streamlit_title()

    # Launch Streamlit using the same Python environment
    streamlit_path = os.path.join(os.path.dirname(sys.executable), "streamlit")
    subprocess.run([streamlit_path, "run", "SnapNotes.py"], cwd=os.path.dirname(os.path.abspath(__file__)))
