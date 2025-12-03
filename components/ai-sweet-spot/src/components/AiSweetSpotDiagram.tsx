import React, { useState } from "react";

type Group = "strategy" | "execution" | "people" | "technology" | null;

const GROUP_META: Record<
  Exclude<Group, null>,
  { name: string; subtitle: string; accent: string; highlights: string[] }
> = {
  strategy: {
    name: "Strategy",
    subtitle: "Clarity on where to play and how to win with AI",
    accent: "#00b8c4",
    highlights: [
      "Executive alignment on priority use cases",
      "Operating model and governance for AI initiatives",
      "North-star metrics and investment roadmap",
    ],
  },
  execution: {
    name: "Execution",
    subtitle: "Delivering measurable value through disciplined delivery",
    accent: "#0093c9",
    highlights: [
      "Value proofs with KPIs and OKRs",
      "Rapid pilots with controlled rollout",
      "Continuous optimization and measurement",
    ],
  },
  people: {
    name: "People",
    subtitle: "Building confidence, capability, and change adoption",
    accent: "#0ea5e9",
    highlights: [
      "Leadership sponsorship and clear comms",
      "Upskilling pathways by function",
      "Change management with feedback loops",
    ],
  },
  technology: {
    name: "Technology",
    subtitle: "Right-sized platforms, data, and guardrails",
    accent: "#0066cc",
    highlights: [
      "Reference architectures for secure AI",
      "Data quality, lineage, and observability",
      "Automation and agent orchestration",
    ],
  },
};

const PILLARS = [
  { id: "strategy", cx: 370, cy: 280, r: 275, label: "STRATEGY", sub: "AI Strategic Roadmap" },
  { id: "execution", cx: 830, cy: 280, r: 275, label: "EXECUTION", sub: "AI-enabled Execution" },
  { id: "people", cx: 370, cy: 620, r: 275, label: "PEOPLE", sub: "AI-powered People" },
  { id: "technology", cx: 830, cy: 620, r: 275, label: "TECHNOLOGY", sub: "AI-integrated Technology" },
] as const;

type PillarId = (typeof PILLARS)[number]["id"];

const INITIATIVES: Array<{
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
  groups: PillarId[];
}> = [
  { x: 230, y: 110, width: 170, height: 40, label: "Unstoppable Company Game", groups: ["strategy"] },
  { x: 400, y: 100, width: 260, height: 40, label: "AI Strategic & Execution Roadmap Workshop", groups: ["strategy"] },
  { x: 655, y: 100, width: 160, height: 40, label: "HTC Campaign", groups: ["strategy"] },
  { x: 820, y: 120, width: 220, height: 40, label: "End in Mind Process Mapping", groups: ["strategy", "execution"] },
  { x: 955, y: 140, width: 180, height: 40, label: "AI Command Room", groups: ["execution"] },
  { x: 990, y: 290, width: 120, height: 40, label: "OKRx", groups: ["execution"] },
  { x: 1010, y: 390, width: 190, height: 40, label: "DDDEEE Framework", groups: ["execution", "technology"] },
  { x: 1010, y: 520, width: 180, height: 40, label: "SaaS Audit Review", groups: ["technology"] },
  { x: 980, y: 625, width: 190, height: 40, label: "Data Audit Review", groups: ["technology"] },
  { x: 830, y: 685, width: 260, height: 40, label: "AI Agents + Automation Integration", groups: ["technology"] },
  { x: 550, y: 745, width: 170, height: 40, label: "Use Case Library", groups: ["technology"] },
  { x: 210, y: 390, width: 160, height: 40, label: "AI Agility Check", groups: ["strategy", "people"] },
  { x: 165, y: 505, width: 170, height: 40, label: "Innovators Culture", groups: ["people"] },
  { x: 165, y: 615, width: 150, height: 40, label: "Critical Thinking", groups: ["people"] },
  { x: 240, y: 730, width: 150, height: 40, label: "Upskilling", groups: ["people"] },
  { x: 345, y: 770, width: 160, height: 40, label: "Access to Talent", groups: ["people"] },
];

const TEXT_MAIN = "#0f1b2d";
const TEXT_MUTED = "#516072";

const useHighlight = (active: Group) => {
  return (groups: Group[]) => {
    if (active === null) return { opacity: 1 };
    return { opacity: groups.includes(active) ? 1 : 0.18 };
  };
};

