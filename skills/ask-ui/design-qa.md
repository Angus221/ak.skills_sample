# Ask UI Design QA

## Comparison target

- Source visual truth: `C:/Users/jakyo/AppData/Local/Temp/codex-clipboard-3b634133-c116-4362-a29e-092db10dbd9e.png`
- Light implementation: `C:/Users/jakyo/.agents/skills/ask-ui/assets/qa/implementation-light.png`
- Dark implementation: `C:/Users/jakyo/.agents/skills/ask-ui/assets/qa/implementation-dark.png`
- Mobile implementation: `C:/Users/jakyo/.agents/skills/ask-ui/assets/qa/implementation-mobile-dark.png`
- Full comparison: `C:/Users/jakyo/.agents/skills/ask-ui/assets/qa/comparison-light.png`
- Focused question comparison: `C:/Users/jakyo/.agents/skills/ask-ui/assets/qa/comparison-question-region.png`

## Capture normalization

- Desktop viewport and CSS size: 1256 × 728 at device scale factor 1.
- Source pixels: 1256 × 728.
- Implementation pixels: 1256 × 728.
- Combined comparison pixels: 2512 × 728.
- Mobile viewport and pixels: 390 × 844 at device scale factor 1.
- State: six-question editable round with recommended answers selected. Dark capture uses the same state. Mobile capture uses the second editable round to verify responsive behavior.

## Full-view comparison evidence

The implementation matches the source's main composition: compact topic header, segmented theme controls, horizontal round tabs, dense bordered question rows, four-column desktop options, green selected and recommended states, independent middle scrolling, and a persistent bottom submission bar. The implementation deliberately preserves more space around Chinese text than the source while retaining the same hierarchy.

The source contains product-specific option icons and a logo mark. The implementation omits these assets because Ask UI has a zero-runtime-dependency constraint and the requested change concerns layout and interaction; native radio and checkbox controls retain clear state and accessibility. This is classified as P3 visual drift rather than a functional or structural mismatch.

## Focused-region comparison evidence

The focused Q1 comparison confirms matching option count, horizontal card structure, green selected treatment, recommendation placement, border weight, and compact label hierarchy. Implementation cards are slightly taller and omit decorative icons, but text remains easier to scan and no controls collide or wrap incorrectly.

## Required fidelity surfaces

- Fonts and typography: Microsoft YaHei and system sans fallbacks closely match the Chinese UI source. Weight, line height, labels, badges, and small descriptions are legible in both themes.
- Spacing and layout rhythm: 100dvh four-region grid keeps the header, tabs, scroll area, and submission bar stable. At 1256 × 728 the middle region measured 529 px client height and 844 px scroll height; the dock remained within y=660–718.
- Colors and visual tokens: light mode uses white surfaces, neutral borders, and restrained green selection. Dark mode maps every surface, border, input, selected state, dialog, and dock through semantic tokens with readable contrast.
- Image quality and asset fidelity: no raster imagery is required by the Ask UI product. Product-specific source icons were not recreated with CSS, inline SVG, glyphs, or placeholders.
- Copy and content: submission instructions are always visible, explicitly marked “提交必读”, and require no acknowledgement checkbox.
- Responsiveness: at 390 × 844 the body scroll width remained 390 px, the middle region ended exactly where the 112 px bottom dock began, and options collapsed to one column.
- Accessibility: semantic radio, checkbox, tab, dialog, button, heading, banner, tabpanel, and contentinfo roles are present. Focus-visible and reduced-motion states are defined.

## Interaction evidence

- Theme switching worked and dark mode remained selected after reload.
- Recommended answers were preselected and the answered counter showed 6 / 6.
- Selecting “其他” without text submitted `selectedOptionIds: ["__other__"]` and an empty `customText`.
- Selecting “其他” with text submitted the same reserved id plus `customText: "线索培育阶段"`.
- The confirmation dialog rendered `其他` and `其他：线索培育阶段` correctly.
- Submitted rounds became read-only, and a newly created second round appeared and became the selected Tab automatically.
- Browser console checks reported no errors or warnings.

## Comparison history

### Iteration 1

- [P1] Header and round heading consumed too much vertical space, materially reducing question density.
- [P1] The “其他” text input was always visible, making every option in its grid row unnecessarily tall.

Fixes:

- Removed the redundant eyebrow and round heading, reduced header and tab heights, and tightened page gaps.
- Kept “其他” as a full option but revealed its supplementary input only after selection.

Post-fix evidence:

- `comparison-light.png` shows the compact header and question region at the same 1256 × 728 target size.
- `comparison-question-region.png` shows aligned four-column choices and compact recommendation rows.
- No actionable P0, P1, or P2 differences remain.

## Follow-up polish

- [P3] A future optional icon pack could bring option-card iconography closer to the source if the zero-dependency constraint is relaxed.
- [P3] Very large desktop displays could expose a user preference for extra-compact row density.

final result: passed
