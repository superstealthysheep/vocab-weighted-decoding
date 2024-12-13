# William 

### Constrained/weighted decoding
- [Awesome-LLM-Constrained-Decoding - gh repo](https://github.com/Saibo-creator/Awesome-LLM-Constrained-Decoding?tab=readme-ov-file)(list of papers)
	- [2017: Lexically Constrained Decoding for Sequence Generation using Grid Beam Search](https://aclanthology.org/P17-1141/)
		- *Require* output to contain *constraint subsequences*
		- Not directly applicable to us (too firm)
	- [2024: Guiding LLMs The Right Way: Fast, Non-Invasive Constrained Generation](https://arxiv.org/abs/2403.06988v1)
		- To read
		- Miiight just be about efficiency improvements?
- [2022: Improving Controllable Text Generation with Position-Aware Weighted Decoding](https://aclanthology.org/2022.findings-acl.272/)
	- To read
		Google Scholar "cited by" page seems interesting: https://scholar.google.com/scholar?cites=12695820997208826002&as_sdt=5,24&sciodt=0,24&hl=en
- [Kiddon 2016: Globally Coherent Text Generation with Neural Checklist Models](https://aclanthology.org/D16-1032/)
	- To read
- [Wen 2015: Semantically Conditioned LSTM-based Natural Language Generation for Spoken Dialogue Systems](https://aclanthology.org/D15-1199/)
	- To read
- [Liang 2024: Controllable Text Generation for Large Language Models: A Survey](https://arxiv.org/abs/2408.12599)
	- Very comprehensive/yummy summary of existing techniques. Looked at section 6 ("decoding-time intervention"), evaluation section, applications section. Good introductory explanation of methods such as PPLM and FUDGE. 
	- In applications section, found mention of a 2023 paper "Lexical Complexity Controlled Sentence Generation for Language Learning" which seems very close to our project goal.
- [Ashok 2024: Controllable Text Generation in the Instruction-Tuning Era](https://arxiv.org/abs/2405.01490)
	- To read
- [Nie 2023: Lexical Complexity Controlled Sentence Generation for Language Learning](https://aclanthology.org/2023.ccl-1.56/)
	- To read
	- Fixed "complexity embeddings" (trained in per vocab? (A: yes) do these get affected by attention? (A: yes)) (just new parameters on input embeddings)
	- Cites 3 previous "lexical CTG" papers (page 2)
	- Control:
		- Semantics via keywords
		- Lexical complexity via 3 levels
	- Brief survey of previous attempts for lexical CTG:
		- decoding-phase logit manipulation (zeroing out? or softer), supposedly not soft enough of an approach; loss of generation quality
			- Darathari et al 2019, Post and Vilar 2018
		- prompting for lexical complexity (how? like "please speak as though i were 5yo"?)
			- Brown et al 2020, Raffel et al 2020, Li and Liang 2021
		- Reranking
			- "after decoding", "does not consider lexical complexity \[at\] training time"
			- Rauvat et al 2022, Pandramish and Sharma, 2020
	- Eval metrics
		Quality
		- BLEU, METEOR, NIST with references
		- n-gram "Entropy", "Distinct" to measure "lexical diversity"
		- GPT-2 perplexity of output
		Control
		- 
	- Wow, this seems very similar to what we want to do. The difference is that these complexity embeddings are fixed at training time and thus can't be adapted to new users flexibly at inference time. Also, the complexity levels (I think?) are locked in via some sort of supervised training process ahead of time? Very text-data-dependent, which means it'd not be feasible to apply in our use case.
	- Lots of references to other related work to investigate
- [Qiang et al 2020: Lexical Simplication with Pretrained Encoders](https://arxiv.org/abs/1907.06226)
	- To read?
- [Barayan et al 2024: Analyzing Zero-Shot Readability-Controlled Sentence Simplification](https://arxiv.org/abs/2409.20246v1#S3)
	- To read? 
	- May have good evals

Handling multi-token "boost vocab"
- Beam search?
- Tokenize boost vocab into sequences, apply boost tokenwise? Or just at final token of the sequence (and catch this via beam search with depth >= max(boost seq lengths))
- Or maybe it's actually easier to just penalize all out-of-vocab sequences? Uhh maybe that's actually a headache

### Tutory stuff
- [Conversational Spaced Repetition - David Bieber](https://davidbieber.com/snippets/2024-03-04-conversational-spaced-repetition/)
	- Brainstorming on using LLM to generate cards/Qs, ask cards/Qs, evaluate user understanding
	- Possibly out of scope for us
	- If in scope, application would be mining vocab from what the user seems to understand well (what they use and what they can read and understand (however, understanding the whole text != understands each word individually))
- [Feng 2023: Sentence Simplification via LLMs](https://arxiv.org/abs/2302.11957)

### Evaluations
- Coherence
	- [How do you measure coherence in a single sentence - r/LanguageTechnology](https://www.reddit.com/r/LanguageTechnology/comments/jof3c6/how_do_you_measure_coherence_in_a_single_sentence/)
		- Maybe check for entailment within the sentence?
		- Perplexity, average word transition score (transition probabilities)
		- Schizophrenia incoherence paper?
			- [Iter, Yoon, Jurafsky 2018: Automatic detection of incoherent speech for diagnosing schizophrenia](https://nlp.stanford.edu/pubs/iter2018shizophrenia.pdf)
Random thought: what if on each generation/token, we print a summary of the total perturbation applied the logit boost (e.g. "the boosted vocab went from taking up x% of the probability to taking up y% of the probability")