export const AiSweetSpotDiagram: React.FC = () => {
  const [activeGroup, setActiveGroup] = useState<Group>(null);
  const hi = useHighlight(activeGroup);

  const onEnter = (group: Group) => () => setActiveGroup(group);
  const onLeave = () => setActiveGroup(null);
  const activeMeta = activeGroup ? GROUP_META[activeGroup] : null;

  return (
    <div className="diagram-shell">
      <div className="diagram-header">
        <div>
          <p className="eyebrow">AI SWEET SPOT</p>
          <h1>Where strategy, delivery, people, and technology intersect</h1>
          <p className="lede">
            Designed for leadership teams that need a clear, enterprise-grade view of how AI lands in the business.
            Hover or tap to explore each pillar and its initiatives.
          </p>
        </div>
        <div className="summary-chip">
          <span className="dot" />
          Enterprise-ready | Interaction-first | Boardroom-safe
        </div>
      </div>

      <div className="diagram-grid">
        <div className="meta-column">
          <div className="card glass">
            <div className="card-head">
              <div>
                <p className="eyebrow subtle">PILLARS</p>
                <h3>Navigate by focus area</h3>
              </div>
              <button className="reset" onClick={() => setActiveGroup(null)}>
                Reset view
              </button>
            </div>
            <div className="group-chips" role="group" aria-label="Select an AI pillar to highlight">
              {PILLARS.map((pillar) => {
                const isActive = activeGroup === pillar.id;
                const accent = GROUP_META[pillar.id as PillarId].accent;
                return (
                  <button
                    key={pillar.id}
                    className={`group-chip ${isActive ? "is-active" : ""}`}
                    style={
                      isActive
                        ? { boxShadow: `0 10px 30px -12px ${accent}66`, borderColor: accent }
                        : undefined
                    }
                    onMouseEnter={() => setActiveGroup(pillar.id)}
                    onMouseLeave={() => setActiveGroup(null)}
                    onFocus={() => setActiveGroup(pillar.id)}
                    onBlur={() => setActiveGroup(null)}
                    aria-pressed={isActive}
                  >
                    <span className="chip-swatch" style={{ background: accent }} aria-hidden />
                    <div>
                      <div className="chip-title">{pillar.label}</div>
                      <div className="chip-sub">{pillar.sub}</div>
                    </div>
                  </button>
                );
              })}
            </div>
          </div>

          <div className="card highlight">
            <p className="eyebrow subtle">ACTIVE VIEW</p>
            <h3>{activeMeta ? activeMeta.name : "All pillars"}</h3>
            <p className="lede">
              {activeMeta
                ? activeMeta.subtitle
                : "Hover over a circle or initiative to see where it fits in your AI operating model."}
            </p>
            <ul className="highlight-list">
              {(activeMeta ? activeMeta.highlights : [
                "Connected view across strategy, execution, people, and technology",
                "Initiatives grouped so sponsors know where to lean in",
                "Signals that business value is being delivered responsibly",
              ]).map((item) => (
                <li key={item}>
                  <span className="bullet" />
                  {item}
                </li>
              ))}
            </ul>
          </div>
        </div>

        <div className="canvas-column">
          <div className="card canvas">
            <div className="canvas-top">
              <div>
                <p className="eyebrow subtle">INTERACTIVE MAP</p>
                <h3>Trace initiatives to their owners</h3>
              </div>
              <div className="legend">
                <span className="legend-dot" />
                Hover, focus, or tap to explore
              </div>
            </div>
            <div className="canvas-wrap">
              <div className="grid-sheen" aria-hidden />
              <svg
                viewBox="0 0 1200 900"
                className="diagram-svg"
                role="img"
                aria-label="AI Sweet Spot diagram showing Strategy, Execution, People and Technology"
              >
                <defs>
                  <radialGradient id="bgGrad" cx="50%" cy="0%" r="90%">
                    <stop offset="0%" stopColor="#f7fbff" />
                    <stop offset="45%" stopColor="#eef4fa" />
                    <stop offset="100%" stopColor="#e7eef7" />
                  </radialGradient>

                  <radialGradient id="circleFill" cx="50%" cy="40%" r="70%">
                    <stop offset="0%" stopColor="rgba(0, 184, 196, 0.12)" />
                    <stop offset="70%" stopColor="rgba(0, 102, 204, 0.05)" />
                    <stop offset="100%" stopColor="transparent" />
                  </radialGradient>

                  <filter id="softShadow" x="-30%" y="-30%" width="160%" height="160%">
                    <feDropShadow dx="0" dy="20" stdDeviation="22" floodColor="#000000" floodOpacity="0.45" />
                  </filter>
                  {PILLARS.map((pillar) => (
                    <filter
                      key={pillar.id}
                      id={`glow-${pillar.id}`}
                      x="-50%"
                      y="-50%"
                      width="200%"
                      height="200%"
                    >
                      <feDropShadow
                        dx="0"
                        dy="0"
                        stdDeviation="16"
                        floodColor={`${GROUP_META[pillar.id as PillarId].accent}`}
                        floodOpacity="0.35"
                      />
                    </filter>
                  ))}
                </defs>

                <rect x="0" y="0" width="1200" height="900" fill="url(#bgGrad)" rx={28} />

                {/* Four main circles */}
                {PILLARS.map((pillar) => {
                  const active = activeGroup === null || activeGroup === pillar.id;
                  const accent = GROUP_META[pillar.id as PillarId].accent;

                  return (
                    <g
                      key={pillar.id}
                      onMouseEnter={onEnter(pillar.id)}
                      onMouseLeave={onLeave}
                      onFocus={onEnter(pillar.id)}
                      onBlur={onLeave}
                      tabIndex={0}
                      role="button"
                      aria-label={`${pillar.label} pillar highlights ${pillar.sub}`}
                      style={{ cursor: "pointer" }}
                      filter={`url(#${active ? `glow-${pillar.id}` : "softShadow"})`}
                    >
                      <circle
                        cx={pillar.cx}
                        cy={pillar.cy}
                        r={pillar.r}
                        fill="url(#circleFill)"
                        stroke={accent}
                        strokeWidth={active ? 3.6 : 1.4}
                        style={hi([pillar.id])}
                      />
                      <text
                        x={pillar.cx}
                        y={pillar.cy - 10}
                        textAnchor="middle"
                        fill={TEXT_MAIN}
                        fontSize={40}
                        letterSpacing="0.28em"
                        fontFamily="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
                        fontWeight={700}
                        style={hi([pillar.id])}
                      >
                        {pillar.label}
                      </text>
                      <text
                        x={pillar.cx}
                        y={pillar.cy + 26}
                        textAnchor="middle"
                        fill={TEXT_MUTED}
                        fontSize={16}
                        letterSpacing="0.2em"
                        style={hi([pillar.id])}
                      >
                        {pillar.sub.toUpperCase()}
                      </text>
                    </g>
                  );
                })}

                {/* AI Sweet Spot */}
                <g>
                  <circle cx={600} cy={450} r={95} fill="#f7f8fb" stroke="#f7f8fb" strokeWidth={2} />
                  <text x={600} y={443} textAnchor="middle" fill="#0f1115" fontSize={20} fontWeight={700}>
                    AI Sweet
                  </text>
                  <text x={600} y={470} textAnchor="middle" fill="#0f1115" fontSize={20} fontWeight={700}>
                    Spot
                  </text>
                </g>

                {/* Inner overlap labels */}
                <text
                  x={600}
                  y={230}
                  textAnchor="middle"
                  fill={TEXT_MUTED}
                  fontSize={16}
                  style={hi(["strategy", "execution"])}
                >
                  Fit for Purpose Systems
                </text>

                <text
                  x={855}
                  y={455}
                  textAnchor="middle"
                  fill={TEXT_MUTED}
                  fontSize={16}
                  style={hi(["execution", "technology"])}
                >
                  Measurable Business Results
                </text>

                <text
                  x={345}
                  y={455}
                  textAnchor="middle"
                  fill={TEXT_MUTED}
                  fontSize={16}
                  style={hi(["strategy", "people"])}
                >
                  Active Employee Engagement
                </text>

                <text
                  x={600}
                  y={705}
                  textAnchor="middle"
                  fill={TEXT_MUTED}
                  fontSize={16}
                  style={hi(["people", "technology"])}
                >
                  Up-to-date Skilled Workforce
                </text>

                {/* Small pill label helper */}
                {INITIATIVES.map((pill) =>
                  renderPill(pill, hi, (pill.groups[0] ?? null) as Group, setActiveGroup)
                )}

                {/* Legend */}
                <text
                  x={600}
                  y={880}
                  textAnchor="middle"
                  fill={TEXT_MUTED}
                  fontSize={12}
                  letterSpacing="0.18em"
                >
                  HOVER OVER ANY PILLAR OR LABEL TO HIGHLIGHT ITS AI INITIATIVES
                </text>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

function renderPill(
  pill: { x: number; y: number; width: number; height: number; label: string; groups: PillarId[] },
  hi: (groups: Group[]) => React.CSSProperties,
  primary: Group,
  setActive: (g: Group | null) => void
) {
  const rx = pill.height / 2;
  const cx = pill.x + pill.width / 2;
  const cy = pill.y + pill.height / 2;

  const accent = pill.groups.length === 1 ? GROUP_META[pill.groups[0]].accent : "#8fb3ff";
  const visibility = hi(pill.groups);

  return (
    <g
      key={pill.label}
      onMouseEnter={() => setActive(primary)}
      onMouseLeave={() => setActive(null)}
      onFocus={() => setActive(primary)}
      onBlur={() => setActive(null)}
      tabIndex={0}
      role="button"
      aria-label={`${pill.label} (${pill.groups.join(" & ")} initiative)`}
      style={{ ...hi(pill.groups), cursor: "pointer" }}
    >
      <rect
        x={pill.x}
        y={pill.y}
        width={pill.width}
        height={pill.height}
        rx={rx}
        ry={rx}
        fill="#ffffff"
        stroke={accent}
        strokeDasharray="5 5"
        opacity={visibility.opacity}
      />
      <text
        x={cx}
        y={cy + 4}
        textAnchor="middle"
        fill="#0f1b2d"
        fontSize={13}
        fontWeight={600}
        style={{ opacity: visibility.opacity }}
      >
        {pill.label}
      </text>
    </g>
  );
}
