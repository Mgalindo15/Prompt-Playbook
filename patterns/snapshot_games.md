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

## 4. Snapshot Write!

Flipping the traditional Snapshot games on their head; this time, you have the model prompt YOU to generate some code, then, ChatGPT will assess your code along three dimensions: logics, conventions, and syntax.

**Prompt skeleton**

```text
Let’s play a different game called Snapshow Write! Unlike the other Snapshot games, this time I want you to provide me with a prompt, and I will provide you with the snapshot of code. Then you can parse my code and analyze it along these dimensions:

1. Overall Logic. Does it accurately attempt to solve the problem specified in the question? Even if there are errors preventing the code from running effectively, is it structured and organized in such a way that makes sense given the nature of the task?
2. Use of conventions. Look at the imports, classes, functions, [hooks, actions, return statements, jsx,] etc… Are they used properly? Is anything missing? Is anything added that shouldn’t be? Could anything be done more efficiently?
3. Syntax. Missing parentheses, curly braces. Typos. Incorrect operators (!=, when it should be !==), etc. Break it down!

Since this game will be analysis heavy, please make the tasks lightweight—not necessarily simple, but I don’t want to be writing a ton of code. Make the focus content driven. The content could be something common like [count updating, form or input creation and manipulation, or something more abstract and creative like a game feature or connecting seemingly unrelated features.]

As usual, no hints or comments. Just provide a scenario and a problem that I can solve with code!

In this particular game I want to use [language, packages] and specifically focus on [features].

```

## Additional Techniques

| Technique |   Highlight   | Explanation |
|-----------|---------------|-------------|
| **Question-Criteria** | “Does it accurately solve ...? Are they used properly? Could anything be done ...?” | Questions control perspective. Use them when trying to get ChatGPT to understand how to think about a problem. |
| **Exceptions** | “Even if there are errors preventing the code from running effectively, ...” | Similar to **Negative Instruction**, Exceptions manipulate ChatGPT's value hierarchy, saying "even if x happens, proceed with y" where y is the intended goal. |
