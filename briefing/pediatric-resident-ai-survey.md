# A Survey of Modern AI for Pediatric Residents

**Research briefing for a one-hour workshop-lecture**  
McLane Children’s Hospital, pediatric residency  
Document type: source briefing (not slides). Compress into a one-hour spine later. Slide **medium**: Quarto Reveal.js as source of truth, PDF/PPTX as fail-safe — [`slides/README.md`](../slides/README.md).

**How to use this document.** This is a teaching brief, not a clinical protocol. It does not provide patient-specific medical direction. Every workshop case is **synthetic**. Claims about 2025–2026 products and policies are dated and tied to sources in [`claim-source-ledger.md`](claim-source-ledger.md). Vendor benchmark tables are **vendor-reported** unless an independent evaluation is cited. Workshop recipes that you can run from an empty folder live in [`workshops.md`](workshops.md).

---

## 0. Scope, methods, and rules of evidence

### 0.1 Audience and goal

The intended audience is pediatric residents with mixed technical literacy. Most do not pay for a frontier subscription. Most have never used an **agent harness** (a program that lets a model read files, run commands, and write artifacts, rather than only chatting). The lecture is a survey of modern machine learning and large language models, followed by live demonstrations of tools that are useful for research, teaching, and low-risk administrative work.

The one-hour live spine cannot cover this briefing. A workable compression is:

| Block | Minutes | Content |
|---|---|---|
| Foundations | 12 | Supervised vs unsupervised vs RL; neural nets; tokens; attention |
| Timeline | 10 | GPT-2 → ChatGPT → GPT-4 → closed/open split |
| Reasoning and tools | 10 | Test-time compute, RAG, harnesses, MCP, skills |
| Frontier and privacy | 8 | August 2026 map; local models; HIPAA |
| Policy | 8 | ICMJE / AAP digital ecosystems vs Grundmeier review / AMA 10 Jun 2026 / FDA / WHO; journal-policy gaps |
| Live workshops | 12 | Two from-scratch demos (Office files + grounded vs ungrounded) |
| Q&A | remainder | Handout covers the other six recipes |

### 0.2 Methods

Sources were retrieved in this order: (1) first-party lab and product posts and model cards; (2) official policy HTML/PDFs (ICMJE, COPE, AAP, AMA, FDA, WHO, HHS); (3) peer-reviewed clinical evaluations; (4) independent technical reports only when they point to a checkable primary source. Secondary blogs were used as **discovery aids**, not as sole support for a factual claim.

Retrieval date for this compilation: 25 August 2026. If a 2026 item could not be opened from the official publisher, it is labeled **unverified** or **secondary-only** rather than quoted as settled fact. After the first pass, full PDFs were added under [`papers/`](papers/README.md) and re-read the same day; ledger rows C16, C18, C19, C43, and C45 were upgraded, and Grundmeier et al. 2026 was added as C52.

### 0.3 Teaching and privacy rules (non-negotiable)

1. **No PHI in any cloud tool** that lacks an executed Business Associate Agreement covering that exact product tier. Consumer ChatGPT, consumer Claude, consumer Gemini, and most free “AI scribes” are not that.
2. **“De-identified” notes are not a loophole.** HIPAA’s safe-harbor method requires removing specified identifiers. A pasted H&P that still contains dates, unique clinical detail, or a recognizable combination is not safe-harbor de-identified.
3. **Local models remove a vendor**, not your Security Rule duties. An unmanaged personal laptop running Ollama is not automatically a compliant system of record.
4. **All live cases are synthetic** and labeled as such. Do not use tonight’s patients, even “just the assessment.”
5. **Do not copy a dose, a differential, or a citation from a model into the chart or a manuscript without independent verification.**

---

## 1. The machine-learning landscape (clinician’s map)

### 1.1 What “AI” means in 2026, and what it meant in the EHR

In clinical operations, “AI” has been used for at least three different things:

- **Rules and scores.** If-then logic, NEWS/PEWS-style early-warning scores, order sets. Some are expert-weighted. Some, including neonatal sepsis rules built by sequential splits of a dataset, are learned from data. They still emit a score or a branch, not tokens.
- **Classical machine learning.** A model is fit to labeled examples (supervised) or to unlabeled structure (unsupervised). Outputs are usually a class, a probability, or a cluster. This is the generation behind sepsis alerts, readmission risk, and many chest X-ray computer-aided detection (CAD) tools.
- **Foundation models / generative AI.** A large neural network is pretrained on broad data, then adapted. It emits **tokens** (pieces of text, code, or other symbols) rather than a single score. Large language models (LLMs) sit here.

