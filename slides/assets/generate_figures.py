#!/usr/bin/env python3
"""Generate lecture figures from briefing facts.

Every numeric claim is labeled with its source in the figure itself.
Do not put “cartoon / not to scale / not a measured model” hedges on the canvas.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
import numpy as np

OUT = Path(__file__).parent / "figures"
OUT.mkdir(exist_ok=True)

GOLD = "#FFB71B"
ORANGE = "#FF4D00"
PURPLE = "#691F74"
PURPLE_WEB = "#5F277E"
TEAL = "#00C4B3"
BLUE = "#003DA6"
INK = "#281241"
PAPER = "#FAF9F7"
MUTED = "#586F78"
WHITE = "#FFFFFF"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "figure.facecolor": PAPER,
        "axes.facecolor": PAPER,
        "axes.edgecolor": INK,
        "text.color": INK,
        "axes.labelcolor": INK,
        "xtick.color": INK,
        "ytick.color": INK,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "figure.dpi": 160,
    }
)


def save(fig, name, tight=True):
    kw = dict(facecolor=PAPER, pad_inches=0.15)
    if tight:
        kw["bbox_inches"] = "tight"
    fig.savefig(OUT / f"{name}.png", **kw)
    fig.savefig(OUT / f"{name}.svg", **kw)
    plt.close(fig)


def rounded(ax, x, y, w, h, fc, ec=None, r=0.04, lw=1.5, z=1):
    p = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle=f"round,pad=0.01,rounding_size={r}",
        facecolor=fc,
        edgecolor=ec or fc,
        linewidth=lw,
        zorder=z,
        mutation_aspect=0.6,
    )
    ax.add_patch(p)
    return p


# --- 1. Hour map ---
def fig_hour_map():
    fig, ax = plt.subplots(figsize=(14.2, 4.55))
    ax.set_xlim(0, 60)
    ax.set_ylim(-0.08, 3.35)
    ax.axis("off")
    blocks = [
        (0, 10, BLUE, "Why tonight\n10 min", 12),
        (10, 8, TEAL, "How AI\nanswers\n8 min", 9),
        (18, 8, PURPLE, "Files &\nchecks\n8 min", 9),
        (26, 8, ORANGE, "Evidence\n8 min", 11),
        (34, 18, PURPLE_WEB, "Live blocks\n18 min", 12),
        (52, 8, GOLD, "Takeaways\n8 min", 11),
    ]
    for x, w, c, lab, fs in blocks:
        rounded(ax, x + 0.3, 1.18, w - 0.6, 1.48, c, r=0.15)
        color = INK if c == GOLD else WHITE
        ax.text(x + w / 2, 1.92, lab, ha="center", va="center", color=color, fontsize=fs, fontweight="bold", linespacing=1.15)
    ax.plot([0, 60], [0.95, 0.95], color=INK, lw=2)
    for t in range(0, 61, 10):
        ax.plot([t, t], [0.82, 0.95], color=INK, lw=1.5)
        ax.text(t, 0.52, f"{t}m", ha="center", fontsize=11, color=MUTED)
    ax.text(
        30,
        0.12,
        "Take-home Labs 5–8 are not on this clock.",
        ha="center",
        fontsize=12,
        color=INK,
        fontstyle="italic",
    )
    save(fig, "hour_map")


# --- 2. Three meanings of AI ---
def fig_three_ais():
    fig, ax = plt.subplots(figsize=(14.2, 6.6))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.6)
    ax.axis("off")
    cards = [
        (0.4, BLUE, "Rules & scores", "If-then · scores · order sets", "PEWS\nfebrile-infant pathway"),
        (5.0, PURPLE, "Classical ML", "Labels in → class / risk out", "Sepsis alert\nchest X-ray read"),
        (9.6, TEAL, "Foundation models", "Next-token output", "Parent letter\nAI scribe"),
    ]
    for x, c, title, mid, bot in cards:
        rounded(ax, x, 0.4, 4.2, 4.9, WHITE, ec=c, r=0.12, lw=3)
        ax.add_patch(Circle((x + 2.1, 4.38), 0.42, facecolor=c, zorder=3))
        ax.text(x + 2.1, 3.52, title, ha="center", fontsize=18, fontweight="bold", color=c)
        ax.text(x + 2.1, 2.52, mid, ha="center", fontsize=13, color=INK)
        ax.text(x + 2.1, 1.32, bot, ha="center", fontsize=13, color=MUTED)
    ax.text(
        7.1,
        5.95,
        "A score, an alert, and a chatbot are all called AI. Those are three different jobs.",
        ha="center",
        fontsize=14,
        color=INK,
    )
    save(fig, "three_ais")


# --- 3. Learning modes ---
def fig_learning_modes():
    fig, axes = plt.subplots(1, 3, figsize=(14.2, 5.6))
    rng = np.random.default_rng(7)
    x_a = rng.normal(1, 0.35, 40)
    y_a = rng.normal(1, 0.35, 40)
    x_b = rng.normal(3, 0.35, 40)
    y_b = rng.normal(3, 0.35, 40)

    for ax in axes:
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal", adjustable="box")

    ax = axes[0]
    ax.scatter(x_a, y_a, c=BLUE, s=36)
    ax.scatter(x_b, y_b, c=ORANGE, s=36)
    ax.set_title("Supervised", color=BLUE, fontweight="bold")

    ax = axes[1]
    ax.scatter(x_a, y_a, c=TEAL, s=36)
    ax.scatter(x_b, y_b, c=TEAL, s=36)
    ax.set_title("Unsupervised", color=PURPLE, fontweight="bold")

    ax = axes[2]
    ax.set_title("Reinforcement", color=ORANGE, fontweight="bold")
    # A roundabout, not a scatter and not a single arrow: try, get scored, nudge, repeat.
    cx, cy, rr = 2.00, 2.12, 1.22
    ring = Circle((cx, cy), rr, fill=False, edgecolor=INK, lw=2.4, alpha=0.18, zorder=1)
    ax.add_patch(ring)
    nodes = [
        (cx, cy + rr, "try", ORANGE, WHITE),
        (cx + rr * 0.92, cy - rr * 0.48, "score", GOLD, INK),
        (cx - rr * 0.92, cy - rr * 0.48, "nudge", PURPLE, WHITE),
    ]
    for x, y, lab, fc, tc in nodes:
        ax.add_patch(Circle((x, y), 0.46, facecolor=fc, edgecolor=WHITE, lw=2.2, zorder=3))
        ax.text(x, y, lab, ha="center", va="center", color=tc, fontsize=10, fontweight="bold", zorder=4)
    ax.annotate(
        "",
        xy=(nodes[1][0] - 0.12, nodes[1][1] + 0.38),
        xytext=(nodes[0][0] + 0.34, nodes[0][1] - 0.18),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.7, mutation_scale=12),
    )
    ax.annotate(
        "",
        xy=(nodes[2][0] + 0.38, nodes[2][1] - 0.08),
        xytext=(nodes[1][0] - 0.38, nodes[1][1] - 0.08),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.7, mutation_scale=12),
    )
    ax.annotate(
        "",
        xy=(nodes[0][0] - 0.34, nodes[0][1] - 0.18),
        xytext=(nodes[2][0] + 0.12, nodes[2][1] + 0.38),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=1.7, mutation_scale=12),
    )
    ax.text(cx, 0.28, "a human + / −, or a unit test", ha="center", fontsize=9, color=MUTED)

    captions = ["structure with group labels", "structure, no labels", "try → score → nudge → try"]
    for ax, lab in zip(axes, captions):
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        ax.set_xlabel(lab, fontsize=11, color=MUTED, labelpad=12)

    fig.align_xlabels(axes)
    save(fig, "learning_modes")


# --- 4. Pediatric shift ---
def fig_pediatric_shift():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    cards = [
        (0.5, BLUE, "Trained here", ["Adult notes", "Adult creatinine", "Adult vital-sign ranges"]),
        (8.3, ORANGE, "Deployed here", ["Weight-based dosing", "Caregiver by proxy", "Rare disease + development"]),
    ]
    title_y = 4.45
    line_ys = [3.55, 2.95, 2.35]
    for x, c, title, lines in cards:
        rounded(ax, x, 1.3, 5.2, 3.8, WHITE, c, lw=3)
        cx = x + 2.6
        ax.text(cx, title_y, title, ha="center", va="center", fontsize=16, fontweight="bold", color=c)
        for y, line in zip(line_ys, lines):
            ax.text(cx, y, line, ha="center", va="center", fontsize=14, color=INK)
    ax.annotate("", xy=(8.15, 3.2), xytext=(5.85, 3.2), arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=3))
    ax.text(7.0, 3.55, "shift", ha="center", va="center", color=PURPLE, fontsize=12, fontweight="bold")
    ax.text(7.0, 5.7, "The training data are mostly adults.", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(7.0, 0.45, "Pediatric Academic Societies 2025: 6% confident AI is developed with adequate pediatric consideration", ha="center", va="center", fontsize=11, color=MUTED)
    save(fig, "pediatric_shift")


# --- 5. Tokens ---
def fig_tokens():
    fig, ax = plt.subplots(figsize=(14.2, 5.0))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")
    sentence = "fever 38.5 °C"
    ax.text(7, 3.55, sentence, ha="center", fontsize=28, fontweight="bold", color=INK, family="DejaVu Sans")
    pieces = [("fev", BLUE), ("er", TEAL), ("38", PURPLE), (".5", ORANGE), ("°C", GOLD)]
    gap = 0.35
    widths = [1.15 + 0.22 * max(len(t) - 2, 0) for t, _ in pieces]
    total = sum(widths) + gap * (len(pieces) - 1)
    x = (14 - total) / 2
    for (t, c), w in zip(pieces, widths):
        rounded(ax, x, 1.35, w, 1.15, c, r=0.08)
        ax.text(x + w / 2, 1.92, t, ha="center", va="center", fontsize=16, fontweight="bold", color=INK if c == GOLD else WHITE)
        x += w + gap
    ax.text(7, 0.55, "Byte-pair pieces · numbers often split · a dose is not one object to the model", ha="center", fontsize=12, color=MUTED)
    save(fig, "tokens")


# --- 5b. Next-token transformer cartoon ---
def fig_next_token():
    fig, ax = plt.subplots(figsize=(14.2, 6.5))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.5)
    ax.axis("off")
    ax.text(
        7.1,
        5.85,
        "A transformer mixes the tokens, picks the next one, adds it, and does it again.",
        ha="center",
        fontsize=14,
        color=INK,
    )

    words = ["The", "infant", "wheezed", "after"]
    xs = np.linspace(2.15, 12.05, len(words))
    y_tok = 4.78
    for x, w in zip(xs, words):
        rounded(ax, x - 1.05, y_tok - 0.42, 2.1, 0.84, BLUE, r=0.08)
        ax.text(x, y_tok, w, ha="center", va="center", color=WHITE, fontsize=14, fontweight="bold")
    ax.text(7.1, 5.32, "tokens in", ha="center", fontsize=11, color=MUTED)

    ax.annotate(
        "",
        xy=(7.1, 3.92),
        xytext=(7.1, 4.28),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=2, mutation_scale=12),
    )

    rounded(ax, 0.85, 2.48, 5.9, 1.38, WHITE, TEAL, lw=3, r=0.1)
    ax.text(3.8, 3.42, "1. Attention mixes them", ha="center", fontsize=15, fontweight="bold", color=TEAL)
    ax.text(3.8, 2.88, "Every token can look at every other token.", ha="center", fontsize=12, color=INK)

    rounded(ax, 7.45, 2.48, 5.9, 1.38, WHITE, PURPLE, lw=3, r=0.1)
    ax.text(10.4, 3.42, "2. Each token is updated", ha="center", fontsize=15, fontweight="bold", color=PURPLE)
    ax.text(10.4, 2.88, "That stack, many times, is a transformer.", ha="center", fontsize=12, color=INK)

    ax.annotate(
        "",
        xy=(7.45, 3.17),
        xytext=(6.75, 3.17),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=2, mutation_scale=12),
    )

    ax.annotate(
        "",
        xy=(7.1, 1.82),
        xytext=(7.1, 2.38),
        arrowprops=dict(arrowstyle="-|>", color=INK, lw=2, mutation_scale=12),
    )

    rounded(ax, 3.85, 0.92, 6.5, 0.82, ORANGE, r=0.08)
    ax.text(7.1, 1.33, "next guess:  feeds", ha="center", va="center", color=WHITE, fontsize=16, fontweight="bold")
    ax.text(
        7.1,
        0.38,
        "Add it to the sentence. Repeat.",
        ha="center",
        fontsize=12,
        color=MUTED,
    )
    save(fig, "next_token")


# --- 6. Attention schematic ---
def fig_attention():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    words = ["The", "infant", "wheezed", "after", "feeds"]
    xs = np.linspace(1.6, 12.4, len(words))
    y_sent = 2.05
    y_query = 4.55
    focus = 2
    qx = xs[focus]

    ax.text(qx, 5.45, "this token", ha="center", fontsize=13, fontweight="bold", color=ORANGE)
    rounded(ax, qx - 1.2, y_query - 0.5, 2.4, 1.05, ORANGE, r=0.08)
    ax.text(qx, y_query, "wheezed", ha="center", va="center", color=WHITE, fontsize=16, fontweight="bold")

    ax.text(0.35, 3.35, "looks\nat", ha="center", va="center", fontsize=12, color=TEAL, fontweight="bold")
    for x, w, i in zip(xs, words, range(len(words))):
        c = ORANGE if i == focus else BLUE
        rounded(ax, x - 1.05, y_sent - 0.5, 2.1, 1.0, c, r=0.08)
        ax.text(x, y_sent, w, ha="center", va="center", color=WHITE, fontsize=14, fontweight="bold")
        ax.annotate(
            "",
            xy=(x, y_sent + 0.55),
            xytext=(qx, y_query - 0.55),
            arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2, mutation_scale=11),
        )

    ax.text(7, 1.15, "the rest of the sentence", ha="center", fontsize=13, color=MUTED)
    ax.text(7, 0.45, "A weight later says how much each word counts.", ha="center", fontsize=13, color=INK)
    save(fig, "attention")


# --- 7. Timeline ---
def fig_timeline():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.96, bottom=0.04)
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 5.8)
    ax.axis("off")
    ax.text(
        7.1,
        0.52,
        "Llama 2 is why a laptop path exists. DeepSeek-R1 showed reasoning-style RL was not OpenAI-only.",
        ha="center",
        va="center",
        fontsize=10,
        color=MUTED,
    )
    y_line = 2.82
    ax.plot([0.35, 13.85], [y_line, y_line], color=BLUE, lw=4, solid_capstyle="round")
    events = [
        ("2019", "GPT-2", True),
        ("2020", "GPT-3  175B", False),
        ("Jan 2022", "InstructGPT", True),
        ("Nov 2022", "ChatGPT", False),
        ("Mar 2023", "GPT-4", True),
        ("Jul 2023", "Llama 2", False),
        ("Sep 2024", "o1", True),
        ("Jan 2025", "DeepSeek-R1", False),
        ("2026", "GPT-5.6 · Opus 5", True),
    ]
    xs = np.linspace(0.85, 13.35, len(events))
    date_off, name_off, gloss_off = 0.28, 0.46, 0.64
    for x, (when, name, above) in zip(xs, events):
        sign = 1 if above else -1
        ax.plot([x, x], [y_line, y_line + sign * 0.14], color=PURPLE, lw=2)
        ax.scatter([x], [y_line], s=92, color=GOLD, zorder=5, edgecolor=PURPLE, linewidths=1.2)
        ax.text(
            x,
            y_line + sign * date_off,
            when,
            ha="center",
            va="center",
            fontsize=9.5,
            color=MUTED,
        )
        ax.text(
            x,
            y_line + sign * name_off,
            name,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=INK,
        )
        extra = {
            "ChatGPT": ("The public era starts here", ORANGE),
            "Llama 2": ("open weights", MUTED),
            "o1": ("test-time compute", MUTED),
            "GPT-5.6 · Opus 5": ("Fable · Kimi K3", MUTED),
        }.get(name)
        if extra:
            lab, col = extra
            ax.text(
                x,
                y_line + sign * gloss_off,
                lab,
                ha="center",
                va="center",
                fontsize=10,
                fontweight="bold" if col == ORANGE else "normal",
                color=col,
            )
    save(fig, "timeline", tight=False)


# --- 8. Three access boxes ---
def fig_three_boxes():
    fig, ax = plt.subplots(figsize=(14.2, 6.8))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.8)
    ax.axis("off")
    cards = [
        (
            0.35,
            ORANGE,
            "Consumer cloud",
            "ChatGPT · Claude · Gemini",
            [
                "Phone or laptop browser.",
                "No hospital privacy contract.",
                "The prompt leaves the building.",
            ],
        ),
        (
            4.95,
            PURPLE,
            "Hospital-governed cloud",
            "EHR tool with a contract",
            [
                "The official cloud path.",
                "A business associate agreement",
                "is what makes it the hospital’s.",
            ],
        ),
        (
            9.55,
            TEAL,
            "Local laptop",
            "Ollama on this machine",
            [
                "The vendor never sees the prompt.",
                "You already use this laptop",
                "for the EHR. That is reasonable.",
            ],
        ),
    ]
    note_ys = [2.35, 1.85, 1.35]
    for x, c, title, kicker, notes in cards:
        rounded(ax, x, 0.55, 4.3, 5.45, WHITE, c, lw=3.5, r=0.1)
        cx = x + 2.15
        ax.text(cx, 5.35, title, ha="center", va="center", fontsize=16, fontweight="bold", color=c)
        ax.text(cx, 4.45, kicker, ha="center", va="center", fontsize=13, color=INK)
        for y, line in zip(note_ys, notes):
            ax.text(cx, y, line, ha="center", va="center", fontsize=13, color=MUTED)
    ax.text(
        7.1,
        0.22,
        "A business associate agreement is what separates the first box from the second.",
        ha="center",
        fontsize=12,
        color=MUTED,
    )
    save(fig, "three_boxes")


# --- 9. RAG ---
def fig_rag():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.0)
    ax.axis("off")
    cards = [
        (0.4, BLUE, "Corpus", ["journals", "guidelines", "PDFs you uploaded"]),
        (5.3, PURPLE, "Retrieve", ["nearest chunks", "not the whole library", ""]),
        (10.2, TEAL, "Generate", ["answer + citations", "that still must", "be opened"]),
    ]
    title_y = 3.55
    line_ys = [2.90, 2.50, 2.10]
    for x, c, title, lines in cards:
        rounded(ax, x, 1.75, 3.4, 2.7, c)
        cx = x + 1.7
        ax.text(cx, title_y, title, ha="center", va="center", color=WHITE, fontsize=16, fontweight="bold")
        for y, line in zip(line_ys, lines):
            if line:
                ax.text(cx, y, line, ha="center", va="center", color=WHITE, fontsize=11)
    for x1, x2 in [(3.85, 5.25), (8.75, 10.15)]:
        ax.annotate("", xy=(x2, 3.1), xytext=(x1, 3.1), arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=3))
    ax.text(
        7,
        5.45,
        "RAG = retrieval-augmented generation",
        ha="center",
        va="center",
        fontsize=15,
        fontweight="bold",
        color=BLUE,
    )
    ax.text(
        7,
        0.95,
        "Gemini Notebook is the best-known example.",
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
    )
    ax.text(
        7,
        0.45,
        "OpenEvidence and UpToDate are other corpora. The source still has to be opened.",
        ha="center",
        va="center",
        fontsize=12,
        color=MUTED,
    )
    save(fig, "rag")


# --- 10. Hallucinations ---
def fig_hallucinations():
    fig, ax = plt.subplots(figsize=(14.2, 6.6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.6)
    ax.axis("off")
    cards = [
        (
            0.4,
            ORANGE,
            "Chatbots, 2022–23",
            [
                ("Invented citation", "A PubMed ID that was never assigned."),
                ("Invented dose", "A number that sounds like a monograph."),
                ("Sounds like a review", "Fluent prose still needs a source."),
            ],
        ),
        (
            7.2,
            TEAL,
            "With tools, 2025–26",
            [
                ("Real paper, wrong claim", "The article exists. That sentence is not in it."),
                ("A rule gets dropped", "“No meds” at the start can be gone by the end."),
                ("Citation theater", "A chip or URL can still dress up the wrong sentence."),
            ],
        ),
    ]
    title_y = 5.15
    pair_ys = [(4.35, 3.95), (3.15, 2.75), (1.95, 1.55)]
    for x, c, title, rows in cards:
        rounded(ax, x, 0.85, 6.4, 4.7, WHITE, c, lw=3)
        cx = x + 3.2
        ax.text(cx, title_y, title, ha="center", va="center", fontsize=17, fontweight="bold", color=c)
        for (y1, y2), (head, expl) in zip(pair_ys, rows):
            ax.text(cx, y1, head, ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
            ax.text(cx, y2, expl, ha="center", va="center", fontsize=12, color=MUTED)
    ax.text(
        7,
        0.4,
        "They still sound confident. Open the source.",
        ha="center",
        va="center",
        fontsize=13,
        color=INK,
    )
    save(fig, "hallucinations")


# --- 11. Test-time compute: what vendors call reasoning ---
def fig_ttc():
    fig, ax = plt.subplots(figsize=(14.2, 5.45))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 5.45)
    ax.axis("off")
    rounded(ax, 0.4, 0.16, 6.3, 5.08, WHITE, ORANGE, lw=3, r=0.1)
    rounded(ax, 7.5, 0.16, 6.3, 5.08, WHITE, TEAL, lw=3, r=0.1)
    ax.text(3.55, 4.72, "Answer once", ha="center", fontsize=18, fontweight="bold", color=ORANGE)
    ax.text(3.55, 4.22, "First fluent sentence. Ship it.", ha="center", fontsize=13, color=MUTED)
    ax.text(3.55, 3.22, "=B2*10", ha="center", fontsize=26, fontweight="bold", family="DejaVu Sans Mono", color=INK)
    ax.text(
        3.55,
        2.05,
        "10 mg/kg × 50 kg → 500 mg.\nNo 400 mg maximum. No test.",
        ha="center",
        fontsize=14,
        color=INK,
        linespacing=1.35,
    )
    ax.text(10.65, 4.72, "Try → test → revise", ha="center", fontsize=18, fontweight="bold", color=TEAL)
    ax.text(10.65, 4.22, "Hidden scratch. Then one answer.", ha="center", fontsize=13, color=MUTED)
    ax.text(
        10.65,
        2.22,
        "Write 500 mg.\nTest the 400 mg maximum.\nKeep 400 mg.\nThen speak.",
        ha="center",
        fontsize=14,
        color=INK,
        linespacing=1.35,
    )
    save(fig, "test_time_compute")


# --- 12. Harness loop ---
def fig_harness():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")

    # Chatbot row — a dead end
    rounded(ax, 0.28, 4.42, 2.15, 0.82, MUTED, r=0.08)
    ax.text(1.35, 4.83, "Chatbot", ha="center", va="center", color=WHITE, fontsize=13, fontweight="bold")
    rounded(ax, 2.85, 4.32, 2.6, 1.02, BLUE, r=0.08)
    ax.text(4.15, 4.83, "Prompt", ha="center", va="center", color=WHITE, fontsize=14, fontweight="bold")
    ax.annotate("", xy=(6.05, 4.83), xytext=(5.55, 4.83), arrowprops=dict(arrowstyle="-|>", color=INK, lw=2))
    rounded(ax, 6.15, 4.32, 7.5, 1.02, GOLD, r=0.08)
    ax.text(9.9, 4.83, "A paragraph in the window", ha="center", va="center", color=INK, fontsize=14, fontweight="bold")
    ax.text(9.9, 3.95, "You copy it. It is not a file. It is not versioned.", ha="center", fontsize=11, color=MUTED)

    # Harness row — the loop
    rounded(ax, 0.28, 2.22, 2.15, 0.82, PURPLE, r=0.08)
    ax.text(1.35, 2.63, "Harness", ha="center", va="center", color=WHITE, fontsize=13, fontweight="bold")
    nodes = [
        (4.00, BLUE, "Prompt", "what you asked"),
        (6.55, PURPLE, "Files", "the folder it can see"),
        (9.10, TEAL, "Tools", "search, code, browser"),
        (11.65, ORANGE, "Artifact", "a file you can open"),
    ]
    for x, c, lab, sub in nodes:
        rounded(ax, x - 1.05, 2.12, 2.1, 1.02, c, r=0.08)
        ax.text(x, 2.63, lab, ha="center", va="center", color=WHITE, fontsize=13, fontweight="bold")
        ax.text(x, 1.72, sub, ha="center", va="center", fontsize=10.5, color=MUTED)
    for x1, x2 in [(5.05, 5.48), (7.60, 8.03), (10.15, 10.58)]:
        ax.annotate("", xy=(x2, 2.63), xytext=(x1, 2.63), arrowprops=dict(arrowstyle="-|>", color=INK, lw=2))
    # Loop: the artifact goes back into the folder.
    ax.annotate(
        "",
        xy=(6.55, 1.42),
        xytext=(11.65, 1.42),
        arrowprops=dict(arrowstyle="-|>", color=PURPLE, lw=1.8, mutation_scale=11),
    )
    ax.text(9.1, 1.18, "edit the file, run it again", ha="center", va="center", fontsize=10.5, color=PURPLE)
    ax.text(
        7,
        0.48,
        "Cursor, Codex, Claude Code, OpenCode: same genus. Labs 1 and 2 only make sense if the file is the product.",
        ha="center",
        fontsize=12,
        color=INK,
    )
    save(fig, "harness_loop")


# --- 13. Benchmark trap ---
def fig_bench():
    fig, ax = plt.subplots(figsize=(14.2, 6.55))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6.55)
    ax.axis("off")
    rounded(ax, 0.40, 2.05, 4.35, 3.75, WHITE, TEAL, lw=3)
    ax.text(2.58, 5.28, "On the exam", ha="center", fontsize=18, fontweight="bold", color=TEAL)
    ax.text(
        2.58,
        3.65,
        "Board-style items\nLeaderboard ratings\nVendor tables",
        ha="center",
        fontsize=14,
        color=INK,
        linespacing=1.45,
    )
    rounded(ax, 5.25, 2.05, 4.35, 3.75, WHITE, ORANGE, lw=3)
    ax.text(7.42, 5.28, "On the ward", ha="center", fontsize=18, fontweight="bold", color=ORANGE)
    ax.text(
        7.42,
        3.55,
        "Specific patient\nSpecific hospital formulary\nSpecific language\nSpecific cultural context",
        ha="center",
        fontsize=13,
        color=INK,
        linespacing=1.42,
    )
    ax.text(
        5,
        1.52,
        "The exam is comparable across models, and many of the exam questions\nare in the training data.",
        ha="center",
        fontsize=12,
        color=INK,
        linespacing=1.3,
    )
    ax.text(
        5,
        0.78,
        "The context of a specific patient, in a specific hospital, and with a specific set of\npreferences and limitations, will likely always be a challenging application for models.",
        ha="center",
        fontsize=12,
        color=INK,
        linespacing=1.3,
    )
    ax.text(
        5,
        0.22,
        "FDA 2026 discussion paper: open-ended generative AI is hard to premarket-test",
        ha="center",
        fontsize=11,
        color=MUTED,
    )
    save(fig, "benchmark_trap")


# --- 14. Hardware honesty ---
def fig_hardware():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    fig.set_tight_layout(False)
    labels = [
        "Typical resident\nlaptop memory\n8–16 GB",
        "Ollama qwen3.8\n27B download\n18 GB",
        "Glimmer 30B\n4-bit envelope\n<20 GB",
        "Comfortable\nlocal box\n24–32 GB graphics",
    ]
    vals = [12, 18, 19, 28]
    colors = [ORANGE, GOLD, TEAL, BLUE]
    ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.62)
    ax.set_xlabel("Gigabytes", fontsize=12, labelpad=10)
    ax.set_xlim(0, 36)
    ax.axvline(16, color=ORANGE, ls="--", lw=1.4)
    ax.text(16.3, 3.45, "many laptops stop here", color=ORANGE, fontsize=10, va="center")
    ax.set_position([0.22, 0.14, 0.72, 0.72])
    save(fig, "hardware", tight=False)


# --- 15. AAP PAS bars ---
def fig_aap_places():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    fig.set_tight_layout(False)
    labs = ["Used AI at work\nprior 12 mo", "Used AI scribes\n(among users)", "Concerned: no\nhuman oversight", "Confident tools are\npediatric-appropriate"]
    vals = [48, 39, 78, 6]
    cols = [BLUE, TEAL, ORANGE, PURPLE]
    ax.bar(labs, vals, color=cols, width=0.62)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% of respondents")
    for i, v in enumerate(vals):
        ax.text(i, v + 2.5, f"{v}%", ha="center", fontsize=14, fontweight="bold")
    ax.set_position([0.10, 0.18, 0.82, 0.68])
    fig.text(
        0.5,
        0.05,
        "Pediatric Academic Societies 2025  ·  US pediatricians’ experiences with artificial intelligence in healthcare",
        ha="center",
        fontsize=10,
        color=MUTED,
    )
    save(fig, "aap_places", tight=False)


# --- 16. Artsi evidence ---
def fig_artsi():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    ax.text(3.5, 5.35, "11", ha="center", va="center", fontsize=72, fontweight="bold", color=TEAL)
    ax.text(
        3.5,
        4.28,
        "independent studies\nof OpenEvidence",
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        linespacing=1.3,
    )
    ax.text(10.5, 5.35, "0", ha="center", va="center", fontsize=72, fontweight="bold", color=ORANGE)
    ax.text(
        10.5,
        4.28,
        "of those 11 synthesized\nas pediatric",
        ha="center",
        va="center",
        fontsize=14,
        color=INK,
        linespacing=1.3,
    )
    rounded(ax, 0.4, 0.95, 6.4, 2.35, WHITE, TEAL, lw=2.5, r=0.1)
    rounded(ax, 7.2, 0.95, 6.4, 2.35, WHITE, ORANGE, lw=2.5, r=0.1)
    ax.text(3.6, 2.95, "Appropriate use in that review", ha="center", fontsize=13, fontweight="bold", color=TEAL)
    ax.text(
        3.6,
        1.95,
        "Guideline-style look-up.\nOften reinforces a plan you already had.",
        ha="center",
        fontsize=13,
        color=INK,
        linespacing=1.4,
    )
    ax.text(10.4, 2.95, "Not the use case they found", ha="center", fontsize=13, fontweight="bold", color=ORANGE)
    ax.text(
        10.4,
        1.95,
        "Complex cases, or changing the plan.\nActing without opening the source.",
        ha="center",
        fontsize=13,
        color=INK,
        linespacing=1.4,
    )
    ax.text(
        7,
        0.58,
        "OpenEvidence does not say how the product is built.",
        ha="center",
        fontsize=14,
        fontweight="bold",
        color=INK,
    )
    ax.text(
        7,
        0.22,
        "Artsi et al. 2026  ·  npj Digit Med  ·  PROSPERO CRD420261289103",
        ha="center",
        fontsize=11,
        color=MUTED,
    )
    save(fig, "artsi_eleven")


# --- 17. Hajj counterexample ---
def fig_hajj():
    fig, ax = plt.subplots(figsize=(14.2, 6.15))
    fig.set_tight_layout(False)
    ax.set_position([0.09, 0.24, 0.44, 0.60])
    labs = ["ChatGPT-4o", "OpenEvidence"]
    vals = [66.7, 26.7]
    ax.bar(labs, vals, color=[ORANGE, TEAL], width=0.42)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% fully accurate (study-defined)")
    ax.set_xlim(-0.7, 1.7)
    for i, v in enumerate(vals):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontsize=15, fontweight="bold")
    rx = 0.78
    fig.text(
        rx,
        0.80,
        "What the bars show",
        ha="center",
        fontsize=15,
        fontweight="bold",
        color=INK,
    )
    fig.text(
        rx,
        0.68,
        "Same 15 questions about adult\ntranscatheter tricuspid therapy.",
        ha="center",
        fontsize=12,
        color=INK,
        linespacing=1.35,
    )
    fig.text(
        rx,
        0.50,
        "Height is the share scored fully\naccurate by the study’s own rule.\nChatGPT-4o: 10 of 15 (66.7%).\nOpenEvidence: 4 of 15 (26.7%).",
        ha="center",
        fontsize=12,
        color=INK,
        linespacing=1.35,
    )
    fig.text(
        rx,
        0.30,
        "OpenEvidence still cited papers.\nThose citations did not make\nthe answers correct.",
        ha="center",
        fontsize=12,
        color=INK,
        linespacing=1.35,
    )
    fig.text(
        0.5,
        0.07,
        "Hajj et al., as reported in Artsi 2026. n = 15 is the whole sample. Adult cardiology — not a pediatric result.",
        ha="center",
        fontsize=11,
        color=MUTED,
    )
    save(fig, "hajj_counterexample", tight=False)


# --- 18. Policy 2026 ---
def fig_policy():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    fig.subplots_adjust(left=0.02, right=0.98, top=0.96, bottom=0.04)
    ax.set_xlim(0.15, 9.85)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    y_line = 3.20
    ax.plot([0.4, 9.6], [y_line, y_line], color=BLUE, lw=4, solid_capstyle="round")
    items = [
        (
            1.00,
            "Jan 20",
            True,
            ["AAP digital ecosystems", "Dedicated AI statement", "still forthcoming"],
        ),
        (
            2.35,
            "Jan",
            False,
            ["ICMJE journals", "Name the tool.", "Authors stay human."],
        ),
        (
            3.70,
            "Apr",
            True,
            ["Grundmeier, Pediatrics", "AI is a tool.", "Counsel companion chatbots."],
        ),
        (
            5.05,
            "Apr 29",
            False,
            ["Bergman, JAMA", "License autonomous AI", "like a clinician."],
        ),
        (
            6.40,
            "Jun 10",
            True,
            ["AMA", "Assistive, with oversight.", "Payer AI must be transparent."],
        ),
        (
            7.75,
            "Aug",
            False,
            ["FDA devices paper", "Risk = what the tool does", "× how bad an error is."],
        ),
        (
            9.10,
            "2026",
            True,
            ["WHO", "Speed evidence for", "policy-makers."],
        ),
    ]
    date_off = 0.24
    gloss0 = 0.50
    gloss_step = 0.28
    for x, when, above, lines in items:
        ax.scatter([x], [y_line], s=120, color=GOLD, zorder=4, edgecolor=PURPLE, lw=1.2)
        sign = 1 if above else -1
        ax.text(
            x,
            y_line + sign * date_off,
            when,
            ha="center",
            va="center",
            fontsize=11,
            fontweight="bold",
            color=PURPLE,
        )
        n = len(lines)
        for i, line in enumerate(lines):
            # First content line sits farthest from the axis so each block
            # reads top-to-bottom. Equal |offsets| keep the line centered
            # between the commentary above and below.
            if above:
                y = y_line + gloss0 + (n - 1 - i) * gloss_step
            else:
                y = y_line - gloss0 - i * gloss_step
            ax.text(
                x,
                y,
                line,
                ha="center",
                va="center",
                fontsize=10,
                color=INK,
            )
    save(fig, "policy_2026", tight=False)


# --- 19. HIPAA ---
def fig_hipaa():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.8)
    ax.axis("off")
    rows = [
        (ORANGE, "Consumer ChatGPT / Claude / Gemini", "Prompt leaves the building"),
        (GOLD, "OpenEvidence “HIPAA” badge", "Still a vendor cloud"),
        (TEAL, "Offline Ollama on your laptop", "Prompt stays here · like Epic on this machine"),
        (BLUE, "Hospital tool with a privacy contract", "The official cloud path"),
    ]
    for i, (c, t, s) in enumerate(rows):
        y = 4.35 - i * 1.15
        rounded(ax, 0.5, y, 13.1, 1.0, c, r=0.08)
        ax.text(0.9, y + 0.52, t, va="center", fontsize=15, fontweight="bold", color=WHITE if c != GOLD else INK)
        ax.text(13.2, y + 0.52, s, va="center", ha="right", fontsize=12, color=WHITE if c != GOLD else INK)
    save(fig, "hipaa")


# --- 20. Parameter scale ---
def fig_scale():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    fig.set_tight_layout(False)
    names = [
        "GPT-3\n175 billion",
        "Qwen3.8\n27 billion local",
        "Glimmer\n30 billion local",
        "DeepSeek-V4-Pro\n1.6 trillion\n49 billion active",
        "Qwen-Max\n2.4 trillion",
        "Kimi K3\n2.8 trillion\nmixture of experts",
    ]
    vals = [0.175, 0.027, 0.030, 1.6, 2.4, 2.8]
    colors = [BLUE, TEAL, TEAL, PURPLE, PURPLE, ORANGE]
    ax.bar(names, vals, color=colors, width=0.62)
    ax.set_ylabel("Total parameters (trillions, log scale)")
    ax.set_yscale("log")
    ax.tick_params(axis="x", labelsize=10)
    ax.set_position([0.10, 0.22, 0.82, 0.62])
    fig.text(
        0.5,
        0.90,
        "Active parameters and distillation matter more than a headline count in the trillions.",
        ha="center",
        fontsize=12,
        color=INK,
    )
    fig.text(
        0.5,
        0.07,
        "Counts from first-party posts cited in the briefing.",
        ha="center",
        fontsize=9,
        color=MUTED,
    )
    fig.text(
        0.5,
        0.035,
        "Local 27-billion and 30-billion models are dense-class; Kimi, Qwen-Max, and DeepSeek-Pro are mixture-of-experts or sparse.",
        ha="center",
        fontsize=9,
        color=MUTED,
    )
    save(fig, "param_scale", tight=False)


# --- 21. Workshop split ---
def fig_workshops():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    ax.text(7, 6.05, "Live blocks vs take-home labs", ha="center", fontsize=17, fontweight="bold", color=BLUE)

    rounded(ax, 0.35, 0.45, 6.5, 5.15, WHITE, PURPLE_WEB, lw=3)
    ax.text(3.6, 5.22, "This hour  ·  Labs 1–4", ha="center", fontsize=15, fontweight="bold", color=PURPLE_WEB)
    live = [
        ("1", "Files from a harness", "Word, Excel, slides from STEM.md"),
        ("2", "Audit the dose sheet", "Fictional teachicillin. Find the error."),
        ("3", "One question, three corpora", "Same febrile-infant question"),
        ("4", "Citation autopsy", "Open PubMed on the first three IDs"),
    ]
    y0 = 4.38
    gap = 0.92
    for i, (n, title, sub) in enumerate(live):
        y = y0 - i * gap
        ax.add_patch(Circle((1.18, y), 0.26, facecolor=PURPLE_WEB, zorder=3))
        ax.text(1.18, y, n, ha="center", va="center", color=WHITE, fontsize=13, fontweight="bold", zorder=4)
        ax.text(1.62, y + 0.15, title, ha="left", va="center", fontsize=13, fontweight="bold", color=INK)
        ax.text(1.62, y - 0.15, sub, ha="left", va="center", fontsize=11, color=MUTED)
    ax.text(3.6, 0.72, "Cursor, then the browser. Watch, then try later.", ha="center", fontsize=11, color=MUTED)

    rounded(ax, 7.15, 0.45, 6.5, 5.15, WHITE, TEAL, lw=3)
    ax.text(10.4, 5.22, "Take-home  ·  Labs 5–8", ha="center", fontsize=15, fontweight="bold", color=TEAL)
    home = [
        ("5", "GitHub Pages journal club", "Markdown → a URL that works on a phone"),
        ("6", "Local model on your laptop", "Ollama, airplane mode"),
        ("7", "Harness loop vs chatbot", "Same request. Files vs a paragraph."),
        ("8", "Gemini Notebook", "Your PDFs. Grounded Q&A."),
    ]
    for i, (n, title, sub) in enumerate(home):
        y = y0 - i * gap
        ax.add_patch(Circle((7.98, y), 0.26, facecolor=TEAL, zorder=3))
        ax.text(7.98, y, n, ha="center", va="center", color=WHITE, fontsize=13, fontweight="bold", zorder=4)
        ax.text(8.42, y + 0.15, title, ha="left", va="center", fontsize=13, fontweight="bold", color=INK)
        ax.text(8.42, y - 0.15, sub, ha="left", va="center", fontsize=11, color=MUTED)
    ax.text(10.4, 0.72, "Recipes in the handout. Free path for each.", ha="center", fontsize=11, color=MUTED)
    save(fig, "workshops_split")


# --- 22. Take-homes icons ---
def fig_takehomes():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    items = [
        (0.35, BLUE, "1", "No patient data\nin consumer tools"),
        (4.95, ORANGE, "2", "Click every\ncitation"),
        (9.55, PURPLE, "3", "Never copy\na dose"),
        (0.35, TEAL, "4", "Harnesses\nemit files"),
        (4.95, GOLD, "5", "Local keeps the prompt\non the laptop"),
        (9.55, PURPLE_WEB, "6", "You still need the\nchild’s age and context"),
    ]
    box_w, box_h = 4.3, 2.2
    for x, c, n, t in items:
        y = 3.3 if n in "123" else 0.65
        rounded(ax, x, y, box_w, box_h, c, r=0.1)
        ink = INK if c == GOLD else WHITE
        ax.text(
            x + 0.58,
            y + box_h / 2,
            n,
            color=ink,
            fontsize=26,
            fontweight="bold",
            va="center",
            ha="center",
        )
        ax.text(
            x + 2.55,
            y + box_h / 2,
            t,
            color=ink,
            fontsize=15,
            fontweight="bold",
            va="center",
            ha="center",
            linespacing=1.35,
        )
    save(fig, "takehomes")


def fig_context_age():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.0)
    ax.axis("off")
    ax.text(7.1, 5.55, "38.5 °C", ha="center", fontsize=42, fontweight="bold", color=GOLD)
    ax.text(7.1, 4.95, "Same number. Different child. Context is the age.", ha="center", fontsize=15, color=INK)
    rounded(ax, 0.45, 0.55, 6.3, 4.05, WHITE, ORANGE, lw=3, r=0.1)
    rounded(ax, 7.45, 0.55, 6.3, 4.05, WHITE, BLUE, lw=3, r=0.1)
    ax.text(3.6, 3.95, "3-week-old", ha="center", fontsize=22, fontweight="bold", color=ORANGE)
    ax.text(3.6, 2.35, "Fever workup.\nHours, not days.\nThe number is a trigger.", ha="center", fontsize=16, color=INK, linespacing=1.4)
    ax.text(10.6, 3.95, "3-year-old", ha="center", fontsize=22, fontweight="bold", color=BLUE)
    ax.text(10.6, 2.35, "Often watch and treat.\nSame temperature.\nDifferent meaning.", ha="center", fontsize=16, color=INK, linespacing=1.4)
    save(fig, "context_age")


def fig_three_eras():
    fig, ax = plt.subplots(figsize=(14.2, 5.4))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 5.4)
    ax.axis("off")
    eras = [
        (0.4, BLUE, "1", "Autocomplete", "Finishes the next\nword or line."),
        (4.95, PURPLE, "2", "Chat", "Holds a conversation.\nStill next-token."),
        (9.5, TEAL, "3", "Tools / checking", "Looks things up.\nRuns code. Still wrong."),
    ]
    for x, c, n, title, body in eras:
        rounded(ax, x, 0.55, 4.25, 4.05, WHITE, c, lw=3, r=0.1)
        ax.text(x + 0.35, 3.95, n, fontsize=16, fontweight="bold", color=c)
        ax.text(x + 2.12, 3.15, title, ha="center", fontsize=20, fontweight="bold", color=c)
        ax.text(x + 2.12, 1.75, body, ha="center", fontsize=15, color=INK, linespacing=1.35)
    save(fig, "three_eras")


def fig_settled():
    fig, ax = plt.subplots(figsize=(14.2, 6.55))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.55)
    ax.axis("off")
    ax.text(13.85, 6.32, "as of August 2026", ha="right", fontsize=11, color=MUTED, fontstyle="italic")
    rounded(ax, 0.28, 0.18, 6.72, 5.90, WHITE, TEAL, lw=3, r=0.1)
    rounded(ax, 7.20, 0.18, 6.72, 5.90, WHITE, ORANGE, lw=3, r=0.1)
    ax.text(3.64, 5.68, "Already in writing", ha="center", va="center", fontsize=18, fontweight="bold", color=TEAL)
    ax.text(10.56, 5.68, "Still missing in pediatrics", ha="center", va="center", fontsize=18, fontweight="bold", color=ORANGE)

    left_x = 0.58
    ax.text(left_x, 5.18, "ICMJE Recommendations, Jan 2026  ·  COPE, 2023", ha="left", va="top", fontsize=11, color=TEAL)
    ax.text(
        left_x,
        4.78,
        "Authors have to be humans who can take\nresponsibility. A chatbot cannot be an author.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )
    ax.text(left_x, 3.78, "AMA House of Delegates, 10 Jun 2026", ha="left", va="top", fontsize=11, color=TEAL)
    ax.text(
        left_x,
        3.38,
        "AI must not replace physician judgment.\nA physician stays in charge.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )
    ax.text(left_x, 2.38, "What that means for you", ha="left", va="top", fontsize=11, color=TEAL)
    ax.text(
        left_x,
        1.98,
        "You remain the author. You remain\nthe one making the call.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )

    right_x = 7.50
    ax.text(right_x, 5.18, "AAP, Jan 2026 (digital-ecosystems policy)", ha="left", va="top", fontsize=11, color=ORANGE)
    ax.text(
        right_x,
        4.78,
        "A dedicated clinical AI statement is still forthcoming.\nThere is no AAP bedside AI policy to follow yet.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )
    ax.text(right_x, 3.78, "FDA, Aug 2026 (discussion paper)", ha="left", va="top", fontsize=11, color=ORANGE)
    ax.text(
        right_x,
        3.38,
        "The FDA is still asking how to test\nchatbot-style tools.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )
    ax.text(right_x, 2.38, "Independent literature", ha="left", va="top", fontsize=11, color=ORANGE)
    ax.text(
        right_x,
        1.98,
        "Pediatric-specific evidence is thin.\nArtsi: 11 OpenEvidence studies, none pediatric.",
        ha="left",
        va="top",
        fontsize=13,
        color=INK,
        linespacing=1.3,
    )
    save(fig, "settled")


def fig_poll_open():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    cards = [
        (0.4, 3.05, BLUE, "1", "Used AI at work\nin the last year?"),
        (7.3, 3.05, TEAL, "2", "Used an AI scribe?"),
        (0.4, 0.4, ORANGE, "3", "Worried if no human\nchecks the output?"),
        (7.3, 0.4, PURPLE, "4", "Trust these tools for\npediatric care?"),
    ]
    for x, y, c, n, label in cards:
        rounded(ax, x, y, 6.5, 2.4, WHITE, c, lw=3, r=0.1)
        ax.add_patch(Circle((x + 0.85, y + 1.2), 0.42, facecolor=c, zorder=3))
        ax.text(x + 0.85, y + 1.2, n, ha="center", va="center", color=WHITE, fontsize=18, fontweight="bold", zorder=4)
        ax.text(x + 3.55, y + 1.2, label, ha="center", va="center", fontsize=20, fontweight="bold", color=INK, linespacing=1.25)
    save(fig, "poll_open")


def fig_two_blocks():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.0)
    ax.axis("off")
    rounded(ax, 0.4, 0.45, 6.4, 4.7, WHITE, PURPLE_WEB, lw=3, r=0.1)
    rounded(ax, 7.4, 0.45, 6.4, 4.7, WHITE, TEAL, lw=3, r=0.1)
    ax.text(3.6, 4.5, "Make → inspect", ha="center", fontsize=24, fontweight="bold", color=PURPLE_WEB)
    ax.text(3.6, 3.85, "Labs 1 and 2", ha="center", fontsize=14, fontweight="bold", color=GOLD)
    ax.text(3.6, 2.25, "Files you can open tomorrow.\nThen find what is wrong.", ha="center", fontsize=16, color=INK, linespacing=1.4)
    ax.text(10.6, 4.5, "Ask → verify", ha="center", fontsize=24, fontweight="bold", color=TEAL)
    ax.text(10.6, 3.85, "Labs 3 and 4", ha="center", fontsize=14, fontweight="bold", color=GOLD)
    ax.text(10.6, 2.25, "A febrile-infant question.\nThen check whether the\ncitations are real.", ha="center", fontsize=16, color=INK, linespacing=1.4)
    save(fig, "two_blocks")


def fig_formula_bug():
    fig, ax = plt.subplots(figsize=(14.2, 4.6))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    rounded(ax, 1.5, 0.45, 11.2, 3.7, WHITE, ORANGE, lw=3, r=0.12)
    ax.text(7.1, 3.45, "Cell C2", ha="center", fontsize=14, color=MUTED)
    ax.text(7.1, 2.25, "=B2*10", ha="center", fontsize=48, fontweight="bold", family="DejaVu Sans Mono", color=INK)
    ax.text(
        7.1,
        1.05,
        "Weight in B2. Ten milligrams per kilogram. No 400 mg maximum.",
        ha="center",
        fontsize=15,
        color=INK,
    )
    save(fig, "formula_bug")


def fig_lab5_flow():
    fig, ax = plt.subplots(figsize=(14.2, 4.6))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 4.6)
    ax.axis("off")
    steps = [
        (0.4, BLUE, "Paper", "One open paper\nor guideline."),
        (3.85, PURPLE, "Eight slides", "A deck you can\nhost or zip."),
        (7.3, ORANGE, "Verify", "Open every\ncitation first."),
        (10.75, TEAL, "Share", "A URL, or a zip\non a phone."),
    ]
    for x, c, title, body in steps:
        rounded(ax, x, 0.7, 3.2, 3.35, WHITE, c, lw=3, r=0.1)
        ax.text(x + 1.6, 3.35, title, ha="center", fontsize=18, fontweight="bold", color=c)
        ax.text(x + 1.6, 1.85, body, ha="center", fontsize=14, color=INK, linespacing=1.35)
    save(fig, "lab5_flow")


def fig_lab6_rules():
    fig, ax = plt.subplots(figsize=(14.2, 5.4))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 5.4)
    ax.axis("off")
    cards = [
        (0.4, ORANGE, "Airplane mode", "Wi-Fi off the\nwhole time."),
        (4.95, PURPLE, "Synthetic data", "Invented H&P.\nNever tonight’s census."),
        (9.5, TEAL, "Hardware limits", "8–16 GB runs 8B-class.\n27B needs more RAM."),
    ]
    for x, c, title, body in cards:
        rounded(ax, x, 0.7, 4.25, 4.05, WHITE, c, lw=3, r=0.1)
        ax.text(x + 2.12, 3.85, title, ha="center", fontsize=20, fontweight="bold", color=c)
        ax.text(x + 2.12, 2.15, body, ha="center", fontsize=16, color=INK, linespacing=1.4)
    save(fig, "lab6_rules")


def main():
    fig_hour_map()
    fig_three_ais()
    fig_learning_modes()
    fig_pediatric_shift()
    fig_tokens()
    fig_next_token()
    fig_attention()
    fig_timeline()
    fig_three_boxes()
    fig_rag()
    fig_hallucinations()
    fig_ttc()
    fig_harness()
    fig_bench()
    fig_hardware()
    fig_aap_places()
    fig_artsi()
    fig_hajj()
    fig_policy()
    fig_hipaa()
    fig_scale()
    fig_workshops()
    fig_takehomes()
    fig_context_age()
    fig_three_eras()
    fig_settled()
    fig_poll_open()
    fig_two_blocks()
    fig_formula_bug()
    fig_lab5_flow()
    fig_lab6_rules()
    print("wrote", len(list(OUT.glob("*.png"))), "pngs to", OUT)


if __name__ == "__main__":
    main()
