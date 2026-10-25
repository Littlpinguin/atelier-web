---
type: 'regex'
pattern: '(?<![\s\S])(?![\s\S]*^#{1,6} [^\n]*\.[ \t]*$)[\s\S]+'
flags: 'm'
target:
  source: 'file'
  path: 'atelier/pages/comment-ca-marche.md'
---
