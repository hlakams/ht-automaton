# Half-Triangle Cellular Automaton

This project is intended to show how cellular automata can not only be used to model general, repetitive behaviors for a variety of physical phenomena -- such as watershed ecosystems and the general paths for a forest-fire model -- but also and any such emergent (repetitive) systems. The cellular automata (CA) theory describes a cell contained within a system that grows (traverse, in this case) depending on overarchng rules. The general theory is based in Conway's Game of Life, which describes an ecosystem of various cellular automatons that interact with one another (in a manner that introduces predator-prey relationships). However, my algorithm for controlled, systemic growth is heavily based upon Langton's Ant instead: the CA senses attributes of cells in its vicinity and alters its decisions for growth based on them. The result such a heavily-repetitive algorithm is an emergent behavior that is can be characterized as a local 2-manifold. The objective can be better interpreted as creating an 'intelligent' system which interacts with itself in a non-competitive ecosystem.

Similar to rules for pattern generators and similar turmites, this specific generator is patterned on a half-triangle (HT) rule. The constraint rule is a simple on/off logic: the inactive area is maroon, while the active nodes are yellow. The shown HTCA will be an initial one CA which each creates HT's based on the absensce/lack of HT (or active nodes, for that matter). After creating a HT (gold), the CA will move either right, left, up, or down based on a randomly-generated value. If the move is legal (not out-of-bounds, onto an activated node, or out-of-moves) it will continue this iterative process. Otherwise, the CA will terminate and leave a non-marker (which can be overwritten by a HT).

This algorithm can represent the complex behavior of animals when migrating, for instance. More importantly, the significance is in training visual pattern-recognition models -- which can be implemented in the likes of self-driving cars (human movement), AR technologies (interference filtering), and neural weather forecasting (correlating cloud/wind movement to climate models). 

I have exhibited the 1CA case, which (initially) had the emergent end behavior of non-complex tessellation. It appears that any nCA case, where n >= (sqrt(max(dim_x, dim_y))), is better suited for very-large planes (min. 200 x 200).

## Methodology
My approach to coding the half-triangle cellular automata (HTCA) was to first learn abour procedural generators, then CA, and finally work from a smaller model towards the end product. I first read about cellular automata with the Langton's Ant; from there, I realized that it is often difficult to discern emergent behavior (attractors) as compared to non-attractor, repetitive manifolds. This led me to investigate similar models further until I gained the intuition to code a simple CA (which was a snake-like model).
After this portion was completed, I chunked up the HTCA into a few different, discernable modules: the initial plane generation, life/death algorithm, and movement in repetition. I described a majority of the HTCA algorithm prior but here is a breakdown of the process:
*   Clean plane (no CA, 50 x 50 size)
*   Randomly-generate initial positions for CA nodes (note: this portion was altered due to errors with sometimes-overlapping nodes, which immediately terminated the behavior)
*   Conditionals for life iteration (HT)
*   Random movement, tiling, and proximity decisions
*   End-node or death sequence (color and delete)

I also found it very useful to draw the frames of movement and note any possible sequences of repetition to eliminate unnecessary code. This was difficult given random positioning, but I think it helped a great deal. This also made it viable to estimate any emergent behavior with fixed-size HT's.  
Due to the nature of the HTCA, I implemented a breaker (counter, sub-counter vars) in lieu of a standard CA terminal condition. However, simply commenting out the breaker and uncommenting the terminal condition + using nCA, n >= 2 will work as well. Note that this currently causes a memory leak.

## Dependencies
*   Matplotlib (pyplot, colors)
*   Numpy (random, zeros for array functionality)
*   PIL (image i/o to gif)
*   os (image garbage collection)
*   gc (misc. garbage collection)

## Previews
Here are gifs that use the PIL image library to illustrate various controls in my HTCA algorithm (uploaded to an external host due to loading issues).
I characterize 2 different types of emergence. This isn't meant to be fully-accurate for topology, but rather descriptive to make the n-manifolds a bit more tangible.

Both HTCA are using a 200px by 200px canvas with one worker. There are no cross-worker interactions as a result.

# Type 1:
NW-SE Diagonal Emergence

HT-length (control) = 13 

Here, the worker is moving randomly and leaves behind a HT footprint at each step. The controller for such behavior is a binary marker (orientation). On orientation == 0 (off), the worker steps NW. However, if the worker decides to not change orientation (== 1), then the choice is to step SE. In the case that the worker is out-of-bounds of the canvas, nothing is done (there is also a dummy 'else' for the rng(0,1) to be in-form with Type 2). With the standard random seed, the emergence is a diagonal line that is similar to the draw NW/SE HT's.

<!-- ![Type1](https://cdn.discordapp.com/attachments/490977707316740109/783092713754722314/test_2.gif "type1") -->
![Type1](https://u.cubeupload.com/lunchpack/test2.gif "type1")

# Type 2:
Tiled Squares Emergence

HT-length (control) = 13

The worker moves stochastically with an HT footprint at each step. The controller for such behavior is also binary marker (orientation). On orientation == 0 (off), the worker steps NW. However, if the worker decides to not change orientation (== 1), then the choice is to step SE. In the case that the worker is out-of-bounds of the canvas, nothing is done. With the standard random seed, the emergence is a series of various tiles, which are individually composed of NW and SE HT tiling.

<!-- ![Type2](https://media.discordapp.net/attachments/760328010326474772/783043424642531358/test.gif "type2") -->
![Type2](https://u.cubeupload.com/lunchpack/test.gif "type2")

Such HTCA can be used to model various physical phenomena -- such as emerging simple attractors in R2. The sub-triangle framework is simple enough to code for emergence, but extensible in a manner that allows extension using other objects, and additional dimensions (such as non-euclidean spaces).
