# Squelettes canoniques de mouvement (React)

Détail de l'étape 6 de `design-taste`, pour un projet React. En HTML statique (la fabrique de l'atelier), le mouvement suit la skill `motion-defilement` : CSS piloté par le défilement d'abord, GSAP pour l'épinglage avec scrub. Ces squelettes corrigent les échecs les plus fréquents des pages générées.

## A. Pile de cartes au défilement (sticky-stack)

Échec classique : le déclencheur part à mi-défilement au lieu de s'épingler en haut. Correctif : `start: "top top"`.

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function StickyStack({ cards }: { cards: React.ReactNode[] }) {
  const ref = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !ref.current) return;
    const ctx = gsap.context(() => {
      const cardEls = gsap.utils.toArray<HTMLElement>(".stack-card");
      cardEls.forEach((card, i) => {
        if (i === cardEls.length - 1) return;
        ScrollTrigger.create({
          trigger: card,
          start: "top top",                              // épingler en haut de la fenêtre
          endTrigger: cardEls[cardEls.length - 1],
          end: "top top",
          pin: true,
          pinSpacing: false,
        });
        gsap.to(card, {
          scale: 0.92,
          opacity: 0.55,
          ease: "none",
          scrollTrigger: {
            trigger: cardEls[i + 1],
            start: "top bottom",
            end: "top top",
            scrub: true,
          },
        });
      });
    }, ref);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <div ref={ref} className="relative">
      {cards.map((card, i) => (
        <div key={i} className="stack-card sticky top-0 min-h-[100dvh] flex items-center justify-center">
          {card}
        </div>
      ))}
    </div>
  );
}
```

Points critiques : `start: "top top"`, `pin: true`, chaque carte sauf la dernière est épinglée, l'échelle et l'opacité sont pilotées par le déclencheur de la carte SUIVANTE. Dans une landing de l'atelier, `motion-defilement` § 6 écarte les cartes qui s'empilent : ce squelette sert hors de ce cadre, sur décision de l'humain.

## B. Défilement horizontal épinglé (scroll-hijack)

Échec classique : l'animation démarre avant l'épinglage, le visiteur voit une demi-diapositive. Même correctif : `start: "top top"`, épingler le conteneur, scruber la piste interne.

```tsx
"use client";
import { useRef, useEffect } from "react";
import { gsap } from "gsap";
import { ScrollTrigger } from "gsap/ScrollTrigger";
import { useReducedMotion } from "motion/react";

gsap.registerPlugin(ScrollTrigger);

export function HorizontalPan({ children }: { children: React.ReactNode }) {
  const wrap = useRef<HTMLDivElement>(null);
  const track = useRef<HTMLDivElement>(null);
  const reduce = useReducedMotion();

  useEffect(() => {
    if (reduce || !wrap.current || !track.current) return;
    const ctx = gsap.context(() => {
      const distance = track.current!.scrollWidth - window.innerWidth;
      gsap.to(track.current, {
        x: -distance,
        ease: "none",
        scrollTrigger: {
          trigger: wrap.current,
          start: "top top",
          end: () => `+=${distance}`,                    // longueur de défilement = déplacement horizontal
          pin: true,
          scrub: 1,
          invalidateOnRefresh: true,
        },
      });
    }, wrap);
    return () => ctx.revert();
  }, [reduce]);

  return (
    <section ref={wrap} className="relative overflow-hidden">
      <div ref={track} className="flex h-[100dvh] items-center">{children}</div>
    </section>
  );
}
```

## C. Apparition en cascade, sans épinglage

Pour « les éléments apparaissent en entrant dans la fenêtre » : en HTML statique, le CSS natif (skill `animation-scroll-reveal`) ; en React, Motion `whileInView`. GSAP reste pour le vrai épinglage avec scrub.

```tsx
"use client";
import { motion, useReducedMotion } from "motion/react";

export function RevealStagger({ items }: { items: string[] }) {
  const reduce = useReducedMotion();
  return (
    <ul className="grid gap-6">
      {items.map((item, i) => (
        <motion.li
          key={item}
          initial={reduce ? false : { opacity: 0, y: 24 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, amount: 0.3 }}
          transition={{ duration: 0.6, delay: i * 0.06, ease: [0.16, 1, 0.3, 1] }}
        >
          {item}
        </motion.li>
      ))}
    </ul>
  );
}
```
