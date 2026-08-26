# Claim-to-source ledger

Compilation date: **25 August 2026**.  
Companion to [`pediatric-resident-ai-survey.md`](pediatric-resident-ai-survey.md).

**Status codes**

| Code | Meaning |
|---|---|
| `retrieved` | Full page or PDF opened in this project |
| `canonical` | Standard bibliographic target; HTML may have timed out |
| `abstract-only` | Title/abstract/metadata retrieved, not full PDF |
| `secondary-only` | Used only as a pointer; do not treat as independent evidence |
| `vendor-reported` | Figure or ranking comes from the lab’s own post |
| `unverified` | Not used as a fact in the briefing |

Do not add rows for textbook ML definitions (supervised/unsupervised) unless a specific paper is cited in the briefing.

| ID | Claim (compressed) | Source | Date of source | Retrieved | Status |
|---|---|---|---|---|---|
| C01 | Transformer / self-attention architecture | Vaswani et al., NeurIPS 2017, arXiv:1706.03762 | 2017 | 25 Aug 2026 | `canonical` (also cited inside FDA 2026 paper) |
| C02 | GPT-2 unsupervised multitask learners | Radford et al., OpenAI 2019 | 2019 | — | `canonical` |
| C03 | GPT-3 175B; in-context learning | Brown et al., NeurIPS 2020, arXiv:2005.14165 | 2020 | — | `canonical` |
| C04 | InstructGPT: SFT + RLHF | Ouyang et al., NeurIPS 2022, arXiv:2203.02155 | 2022 | — | `canonical` |
| C05 | ChatGPT launch 30 Nov 2022 | OpenAI “Introducing ChatGPT” | 2022-11-30 | timeout | `canonical` |
| C06 | GPT-4 multimodal technical report | OpenAI GPT-4 report | 2023-03-14 | timeout | `canonical` |
| C07 | o1: RL on chain of thought; train-time and test-time compute | OpenAI “Learning to reason with LLMs” https://openai.com/index/learning-to-reason-with-llms/ | 2024-09 | planning corpus | `retrieved` / `canonical` |
| C08 | RLVR named in Tulu 3 | Lambert et al. 2024 | 2024 | — | `canonical` (method name) |
| C09 | MCP open-sourced; USB-C metaphor in current docs | https://www.anthropic.com/news/model-context-protocol ; https://modelcontextprotocol.io/docs/getting-started/intro | 2024-11-25; docs 2026 | 25 Aug 2026 | `retrieved` |
| C10 | Agent Skills launched; open standard Dec 2025 | https://www.anthropic.com/news/skills | 2025-10-16 / 2025-12-18 | 25 Aug 2026 | `retrieved` |
| C11 | ICMJE: disclose AI; no chatbot authors; humans accountable | https://www.icmje.org/icmje-recommendations.pdf §II.A.4 and §V | Jan 2026 update reported on secondary pages; PDF retrieved | 25 Aug 2026 | `retrieved` |
| C12 | COPE: AI cannot be author; disclose tool and use | COPE position “Authorship and AI tools” | 2023 (still cited) | timeout; corroborated via Pediatrics instructions | `canonical` |
| C13 | *Pediatrics*: AI not an author; disclose name, manufacturer, how used; cover letter + Methods/Acknowledgments | https://publications.aap.org/pediatrics/pages/author-instructions | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C14 | AAP digital-ecosystems policy 20 Jan 2026; AI forthcoming in separate statement | *Pediatrics* 157(2):e2025075320 doi:10.1542/peds.2025-075320 | 2026-01-20 | 25 Aug 2026 | `retrieved` |
| C15 | PLACES/PAS: 48% used AI at work; 39% scribes; 78% concerned about no oversight; 6% confident in pediatric-appropriate development | https://www.aap.org/en/research/pas-abstracts/us-pediatricians-experiences-with-artificial-intelligence-in-healthcare-in-2025/ | 2025 abstract | 25 Aug 2026 | `abstract-only` |
| C16 | AMA 2026 HOD: AI assistive not replacement; payer AI transparency; physician review of coverage | AMA press release dated 10 June 2026 | 2026-06-10 | 25 Aug 2026 | `retrieved` (saved PDF; HOD item numbers still not on page) |
| C17 | AMA H-480.931 reaffirmed 2026 | AMA PolicyFinder | 2026 | 25 Aug 2026 | `retrieved` |
| C18 | Bergman, Wachter, Emanuel licensure framework; six elements; HHS Office of Clinical AI Oversight | *JAMA* 2026;335(20):1751-1754 doi:10.1001/jama.2026.5483 | online 2026-04-29; print 26 May 2026 | 25 Aug 2026 | `retrieved` (full PDF; Viewpoint, not original research) |
| C19 | WHO B09667: AI complements rather than replaces judgement in EIP | WHO discussion paper doi:10.2471/B09667 | 2026 | 25 Aug 2026 | `retrieved` (full PDF) |
| C20 | FDA GenAI device discussion paper: not guidance; two-axis risk; competency-based idea; docket FDA-2026-N-7874 | Official docket attachment in `briefing/papers/` | 2026-08 | 25 Aug 2026 | `retrieved`. Comment-close 19 Oct 2026 remains docket/press metadata (not in PDF body) |
| C21 | FDA does not regulate AI as such; regulates devices | Same discussion paper §III | 2026 | 25 Aug 2026 | `retrieved` |
| C22 | FDA examples: child sore-throat triage vs chest-pain ED; insulin vs OTC hydrocortisone | Same paper §IV | 2026 | 25 Aug 2026 | `retrieved` |
| C23 | OCR tracking-technology bulletin: BAA required for tracking vendors with PHI | https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html | updated 2024; still posted | 25 Aug 2026 | `retrieved` |
| C24 | OpenAI HIPAA-eligible products are a specific list; consumer ChatGPT not on that list as eligible | https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C25 | GPT-5.6 GA 9 Jul 2026; Sol/Terra/Luna; price updates 30 Jul and 21 Aug | https://openai.com/index/gpt-5-6/ | 2026-07-09 | 25 Aug 2026 | `retrieved` `vendor-reported` for benchmarks |
| C26 | GPT-5.6 Sol vendor: Agents’ Last Exam 53.6; BrowseComp 92.2%; OSWorld 2.0 62.6% | Same | 2026-07-09 | 25 Aug 2026 | `vendor-reported` |
| C27 | Fable 5 / Mythos 5 announced 9 Jun 2026; suspended 12 Jun; restored 1 Jul; $10/$50 per MTok; Mythos restricted (Glasswing) | https://www.anthropic.com/research/claude-fable-5-mythos-5 | 2026-06-09 | 25 Aug 2026 | `retrieved` `vendor-reported` for capability claims |
| C28 | Fable classifiers fall back to Opus 4.8; <5% of sessions on average | Same | 2026-06-09 | 25 Aug 2026 | `vendor-reported` |
| C29 | Opus 5 launch 24 Jul 2026; $5/$25 per MTok; default on Max | https://www.anthropic.com/news/claude-opus-5 | 2026-07-24 | 25 Aug 2026 | `retrieved` `vendor-reported` for evals |
| C30 | Gemini 3.7 Flash 13 Aug 2026; intro $0.75/$3.75 per MTok through 31 Dec 2026 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/ | 2026-08-13 | 25 Aug 2026 | `retrieved` `vendor-reported` |
| C31 | NotebookLM renamed Gemini Notebook 16 Jul 2026; cloud computer tier-gated | https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/ | 2026-07-16 | 25 Aug 2026 | `retrieved` |
| C32 | Muse Spark introduced 8 Apr 2026; closed; multimodal; 1000+ physicians for health data curation (vendor) | https://ai.meta.com/blog/introducing-muse-spark-msl/ | 2026-04-08 | 25 Aug 2026 | `retrieved` `vendor-reported` |
| C33 | Muse Glimmer 30B Apache 2.0; distilled from Spark; ~4-bit <20 GB; local agents | https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model | 2026-08 | 25 Aug 2026 | `retrieved` |
| C34 | Kimi K3: 2.8T, 16/896 experts, 1M context; trails Fable and GPT-5.6 Sol on lab suite; weights by 27 Jul 2026; API $0.30/$3/$15 | https://www.kimi.com/blog/kimi-k3 | 2026-07 | 25 Aug 2026 | `retrieved` `vendor-reported` |
| C35 | Kimi K3 limitations: thinking-history sensitivity; excessive proactiveness | Same | 2026 | 25 Aug 2026 | `retrieved` (lab self-report) |
| C36 | DeepSeek-V4-Pro 1.6T/49B active; Flash 284B/13B; 1M context | arXiv:2606.19348 https://arxiv.org/html/2606.19348 | 2026 | 25 Aug 2026 | `retrieved` |
| C37 | Qwen 3.8-Max: 2.4T; open-weight intent “next week” from 3 Aug 2026 post | https://qwen.ai/blog/qwen3.8-max | 2026-08-03 | 25 Aug 2026 | `retrieved` (index listing) |
| C38 | Ollama `qwen3.8` 27B, 18 GB, 256K, text+image, thinking+tools | https://ollama.com/library/qwen3.8 | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C39 | Ollama can launch Claude Code, OpenCode, Hermes, OpenClaw | https://ollama.com | 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C40 | GLM-5.3 14 Aug 2026; same base as 5.2; post-training only; weights in two weeks after safety work | https://z.ai/blog/glm-5.3 | 2026-08-14 | 25 Aug 2026 | `retrieved` `vendor-reported` evals |
| C41 | GLM-5.3 vendor Terminal-Bench 3.0 4.6→28.3; CyberGym 84.5% | Same | 2026-08-14 | 25 Aug 2026 | `vendor-reported` |
| C42 | OpenEvidence partners NEJM, JAMA, Nature, Cochrane, AAP among societies; 200M consultations; HIPAA/SOC2 claims | https://www.openevidence.com/about/ | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` **vendor claims** |
| C43 | OpenEvidence SR: 11 studies to Jan 2026; PROSPERO CRD420261289103; lower fabricated citations vs general LLMs where measured (minority of studies); often reinforces decisions; no pediatric synthesis | Artsi et al. *npj Digit Med* doi:10.1038/s41746-026-03077-4 | published 2026-08-12 (accepted 26 Jul 2026) | 25 Aug 2026 | `retrieved` (article-in-press PDF) |
| C44 | “>40% of US physicians daily” | Same review: company-reported, repeated as “reportedly” | 2026 | 25 Aug 2026 | **do not treat as audited** |
| C45 | UpToDate Expert AI announced 24 Sep 2025; Enterprise Q4 2025; vendor 7,600 experts | Wolters Kluwer announcement page | 2025-09-24 | 25 Aug 2026 | `retrieved` (saved WK PDF). 6 Aug 2026 “~2,500 US hospitals” is a related vendor item on the same print |
| C46 | Claude Code: terminal/IDE agent; GitHub anthropics/claude-code | https://www.anthropic.com/product/claude-code | 2026 | 25 Aug 2026 | `retrieved` |
| C47 | Codex sandbox: OS-enforced; workspace-write default pattern; Seatbelt / bubblewrap / Windows elevated sandbox | OpenAI engineering + developers.openai.com/codex/concepts/sandboxing | 2026 | 25 Aug 2026 | `retrieved` |
| C48 | OpenClaw: personal assistant, many chat channels, Gateway, skills | https://github.com/openclaw/openclaw | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C49 | Hermes Agent: Nous Research; OpenClaw import; skills/memory | https://github.com/nousresearch/hermes-agent | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C50 | OpenCode: open-source coding agent anomalyco/opencode | https://github.com/anomalyco/opencode | accessed 25 Aug 2026 | 25 Aug 2026 | `retrieved` |
| C51 | 2024 DHAC GenAI TPLC meeting is **not** the 2026 discussion paper | FDA media/184078 vs 2026 discussion paper (DHAC exec summary cited in 2026 PDF as media/182871) | 2024 vs 2026 | 25 Aug 2026 | do not conflate |
| C52 | Generative AI SOTA review for families/pediatricians; AI is not a friend or caregiver; 72% teens used companion chatbots (via Common Sense Media 2025) | Grundmeier et al. *Pediatrics* 2026;157(4):e2025074912 | accepted 2026-01-07; issue Apr 2026 | 25 Aug 2026 | `retrieved` (full PDF). **Not AAP policy.** 72% not independently re-fetched |
| C54 | Gemma 4 family 2 Apr 2026; 31B dense is the open-weight flagship; Q4_0 ~17.5 GB on Google’s memory table | https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ and https://ai.google.dev/gemma/docs/core/model_card_4 | 2026-04-02 | 26 Aug 2026 | `retrieved` |

