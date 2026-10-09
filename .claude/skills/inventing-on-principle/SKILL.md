---
name: inventing-on-principle
description: Help users discover a concrete guiding principle, recognize violations of it in the world, and turn that principle into useful inventions, software, teaching tools, workflows, or experiments. Inspired by Bret Victor's talk "Inventing on Principle." Use when the user asks about purpose-driven invention, first principles for creative work, identifying a personal or product principle, or designing tools that make ideas easier to explore.
---

# Inventing on Principle

Help the user move from a vague interest or value to a specific, actionable principle—and then use it to guide concrete work.

The central inspiration is Bret Victor's talk **"Inventing on Principle"**: rather than only following passion or chasing opportunities, identify something important, necessary, and right; notice where the world violates it; imagine a better world; and use your work to help make that world real.

## Core ideas

1. **A principle is a cause, not just a preference.** It names something the user believes should be true about the world or about how people work, learn, create, or live.
2. **Make the principle actionable.** "Make software simple" is too vague. "A person should never lose their work because a tool hides the current state" is easier to test. Prefer a principle that helps answer a concrete yes/no question.
3. **Look for violations, not just opportunities.** Ask where the principle is currently violated, who is constrained by it, what ideas or human capabilities are being stunted, and why this matters.
4. **Imagine a better world.** Describe what would be different if the violation no longer existed.
5. **Invent in response.** A product, prototype, teaching method, workflow, interface, research direction, or small experiment can be a way to act on the principle.
6. **Stay close to the work.** For creative and technical tools, shorten the feedback loop between an action and seeing its consequences. Make hidden states visible, support exploration, and reduce unnecessary mental simulation.
7. **Treat principle-finding as self-discovery.** A strong principle may take time. Explore different kinds of work and experiences; notice what consistently feels meaningful, frustrating, unjust, or full of possibility.
8. **A principle should guide decisions.** If it cannot change what the user builds, measures, prioritizes, or rejects, sharpen it.

## How to work with the user

Use the workflow below. Do not force every step into every answer; match the depth to the request.

### Step 1 — Identify the domain and the people affected
Ask or infer what the user wants to improve: software development, education, AI-assisted thinking, creative work, personal knowledge systems, organizations, or another domain.

Clarify:
- Who is creating, learning, deciding, or using the system?
- What are they trying to accomplish?
- What currently gets in their way?

### Step 2 — Find the recurring friction
Ask for a concrete moment rather than a broad opinion:
- What repeatedly frustrates you?
- What do people accept as "just how things work"?
- When have you seen a person struggle because a tool, process, or institution hides something important?
- What makes you think, "It shouldn't have to be this way"?

Look for recurring patterns across several experiences, not only a single annoyance.

### Step 3 — Draft a candidate principle
Create 2–4 candidate principles in plain language. Make them specific, human-centered, and testable.

Useful templates:
- "People should be able to ___ without ___."
- "Whenever someone changes ___, they should be able to see/understand ___ immediately."
- "No one should have to ___ just because ___."
- "A tool for ___ should make ___ visible, so that people can ___."

Avoid presenting these as the user's settled beliefs. Label them as hypotheses and invite the user to select, reject, or revise them.

### Step 4 — Test whether the principle is actionable
For each candidate, test:
- **Specificity:** Can it distinguish a good design from a bad one?
- **Observability:** Can we identify a real violation?
- **Generativity:** Does it suggest multiple possible inventions?
- **Meaning:** Does it connect to something the user genuinely cares about?
- **Durability:** Would it still matter beyond one project or current trend?

Ask a crisp test question, ideally answerable with yes/no. If the principle cannot guide a decision, rewrite it.

### Step 5 — Map the violation
Describe:
- Current behavior or system
- The exact point where the principle is violated
- Who bears the cost
- What is hidden, delayed, blocked, or needlessly difficult
- What a better state would look like

Do not assume every inconvenience is a moral wrong. Help the user distinguish a minor preference, a solvable usability problem, and a deeper violation of a value.

### Step 6 — Turn it into invention
Propose a small set of responses, from smallest to largest:
1. A tiny experiment that can be tried today
2. A prototype or workflow change
3. A reusable tool or product concept
4. A longer-term research or institutional change, if appropriate

For each idea, explain how it embodies the principle. Prefer the smallest experiment that can reveal whether the principle is useful.

### Step 7 — Design immediate feedback where relevant
For software, interfaces, data tools, educational material, and AI workflows, explicitly consider:
- Can users see the result of an action quickly?
- Can they inspect the underlying data or reasoning when useful?
- Can they move between representation and outcome?
- Are comparisons visible?
- Can they safely experiment, undo, and explore?
- Is important state hidden behind modes, steps, or opaque automation?
- Does the tool help users notice consequences they did not know to look for?

Do not blindly apply "instant feedback" where delay, reflection, privacy, safety, or deliberate pacing is important. Explain trade-offs.

### Step 8 — Define a test
Turn the idea into a small validation plan:
- Hypothesis
- Target user
- Smallest experiment
- Observable signal or metric
- What would disconfirm the hypothesis
- Next decision

Use qualitative observations as well as metrics. The goal is to learn whether the principle leads to a better outcome, not to manufacture confirmation.

### Step 9 — Capture the principle
When useful, finish with this compact record:

**Principle:** One sentence.
**Why it matters:** The human capability or value at stake.
**Violation to watch for:** An observable failure.
**Better world:** What becomes possible when the principle is honored.
**Invention to try:** The smallest practical intervention.
**Test:** What evidence would show progress—or show the principle needs revision?

## Response style

- Be thoughtful, concrete, and exploratory—not motivational or preachy.
- Do not tell the user what their life principle "is." Help them discover it from their own experiences.
- Prefer specific examples and sharp questions over abstract slogans.
- Distinguish the principle from the solution: one principle may inspire many inventions.
- Do not equate monetization, novelty, or shipping a product with meaningful work.
- Do not claim that the principle is objectively correct merely because it is strongly held. Encourage counterexamples and ethical reflection.
- When useful, explicitly connect the idea to the user's current project, but do not invent personal motivations.
- Avoid reproducing long passages from the talk. Summarize its ideas in original language and attribute the inspiration to Bret Victor.

## Example

User: "I want to make AI tools for students."

Weak response: "Make AI education simple and engaging."

Better process:
1. Ask what students currently cannot do well, and where AI tools interfere with learning.
2. Offer candidate principles, such as "Students should be able to inspect and challenge an AI explanation rather than merely accept its answer."
3. Make the principle testable: "Can a student identify the assumptions and verify the key steps behind this answer?"
4. Identify violations in a real learning task.
5. Prototype an explanation view that exposes assumptions, intermediate steps, counterexamples, and a way to change inputs.
6. Test whether students understand more and can transfer the method to a new problem.

The example is illustrative, not a claim that this must be the user's own principle.
