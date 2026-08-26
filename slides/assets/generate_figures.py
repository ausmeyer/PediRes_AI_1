#!/usr/bin/env python3
"""Generate lecture figures from briefing facts.

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
        (0, 10, BLUE, "Foundations\n10 min"),
        (10, 8, TEAL, "Timeline\n8"),
        (18, 8, PURPLE, "Reasoning\n+ tools 8"),
        (26, 8, ORANGE, "Frontier\n+ HIPAA 8"),
        (34, 8, GOLD, "Policy\n8"),
        (42, 18, PURPLE_WEB, "Live labs\n18 min"),
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
        (0.4, BLUE, "Rules & scores", "If-then · scores · order sets", "Written by people\nor split from data"),
        (5.0, PURPLE, "Classical ML", "Labels in → class / risk out", "Sepsis alert\nchest X-ray read"),
        (9.6, TEAL, "Foundation models", "Next-token output", "Chat · scribes\nagents"),
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
    ax.text(7.0, 5.7, "Adult area-under-curve is an adult result", ha="center", va="center", fontsize=16, fontweight="bold", color=INK)
    ax.text(7.0, 0.45, "Pediatric Academic Societies 2025: 6% confident AI is developed with adequate pediatric consideration", ha="center", va="center", fontsize=11, color=MUTED)
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
    ax.text(7, 0.45, "A weight later says how much each word counts. That mix is context.", ha="center", fontsize=13, color=INK)
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
        (2022.2, "InstructGPT\nhuman feedback", 3.5),
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
    save(fig, "timeline")


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
            "Company app",
            ["Sol · Fable · Opus 5", "Gemini 3.7 · Muse Spark"],
            [
                "You use these through a company",
                "website or phone app. There is",
                "no hospital privacy contract.",
            ],
        ),
        (
            4.95,
            PURPLE,
            "Open datacenter",
            ["Kimi K3 · DeepSeek V4", "Qwen-Max · GLM-5.3*"],
            [
                "The weights can be downloaded,",
                "but you still need a graphics-card cluster.",
                "A laptop cannot host these.",
            ],
        ),
        (
            9.55,
            TEAL,
            "Open laptop",
            ["Qwen3.8-27B", "Muse Glimmer 30B"],
            [
                "The vendor never sees the prompt.",
                "You already use this laptop for",
                "the EHR. That is reasonable.",
            ],
        ),
    ]
    model_ys = [4.45, 4.00]
    note_ys = [2.35, 1.90, 1.45]
    for x, c, title, models, notes in cards:
        rounded(ax, x, 0.55, 4.3, 5.45, WHITE, c, lw=3.5, r=0.1)
        cx = x + 2.15
        ax.text(cx, 5.45, title, ha="center", va="center", fontsize=18, fontweight="bold", color=c)
        for y, line in zip(model_ys, models):
            ax.text(cx, y, line, ha="center", va="center", fontsize=13, color=INK)
        for y, line in zip(note_ys, notes):
            ax.text(cx, y, line, ha="center", va="center", fontsize=11, color=MUTED)
    ax.text(
        7.1,
        6.45,
        "*GLM-5.3 weights not public",
        ha="center",
        va="center",
        fontsize=13,
        color=MUTED,
    )
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
    ax.text(7, 5.2, "Retrieve, then generate. The corpus is the choice.", ha="center", va="center", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(7, 0.55, "OpenEvidence, UpToDate, and ChatGPT-with-search are different corpora", ha="center", va="center", fontsize=11, color=MUTED)
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
        "Hallucinations changed shape. They are still here.",
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


# --- 11. Test-time compute schematic ---
def fig_ttc():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    x = np.linspace(0.2, 8, 80)
    y = 1 - np.exp(-0.45 * x)
    ax.plot(x, y, color=PURPLE, lw=3.5)
    ax.fill_between(x, 0, y, color=TEAL, alpha=0.18)
    ax.set_xlabel("Test-time compute  (thinking tokens / tool steps)", fontsize=12)
    ax.set_ylabel("Task success", fontsize=12)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_ylim(0, 1.02)
    fig.subplots_adjust(top=0.78)
    fig.text(0.5, 0.96, "Extra compute at answer time", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    fig.text(
        0.5,
        0.91,
        "Not reasoning as we think about it. More like guess and grade.",
        ha="center",
        fontsize=13,
        color=INK,
    )
    fig.text(0.5, 0.87, "o1 (Sep 2024) made this the product", ha="center", fontsize=11, color=MUTED)
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
    ax.text(2.6, 4.2, "On the exam", ha="center", fontsize=18, fontweight="bold", color=TEAL)
    ax.text(2.6, 2.7, "Board-style exams\nLeaderboard ratings\nVendor tables", ha="center", fontsize=14)
    rounded(ax, 5.3, 1.2, 4.2, 3.6, WHITE, ORANGE, lw=3)
    ax.text(7.4, 4.2, "On the ward", ha="center", fontsize=18, fontweight="bold", color=ORANGE)
    ax.text(7.4, 2.7, "This infant\nThis hospital’s formulary\nThis family’s language", ha="center", fontsize=14)
    ax.text(5, 5.4, "The exam and the ward", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(5, 0.45, "FDA 2026 discussion paper: open-ended generative AI is hard to premarket-test", ha="center", fontsize=11, color=MUTED)
    save(fig, "benchmark_trap")


# --- 14. Hardware honesty ---
def fig_hardware():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    labels = [
        "Typical resident\nlaptop memory\n8–16 GB",
        "Ollama qwen3.8\n27B download\n18 GB",
        "Glimmer 30B\n4-bit envelope\n<20 GB",
        "Comfortable\nlocal box\n24–32 GB graphics",
    ]
    vals = [12, 18, 19, 28]
    colors = [ORANGE, GOLD, TEAL, BLUE]
    ax.barh(labels[::-1], vals[::-1], color=colors[::-1], height=0.62)
    ax.set_xlabel("Gigabytes (approximate)", fontsize=12, labelpad=10)
    ax.set_xlim(0, 36)
    ax.set_title("Local models: hardware honesty", fontsize=17, fontweight="bold", color=BLUE, pad=10)
    ax.axvline(16, color=ORANGE, ls="--", lw=1.4)
    ax.text(16.3, 3.45, "many laptops stop here", color=ORANGE, fontsize=10, va="center")
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
    ax.set_title("US pediatricians and AI, 2025", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(
        0.5,
        -0.18,
        "Pediatric Academic Societies 2025  ·  US pediatricians’ experiences with artificial intelligence in healthcare",
        transform=ax.transAxes,
        ha="center",
        fontsize=10,
        color=MUTED,
    )
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
    ax.set_title("Grounding and accuracy can diverge", fontsize=16, fontweight="bold", color=BLUE)
    ax.text(0.5, -0.2, "Hajj et al. as reported in Artsi 2026: 15 clinician-facing transcatheter tricuspid questions.", transform=ax.transAxes, ha="center", fontsize=10, color=MUTED)
    save(fig, "hajj_counterexample")


# --- 18. Policy 2026 ---
def fig_policy():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
    ax.set_xlim(0.15, 9.85)
    ax.set_ylim(0.2, 6.45)
    ax.axis("off")
    y_line = 3.12
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
    for x, when, above, lines in items:
        ax.scatter([x], [y_line], s=120, color=GOLD, zorder=4, edgecolor=PURPLE, lw=1.2)
        if above:
            ax.text(
                x,
                y_line + 0.18,
                when,
                ha="center",
                va="bottom",
                fontsize=11,
                fontweight="bold",
                color=PURPLE,
            )
            top = y_line + 0.48 + 0.30 * len(lines)
            for i, line in enumerate(lines):
                ax.text(x, top - i * 0.30, line, ha="center", va="bottom", fontsize=10, color=INK)
        else:
            ax.text(
                x,
                y_line - 0.18,
                when,
                ha="center",
                va="top",
                fontsize=11,
                fontweight="bold",
                color=PURPLE,
            )
            for i, line in enumerate(lines):
                ax.text(
                    x,
                    y_line - 0.48 - i * 0.30,
                    line,
                    ha="center",
                    va="top",
                    fontsize=10,
                    color=INK,
                )
    ax.text(5.0, 6.15, "2026 statements with a public citation", ha="center", fontsize=17, fontweight="bold", color=BLUE)
    save(fig, "policy_2026")


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
    ax.text(7, 5.5, "Where the prompt goes", ha="center", fontsize=16, fontweight="bold", color=BLUE)
    save(fig, "hipaa")


# --- 20. Parameter scale ---
def fig_scale():
    fig, ax = plt.subplots(figsize=(14.2, 6.4))
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
    ax.set_title(
        "Size exploded. Active parameters and distillation matter more than a headline count in the trillions.",
        fontsize=12,
        fontweight="bold",
        color=BLUE,
    )
    ax.tick_params(axis="x", labelsize=10)
    ax.text(
        0.5,
        -0.28,
        "Counts from first-party posts cited in the briefing. Local 27-billion and 30-billion models are dense-class; Kimi, Qwen-Max, and DeepSeek-Pro are mixture-of-experts or sparse.",
        transform=ax.transAxes,
        ha="center",
        fontsize=9,
        color=MUTED,
    )
    save(fig, "param_scale")


# --- 21. Workshop split ---
def fig_workshops():
    fig, ax = plt.subplots(figsize=(14.2, 6.2))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 6.2)
    ax.axis("off")
    rounded(ax, 0.4, 0.7, 6.4, 4.7, WHITE, PURPLE_WEB, lw=3)
    ax.text(3.6, 4.85, "This hour", ha="center", fontsize=16, fontweight="bold", color=PURPLE_WEB)
    ax.text(3.6, 3.15, "W1  Office files from a harness\nW6  Dosing sheet audit\nW4  Same question, three corpora\nW5  Citation autopsy", ha="center", fontsize=14)
    ax.text(3.6, 1.35, "Cursor, then three browsers", ha="center", fontsize=13, color=MUTED)
    rounded(ax, 7.2, 0.7, 6.4, 4.7, WHITE, TEAL, lw=3)
    ax.text(10.4, 4.85, "Take-home", ha="center", fontsize=16, fontweight="bold", color=TEAL)
    ax.text(10.4, 2.85, "W2 Pages  ·  W3 Ollama\nW7 loop  ·  W8 Notebook", ha="center", fontsize=14)
    ax.text(7, 5.8, "Live labs vs take-home labs", ha="center", fontsize=17, fontweight="bold", color=BLUE)
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
        (4.95, GOLD, "5", "Local models\nare reasonable"),
        (9.55, PURPLE_WEB, "6", "AAP AI policy\nstill forthcoming"),
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
    ax.text(7.1, 5.8, "Six things to leave with", ha="center", fontsize=18, fontweight="bold", color=BLUE)
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
