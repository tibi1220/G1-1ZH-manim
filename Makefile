all:
	manim -p ./main.py FullScene

anim:
	manim-slides FullScene

complex:
	manim -p ./complex.py Complex

canim:
	manim-slides Complex

sets:
	manim -p ./sets.py Sets

setanim:
	manim-slides Sets

seqs:
	manim -p ./sequences.py Sequences

seqanim:
	manim-slides Sequences

functions:
	manim -p ./functions.py Functions

fanim:
	manim-slides Functions
