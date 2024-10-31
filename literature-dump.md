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
	- To read
- [Ashok 2024: Controllable Text Generation in the Instruction-Tuning Era](https://arxiv.org/abs/2405.01490)
	- To read

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

# Others: feel free to add your own sections