The 2026 FDA discussion paper is explicit that FDA does not regulate “AI as such”; it regulates products that meet the statutory definition of a medical device, using a risk-based approach ([FDA CDRH 2026](#ref-fda-2026)). That distinction matters for residents: ChatGPT answering a board-style question is not an FDA-cleared device. An ambient scribe or a triage bot **might** be, depending on intended use.

### 1.2 Supervised learning

**Definition.** The training set pairs inputs \(x\) with labels \(y\). The algorithm learns a mapping \(\hat{y} = f(x)\). Clinical analogy: you show a model 50,000 chest radiographs already read by radiologists; it learns to emit “pneumonia / not pneumonia.”

**Common model families (audience-level):**

| Family | Typical job | Pediatric-adjacent example |
|---|---|---|
| Linear / logistic regression | Interpretable association, baseline risk | Adjusted odds of PICU transfer |
| Trees and random forests | Nonlinear tabular prediction | ED triage features → admission |
| Gradient boosting (XGBoost, LightGBM) | Strong tabular performance | Many EHR risk models |
| Support vector machines | High-dimensional classification | Older text/image pipelines |
| Convolutional neural nets | Images, waveforms | CXR, retinal photos, ECG |
| Recurrent nets / older sequence models | Time series (largely superseded) | Vital-sign streams |

**What “supervised” does not buy you.** Labels can be wrong (billing codes ≠ diagnoses). The population can shift (a model trained on 2019 RSV will misbehave in 2022). Performance on the training hospital may not travel. And a high AUROC is not a treatment recommendation.

### 1.3 Unsupervised learning

**Definition.** There are no labels. The algorithm finds structure: clusters, low-dimensional embeddings, density estimates, or generative models of “what data look like.”

**Common families:** k-means and hierarchical clustering; principal component analysis and other dimensionality reduction; topic models on notes; autoencoders; and, in a broad sense, the **self-supervised pretraining** that produces LLMs (the model predicts a hidden piece of its own input).

Clinical analogy: unsupervised clustering of wheeze phenotypes is a hypothesis generator. It does not tell you which cluster should get steroids.

### 1.4 Reinforcement learning (RL)

**Definition.** An agent takes actions in an environment and receives a **reward**. It learns a policy that increases expected reward. This is how some robots and game-playing systems are trained. It is also, since 2022–2025, how language models are steered after pretraining.

Two reward styles matter later:

- **RLHF (reinforcement learning from human feedback).** A preference model trained on “which answer did the rater like?” steers the LLM. This is the InstructGPT / ChatGPT-era recipe ([Ouyang et al. 2022](#ref-ouyang-2022); [OpenAI 2022](#ref-chatgpt-2022)).
- **RLVR (reinforcement learning with verifiable rewards).** The reward is an automatic check: unit tests pass, the math answer matches, the compiler succeeds. This is the reasoning-model recipe of 2024–2026 ([OpenAI 2024](#ref-o1-2024); [Lambert et al. / Tulu 3, 2024](#ref-tulu3) as the named method).

Clinical analogy: RLHF is like training a resident on attending gestalt. RLVR is like training on whether the NG tube is in the stomach on x-ray—there is a checkable fact.

### 1.5 Where this sits in a children’s hospital today

Residents already touch all three layers, usually without noticing:

- **Supervised:** radiology worklists, sepsis scores, census prediction.
- **Unsupervised / embedding:** “similar patients,” search over notes.
- **Generative:** ambient documentation, inbox draft replies, OpenEvidence-style Q&A, ChatGPT on a phone between cases.

The AAP Periodic Survey / PLACES abstract on 2025 pediatrician experience reported that 48% of respondents had used AI at work in the prior 12 months; among users, documentation was the most common frequent use, and 39% had used AI scribes. Top concern: reliance on AI without human oversight (78% concerned or very concerned). Only 6% were confident that AI tools are developed with adequate consideration of the pediatric population ([AAP PAS abstract, 2025](#ref-aap-places-2025); conference abstract, not a peer-reviewed paper). That last number is the pediatric-specific punchline of this lecture.

### 1.6 Pediatric-specific failure modes (pin this)

Adult-majority training data produce systematic, not random, errors in child health:

- **Dosing is not a small adult.** mg/kg, mg/m², postnatal age, corrected gestational age, and maximum caps all have to be right simultaneously. Token models are bad at this (see §2.3 and Workshop 6).
- **Vital-sign and lab ranges move with age.** A “normal” creatinine or heart rate copied from an adult prior is a harm event.
- **Development is a moving endpoint.** Language delay at 18 months is not the same task as at 4 years; models flatten this.
- **The historian is often not the patient.** Caregiver-by-proxy history, adolescent confidentiality, and non-accidental injury documentation have legal and ethical structure models do not reliably keep.
- **Rare disease and metabolism.** Long-tail inborn errors are exactly where next-token priors are weakest and where fluency is most seductive.
- **Devices and formulations.** Liquid concentrations, chewables vs tabs, and off-label use are messy in text.
- **Representation.** Skin findings, pulse oximetry, and language access: if the pretraining photos and notes are adult and English, the model’s “typical” is not your clinic.

None of this is an argument against using AI for **low-stakes drafting**. It is an argument against using AI as a **silent co-signer**.

---

## 2. Neural networks, attention, tokens, and why LLMs were even possible

### 2.1 Neural networks, without the mysticism

A neural network is a stack of matrix multiplications and simple nonlinearities. Each layer transforms a representation of the input. “Deep” means many layers. Training is almost always **gradient descent**: nudge millions or billions of numbers (weights) so that a loss function falls.

For images, convolutional nets dominated the 2010s. For language, the field used recurrent nets (RNNs, LSTMs) that read left to right and struggled with long-range dependencies and parallel training. That bottleneck is why **attention** mattered.

### 2.2 Attention is all you need (2017)

Vaswani and colleagues replaced recurrence with **self-attention**: every position in a sequence can look at every other position, in parallel, and mix information according to learned relevance ([Vaswani et al. 2017](#ref-vaswani-2017)). The architecture is the **Transformer**.

Clinician’s picture: attention is a soft, learned “what should I look at in this note before I write the next word?” It is not “the model is paying attention” in the human sense. It is a computational pattern.

Transformers enabled:

- **Massive parallel training** on GPUs/TPUs (no sequential RNN bottleneck).
- **Longer effective context** than vanilla RNNs of that era.
- A single architecture that later absorbed vision, audio, and tools.

The 2026 FDA glossary still points to this paper as the reference architecture for foundation models ([FDA CDRH 2026](#ref-fda-2026)).

### 2.3 What a token is

Models do not read letters or words as humans do. A **tokenizer** chops text into **tokens**: common words, subwords, punctuation, and special symbols.

Examples (illustrative, tokenizer-dependent):

- `"acetaminophen"` might be one token in a medical-heavy vocabulary, or three pieces in a general vocabulary.
- `"QTc"` might be `Q`, `Tc` or a single token.
- A space and a newline are tokens too. So is a JSON brace.

**Why this matters clinically:**

- **Numbers are fragile.** `"12.5 mg/kg"` can be split so that the model is not doing arithmetic on a single integer; it is predicting the next fragment. This is one reason dosing hallucinations are dangerous. A model that “calculates” in prose is often concatenating fragments that look like arithmetic.
- **Rare pediatric strings** (enzyme names, gene variants, brand/generic pairs) may be over-split and poorly learned.
- **Context windows** are measured in tokens, not pages. A 128,000-token window is roughly a short book, not “the entire EHR.” A 1,000,000-token window is a different product class (and is often used poorly: the model still attends unevenly; “lost in the middle” remains a research finding from 2023 onward).
- **The chat UI hides the tokenizer.** Residents think in sentences. The model thinks in pieces. When you see a weird hyphen break in a gene name, you are looking at tokenization.

Byte-pair encoding (BPE) and SentencePiece are the usual algorithms. You do not need to implement them. You do need to remember that **the unit of learning is the token**.

### 2.4 How text is learned (pretraining)

The core objective of a decoder-only LLM (GPT-style) is: **given previous tokens, predict the next token.** Do this on trillions of tokens of text (and, later, images, audio, code, and tool traces). The model is not “looking up” a sentence. It is compressing statistical structure into weights.

Implications residents should keep:

1. **Fluency is not knowledge.** The same mechanism that writes a perfect-sounding progress note can invent a PMID.
2. **The model is a prior over text**, not a database. Retrieval (RAG) and tools are how you bolt a database onto that prior.
3. **Pretraining data are not a pediatric textbook.** Children, rare disease, and non-English notes are underrepresented relative to adult internet text and GitHub.

### 2.5 Preliminaries that had to exist before LLMs

Training GPT-class models required a stack that did not exist in 2012:

- **Hardware:** large GPU/TPU clusters; high-bandwidth interconnects.
- **Software:** mixed-precision training, sharded optimizers, data loaders that can feed billions of tokens.
- **Data:** web-scale crawls, books, code, later licensed journals and synthetic traces.
- **Scaling laws:** empirical observation that loss falls predictably as you scale parameters, data, and compute together (Kaplan et al. 2020, arXiv:2001.08361; Hoffmann et al. “Chinchilla” 2022, arXiv:2203.15556; both **canonical**, not re-fetched this pass). You cannot skip data and only buy parameters.
- **Alignment layer:** unfiltered next-token models are not usable products. Instruction tuning and RLHF made ChatGPT possible.

Meta’s 2026 Muse Spark post is a current example of the same idea: they report fitting a scaling law after rebuilding the pretraining stack and claim more than an order of magnitude less compute than Llama 4 Maverick for the same capability level—**vendor-reported** ([Meta Superintelligence Labs, 8 Apr 2026](#ref-muse-spark)).

---

## 3. Timeline: GPT-2, GPT-3, ChatGPT, GPT-4, and the first arms race

Dates below are first-party or canonical paper dates. “Changed the world” claims are interpretive; the product dates are not.

### 3.1 GPT-2 (2019)

OpenAI’s GPT-2 showed that a large Transformer language model, trained unsupervised, could do many tasks without task-specific architectures ([Radford et al. 2019](#ref-gpt2)). The staged release (because of misuse concerns) was itself a preview of later safety arguments.

### 3.2 GPT-3 (2020)

GPT-3 scaled to 175 billion parameters and popularized **in-context learning**: show a few examples in the prompt, get a new task done without weight updates ([Brown et al. 2020](#ref-gpt3)). This is the ancestor of “just paste the rubric and the notes.” It is also the ancestor of prompt injection (the model cannot tell your instructions from an attacker’s text in the same context).

### 3.3 InstructGPT and ChatGPT (2022)

Raw GPT-3 was a completion engine. **InstructGPT** used supervised fine-tuning on demonstrations plus RLHF so the model followed instructions ([Ouyang et al. 2022](#ref-ouyang-2022)). **ChatGPT** launched 30 November 2022 as a conversational product on that lineage ([OpenAI 2022](#ref-chatgpt-2022)). That product, not the GPT-3 paper, is what made non-engineers care.

What changed for medicine immediately: fluent discharge instructions, fabricated citations, and a wave of “I asked ChatGPT” in morning report. The capability was real. The grounding was not.

### 3.4 GPT-4 (March 2023)

GPT-4 added multimodal input (images) and another jump in exam-style and professional benchmarks ([OpenAI 2023](#ref-gpt4)). It also made clear that **productization** (tools, browsing, plugins, later memory) would matter as much as raw scores.

### 3.5 The 2023–2024 closed-model arms race

Once ChatGPT proved demand, every large lab shipped a conversational frontier model. A resident-level map, not a complete catalog:

| Window | What happened | Why it mattered |
|---|---|---|
| Mar 2023 | GPT-4 | Multimodal, “good enough” professional text |
| 2023 | Anthropic Claude 1–2; Google Bard/Gemini start | Second and third closed vendors |
| Jul 2023 | Meta Llama 2 open weights | Serious local and open-weight ecosystem |
| Late 2023–2024 | Gemini 1.x, Claude 3, GPT-4o | Speed, voice, cheaper tokens |
| 2024 | Context windows to 128K–1M (product-dependent) | Whole-guideline prompting |
| Sep 2024 | OpenAI o1 | Reasoning / test-time compute as a product |

**Llama as the open-weight shock (2023–2025).** Meta’s Llama 2 (July 2023) made a capable 7B–70B family widely downloadable. That, more than any single paper, created the hobbyist-to-hospital-IT path: llama.cpp, Ollama, and “can we put this on a box in the data center?” Llama 3.x expanded quality; Llama 4 was Meta’s last widely discussed Llama-branded generation before the **Muse** rebrand under Meta Superintelligence Labs in 2026 (Muse Spark launch explicitly compares pretraining efficiency to Llama 4 Maverick ([Meta, 8 Apr 2026](#ref-muse-spark))). The institutional lesson: **open-weight does not mean a lab will stay open-weight forever.** Glimmer (Apache 2.0, August 2026) is a partial return of local weights after a closed flagship.

**DeepSeek-R1 (January 2025)** was the public proof that reasoning-style RL could be replicated outside OpenAI at much lower apparent cost. It accelerated every lab’s post-training stack and is why 2025–2026 launch posts talk about **effort sliders** instead of only parameter counts.

The pattern: **closed labs competed on capability and product**; **open-weight labs competed on downloadability, cost, and the right to run without a vendor**. Both matter to a resident who cannot put PHI in a consumer chatbot.

### 3.6 Prompting vs tools vs agents (a one-minute taxonomy)

| Mode | What you do | Failure mode |
|---|---|---|
| **Prompting** | Write a better question | The model still cannot see your files or the literature |
| **Tools** | Model may search, fetch, calculate | Tool output can be wrong; model can ignore it |
| **Agent / harness** | Model loops: plan → act → observe | Drift, compaction, overreach, sandbox holes |

Residents mostly live in row 1. This lecture is an invitation to row 3 for **artifacts**, not for **orders**.

---

## 4. Closed frontier vs open-weight frontier; scale; multimodality

### 4.1 Closed vs open-weight (precise language)

- **Closed / proprietary:** you call an API or a chat app. You do not get the weights. GPT-5.6, Claude Fable 5, Gemini 3.7 Flash, Muse Spark sit here.
- **Open-weight:** the parameters can be downloaded (licenses vary: Apache 2.0, MIT, custom). You still may not get training data, full code, or a license that allows medical use. Llama, Qwen, DeepSeek, Kimi K3, Muse Glimmer sit here.
- **Open source** in software’s strict sense (training code + data + weights) is rarer than marketing implies. Prefer “open-weight.”

Open-weight models created an ecosystem: Hugging Face, llama.cpp, Ollama, vLLM, SGLang, LM Studio, Unsloth, and a generation of agent harnesses that can point at localhost. That ecosystem is why “run a good model on your own hardware” is a 2026 sentence rather than a research fantasy.

### 4.2 The explosion in size—and why size stopped being the only story

Parameter counts went from millions (AlexNet) to billions (GPT-2/3) to trillions (MoE models). **Mixture-of-Experts (MoE)** is the usual trick at the high end: many expert subnetworks, few active per token. Kimi K3 is described by Moonshot as a 2.8-trillion-parameter model activating 16 of 896 experts ([Moonshot / Kimi K3, 2026](#ref-kimi-k3)). DeepSeek-V4-Pro is described as 1.6T total / 49B active ([DeepSeek-AI 2026](#ref-deepseek-v4)). Qwen 3.8-Max is described as 2.4T ([Qwen 2026](#ref-qwen38-max)).

For residents, the useful distinction is not 2.8T vs 30B. It is:

- **Frontier closed API:** best quality, data leave your device, costs money.
- **Frontier open-weight (datacenter):** downloadable but not a laptop model.
- **Local 27B–30B class:** fits a high-end GPU or unified-memory Mac; good enough for many writing and coding tasks; **not** GPT-5.6.
- **Local 8B-and-under:** fits ordinary laptops; quality drops; still useful for private brainstorming.

### 4.3 Multimodality, briefly

A **multimodal** model accepts more than text: images, audio, video, screenshots of a growth chart, a rash photo, a PDF page rendered as pixels. Muse Spark is described as natively multimodal with visual chain-of-thought ([Meta, 8 Apr 2026](#ref-muse-spark)). Muse Glimmer ships a perception encoder for interleaved text and images ([Meta, Aug 2026](#ref-muse-glimmer)). Qwen3.8-27B on Ollama is tagged vision + tools + thinking, 256K context ([Ollama library, retrieved 25 Aug 2026](#ref-ollama-qwen38)). Claude Fable 5 is described by Anthropic as state of the art on vision tasks including screenshot-to-code ([Anthropic, 9 Jun 2026 / restored 1 Jul 2026](#ref-fable-mythos)).

**Pediatric caution:** a photo of a child is PHI if it is identifiable. A screenshot of Epic is almost always PHI. Multimodality increases capability and leak surface at the same time.

---

## 5. Fine-tuning, RAG, and hallucinations

### 5.1 Fine-tuning (changing the weights)

After pretraining, labs (and some hospitals) **fine-tune**:

- **SFT (supervised fine-tuning):** show desired answers.
- **Preference / RLHF / DPO:** show which of two answers is better.
- **RLVR / agentic RL:** reward checkable outcomes (tests, tools, long-horizon tasks).
- **LoRA / QLoRA:** cheap adapters so a 27B model can be specialized on a workstation.

Fine-tuning is how a general model becomes a coding model, a “helpful assistant,” or (in principle) a specialty model. It is **not** how you should inject last week’s AAP guideline. Guidelines change; weights do not, until you retrain.

**Distillation** is the cousin: train a smaller student to match a larger teacher’s outputs (logits or traces). Muse Glimmer is explicitly distilled from Muse Spark ([Meta 2026](#ref-muse-glimmer)). GLM-5.3 is the other trick: **do not pretrain again**; spend the compute on post-training in richer environments ([Z.ai 2026](#ref-glm53)). Both are why “the 30B on your laptop” can feel closer to last year’s frontier than physics would suggest—and why it still is not this week’s API flagship.

**Decision rule for a resident project**

- Need the model to **sound like your team** or emit JSON your script expects → fine-tune or a Skill.  
- Need the model to **know a document that changed last month** → RAG / Notebook / OpenEvidence / UpToDate.  
- Need the model to **do arithmetic** → code or a spreadsheet, not prose.  
- Need **privacy** → local weights or a BAA’d enterprise product, not a free phone app.

### 5.2 RAG (retrieval-augmented generation)—not “RAGE”

**RAG** means: retrieve documents first, then generate an answer **conditioned on those documents**. The model is still an LLM. The difference is the prompt now contains evidence.

Clinical products differ in **what** they retrieve:

| Product class | Corpus | Typical failure |
|---|---|---|
| General chatbot with web search | The open web | Wrong page, outdated page, SEO junk |
| Gemini Notebook (formerly NotebookLM) | **Your** uploaded sources | Garbage in, fluent garbage out; not a BAA |
| OpenEvidence | Licensed journals / partner content | Corpus gaps; vendor claims vs independent eval |
| UpToDate Expert AI | UpToDate editorial corpus | Bound to that corpus; independent validation limited |
| Homegrown RAG over PDFs | Whatever you indexed | Bad chunking, missed tables, citation theater |

RAG **reduces** hallucination of facts that are in the retrieved text. It does **not** eliminate:

- retrieval of the wrong paper,
- confident synthesis that the paper does not support,
- leftover parametric (memorized) claims mixed with retrieved claims,
- fabricated citations if the model is allowed to “complete” the bibliography.

The 2026 *npj Digital Medicine* systematic review of OpenEvidence (article in press; full PDF in [`papers/`](papers/README.md)) found, in the 11 included studies, generally relevant cited answers and **lower fabricated-citation rates than general-purpose LLMs in studies that measured hallucination**, with weaker performance in complex scenarios and a tendency to **reinforce rather than change** decisions. The reviewers themselves flag small samples, heterogeneous methods, and a moving product. They also note that **only a minority of included studies formally assessed citation fabrication**, that **interpretive error can occur with real citations**, and that at least one specialty comparison (transcatheter tricuspid questions) favored ChatGPT-4o on “fully accurate” answers (66.7% vs 26.7%). None of the 11 studies is synthesized as pediatric ([Artsi et al. 2026](#ref-artsi-2026)). That is the right epistemic posture: promising, not proven as a standard of care.

### 5.3 Hallucinations: older chatbots vs newer tool-using models

**Older (2022–2023) chatbots.** Next-token models with no tools. Hallucinations are the default when the prompt asks for a specific fact (PMID, dose, lab cutoff). The prose is the tell: it sounds like a review article.

**Newer (2024–2026) models with tools.** The model can search, fetch a PDF, run code, and quote. **Grounded** answers get better. New failure modes appear:

- **Tool-using confabulation:** the model cites a real paper for a claim the paper does not make.
- **Harness amnesia:** long sessions compact memory and drop a constraint you stated 40 turns ago.
- **Citation laundering:** a RAG system lists real DOIs while the sentence is still wrong.
- **Fallback opacity:** Fable 5 may silently answer as Opus 4.8 on some topics ([Anthropic 2026](#ref-fable-mythos)); the user may not notice the quality drop.

FDA’s 2026 discussion paper uses **confabulations (or hallucinations) that may appear authentic to users** as a named GenAI device risk ([FDA CDRH 2026](#ref-fda-2026)). That language is useful for residents: the danger is authenticity, not sci-fi.

**Practical rule:** if the task is **look up**, use a grounded tool and click through. If the task is **draft**, use a model and rewrite. If the task is **calculate a dose**, use a calculator or a verified spreadsheet, not a paragraph of model text.

---

## 6. The reasoning paradigm: what it is, why it was a big deal, why coding came first

### 6.1 What “reasoning” means here (and what it does not)

In 2024–2026 marketing, “reasoning model” means approximately:

1. The model **spends test-time compute**—it generates a long hidden or semi-hidden chain of thought before answering.
2. That behavior was **trained with RL**, not just prompted with “think step by step.”
3. Performance **scales with thinking time** (up to a point), not only with parameter count.

OpenAI’s September 2024 o1 post states that a large-scale RL algorithm teaches the model to use chain of thought, and that performance improves with more RL (train-time compute) and more time thinking (test-time compute) ([OpenAI 2024](#ref-o1-2024)). DeepSeek-R1 (January 2025) showed that verifier-driven RL on math and code could produce similar behavior in an open-weight lineage (canonical paper: DeepSeek-AI 2025; treat as the public replication event even if you never open the PDF).

**It is not** human clinical reasoning. It does not guarantee causal inference, does not know your patient, and does not carry malpractice insurance. It **is** a search process in token space, shaped by rewards.

### 6.2 Why it was technically a big deal

Pre-2024 scaling was mostly **pretrain bigger**. Reasoning models added a second scaling axis: **think longer at inference**. That changed product design (effort sliders: low / high / max / ultra), pricing (you pay for thinking tokens), and agent design (the model can retry, backtrack, and call tools inside the thought loop).

The named training idea is **RLVR**: reward = automatic checker ([Tulu 3 / Lambert et al. 2024](#ref-tulu3); widely used thereafter). Math and **code** are the on-ramp because they have checkers. Clinical medicine mostly does not: two attendings can disagree, and the “reward” arrives years later as an outcome.

### 6.3 Why coding fine-tuning led to computer use

Once models were RL’d on repositories, unit tests, and terminals, the natural next environment was **the computer itself**: screenshots, mouse, keyboard, browser, IDE. Anthropic reports Opus 5 outperforming other models on OSWorld 2.0, a computer-use benchmark, at a given cost ([Anthropic, 24 Jul 2026](#ref-opus5)). OpenAI reports GPT-5.6 Sol at 62.6% on OSWorld 2.0 in its launch post ([OpenAI, 9 Jul 2026](#ref-gpt56)). Those numbers are **vendor-reported** and harness-dependent. The qualitative point is solid: **the model is no longer only a text box**.

For residents, “computer use” is how you get Word, Excel, and PowerPoint files without Microsoft Copilot, and how an agent can push a slide deck to GitHub. It is also how an agent can email the wrong person or `rm` a directory if the harness is too permissive.

**Why coding was the on-ramp, in one paragraph.** A unit test is a cheap, automatic attending. A compiler is a cheap, automatic pharmacist for syntax. Once labs could RL on those rewards, they had a factory for models that **operate tools**. The same factory does not exist for “was this the right antibiotic for this neonate?” That is why your 2026 frontier model is supernaturally good at writing Python and only modestly better than 2024 at being a pediatrician. Do not confuse those curves.

### 6.4 Multistep / multiturn processes: strengths and limits

**Strengths.** Decomposition; tool use; self-checks; long documents; “write the spreadsheet then audit the formulas.”

**Limits.**

- **Error compounding.** A wrong assumption at turn 2 poisons turn 20.
- **Goal drift.** The agent “helpfully” expands scope (Kimi K3’s own blog lists excessive proactiveness as a limitation ([Moonshot 2026](#ref-kimi-k3))).
- **Context compaction.** Harnesses summarize; your “never use real names” line may vanish.
- **Evaluator-in-the-loop is still you.** A 40-step agent that nobody reads is a 40-step hallucination.
- **Not a substitute for a protocol.** A multiturn “workup of fever in a neonate” is an educational toy, not a care pathway.

---

## 7. The tooling stack: harnesses, MCP, skills, orchestration

This is the section most residents have not seen. The model is the engine. The **harness** is the car.

### 7.1 Four layers (keep this diagram in your head)

1. **Model.** GPT-5.6 Sol, Claude Opus 5, Qwen3.8-27B, …
2. **Tools.** File read/write, shell, browser, calculators, PubMed, Office generators.
3. **Harness.** The loop: send context → model requests a tool → harness runs it → append result → repeat. Codex, Claude Code, Cursor, OpenCode, Hermes, OpenClaw are harnesses.
4. **Orchestration.** Multiple agents, schedulers, memory stores, permission brokers, MCP servers, skills.

ChatGPT-in-Safari is layer 1 with a thin layer 2. The surprising demos in this lecture live at layers 3–4.

### 7.2 MCP (Model Context Protocol)

Anthropic open-sourced MCP on 25 November 2024 as a standard for connecting assistants to data sources and tools, with SDKs, local server support in Claude Desktop, and a repository of example servers (Google Drive, Slack, GitHub, Postgres, Puppeteer, and others) ([Anthropic 2024](#ref-mcp-2024)). The current docs describe MCP as “USB-C for AI applications”: one protocol, many clients (Claude, ChatGPT, VS Code, Cursor, …) ([MCP documentation, retrieved 25 Aug 2026](#ref-mcp-docs)).

**Resident translation:** instead of pasting a PDF into chat, you attach a **PubMed server**, a **folder of guidelines**, or an **Office-file server**. The model calls tools through a standard plug.

**Limits:** each MCP server is a new attack surface (a malicious server can exfiltrate whatever the harness will send). Hospital IT will not love a random GitHub MCP pointed at a shared drive. Treat MCP like a USB port on a crash cart: useful, and not something you plug into from a stranger’s cable.

**Orchestration** is the layer above one agent: multiple workers, a scheduler (cron), shared memory files (`AGENTS.md`, `SOUL.md`, `MEMORY.md` in OpenClaw/Hermes-style workspaces), and permission brokers. This is how “personal assistants” such as OpenClaw persist across WhatsApp and a laptop ([OpenClaw README](#ref-openclaw)). It is also how **shadow IT** appears in a residency: a well-meaning intern runs a gateway that can read email. Do not do that on a hospital mailbox.

### 7.3 Skills

Anthropic launched **Agent Skills** on 16 October 2025: folders containing instructions, scripts, and resources that the model loads when relevant. Skills are composable, portable across Claude apps / Claude Code / API, and can include executable code (for example, real Excel formulas rather than hallucinated ones). A December 2025 update published Agent Skills as an open standard ([Anthropic 2025](#ref-skills-2025)). The same `SKILL.md` pattern now shows up in OpenClaw, Hermes, and other harnesses (first-party GitHub READMEs describe SKILL.md workspaces; treat cross-product “40+ agents” counts as secondary).

**Resident translation:** a skill is a reusable playbook—“how we format a journal-club deck,” “how we audit a dosing spreadsheet”—not a clever prompt you retype.

### 7.4 Current harnesses (as of 25 August 2026)

Facts below are from first-party pages unless marked otherwise. Rankings are not included; they rot weekly.

**Claude Code (Anthropic).** Agentic coding tool that reads a codebase, edits files, runs commands, and handles git from the terminal, IDE, desktop, web, GitHub, and Slack ([Anthropic product page; GitHub `anthropics/claude-code`](#ref-claude-code)). Typical requirement: Claude subscription or API. Limits relevant to long work: file-based memory with documented truncation behavior in community issue trackers (treat the exact 25 KB / 200-line cap as **implementation detail**, verify against current docs before teaching the number). Permission model is prompt-and-deny rather than OS-enforced sandbox by default.

**Codex (OpenAI).** Local software agent (CLI, IDE, ChatGPT desktop) with an explicit **sandbox**: spawned commands inherit filesystem and network boundaries. Default-ish low-friction mode is workspace-write without internet unless enabled. Isolation uses OS facilities (Seatbelt on macOS; bubblewrap/seccomp on Linux; a custom elevated sandbox on Windows) ([OpenAI Codex sandbox docs; OpenAI engineering posts](#ref-codex-sandbox)). This is the harness to show when the teaching point is **containment**.

**Cursor.** AI-native IDE (fork of VS Code) used heavily for agentic coding; Fable 5 and GPT-5.6 launch posts both quote CursorBench / Cursor leadership ([Anthropic 2026](#ref-fable-mythos); [OpenAI 2026](#ref-gpt56)). For residents: Cursor is a **paid harness** most will not have. The conceptual lesson transfers to free OpenCode.

**OpenCode.** Open-source coding agent (`anomalyco/opencode` on GitHub; large public star count as of retrieval). Ollama’s homepage lists `ollama launch opencode --model qwen3.8` as a first-class launch path ([Ollama 2026](#ref-ollama)). Point: model-agnostic harness, including local models.

**OpenClaw.** Personal assistant that runs on your devices and meets you in existing chat channels (WhatsApp, Telegram, Slack, Discord, iMessage, many others), with a Gateway, skills, plugins, and ClawHub ([GitHub `openclaw/openclaw`; homepage openclaw.ai](#ref-openclaw)). Built for a **single operator**. Limits: you now have a long-running agent with messaging-channel credentials—powerful and easy to misconfigure. Not a hospital-approved PHI pathway.

**Hermes Agent (Nous Research).** Python agent with a learning loop, memories, skills, messaging channels, and an OpenClaw import path ([GitHub `nousresearch/hermes-agent`](#ref-hermes)). Ollama lists `ollama launch hermes --model qwen3.8`. Limits: self-improving skills are a supply-chain question (what did the agent just install?).

### 7.5 Why consider modern tooling at all?

Because the job of a resident is **artifact production under time pressure**: slide decks, Excel trackers, letters, journal-club notes, IRB drafts, abstracts. Chatbots produce text. Harnesses produce **files**. Files can be audited, versioned, and submitted. That is the entire pedagogical point of Workshops 1, 2, and 7.

### 7.6 Strengths and limitations of the stack (summary)

| Strength | Matching limitation |
|---|---|
| Tools ground the model in files and data | Tools can be wrong, slow, or malicious |
| MCP standardizes plugs | Every plug is a permission decision |
| Skills capture local procedure | Skills execute code; install only from trusted sources ([Anthropic 2025](#ref-skills-2025)) |
| Sandboxes (Codex) constrain blast radius | MCP and “full access” modes punch holes |
| Multistep agents finish bigger jobs | Compaction, drift, and silent truncation |
| Local models + harnesses avoid a BAA | Hardware, quality, and unmanaged-device risk |

---

## 8. Benchmarking: in-sample vs out-of-sample, and why MedQA is not a sick child

### 8.1 The resident’s statistics intuition, reused

You already know the difference between **training performance** and **test performance**, and between **internal** and **external** validation. LLM leaderboards violate those instincts constantly.

- **In-sample / contaminated evals.** If the test questions (USMLE-style items, GitHub issues, “Humanity’s Last Exam” items) appeared in pretraining or in fine-tuning, the score is memorization plus reasoning, in unknown proportion.
- **Out-of-sample.** A private, continuously refreshed exam (CursorBench, a hospital’s own chart-review set, Z.ai’s unpublished Code Bench) is closer to a true test—and is also **uninspectable**, so you must trust the vendor.
- **Harness-dependent scores.** Kimi K3’s own footnotes state that coding numbers were obtained under Kimi Code, Claude Code, or Codex depending on the row, and that other labs’ numbers were taken from those labs’ blogs ([Moonshot 2026](#ref-kimi-k3)). **Comparing “88.2 vs 88.8 on Terminal-Bench” across press releases is not a meta-analysis.**

### 8.2 What current evals actually measure

| Eval family | What it is | What it is not |
|---|---|---|
| GPQA, HLE, FrontierMath | Hard closed-ended questions | Clinical judgment at the bedside |
| SWE-Bench, DeepSWE, Terminal-Bench | Can the agent patch a repo / use a terminal? | Can you care for a neonate |
| OSWorld, computer-use suites | Can the agent operate a desktop? | Safe to let it into Epic |
| BrowseComp | Agentic web research | Evidence-based medicine |
| MedQA / NEJM CPC-style | Exam items, often leaked | A child in front of you |
| GDPval / “knowledge work” | Slides, spreadsheets, memos | A peer-reviewed paper |

OpenAI, Anthropic, Google, Moonshot, and Z.ai all lead with these numbers in 2026 launch posts. Teach residents to ask: **Was this independent? Was the harness disclosed? Was the split frozen before training? Does the construct match the clinical job?**

### 8.3 Clinical LLM evaluation is still immature

The OpenEvidence review is a microcosm: 11 studies, heterogeneous methods, a product that changes under you, strongest on guideline-like questions, weaker on complex cases ([Artsi et al. 2026](#ref-artsi-2026)). That is the state of the field, not a knock on one vendor.

FDA’s discussion paper goes further: bounded input/output testing may be **impractical** for open-ended GenAI devices; CDRH is considering competency-style benchmarking plus clinical confirmation, possibly without a prospective trial in every case ([FDA CDRH 2026](#ref-fda-2026)). If the regulator of devices is still asking how to test these systems, a residency program should not treat a leaderboard screenshot as privileging.

**Pediatric-specific hole:** adult-majority training data, weight-based dosing, developmental stages, caregiver-by-proxy consent, and rare disease. The AAP PAS abstract’s “6% confident in pediatric-appropriate development” is the prior you should carry ([AAP 2025](#ref-aap-places-2025)).

---

## 9. Frontier map (as of 25 August 2026)

**Rule for this section:** launch-post numbers are the lab’s own. Independent indices exist and disagree with each other and with vendors. Do not memorize Elo points. Memorize **access class**, **cost class**, and **whether weights ship**.

### 9.1 Closed frontier

**GPT-5.6 family (OpenAI, general availability 9 July 2026).** Flagship **Sol**, balanced **Terra**, cost-efficient **Luna**. Launch post emphasizes performance per dollar, coding-agent scores, BrowseComp, OSWorld, document/slide generation, programmatic tool calling, and an `ultra` setting that coordinates multiple agents. Safeguards described as layered (model + real-time checks + access calibration). Subsequent price cuts announced 30 July (Luna, Terra) and 21 August (Sol) ([OpenAI 2026](#ref-gpt56)). **Access:** ChatGPT / API; not open-weight. **HIPAA:** only listed HIPAA-eligible OpenAI products with a BAA, not consumer ChatGPT ([OpenAI Help Center](#ref-openai-hipaa)).

**Claude Fable 5 and Claude Mythos 5 (Anthropic, announced 9 June 2026; access suspended 12 June; restored 1 July 2026).** Fable 5 is described as a Mythos-class model made safe for general use, with conservative classifiers that sometimes fall back to Opus 4.8 (Anthropic: on average in fewer than 5% of sessions). Mythos 5 is the same underlying model with some safeguards lifted, initially for Project Glasswing cyberdefenders with the US government; Anthropic claims strongest cybersecurity capabilities of any model. Price stated at $10 / $50 per million input/output tokens ([Anthropic 2026](#ref-fable-mythos)). **Access:** Fable generally available; Mythos restricted. **Do not tell residents to “just use Mythos.”**

**Claude Opus 5 (Anthropic, 24 July 2026).** Positioned as near-Fable intelligence at half the price ($5 / $25 per million tokens, same as Opus 4.8); default on Claude Max; strongest on Claude Pro. Vendor claims SOTA on Frontier-Bench and GDPval-AA, strong computer use (OSWorld 2.0), improved life-sciences internal evals, and **no data-retention requirements for general access** (unlike some Fable constraints). Cyber classifiers are less restrictive than Fable’s; biology-blocked Fable requests now route to Opus 5 ([Anthropic 2026](#ref-opus5)).

**Gemini (Google).** Workhorse line moved fast in mid-2026: **3.6 Flash** (21 July 2026) then **3.7 Flash** (13 August 2026), the latter described as the most intelligent Flash workhorse for coding and agents, introductory price $0.75 / $3.75 per million tokens through 31 December 2026 ([Google 2026](#ref-gemini-37)). Gemini Spark (personal agent for Pro/Ultra) switched to 3.7 Flash the same day. **Gemini Notebook** is the 16 July 2026 rename of NotebookLM, with a secure cloud computer rolling out first to Ultra / certain Workspace tiers ([Google 2026](#ref-gemini-notebook)).

**Muse Spark (Meta Superintelligence Labs, 8 April 2026).** Closed, natively multimodal reasoning model with tool use, visual chain of thought, and multi-agent “Contemplating mode.” Available at meta.ai / Meta AI app; API was a private then public preview in later 1.1 notes. Meta reports health-reasoning collaboration with over 1,000 physicians for training data curation—**vendor-described, not an independent trial** ([Meta 2026](#ref-muse-spark)). Muse Spark **weights are not public**.

### 9.2 Open-weight frontier

**Kimi K3 (Moonshot).** 2.8T-parameter MoE, native vision, 1M-token context; described as the first open 3T-class model. Moonshot says overall performance still trails Fable 5 and GPT-5.6 Sol but outperforms other tested models on their suite. API pricing stated at $0.30 cache-hit / $3.00 cache-miss input and $15.00 output per million tokens. Full weights promised by 27 July 2026 ([Moonshot 2026](#ref-kimi-k3)). Limitations listed by the lab itself: sensitivity to missing thinking history; excessive proactiveness; UX gap vs Fable and Sol.

**DeepSeek V4.** Technical report describes V4-Pro (1.6T / 49B active) and V4-Flash (284B / 13B active), both with 1M-token context and hybrid compressed attention ([DeepSeek-AI 2026](#ref-deepseek-v4)). Later product posts describe MIT open weights and GA checkpoints in July–August 2026; treat checkpoint dates as **verify-on-Hugging-Face** at lecture time.

**Qwen 3.8.** Two layers: **Qwen 3.8-Max**, described 3 August 2026 as a 2.4T Max-class model with open weights to follow ([Qwen 2026](#ref-qwen38-max)); and **Qwen3.8-27B**, the laptop-relevant dense (or dense-class) model. Ollama’s library lists `qwen3.8` / `qwen3.8:27b` as an 18 GB, 256K-context, text+image build with thinking and tools, and one-command launch into Claude Code, OpenCode, Hermes, and OpenClaw ([Ollama](#ref-ollama-qwen38)). GitHub org `QwenLM/Qwen3.8` exists as the series repo ([QwenLM 2026](#ref-qwen38-gh)).

**Muse Glimmer 30B (Meta Superintelligence Labs, August 2026).** Open weights under Apache 2.0. Distilled from Muse Spark (logit distillation → mid-training → SFT + on-policy distillation + RL). Designed for always-on **local** agents; 4-bit quantization to under 20 GB so a 24/32 GB GPU (or high-end Mac) can hold weights + KV cache + perception encoder + drafter. Ships a DFlash speculative-decoding drafter. Documented partners for local run: Ollama, LM Studio, Unsloth, llama.cpp, MLX, ExecuTorch, vLLM, SGLang ([Meta 2026](#ref-muse-glimmer)).

**GLM-5.3 (Z.ai, 14 August 2026).** Same base as GLM-5.2; **all gains from post-training**. Vendor claims large jumps on Terminal-Bench 3.0 (4.6 → 28.3) and DeepSWE, plus emergent cyber capability (CyberGym 84.5%, vendor table). **Open weights “in two weeks after launch, once safety evaluation and hardening are complete.”** As of 25 August 2026 that window is still open: **do not teach GLM-5.3 as a downloadable local model yet** ([Z.ai 2026](#ref-glm53)). Hugging Face listed as “coming soon” on the launch post.

### 9.3 How to present this in 8 minutes

Draw three boxes: **closed API**, **open datacenter**, **open laptop**. Place Sol / Fable / Opus 5 / Gemini 3.7 / Muse Spark in the first; Kimi K3 / DeepSeek V4 / Qwen-Max / (soon) GLM-5.3 in the second; Qwen3.8-27B / Muse Glimmer / smaller Qwen and Gemma-class models in the third. Then say: **your unpaid phone uses box 1 without a BAA; your research laptop can use box 3; the hospital EHR, if anything, will someday be a governed version of box 1.**

---

## 10. Domain-specific tools, local models, and privacy

### 10.1 OpenEvidence

**What the company says.** OpenEvidence is an AI copilot for verified US clinicians, official AI partner of NEJM, JAMA Network, Nature Portfolio, Cochrane, and others, with society partnerships including AAP, ACC, ADA, AAFP, ACOG, ACEP, NCCN, and more. It claims to be the most widely used medical AI among verified US clinicians, “over 200 million” consultations, HIPAA compliant and SOC 2 Type II, free for healthcare professionals ([OpenEvidence About, retrieved 25 Aug 2026](#ref-oe-about)). Access is gated (NPI / professional verification in US practice).

**What independent literature says.** Artsi et al. (accepted 26 July 2026; published 12 August 2026; article-in-press PDF re-read 25 August 2026) systematically reviewed peer-reviewed evaluations from inception through January 2026 (PROSPERO CRD420261289103): **11 studies**, 15–130 questions each, mixed designs (cross-sectional comparators 4/11, guideline benchmarking 3/11, vignette 2/11, retrospective 2/11). Findings: generally relevant, evidence-supported answers; lower fabricated-citation rates than general LLMs **where measured** (a minority of studies); strongest on guideline-based questions (some reports >80% accuracy in those narrow sets); variable in complex scenarios; often **reinforces rather than alters** decisions; evidence limited by heterogeneity, small samples, expert-judgment endpoints rather than patient outcomes, and product drift ([Artsi et al. 2026](#ref-artsi-2026)). Counterexample worth a slide: Hajj et al. (inside that review) reported ChatGPT-4o fully accurate more often than OpenEvidence on 15 transcatheter tricuspid questions (66.7% vs 26.7%). Low et al. reported clinically relevant answers for 48% of evidence-available questions vs <5% for general-purpose models—do not generalize that 48% beyond that 50-question set. The “used daily by over 40% of US physicians” figure is **company-reported**, repeated as “reportedly” in the review; do not present it as an audited market-share study. **No included study is pediatric.** Evidence grounding is not the same as clinical correctness.

**How to use it as a resident.** Fast literature-grounded Q&A at the point of curiosity. Click every citation. Do not paste identifiers. It is not UpToDate, not a protocol, not a consultant.

### 10.2 UpToDate Expert AI

Wolters Kluwer announced UpToDate Expert AI on **24 September 2025**: generative answers grounded in UpToDate’s expert-authored, peer-reviewed content, with click-through to assumptions, source topic, and step-by-step rationale. Vendor copy: Clinical Intelligence “emulating how expert clinicians reason,” drawing on **7,600** medical experts (WK figure). Initial availability: select UpToDate Enterprise Edition customers in Q4 2025 ([Wolters Kluwer 2025](#ref-utd-ai)). A later WK press item dated **6 August 2026**, linked from the same saved page, claims Expert AI adoption “reaching approximately 2,500 U.S. hospitals and health systems” plus AI drug-dosing content—**vendor claims, not an independent trial**.

**Contrast with OpenEvidence.** UpToDate is an **editorial corpus** with human authors and institutional contracts many children’s hospitals already pay for. OpenEvidence is a **licensed-literature RAG product** that is free at the point of use for verified US clinicians and ad-supported in vendor descriptions (ad-funding details are secondary; do not over-claim). A reasonable resident heuristic: OpenEvidence for “what did the journals say recently?”; UpToDate for “what does our standard reference currently recommend?”; neither for “what should I do for this patient without looking.”

Independent, pediatric-specific, prospective trials of Expert AI were **not retrieved** for this briefing. Absence of evidence is not evidence of absence; it is a gap.

### 10.3 Other clinical AI you will be asked about

Ambient **scribes**, inbox drafting, and radiology/pathology assistive devices are a different regulatory class (closer to FDA-cleared SaMD when they diagnose or drive orders). This lecture does not certify any of them. If your hospital deploys one, the questions are: intended use, BAA, pediatric validation, how to override, and who is liable.

Scribes are where most pediatricians already are, according to the 2025 PAS abstract ([AAP 2025](#ref-aap-places-2025)). The failure mode is not “the note is ugly.” It is **fluent omission** (the model never heard the social history you took in the hallway) and **fluent commission** (it adds a ROS you did not perform). Sign notes as if a tired intern drafted them—because something like that did.

### 10.4 Local models: quality, roles, hardware honesty

**Ollama** is the lowest-friction local runtime for many clinicians: install, `ollama run qwen3.8`, optional launch into OpenCode / Hermes / OpenClaw / Claude Code ([Ollama](#ref-ollama)). Alternatives: **LM Studio** (GUI), **llama.cpp** (metal/CUDA, GGUF), **vLLM / SGLang** (server), **MLX** (Apple). Hugging Face is the weight warehouse, not the app.

**Qwen3.8-27B (Ollama default `qwen3.8`).** 18 GB download in the library listing, 256K context, text+image, thinking on by default ([Ollama](#ref-ollama-qwen38)). This is the “best currently convenient local” candidate for a well-equipped demo machine.

**Muse Glimmer 30B.** Apache 2.0, agent-oriented, image+text, designed for 24/32 GB envelopes after 4-bit quantization ([Meta 2026](#ref-muse-glimmer)). Overlaps Qwen3.8-27B’s hardware class.

**What most residents actually own.** 8–16 GB RAM Windows laptops, no discrete GPU. Those machines can run **8B-class** GGUF models slowly, not 27B at 4-bit. **Do not oversell.** The teaching point is: *a private, offline model exists and is surprisingly good for drafting and coding*; *it is not the closed frontier*; *your ThinkPad is not a 32 GB Mac Studio*.

### 10.5 HIPAA, BAAs, and “zero HIPAA concerns”

The last phrase in the planning prompt is **too strong**. Tighten it for the lecture:

- **Consumer ChatGPT / Claude / Gemini:** generally **no BAA**. Putting PHI there is an impermissible disclosure (45 CFR 164.502(e), 164.504(e); [HHS business-associate framing](#ref-hhs-ba); [OpenAI HIPAA-eligible products list](#ref-openai-hipaa)).
- **OpenAI HIPAA-eligible products** (as listed by OpenAI) include specific ChatGPT-for-healthcare / enterprise regulated workspace offerings and API with Modified Retention, **after** a BAA. Codex Local is covered only in those account conditions ([OpenAI Help](#ref-openai-hipaa)).
- **Fully offline local inference** on a device you control, with no telemetry, means **no vendor BA**. It does **not** mean HIPAA does not apply: the laptop is still a workstation that can store ePHI, get stolen, and sync to iCloud.
- **OpenEvidence’s “HIPAA compliant” badge** is a vendor claim on their About page ([OpenEvidence](#ref-oe-about)). It is not a reason to paste full identifiers into a phone on public Wi-Fi.

HHS OCR’s tracking-technology bulletin remains relevant: pixels and SDKs on covered-entity websites can disclose ePHI to vendors without a BAA ([HHS OCR](#ref-ocr-tracking)). Residents building “helpful” web tools should not embed analytics on pages that handle patient stories.

---

## 11. Organization and individual statements since January 2026, and the limits of journal AI policy

Salience here means: **does a pediatric resident need to change behavior this month?** Scale: high / medium / low, with a one-line reason. Full ledger rows are in [`claim-source-ledger.md`](claim-source-ledger.md).

### 11.1 Salience table (January–August 2026)

| Date | Statement | Who | What it actually says (compressed) | Salience for residents | Notes |
|---|---|---|---|---|---|
| 20 Jan 2026 | *Digital Ecosystems, Children, and Adolescents* policy statement | AAP, *Pediatrics* | Updates media/digital-ecosystem guidance; **explicitly defers a dedicated AI policy statement** as forthcoming ([AAP 2026](#ref-aap-digital-2026)) | **High** as context: AAP knows AI is reshaping childhood and has **not** yet issued the AI-specific clinical policy | Do not invent an AAP “AI in pediatric practice” guideline that does not exist |
| Apr 2026 | *Generative Artificial Intelligence: Implications for Families and Pediatricians* | Grundmeier, Fiks, Jenssen, Proctor, Ferro, Johnson (CHOP Section of Informatics), *Pediatrics* | SOTA review: generative AI is a **tool**, not a friend or caregiver; 72% of US adolescents have used AI chatbots as companions (Grundmeier citing Common Sense Media, July 2025); counsel supervision, AI literacy, and review of AI-generated materials before recommending them; health-AI regulation still does not specifically consider pediatric care ([Grundmeier et al. 2026](#ref-grundmeier-2026)) | **High** for well-child counseling and “my teen has a chatbot friend” | **Not AAP policy.** Authors disclosed genAI for organization/grammar. The 72% figure was not independently re-fetched from the Common Sense PDF |
| Jan 2026 (Recommendations update) | ICMJE Recommendations, including §II.A.4 and §V on AI | ICMJE | Disclose AI-assisted technology in cover letter and manuscript; chatbots **cannot be authors**; humans accountable; review for error/bias/plagiarism ([ICMJE](#ref-icmje)) | **High** for any abstract, case report, or QI manuscript | *Pediatrics* author instructions implement the same logic ([AAP *Pediatrics*](#ref-pediatrics-ai)) |
| Standing (2023; still operative) | Authorship and AI tools | COPE | AI tools cannot be authors; disclose tool and how used; authors liable for ethics breaches ([COPE](#ref-cope-ai)) | **High** (same operational content as ICMJE) | Position statement, not a 2026 rewrite |
| 29 Apr 2026 (print 26 May 2026) | *A Licensure Framework for Autonomous Clinical AI* | Bergman, Wachter, Emanuel, *JAMA* 335(20):1751–1754 | Viewpoint: autonomous clinical AI (care determinations **without per-case clinician review**) should be licensed more like a clinician than cleared like a static device; six elements (exams, supervised deployment, scope, time-limited recertification, layered accountability, federal competency preemption with state scope); propose an HHS **Office of Clinical AI Oversight** ([JAMA 2026](#ref-bergman-2026)) | **Medium**: conceptual; not law | Full PDF retrieved. Do not import their cited Kenya/Pakistan/NOHARM studies as independently verified here |
| **10 Jun 2026** | HOD policies on AI as assistive, physician oversight, payer AI | AMA | AI must not replace physician judgment; oppose autonomous/semiautonomous AI as a substitute for physician review in coverage determinations; demand transparency of logic/data/guidelines; audits when models or guidelines change ([AMA 2026](#ref-ama-2026)) | **High** for prior-auth and “the insurance bot denied it” | Press-release date now confirmed on the saved AMA PDF. Exact HOD item numbers still belong on PolicyFinder when slides are built |
| AMA Policy H-480.931 | Assessing the intersection of AI and health care | AMA | Reaffirmed 2026: ethical, equitable, evidence-based AI; national governance; do not adopt tools beyond the practice’s ability to mitigate risk ([AMA PolicyFinder](#ref-ama-h480)) | **Medium** | Broader than the new HOD payer items |
| 2026 (WHO ref. B09667) | *Artificial intelligence and evidence-informed policy* discussion paper | WHO | AI can speed evidence use across the EIP cycle; **complements rather than replaces human judgement**; risks include opacity, bias, equity, privacy, cybersecurity, regulatory gaps; practical line is living evidence + human-in-the-loop ([WHO](#ref-who-b09667)) | **Low–medium** for daily resident work; useful for “why governance lags capability” | Full PDF retrieved. Discussion paper for **policy-makers**, not a pediatric practice guideline |
| 18 Aug 2026 | *Considerations for the Regulation of Generative AI-Enabled Medical Devices* | FDA CDRH / DHCoE | **Not guidance.** Two-axis risk heuristic (device activity × consequence of error); competency-based premarket idea (benchmarking + clinical confirmation); postmarket monitoring; 26 discussion questions; comments to docket **FDA-2026-N-7874** through **19 Oct 2026** ([FDA CDRH 2026](#ref-fda-2026)) | **High** intellectually; **low** as a current clearance checklist | General-purpose chatbots are **not** devices merely because a doctor uses them; intended use matters. Pediatric examples in the paper include care-escalation for a child with sore throat vs chest-pain ED advice |
| 16 Jul 2026 | NotebookLM → Gemini Notebook | Google | Same product, ecosystem integration, secure cloud computer for some tiers ([Google 2026](#ref-gemini-notebook)) | **Medium** as a research tool; **not** a policy statement | Privacy: Google’s “we don’t train on uploads” ≠ hospital BAA |

**Still not retrieved: a 2026 AAP clinical AI *policy statement*.** Grundmeier et al. (*Pediatrics*, April 2026) is a CHOP informatics **state-of-the-art review**, useful for counseling families, and is **not** that forthcoming AAP policy. AAP also maintains an AI-in-pediatric-health-care resource page and an asynchronous course *Introduction to AI for Everyday Care* (shopAAP; June 2026 launch in search snippets). Those are education, not a policy statement. The digital-ecosystems paper remains the 2026 AAP policy that **names** AI and postpones the dedicated statement.

### 11.2 What journal and organizational policies still fail to do

Current medical-journal AI policy is, in practice, a **disclosure regime**:

- Name the tool and manufacturer.
- Say what you used it for (writing vs analysis vs figures).
- Promise you checked the output.
- Do not list the model as an author.

That is necessary and insufficient.

**Gap 1 — Disclosure theater.** A sentence “ChatGPT was used to improve grammar” does not tell a reviewer whether the systematic search, the statistics, or the figures were model-generated. Journals rarely require **prompts, logs, or version hashes**.

**Gap 2 — No shared evaluation.** ICMJE tells authors to watch for incorrect, incomplete, or biased output. It does not require a methods standard for *how* that check was done (spot-check? independent re-analysis? citation-by-citation PMID verification?).

**Gap 3 — Reviewer and editor AI is under-specified in practice.** ICMJE has sections on reviewer/editor use (Recommendations §V). Enforcement and logging vary by journal. A resident peer-reviewing for a local QI booklet has no template.

**Gap 4 — Pediatric underrepresentation is not a disclosure item.** You can comply perfectly with *Pediatrics* AI authorship rules and still publish a model-written paragraph that assumes adult creatinine cutoffs.

**Gap 5 — Tools moved from “writing assistance” to “agents that run code and fabricate files.”** 2023 COPE/ICMJE language still talks like chatbots. 2026 agents write spreadsheets with wrong formulas. Policy has not caught the harness.

**Gap 6 — Payer and documentation AI.** AMA 2026 HOD language on coverage determinations is the rare policy that names **power** (denials), not just manuscripts. Residents feel this before they feel ICMJE.

**Gap 7 — Forthcoming AAP AI statement.** Until it exists, residents should not treat social-media summaries of “AAP says X about ChatGPT” as policy. Grundmeier et al. 2026 is citable **guidance-shaped review**, not AAP policy. Use ICMJE + local GME/hospital rules + “no PHI in consumer tools.”

**Gap 8 — Education vs operations.** GME offices often have no AI curriculum while the hospital has a scribe vendor and the residents have ChatGPT on their phones. This lecture is a patch, not a policy. Ask who at McLane / Baylor Scott & White owns: (a) ambient documentation, (b) acceptable use on personal devices, (c) research-IRB language for LLM-assisted abstraction.

**What a *good* journal policy would add (proposal, labeled as such).** Versioned tool names; whether retrieval was used; whether any number or citation was not independently verified; data-flow (local vs cloud); and a pediatric-specific attestment when the topic is child health. That is **not** current ICMJE. It is what this briefing recommends you do anyway for your own QI and case reports.

### 11.3 Individual statements worth a slide

Bergman, Wachter, and Emanuel (*JAMA*, online 29 April 2026; print 26 May 2026) are the highest-profile **individual** 2026 argument that **autonomous** clinical AI—care determinations without per-case review—should be licensed more like a clinician than cleared like a static device ([Bergman et al. 2026](#ref-bergman-2026)). They specify six elements and an HHS Office of Clinical AI Oversight. They cite workforce shortfall, state-law fragmentation (≥47 states, >250 bills, in their telling), and a December 2025 executive order on preemption; those supporting citations were **not** re-fetched here. Patel and Blumenthal’s competency-regulation argument is cited alongside it in the FDA paper ([FDA CDRH 2026](#ref-fda-2026)). These are **opinions in major journals**, not statutes. Salience: they explain why the FDA discussion paper sounds like medical education (benchmarks, then supervised practice, then ongoing assessment). For residents, the operational line is still AMA 10 June 2026: assistive, not replacement, especially for payer denials.

---

## 12. Workshop catalog (overview)

Eight from-scratch demos. Full copy-paste recipes, timing, HIPAA posture, and intentional failure modes: [`workshops.md`](workshops.md).

Design rule: **presenter-led sophisticated run** plus a **free path** a resident can repeat without a subscription. Empty folder at t = 0. Synthetic cases only.

| # | Demo | Surprising artifact | Teaching point |
|---|---|---|---|
| 1 | Office files without Office | `.docx` + `.xlsx` + `.pptx` from a harness | Chatbots talk; harnesses emit files |
| 2 | GitHub Pages journal club | Live Reveal.js URL, no manual coding | Versioned teaching materials |
| 3 | Air-gapped local model | Offline summary of a synthetic H&P | Vendor-free path; hardware honesty |
| 4 | Same question, three systems | Fabricated vs grounded citations | RAG is a corpus choice |
| 5 | Citation autopsy | PMIDs that do not exist or do not match | Fluent bibliographies lie |
| 6 | Dosing spreadsheet audit | Excel that looks official and is wrong | Never copy a dose from a model |
| 7 | Harness vs chatbot | Working repo vs stuck paste | The loop is the product |
| 8 | Gemini Notebook | Source-grounded Q&A + optional overview | Research notebook ≠ BAA |

Live hour: run **1**, **6**, **4**, and **5**. Hand out 2, 3, 7, and 8.

Optional ninth (2 minutes): ICMJE/*Pediatrics* disclosure quiz on a dummy manuscript.

### 12.1 Other tools worth 90 seconds in the lecture

- **Gemini Notebook** (Workshop 8): best free-ish grounded notebook for **your** PDFs.  
- **PubMed / PMC + a harness file tool:** still the honest literature workflow.  
- **Zotero or Paperpile + export:** do not let the model be your only library.  
- **Observable / GitHub Pages:** interactive teaching, not just slides.  
- **Hospital UpToDate / Lexicomp / Micromedex:** still the dose source of record.  
- **Enterprise Copilot / Epic tools:** only if your institution contracted them; they are not this lecture’s free path.

### 12.2 When not to use a model (say this out loud)

- Any **weight-based dose** you will give.
- Any **rare metabolic / gene / enzyme** question without a primary source open.
- Any **safeguarding / non-accidental injury** documentation (too high-stakes, too easy to editorialize).
- Any **real patient identifier** in a consumer tool.
- Any **citation** you have not opened.
- Any **email to a family** you have not rewritten in your own voice.

---

## Glossary

**Agent.** A model plus a loop that can use tools and take sequential actions.

**BAA (Business Associate Agreement).** HIPAA contract required before a vendor creates, receives, maintains, or transmits PHI on a covered entity’s behalf.

**Context window.** Maximum tokens the model can consider at once.

**Foundation model.** Broadly pretrained model adapted to many tasks (FDA glossary language in [FDA CDRH 2026](#ref-fda-2026)).

**Harness.** Software that implements the agent loop, permissions, and tool execution.

**MCP.** Open standard for connecting AI apps to tools and data ([Anthropic 2024](#ref-mcp-2024)).

**MoE (Mixture of Experts).** Architecture that activates a subset of parameters per token.

**Open-weight.** Downloadable parameters; not necessarily open data or open training code.

**RAG.** Retrieve documents, then generate conditioned on them.

**RLHF / RLVR.** Reinforcement learning from human preferences vs from automatic checkers.

**Skill.** Packaged instructions ± code the agent loads on demand (`SKILL.md`).

**Token.** Subword unit the model reads and writes.

**Transformer.** Attention-based neural architecture ([Vaswani et al. 2017](#ref-vaswani-2017)).

---

## Suggested live spine (for the later slide deck)

1. “AI” in the EHR is mostly old supervised models; ChatGPT is a different species.  
2. Tokens and next-token prediction explain fluency **and** hallucinations.  
3. ChatGPT (Nov 2022) was a product shock; reasoning models (2024–) were a training shock; harnesses (2025–) were an interface shock.  
4. Closed vs open-weight vs local is an access and privacy taxonomy, not a quality league table.  
5. RAG is only as good as the corpus; OpenEvidence ≠ UpToDate ≠ ChatGPT.  
6. Journal policy = disclosure; it does not validate pediatric safety.  
7. Demo: files from an empty folder. Demo: fake citations vs grounded quotes.  
8. Homework: never paste PHI; verify every dose and every PMID.

---

## Appendix A. Resident pocket card (one page)

**Do**

- Use OpenEvidence or UpToDate Expert AI (if licensed) for **lookup**, then click the source.
- Use a harness to draft **slides, trackers, and letters** from synthetic or de-identified-by-policy text.
- Run a local model offline for private brainstorming when hardware allows.
- Disclose AI on any manuscript per *Pediatrics*/ICMJE (tool, manufacturer, how used).
- Keep git history of teaching decks.

**Do not**

- Paste PHI into consumer ChatGPT/Claude/Gemini.
- Copy a dose or a PMID you have not opened.
- Treat SWE-Bench or a chat “95% on USMLE” as clinical privilege.
- List a model as an author.
- Trust a 40-step agent you did not read.

**If asked “which model should I pay for?”**  
None, until you have a use that files and retrieval cannot cover. Then: whatever your institution already licensed, or a single frontier chat for non-PHI writing—not five subscriptions.

**If asked “is local HIPAA-safe?”**  
Safer against **vendor** disclosure if truly offline. Not automatically a compliant workstation. No real notes in the lecture demos.

## Appendix B. How this compilation labeled evidence

- **Retrieved:** page or PDF opened 25 August 2026.
- **Vendor-reported:** benchmark or adoption number from a lab or product About page.
- **Abstract-only:** peer-reviewed bibliographic record without full PDF.
- **Canonical:** standard paper whose HTML timed out but whose identity is not in dispute (GPT-2/3/4, ChatGPT launch).
- **Proposal:** the author’s recommended journal-policy additions in §11.2; not current ICMJE.

---

## References

Primary and canonical sources. Retrieval date 25 August 2026 unless noted. Status tags: **retrieved** (full page/PDF opened this project), **canonical** (standard paper/product URL; some OpenAI HTML timed out in this environment), **abstract-only**, **secondary-only**.

<a id="ref-vaswani-2017"></a>Vaswani A, Shazeer N, Parmar N, et al. Attention is all you need. *Adv Neural Inf Process Syst.* 2017;30. arXiv:1706.03762. **canonical** (also cited in FDA 2026 discussion paper).

<a id="ref-gpt2"></a>Radford A, Wu J, Child R, et al. Language models are unsupervised multitask learners. OpenAI technical report; 2019. **canonical**.

<a id="ref-gpt3"></a>Brown TB, Mann B, Ryder N, et al. Language models are few-shot learners. *Adv Neural Inf Process Syst.* 2020;33. arXiv:2005.14165. **canonical**.

<a id="ref-ouyang-2022"></a>Ouyang L, Wu J, Jiang X, et al. Training language models to follow instructions with human feedback. *Adv Neural Inf Process Syst.* 2022;35. arXiv:2203.02155. **canonical**.

<a id="ref-chatgpt-2022"></a>OpenAI. Introducing ChatGPT. 30 November 2022. https://openai.com/index/chatgpt/ **canonical** (fetch timeout in this compilation).

<a id="ref-gpt4"></a>OpenAI. GPT-4 technical report. 14 March 2023. https://openai.com/index/gpt-4-research/ **canonical**.

<a id="ref-o1-2024"></a>OpenAI. Learning to reason with LLMs. September 2024. https://openai.com/index/learning-to-reason-with-llms/ **retrieved** (planning corpus) / **canonical**.

<a id="ref-tulu3"></a>Lambert N, et al. Tulu 3: Pushing frontiers in open language model post-training (introduces the name RLVR). 2024. **canonical** for the method name; not re-fetched as HTML this pass.

<a id="ref-mcp-2024"></a>Anthropic. Introducing the Model Context Protocol. 25 November 2024. https://www.anthropic.com/news/model-context-protocol **retrieved**.

<a id="ref-mcp-docs"></a>Model Context Protocol documentation. What is the Model Context Protocol (MCP)? https://modelcontextprotocol.io/docs/getting-started/intro **retrieved** 25 Aug 2026.

<a id="ref-skills-2025"></a>Anthropic. Introducing Agent Skills. 16 October 2025 (updated 18 December 2025). https://www.anthropic.com/news/skills **retrieved**.

<a id="ref-icmje"></a>International Committee of Medical Journal Editors. Recommendations for the Conduct, Reporting, Editing, and Publication of Scholarly Work in Medical Journals. https://www.icmje.org/icmje-recommendations.pdf **retrieved** (PDF text). Includes §II.A.4 AI-assisted technology and §V use of AI in publishing.

<a id="ref-cope-ai"></a>Committee on Publication Ethics. Authorship and AI tools. https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools **canonical** (HTML timeout this pass; language corroborated via *Pediatrics* author instructions citing COPE).

<a id="ref-pediatrics-ai"></a>American Academy of Pediatrics. Author instructions: Artificial intelligence. https://publications.aap.org/pediatrics/pages/author-instructions **retrieved**.

<a id="ref-aap-digital-2026"></a>American Academy of Pediatrics. Digital ecosystems, children, and adolescents: policy statement. *Pediatrics.* 2026;157(2):e2025075320. doi:10.1542/peds.2025-075320. Published 20 January 2026. **retrieved**. States that AI will be covered in a separate forthcoming policy statement.

<a id="ref-grundmeier-2026"></a>Grundmeier RW, Fiks AG, Jenssen BP, Proctor SN, Ferro DF, Johnson KB; Section of Informatics at Children’s Hospital of Philadelphia. Generative artificial intelligence: implications for families and pediatricians. *Pediatrics.* 2026;157(4):e2025074912. doi:10.1542/peds.2025-074912. Accepted 7 January 2026. **retrieved** (full PDF in [`papers/pediatrics.2025074912.pdf`](papers/pediatrics.2025074912.pdf)). State-of-the-art review, **not** AAP policy. 72% adolescent companion-chatbot figure is attributed there to Common Sense Media (Robb and Mann, 2025); that underlying PDF was not opened this pass.

<a id="ref-aap-places-2025"></a>AAP. US pediatricians’ experiences with artificial intelligence in healthcare in 2025. PAS abstract. https://www.aap.org/en/research/pas-abstracts/us-pediatricians-experiences-with-artificial-intelligence-in-healthcare-in-2025/ **retrieved** (abstract page). Conference abstract, not a full paper.

<a id="ref-ama-2026"></a>American Medical Association. AMA policies to ensure AI supports—not replaces—physician judgment. Press release dated **10 June 2026**. https://www.ama-assn.org/press-center/ama-press-releases/ama-policies-ensure-ai-supports-not-replaces-physician-judgment **retrieved** (saved PDF in [`papers/`](papers/README.md)). HOD item numbers still not on the press page.

<a id="ref-ama-h480"></a>AMA Policy H-480.931, Assessing the Intersection Between AI and Health Care. Year last modified 2026 (reaffirmed). https://policysearch.ama-assn.org/ **retrieved** (policy text).

<a id="ref-bergman-2026"></a>Bergman A, Wachter RM, Emanuel EJ. A licensure framework for autonomous clinical AI. *JAMA.* 2026;335(20):1751-1754. Published online 29 April 2026. doi:10.1001/jama.2026.5483. **retrieved** (full PDF in [`papers/`](papers/README.md)). Viewpoint/Perspective, not original research.

<a id="ref-who-b09667"></a>World Health Organization. Artificial intelligence and evidence-informed policy: emerging challenges and opportunities: discussion paper. Geneva: WHO; 2026. WHO reference B09667. doi:10.2471/B09667. https://www.who.int/publications/i/item/B09667 **retrieved** (full PDF in [`papers/B09667-eng.pdf`](papers/B09667-eng.pdf)).

<a id="ref-fda-2026"></a>FDA Center for Devices and Radiological Health. Considerations for the Regulation of Generative AI-Enabled Medical Devices: Discussion Paper and Request for Feedback. August 2026. Docket FDA-2026-N-7874. **retrieved** (official attachment [`papers/FDA-2026-N-7874-0001_attachment_1.pdf`](papers/FDA-2026-N-7874-0001_attachment_1.pdf)). Front matter: discussion only; not draft or final guidance; not a policy change. Comment-close date **19 October 2026** is from docket/press metadata used in the first pass; it is **not printed in the PDF body**.

<a id="ref-ocr-tracking"></a>HHS Office for Civil Rights. Use of online tracking technologies by HIPAA covered entities and business associates. https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/hipaa-online-tracking/index.html **retrieved**.

<a id="ref-hhs-ba"></a>HHS. Business associates. https://www.hhs.gov/hipaa/for-professionals/privacy/guidance/business-associates/index.html **canonical**.

<a id="ref-openai-hipaa"></a>OpenAI Help Center. HIPAA eligible products and functionality. https://help.openai.com/en/articles/20001069-hipaa-eligible-products-and-functionality **retrieved**.

<a id="ref-gpt56"></a>OpenAI. GPT-5.6: Frontier intelligence that scales with your ambition. 9 July 2026 (updates 30 July and 21 August 2026). https://openai.com/index/gpt-5-6/ **retrieved**.

<a id="ref-fable-mythos"></a>Anthropic. Claude Fable 5 and Claude Mythos 5. 9 June 2026; access notes 12 June and 1 July 2026. https://www.anthropic.com/research/claude-fable-5-mythos-5 **retrieved**.

<a id="ref-opus5"></a>Anthropic. Introducing Claude Opus 5. 24 July 2026. https://www.anthropic.com/news/claude-opus-5 **retrieved**.

<a id="ref-gemini-37"></a>Google. Introducing Gemini 3.7 Flash. 13 August 2026. https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/ **retrieved**.

<a id="ref-gemini-notebook"></a>Woodward J. NotebookLM is now Gemini Notebook. 16 July 2026. https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/ **retrieved**.

<a id="ref-muse-spark"></a>Meta Superintelligence Labs. Introducing Muse Spark: scaling towards personal superintelligence. 8 April 2026. https://ai.meta.com/blog/introducing-muse-spark-msl/ **retrieved**.

<a id="ref-muse-glimmer"></a>Meta Superintelligence Labs. Introducing Muse Glimmer: an open agentic model that runs on your device. August 2026. https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model **retrieved**.

<a id="ref-kimi-k3"></a>Moonshot AI. Kimi K3: open frontier intelligence. https://www.kimi.com/blog/kimi-k3 **retrieved**. Technical report: arXiv:2607.24653.

<a id="ref-deepseek-v4"></a>DeepSeek-AI. DeepSeek-V4: towards highly efficient million-token context intelligence. arXiv:2606.19348. https://arxiv.org/html/2606.19348 **retrieved**.

<a id="ref-qwen38-max"></a>Qwen team, Alibaba Group. Qwen3.8-Max: a new bar for coding and cowork. 3 August 2026. Listed on https://qwen.ai/blog/qwen3.8-max **retrieved** (index + listing; 2.4T, open-weight intent). The local [`papers/Qwen.pdf`](papers/Qwen.pdf) is a one-page marketing screenshot of a long-horizon coding demo (oh-my-cli; “as of July 30, 2026 … 151 issues”); it does **not** independently confirm parameter count.

<a id="ref-qwen38-gh"></a>QwenLM. Qwen3.8 GitHub repository. https://github.com/QwenLM/Qwen3.8 **retrieved**.

<a id="ref-ollama"></a>Ollama. Product homepage. https://ollama.com **retrieved** 25 Aug 2026.

<a id="ref-ollama-qwen38"></a>Ollama library. qwen3.8. https://ollama.com/library/qwen3.8 **retrieved** 25 Aug 2026.

<a id="ref-glm53"></a>Z.ai. GLM-5.3: frontier coding with emergent cyber capabilities. 14 August 2026. https://z.ai/blog/glm-5.3 **retrieved**.

<a id="ref-oe-about"></a>OpenEvidence. About. https://www.openevidence.com/about/ **retrieved**.

<a id="ref-artsi-2026"></a>Artsi Y, Sorin V, Glicksberg BS, et al. OpenEvidence clinical question-answering platform: systematic review of early evaluations. *npj Digit Med.* Published 12 August 2026. doi:10.1038/s41746-026-03077-4. Received 16 February 2026; accepted 26 July 2026. PROSPERO CRD420261289103. **retrieved** (article-in-press PDF in [`papers/s41746-026-03077-4_reference.pdf`](papers/s41746-026-03077-4_reference.pdf); publisher warns of possible remaining errors). No pediatric-specific synthesis.

<a id="ref-utd-ai"></a>Wolters Kluwer Health. Wolters Kluwer’s new UpToDate Expert AI provides clinicians and health systems with the fast, reliable GenAI clinical decision support they need. 24 September 2025. https://www.wolterskluwer.com/en/news/uptodate-expert-ai-genai-clinical-decision-support **retrieved** (saved WK page in [`papers/`](papers/README.md)). Vendor copy. Related 6 August 2026 WK item on the same print claims ~2,500 US hospitals; still vendor.

<a id="ref-claude-code"></a>Anthropic. Claude Code product page. https://www.anthropic.com/product/claude-code ; GitHub https://github.com/anthropics/claude-code **retrieved**.

<a id="ref-codex-sandbox"></a>OpenAI. Unrolling the Codex agent loop; Building a safe, effective sandbox to enable Codex on Windows; Codex sandbox documentation. https://openai.com/index/unrolling-the-codex-agent-loop/ ; https://openai.com/index/building-codex-windows-sandbox/ ; https://developers.openai.com/codex/concepts/sandboxing **retrieved**.

<a id="ref-openclaw"></a>OpenClaw. https://github.com/openclaw/openclaw ; https://openclaw.ai **retrieved** (GitHub README).

<a id="ref-hermes"></a>Nous Research. Hermes Agent. https://github.com/nousresearch/hermes-agent **retrieved** (GitHub README).

<a id="ref-opencode"></a>anomalyco/opencode. https://github.com/anomalyco/opencode **retrieved** (GitHub landing).
