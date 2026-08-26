#!/usr/bin/env python3
"""Generate lecture figures from briefing facts (25 Aug 2026).

Every numeric claim is labeled with its source in the figure itself.
Schematics that are not measured data say so on the canvas.
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


def save(fig, name):
    fig.savefig(OUT / f"{name}.png", bbox_inches="tight", facecolor=PAPER, pad_inches=0.15)
    fig.savefig(OUT / f"{name}.svg", bbox_inches="tight", facecolor=PAPER, pad_inches=0.15)
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
    fig, ax = plt.subplots(figsize=(14.2, 4.2))
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 3.2)
    ax.axis("off")
    blocks = [
        (0, 12, BLUE, "Foundations\n12 min"),
        (12, 10, TEAL, "Timeline\n10"),
        (22, 10, PURPLE, "Reasoning\n+ tools 10"),
        (32, 8, ORANGE, "Frontier\n+ HIPAA 8"),
        (40, 8, GOLD, "Policy\n8"),
        (48, 12, PURPLE_WEB, "Live labs\n12 min"),
    ]
    for x, w, c, lab in blocks:
        rounded(ax, x + 0.3, 1.15, w - 0.6, 1.35, c, r=0.15)
        color = INK if c == GOLD else WHITE
        ax.text(x + w / 2, 1.82, lab, ha="center", va="center", color=color, fontsize=13, fontweight="bold")
    ax.plot([0, 60], [0.85, 0.85], color=INK, lw=2)
    for t in range(0, 61, 10):
        ax.plot([t, t], [0.72, 0.85], color=INK, lw=1.5)
        ax.text(t, 0.42, f"{t}m", ha="center", fontsize=11, color=MUTED)
    ax.text(30, 2.9, "The live hour", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    save(fig, "hour_map")


# --- 2. Three meanings of AI ---
def fig_three_ais():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    cards = [
        (0.4, BLUE, "Rules & scores", "If-then · PEWS · order sets", "Not learned\nfrom data"),
        (5.0, PURPLE, "Classical ML", "Labels in → class / risk out", "Sepsis alert\nCXR CAD"),
        (9.6, TEAL, "Foundation models", "Tokens out, not a score", "Chat · scribes\nagents"),
    ]
    for x, c, title, mid, bot in cards:
        rounded(ax, x, 0.6, 4.2, 5.1, WHITE, ec=c, r=0.12, lw=3)
        ax.add_patch(Circle((x + 2.1, 4.55), 0.42, facecolor=c, zorder=3))
        ax.text(x + 2.1, 3.7, title, ha="center", fontsize=18, fontweight="bold", color=c)
        ax.text(x + 2.1, 2.7, mid, ha="center", fontsize=13, color=INK)
        ax.text(x + 2.1, 1.5, bot, ha="center", fontsize=13, color=MUTED)
    ax.text(7.1, 6.05, "Same word. Three jobs.", ha="center", fontsize=18, fontweight="bold", color=BLUE)
    save(fig, "three_ais")


# --- 3. Learning modes ---
def fig_learning_modes():
    fig, axes = plt.subplots(1, 3, figsize=(14.2, 5.6))
    rng = np.random.default_rng(7)
    captions = ["x paired with y", "structure, no labels", "try → signal → try again"]

    for ax in axes:
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_aspect("equal", adjustable="box")

    ax = axes[0]
    ax.scatter(rng.normal(1, 0.35, 40), rng.normal(1, 0.35, 40), c=BLUE, s=36)
    ax.scatter(rng.normal(3, 0.35, 40), rng.normal(3, 0.35, 40), c=ORANGE, s=36)
    ax.set_title("Supervised", color=BLUE, fontweight="bold")

    ax = axes[1]
    pts = rng.normal(2, 0.55, size=(80, 2))
    ax.scatter(pts[:, 0], pts[:, 1], c=TEAL, s=28, alpha=0.85)
    ax.set_title("Unsupervised", color=PURPLE, fontweight="bold")

    ax = axes[2]
    ax.set_title("Reinforcement", color=ORANGE, fontweight="bold")
    ax.annotate("", xy=(3.3, 3.2), xytext=(0.7, 0.7), arrowprops=dict(arrowstyle="->", color=PURPLE, lw=3))
    ax.text(0.7, 0.35, "action", color=MUTED, fontsize=11)
    ax.text(2.55, 3.45, "reward", color=ORANGE, fontsize=12, fontweight="bold")

    for ax, lab in zip(axes, captions):
        ax.set_xlim(0, 4)
        ax.set_ylim(0, 4)
        ax.set_xlabel(lab, fontsize=11, color=MUTED, labelpad=12)

    fig.align_xlabels(axes)
    fig.suptitle("How the model is taught", fontsize=18, fontweight="bold", color=BLUE, y=1.02)
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
    ax.text(7.0, 5.7, "A high AUROC on adults is not a pediatric recommendation", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(7.0, 0.45, "AAP PAS 2025 abstract: 6% confident AI is developed with adequate pediatric consideration", ha="center", va="center", fontsize=11, color=MUTED)
    save(fig, "pediatric_shift")


# --- 5. Tokens ---
def fig_tokens():
    fig, ax = plt.subplots(figsize=(14.2, 5.0))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.text(7, 4.45, "Models do not read letters. They read tokens.", ha="center", fontsize=18, fontweight="bold", color=BLUE)
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


# --- 6. Attention schematic ---
def fig_attention():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.4)
    ax.axis("off")
    ax.text(7, 6.1, "Attention: every token can look at every other token", ha="center", fontsize=17, fontweight="bold", color=BLUE)

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
    ax.text(7, 0.45, "A weight later says how much each word counts. That mix is context, not understanding.", ha="center", fontsize=13, color=INK)
    save(fig, "attention")


# --- 7. Timeline ---
def fig_timeline():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    ax.set_xlim(2018.5, 2026.8)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.plot([2019, 2026.4], [2.4, 2.4], color=BLUE, lw=4, solid_capstyle="round")
    events = [
        (2019.2, "GPT-2", 3.3),
        (2020.4, "GPT-3\n175B", 1.0),
        (2022.2, "InstructGPT\nRLHF", 3.5),
        (2022.9, "ChatGPT\n30 Nov 2022", 0.7),
        (2023.25, "GPT-4", 3.4),
        (2024.75, "o1\nreason", 0.75),
        (2026.3, "GPT-5.6 · Opus 5\nFable · Kimi K3", 3.35),
    ]
    for yr, lab, y in events:
        ax.plot([yr, yr], [2.4, 2.7 if y > 2.4 else 2.1], color=PURPLE, lw=2)
        ax.scatter([yr], [2.4], s=90, color=GOLD, zorder=5, edgecolor=PURPLE, linewidths=1.2)
        ax.text(yr, y, lab, ha="center", va="bottom" if y > 2.4 else "top", fontsize=11, fontweight="bold", color=INK)
    ax.text(2022.7, 5.4, "The public era starts here", ha="center", fontsize=16, fontweight="bold", color=ORANGE)
    ax.annotate("", xy=(2022.9, 2.55), xytext=(2022.7, 5.15), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.6))
    ax.text(2022.5, 5.75, "Dates from first-party launch posts / canonical papers  ·  cutoff 25 Aug 2026", ha="center", fontsize=10, color=MUTED)
    save(fig, "timeline")


# --- 8. Three access boxes ---
def fig_three_boxes():
    fig, ax = plt.subplots(figsize=(14.2, 6.6))
    ax.set_xlim(0, 14.2)
    ax.set_ylim(0, 6.6)
    ax.axis("off")
    boxes = [
        (0.35, ORANGE, "Closed API", "Sol · Fable · Opus 5\nGemini 3.7 · Muse Spark", "Personal phone\n· no BAA"),
        (4.95, PURPLE, "Open datacenter", "Kimi K3 · DeepSeek V4\nQwen-Max · GLM-5.3*", "Weights, still a rack\nof GPUs"),
        (9.55, TEAL, "Open laptop", "Qwen3.8-27B\nMuse Glimmer 30B", "Privacy architecture\nnot a quality trophy"),
    ]
    for x, c, t, mid, bot in boxes:
        rounded(ax, x, 0.7, 4.3, 5.2, WHITE, c, lw=3.5, r=0.1)
        ax.text(x + 2.15, 5.25, t, ha="center", fontsize=18, fontweight="bold", color=c)
        ax.text(x + 2.15, 3.55, mid, ha="center", fontsize=13, color=INK)
        ax.text(x + 2.15, 1.55, bot, ha="center", fontsize=12, color=MUTED)
    ax.text(7.1, 6.25, "August 2026 access map  ·  *GLM-5.3 weights not public as of 25 Aug 2026", ha="center", fontsize=13, color=MUTED)
    save(fig, "three_boxes")


# --- 9. RAG ---
def fig_rag():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.8)
    ax.axis("off")
    cards = [
        (0.4, BLUE, "Corpus", ["journals", "guidelines", "PDFs in the corpus"]),
        (5.3, PURPLE, "Retrieve", ["nearest chunks", "not the whole library", ""]),
        (10.2, TEAL, "Generate", ["answer + citations", "that still must", "be opened"]),
    ]
    title_y = 3.35
    line_ys = [2.70, 2.30, 1.90]
    for x, c, title, lines in cards:
        rounded(ax, x, 1.6, 3.4, 2.6, c)
        cx = x + 1.7
        ax.text(cx, title_y, title, ha="center", va="center", color=WHITE, fontsize=16, fontweight="bold")
        for y, line in zip(line_ys, lines):
            if line:
                ax.text(cx, y, line, ha="center", va="center", color=WHITE, fontsize=11)
    for x1, x2 in [(3.85, 5.25), (8.75, 10.15)]:
        ax.annotate("", xy=(x2, 2.9), xytext=(x1, 2.9), arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=3))
    ax.text(7, 5.2, "RAG is a corpus choice, not a synonym for “true”", ha="center", va="center", fontsize=17, fontweight="bold", color=BLUE)
    ax.text(7, 0.55, "OpenEvidence ≠ UpToDate ≠ ChatGPT with search  ·  retrieval error still looks fluent", ha="center", va="center", fontsize=11, color=MUTED)
    save(fig, "rag")


# --- 10. Hallucinations ---
def fig_hallucinations():
    fig, ax = plt.subplots(figsize=(14.2, 6.6))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.6)
    ax.axis("off")
    ax.text(
        7,
        6.25,
        "Hallucinations changed shape. They did not vanish.",
        ha="center",
        va="center",
        fontsize=16,
        fontweight="bold",
        color=BLUE,
    )
    cards = [
        (
            0.4,
            ORANGE,
            "Chatbots, 2022–23",
            [
                ("Invented citation", "A PubMed ID that was never assigned."),
                ("Invented dose", "A number that sounds like a monograph."),
                ("Sounds like a review", "Fluent prose is not a source."),
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


# --- 11. Test-time compute schematic ---
def fig_ttc():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    x = np.linspace(0.2, 8, 80)
    y = 1 - np.exp(-0.45 * x)
    ax.plot(x, y, color=PURPLE, lw=3.5)
    ax.fill_between(x, 0, y, color=TEAL, alpha=0.18)
    ax.set_xlabel("Test-time compute  (thinking tokens / tool steps)", fontsize=12)
    ax.set_ylabel("Task success", fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title("Extra compute at answer time", fontsize=16, fontweight="bold", color=BLUE, pad=12)
    ax.text(0.5, 0.92, "Not reasoning as we think about it. More like guess and grade.", transform=ax.transAxes, ha="center", fontsize=13, color=INK)
    ax.text(0.4, 0.82, "o1 (Sep 2024) made this the product", transform=ax.transAxes, fontsize=11, color=MUTED)
    save(fig, "test_time_compute")


# --- 12. Harness loop ---
def fig_harness():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    nodes = [
        (2.2, 3.2, BLUE, "Prompt"),
        (5.3, 4.7, PURPLE, "Files"),
        (5.3, 1.7, TEAL, "Tools"),
        (8.6, 3.2, ORANGE, "Tests"),
        (11.6, 3.2, GOLD, "Artifact"),
    ]
    for x, y, c, lab in nodes:
        rounded(ax, x - 1.15, y - 0.7, 2.3, 1.4, c, r=0.1)
        ax.text(x, y, lab, ha="center", va="center", color=INK if c == GOLD else WHITE, fontsize=15, fontweight="bold")
    arrows = [((3.35, 3.5), (4.15, 4.5)), ((3.35, 2.9), (4.15, 2.0)), ((6.45, 4.7), (7.45, 3.7)), ((6.45, 1.7), (7.45, 2.7)), ((9.75, 3.2), (10.45, 3.2))]
    for (x1, y1), (x2, y2) in arrows:
        ax.annotate("", xy=(x2, y2), xytext=(x1, y1), arrowprops=dict(arrowstyle="-|>", color=INK, lw=2))
    ax.text(7, 5.85, "A chatbot returns paragraphs. A harness returns files.", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    save(fig, "harness_loop")


# --- 13. Benchmark trap ---
def fig_bench():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    rounded(ax, 0.5, 1.2, 4.2, 3.6, WHITE, TEAL, lw=3)
    ax.text(2.6, 4.2, "In-sample", ha="center", fontsize=18, fontweight="bold", color=TEAL)
    ax.text(2.6, 2.7, "MedQA · USMLE-style\nLeaderboard Elo\nVendor tables", ha="center", fontsize=14)
    rounded(ax, 5.3, 1.2, 4.2, 3.6, WHITE, ORANGE, lw=3)
    ax.text(7.4, 4.2, "Out-of-sample", ha="center", fontsize=18, fontweight="bold", color=ORANGE)
    ax.text(7.4, 2.7, "This infant\nThis hospital’s formulary\nThis family’s language", ha="center", fontsize=14)
    ax.text(5, 5.4, "Passing a test the model has seen ≠ bedside competence", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(5, 0.45, "FDA 2026 discussion paper: open-ended GenAI is hard to premarket-test  ·  not guidance", ha="center", fontsize=11, color=MUTED)
    save(fig, "benchmark_trap")


# --- 14. Hardware honesty ---
def fig_hardware():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    labels = ["Typical resident\nlaptop RAM\n8–16 GB", "Ollama qwen3.8\n27B download\n18 GB", "Glimmer 30B\n4-bit envelope\n<20 GB", "Comfortable\nlocal box\n24–32 GB GPU"]
    vals = [12, 18, 19, 28]
    colors = [ORANGE, GOLD, TEAL, BLUE]
    bars = ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.62)
    ax.set_xlabel("Gigabytes (approximate)", fontsize=12)
    ax.set_xlim(0, 36)
    ax.set_title("Local models: hardware honesty", fontsize=17, fontweight="bold", color=BLUE, pad=10)
    ax.axvline(16, color=ORANGE, ls="--", lw=1.4)
    ax.text(16.3, 3.45, "many laptops stop here", color=ORANGE, fontsize=10)
    ax.text(0, -0.9, "Sources: Ollama library qwen3.8 listing (18 GB) and Meta Glimmer post (~4-bit <20 GB), retrieved 25 Aug 2026. Midpoint 12 GB is illustrative of the 8–16 GB class, not a measured fleet.", fontsize=9, color=MUTED, wrap=True)
    save(fig, "hardware")


# --- 15. AAP PAS bars ---
def fig_aap_places():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    labs = ["Used AI at work\nprior 12 mo", "Used AI scribes\n(among users)", "Concerned: no\nhuman oversight", "Confident tools are\npediatric-appropriate"]
    vals = [48, 39, 78, 6]
    cols = [BLUE, TEAL, ORANGE, PURPLE]
    ax.bar(labs, vals, color=cols, width=0.62)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% of respondents")
    for i, v in enumerate(vals):
        ax.text(i, v + 2.5, f"{v}%", ha="center", fontsize=14, fontweight="bold")
    ax.set_title("US pediatricians and AI, 2025  ·  PAS abstract, not a full paper", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(0.5, -0.22, "AAP PAS abstract “US pediatricians’ experiences with artificial intelligence in healthcare in 2025”  ·  conference abstract only", transform=ax.transAxes, ha="center", fontsize=10, color=MUTED)
    save(fig, "aap_places")


# --- 16. Artsi evidence ---
def fig_artsi():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6)
    ax.axis("off")
    # 11 squares
    ax.text(7, 5.55, "OpenEvidence independent evidence  ·  Artsi et al. 2026", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    for i in range(11):
        r, c = divmod(i, 6)
        rounded(ax, 1.2 + c * 2.0, 3.15 - r * 1.35, 1.7, 1.1, TEAL if i < 11 else WHITE)
        ax.text(1.2 + c * 2.0 + 0.85, 3.15 - r * 1.35 + 0.55, "study", ha="center", va="center", color=WHITE, fontsize=11, fontweight="bold")
    ax.text(7, 0.7, "11 studies  ·  0 synthesized as pediatric  ·  product still moving  ·  article-in-press", ha="center", fontsize=13, color=MUTED)
    ax.text(7, 0.25, "PROSPERO CRD420261289103  ·  npj Digit Med doi:10.1038/s41746-026-03077-4", ha="center", fontsize=10, color=MUTED)
    save(fig, "artsi_eleven")


# --- 17. Hajj counterexample ---
def fig_hajj():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    labs = ["ChatGPT-4o", "OpenEvidence"]
    vals = [66.7, 26.7]
    ax.bar(labs, vals, color=[ORANGE, TEAL], width=0.45)
    ax.set_ylim(0, 100)
    ax.set_ylabel("% fully accurate (study-defined)")
    for i, v in enumerate(vals):
        ax.text(i, v + 2, f"{v:.1f}%", ha="center", fontsize=16, fontweight="bold")
    ax.set_title("Grounding is not always “more accurate”", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(0.5, -0.2, "Hajj et al. as reported in Artsi 2026: 15 clinician-facing transcatheter tricuspid questions. Not a pediatric study.", transform=ax.transAxes, ha="center", fontsize=10, color=MUTED)
    save(fig, "hajj_counterexample")


# --- 18. Policy 2026 ---
def fig_policy():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0.6, 9.2)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    ax.plot([1, 8.6], [1.4, 1.4], color=BLUE, lw=4, solid_capstyle="round")
    items = [
        (1.4, "Jan 20", "AAP digital\necosystems\nAI forthcoming"),
        (2.8, "Apr", "Grundmeier\nPediatrics\nreview, not policy"),
        (4.2, "Apr 29", "Bergman\nJAMA\nlicensure"),
        (5.6, "Jun 10", "AMA HOD\nassistive,\nnot replace"),
        (7.0, "Aug", "FDA GenAI\ndevices paper\nNOT guidance"),
        (8.3, "2026", "WHO B09667\nEIP, not\nbedside"),
    ]
    for x, when, lab in items:
        ax.scatter([x], [1.4], s=110, color=GOLD, zorder=4, edgecolor=PURPLE, lw=1.2)
        ax.text(x, 1.85, when, ha="center", fontsize=11, fontweight="bold", color=PURPLE)
        ax.text(x, 3.55, lab, ha="center", fontsize=11, color=INK)
    ax.text(4.9, 5.7, "2026 statements with a public citation", ha="center", fontsize=17, fontweight="bold", color=BLUE)
    save(fig, "policy_2026")


# --- 19. HIPAA ---
def fig_hipaa():
    fig, ax = plt.subplots(figsize=(14.2, 5.8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 5.8)
    ax.axis("off")
    rows = [
        (ORANGE, "Consumer ChatGPT / Claude / Gemini", "No BAA  ·  PHI = impermissible disclosure"),
        (GOLD, "OpenEvidence “HIPAA” badge", "Vendor claim  ·  not a reason to paste identifiers"),
        (TEAL, "Offline Ollama on your laptop", "No vendor BA  ·  stolen laptop still ePHI"),
        (BLUE, "Hospital tool with executed BAA", "The only green light for real notes"),
    ]
    for i, (c, t, s) in enumerate(rows):
        y = 4.35 - i * 1.15
        rounded(ax, 0.5, y, 13.1, 1.0, c, r=0.08)
        ax.text(0.9, y + 0.52, t, va="center", fontsize=15, fontweight="bold", color=WHITE if c != GOLD else INK)
        ax.text(13.2, y + 0.52, s, va="center", ha="right", fontsize=12, color=WHITE if c != GOLD else INK)
    ax.text(7, 5.5, "HIPAA is a contract and a workstation, not a vibe", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    save(fig, "hipaa")


# --- 20. Parameter scale ---
def fig_scale():
    fig, ax = plt.subplots(figsize=(14.2, 6.0))
    names = ["GPT-3\n175B", "Qwen3.8\n27B local", "Glimmer\n30B local", "DeepSeek-V4-Pro\n1.6T / 49B act.", "Qwen-Max\n2.4T", "Kimi K3\n2.8T MoE"]
    vals = [0.175, 0.027, 0.030, 1.6, 2.4, 2.8]
    colors = [BLUE, TEAL, TEAL, PURPLE, PURPLE, ORANGE]
    ax.bar(names, vals, color=colors, width=0.62)
    ax.set_ylabel("Total parameters (trillions, log scale)")
    ax.set_yscale("log")
    ax.set_title("Size exploded. Active parameters and distillation matter more than the headline T.", fontsize=14, fontweight="bold", color=BLUE)
    ax.text(0.5, -0.22, "Counts from first-party posts / reports cited in the briefing. Local 27B/30B are dense-class; Kimi/Qwen-Max/DeepSeek-Pro are MoE or sparse.", transform=ax.transAxes, ha="center", fontsize=9, color=MUTED)
    save(fig, "param_scale")


# --- 21. Workshop split ---
def fig_workshops():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    rounded(ax, 0.4, 0.7, 6.4, 4.7, WHITE, PURPLE_WEB, lw=3)
    ax.text(3.6, 4.85, "This hour", ha="center", fontsize=16, fontweight="bold", color=PURPLE_WEB)
    ax.text(3.6, 3.3, "W1  Office files from a harness\nW4  Same question, three corpora", ha="center", fontsize=15)
    ax.text(3.6, 1.5, "Cursor  ·  three browsers", ha="center", fontsize=13, color=MUTED)
    rounded(ax, 7.2, 0.7, 6.4, 4.7, WHITE, TEAL, lw=3)
    ax.text(10.4, 4.85, "Take-home", ha="center", fontsize=16, fontweight="bold", color=TEAL)
    ax.text(10.4, 2.85, "W2 Pages  ·  W3 Ollama\nW5 citations  ·  W6 dosing audit\nW7 loop  ·  W8 Notebook", ha="center", fontsize=14)
    ax.text(7, 5.8, "Live labs vs take-home labs", ha="center", fontsize=17, fontweight="bold", color=BLUE)
    save(fig, "workshops_split")


# --- 22. Take-homes icons ---
def fig_takehomes():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    items = [
        (0.5, BLUE, "1", "No PHI in consumer tools"),
        (5.0, ORANGE, "2", "Click every citation"),
        (9.5, PURPLE, "3", "Never copy a dose"),
        (0.5, TEAL, "4", "Harnesses emit files"),
        (5.0, GOLD, "5", "Local ≠ compliant"),
        (9.5, PURPLE_WEB, "6", "AAP AI policy still forthcoming"),
    ]
    for x, c, n, t in items:
        y = 3.35 if n in "123" else 0.7
        rounded(ax, x, y, 4.1, 2.15, c, r=0.1)
        ax.text(x + 0.45, y + 1.07, n, color=WHITE if c != GOLD else INK, fontsize=22, fontweight="bold", va="center")
        ax.text(x + 1.15, y + 1.07, t, color=WHITE if c != GOLD else INK, fontsize=14, fontweight="bold", va="center")
    ax.text(7, 5.75, "Six things to leave with", ha="center", fontsize=18, fontweight="bold", color=BLUE)
    save(fig, "takehomes")


def main():
    fig_hour_map()
    fig_three_ais()
    fig_learning_modes()
    fig_pediatric_shift()
    fig_tokens()
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
    print("wrote", len(list(OUT.glob("*.png"))), "pngs to", OUT)


if __name__ == "__main__":
    main()
