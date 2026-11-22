# Figma Wireframe Specification

**Design System**
- **Primary Colour**: #FF3F6C (Myntra Rose)
- **Secondary Colour**: #282C3F (Charcoal)
- **Neutral**: #F5F5F6 (Light Gray)
- **Accent**: #00A859 (Success Green) for confidence badges.

**Typography**
- **Font Family**: Inter, sans‑serif.
- **Headings**: 20 pt, weight 600.
- **Body**: 14 pt, weight 400.
- **Caption**: 12 pt, weight 300.

**Layout Grid**
- 8 px baseline grid.
- 4‑column mobile grid, each column 84 dp, gutter 16 dp.
- Padding: 16 dp on left/right, 12 dp top/bottom.

**Components**
1. **Size Recommendation Card** – rounded rectangle, shadow, height 56 dp, includes size label, confidence percentage, and “Apply” CTA button.
2. **Bottom‑Sheet Modal** – slides up from bottom, full‑width, contains input fields (height, weight, body‑type dropdown) and a submit button.
3. **Size Chart** – horizontal scrollable bar chart displaying garment measurements vs user measurements, colour‑coded for fit risk.
4. **Heatmap Tile** – small matrix (3 × 3) showing category‑size non‑fit intensity (colour gradient from green to red).

**Interaction Rules**
- Tap on the **Recommend** button triggers modal.
- Selecting a size in the chart updates the card in real‑time.
- All elements must have ARIA labels for screen readers.
- Touch targets ≥48 dp.

**Export Assets**
- Export PNGs at 2× for all icons.
- Provide SVGs for scalable components.

**Version**: v1.0 – ready for hand‑off to developers.
