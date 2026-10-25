---
type: 'llm'
---

PASS if the reply (a) identifies at least three causes of horizontal overflow on a phone among the fixed 1200 px container, the 100vw band with side padding, the fixed three-column grid of 300 px, the 1400 px image and the 900 px table, (b) gives a fix for each (for example min(), max-width: 100%, a single column under a breakpoint, a scrolling wrapper for the table), and (c) says the rendering still has to be measured or captured at phone width (for example a script or a capture at 375 or 390 px, or scrollWidth against clientWidth) rather than concluding from the code alone.
FAIL otherwise.
