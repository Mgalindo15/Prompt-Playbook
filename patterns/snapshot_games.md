---
title: Snapshot Games
subtitle: Conversational code-review mini-games
tags: prompt-pattern, code-learning
date: 2025-07-22
---

> **Pattern family:** “Snapshot”  
> Teach or assess code understanding by letting the LLM play different roles.

## 1. Snapshot (Original)

Ask the model for an unlabeled code snippet and analyse it along three axes  
(placement, purpose, syntax). Then let the model grade your analysis.  

**Prompt skeleton**

```text
Let’s play a game. I'm going to call this game "Snapshot (Original)". When I refer to this game, I'm referring to the game where you supply a snapshot of code, and I have to explain it along these 3 dimensions: 

1. Where would this code conventionally be located? FE/BE, folder, filename..?
2. What is the purpose of this code? What does it do? 
3. Explain syntax components. 

I will analyze the code and answer each of these questions. Then you will analyze my response and validate what I was correct about, and provide explanations for what I was incorrect about.

When you provide the snapshot of code, please do not include any hints or comments that may point me toward the correct answer. The code should provide sufficient context for me to answer these questions.

In this particular game I want to use [language, packages] and specifically focus on [features].
```

## Key Techniques (why this prompt works)

| Technique |   Highlight   | Explanation |
|-----------|---------------|-------------|
| **Naming** | "Snapshot (Original)” | Assigning a **stable label** lets the LLM bind follow-up instructions to that context, reducing drift.
| **Definition lock-in** | “When I refer to this game … I mean you supply code, I analyse …” | Explicitly codifies what the game **is** before it starts—guards against hallucinated rule changes. |
| **Negative instruction** | “Please **do not include comments**” | Overwrites the model’s helpful-by-default habit; keeps the exercise authentic.|
| **Placeholders** | [language, packages, features] | Creates a reusable template—swap SQL, React, etc., without rewriting the prompt.|

## 2. Snapshot (Blank)

Ask the model for an unlabeled code snippet that contains several **numbered blanks** (`__1__`, `__2__`, …).  
You will fill the blanks; the model will then grade your answers.

**Prompt skeleton**

```text
Let's play a different game called Snapshot (Blank).
As in Snapshot (Original), you will send me a code snapshot;
however, in this version please replace some tokens with numbered
blanks: __1__, __2__, __3__, …

The blanks may stand for variables, functions (e.g., hooks), class names,
or other identifiers that are inferable from context.

I will reply by listing the numbers and my proposed replacements.
You will critique my answers.

Do not include any comments or hints—only the bare snippet.

For this round, use [language, packages] and focus on [features].

```

## Additional Techniques

| Technique |   Highlight   | Explanation |
|-----------|---------------|-------------|
| **Parent/Sister Reference** | “as in Snapshot (Original)” | Chains this prompt to a previously defined game, tightening context memory and reducing spec drift. |
| **Rule Update After Recall** | “however, in this version …” | Explicitly states the delta from the parent game, so the model doesn’t overwrite earlier rules entirely but layers new constraints. |
| **Numbered Placeholders** | `__1__`, `__2__` … | Using a consistent `__n__` pattern makes the grading loop trivial—model can map indices to answers programmatically. |
| **Negative Instruction Reinforcement** | “Do not include any comments or hints” | High-likelihood habits need additional negative reinforcement to ensure they stay turned off. |

## 3. Snapshot (Bug)

Ask the model for a numbered code snippet that contains several bugs. Provide the line number and subsequent bugged code / fix. The model will then grade your answers.

**Prompt skeleton**

```text
Let’s play a different game called "Snapshot (Bug)". In this game, you provide a snapshot of code (like in Snapshot (Original)); however, in this snapshot, I want you to include a few bugs that would return errors. These could be type errors, logical errors, runtime errors, whatever.

When you provide this snapshot of code, do not supply any hints, comments, numbers or anything that could help me discern what the bugs are or where they may be located. Let me do all that on my own. Simply provide the snapshot of code with line numbers (1 → n) on the lefthandsize of the code for my reference and await my response.

In my response, I will return each bug in a numbered list. Please go through each one and let me know if it is correct / incorrect, as well as any bugs that I failed to find. Go in detail, especially with the ones that I was incorrect about / failed to find.

In this particular game I want to use [language, packages] and specifically focus on [features].

```

## Additional Techniques

| Technique |   Highlight   | Explanation |
|-----------|---------------|-------------|
| **Specific-Non-Specific** | “type errors, logical errors, runtime errors, whatever” | after providing specific categorical examples, "whatever" is encoded as "along these lines" |
| **Function, then Form** | “with line numbers (1 -> n) on the **lefthand side**” | Generate the "n" number lines first, then control what those lines look like. |
|
