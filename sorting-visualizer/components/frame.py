import json
from pathlib import Path

import streamlit.components.v1 as components


def _compute_highlights(frames):
    highlights = []
    prev = None
    for arr in frames:
        if prev is None:
            highlights.append([])
        else:
            changed = [i for i, (a, b) in enumerate(zip(prev, arr)) if a != b]
            highlights.append(changed[:4])
        prev = arr
    return highlights


def draw_frames(initial, frames, fps=12):
    base_dir = Path(__file__).parent / "bar-component"
    html_tpl = (base_dir / "bar-component.html").read_text(encoding="utf-8")
    css = (base_dir / "bar-component.css").read_text()
    js = (base_dir / "bar-component.js").read_text()

    highlights = _compute_highlights(frames)

    payload = {
        "initial": initial,
        "frames": frames,
        "highlights": highlights,
        "fps": fps,
    }

    html = (
        html_tpl
        .replace("/*__CSS__*/", css)
        .replace("/*__JS__*/", js)
        .replace("__DATA__", json.dumps(payload))
    )

    components.html(html, height=660, scrolling=False)