## Search log (this compilation)

Queries and fetches included, among others: official GPT-5.6, Fable/Mythos, Opus 5, Kimi K3, GLM-5.3, DeepSeek-V4 HTML, Qwen3.8 GitHub and qwen.ai, Muse Spark/Glimmer, Gemini 3.7 Flash, Gemini Notebook, OpenEvidence About, Artsi 2026, ICMJE PDF, Pediatrics author instructions, AAP digital ecosystems, AMA press release, WHO B09667, FDA discussion paper PDF text, MCP intro, Agent Skills, Ollama library qwen3.8, Codex sandbox posts, OpenClaw/Hermes/OpenCode GitHub, Wolters Kluwer Expert AI, HHS OCR tracking, OpenAI HIPAA help article.

**Local PDF re-read 25 Aug 2026** (`briefing/papers/`): Artsi article-in-press; Bergman *JAMA*; WHO B09667; FDA docket attachment; AMA 10 Jun 2026 press PDF; WK Expert AI page; Qwen one-page marketing shot; Grundmeier *Pediatrics* 2026;157(4):e2025074912.

**Intentionally unused as facts:** BenchLM / FelloAI / ThursdAI rankings except as discovery; OpenEvidence vs UpToDate comparison blogs; “65% of US doctors” marketing; GLM-5.3 independent cyber league tables; any invented DOI; Kenya/Pakistan/NOHARM outcome numbers as quoted by Bergman (those primary papers were not opened).

## Known holes (do not paper over)

1. OpenAI ChatGPT/GPT-4 HTML timed out; dates rest on canonical URLs.  
2. Official `fda.gov` HTML landing for the 2026 discussion paper still not fetched; docket PDF is in-repo. Comment-close date not in PDF body.  
3. UpToDate Expert AI independent pediatric trials: none retrieved.  
4. GLM-5.3 weights: not public as of 25 Aug 2026 per vendor.  
5. AMA HOD **item numbers**: still not on the 10 June 2026 press PDF.  
6. Claude Code MEMORY.md byte cap: community issues, not used as a hard number in the briefing body.  
7. AAP dedicated AI **policy**: **forthcoming**, not published in this window. Grundmeier 2026 is a review, not that policy.  
8. Common Sense Media 2025 teen-companion survey PDF (Robb and Mann): cited by Grundmeier; not opened here.  
9. `Qwen.pdf` does not contain the 2.4T / open-weight-timeline spec.
