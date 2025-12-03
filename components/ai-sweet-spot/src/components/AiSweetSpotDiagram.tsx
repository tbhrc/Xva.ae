import React, { useState } from "react";

type Group = "strategy" | "execution" | "people" | "technology" | null;

const PILLAR_COLOUR = "#f5f5f5";
const PILLAR_MUTED = "rgba(220,220,220,0.28)";
const TEXT_MAIN = "#f5f5f5";
const TEXT_MUTED = "#c0c0c0";
const BG = "#050505";

const useHighlight = (active: Group) => {
  return (groups: Group[]) => {
    if (active === null) return { opacity: 1 };
    return { opacity: groups.includes(active) ? 1 : 0.25 };
  };
};

export const AiSweetSpotDiagram: React.FC = () => {
  const [activeGroup, setActiveGroup] = useState<Group>(null);
  const hi = useHighlight(activeGroup);

  const onEnter = (group: Group) => () => setActiveGroup(group);
  const onLeave = () => setActiveGroup(null);

  return (
    <div className="diagram-container">
      <svg
        viewBox="0 0 1200 900"
        className="diagram-svg"
        role="img"
        aria-label="AI Sweet Spot diagram showing Strategy, Execution, People and Technology"
      >
        <defs>
          <radialGradient id="bgGrad" cx="50%" cy="0%" r="90%">
            <stop offset="0%" stopColor="#202020" />
            <stop offset="50%" stopColor="#050505" />
            <stop offset="100%" stopColor="#000000" />
          </radialGradient>

          <radialGradient id="circleFill" cx="50%" cy="40%" r="70%">
            <stop offset="0%" stopColor="rgba(255,255,255,0.08)" />
            <stop offset="70%" stopColor="rgba(255,255,255,0.01)" />
            <stop offset="100%" stopColor="transparent" />
          </radialGradient>
        </defs>

        <rect x="0" y="0" width="1200" height="900" fill="url(#bgGrad)" />

        {/* Four main circles */}
        <g
          onMouseEnter={onEnter("strategy")}
          onMouseLeave={onLeave}
          onFocus={onEnter("strategy")}
          onBlur={onLeave}
          tabIndex={0}
          role="button"
          aria-label="Strategy pillar – highlights strategy-related initiatives"
          style={{ cursor: "pointer" }}
        >
          <circle
            cx={380}
            cy={300}
            r={260}
            fill="url(#circleFill)"
            stroke={PILLAR_COLOUR}
            strokeWidth={2}
            style={{
              ...hi(["strategy"]),
            }}
          />
          <text
            x={380}
            y={290}
            textAnchor="middle"
            fill={TEXT_MAIN}
            fontSize={40}
            letterSpacing="0.3em"
            fontFamily="system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif"
            fontWeight={700}
            style={hi(["strategy"])}
          >
            STRATEGY
          </text>
          <text
            x={380}
            y={320}
            textAnchor="middle"
            fill={TEXT_MUTED}
            fontSize={16}
            letterSpacing="0.22em"
            style={hi(["strategy"])}
          >
            AI STRATEGIC ROADMAP
          </text>
        </g>

        <g
          onMouseEnter={onEnter("execution")}
          onMouseLeave={onLeave}
          onFocus={onEnter("execution")}
          onBlur={onLeave}
          tabIndex={0}
          role="button"
          aria-label="Execution pillar – highlights execution-related initiatives"
          style={{ cursor: "pointer" }}
        >
          <circle
            cx={820}
            cy={300}
            r={260}
            fill="url(#circleFill)"
            stroke={PILLAR_COLOUR}
            strokeWidth={2}
            style={hi(["execution"])}
          />
          <text
            x={820}
            y={290}
            textAnchor="middle"
            fill={TEXT_MAIN}
            fontSize={40}
            letterSpacing="0.3em"
            fontWeight={700}
            style={hi(["execution"])}
          >
            EXECUTION
          </text>
          <text
            x={820}
            y={320}
            textAnchor="middle"
            fill={TEXT_MUTED}
            fontSize={16}
            letterSpacing="0.22em"
            style={hi(["execution"])}
          >
            AI-ENABLED EXECUTION
          </text>
        </g>

        <g
          onMouseEnter={onEnter("people")}
          onMouseLeave={onLeave}
          onFocus={onEnter("people")}
          onBlur={onLeave}
          tabIndex={0}
          role="button"
          aria-label="People pillar – highlights people-related initiatives"
          style={{ cursor: "pointer" }}
        >
          <circle
            cx={380}
            cy={600}
            r={260}
            fill="url(#circleFill)"
            stroke={PILLAR_COLOUR}
            strokeWidth={2}
            style={hi(["people"])}
          />
          <text
            x={380}
            y={590}
            textAnchor="middle"
            fill={TEXT_MAIN}
            fontSize={40}
            letterSpacing="0.3em"
            fontWeight={700}
            style={hi(["people"])}
          >
            PEOPLE
          </text>
          <text
            x={380}
            y={620}
            textAnchor="middle"
            fill={TEXT_MUTED}
            fontSize={16}
            letterSpacing="0.22em"
            style={hi(["people"])}
          >
            AI-POWERED PEOPLE
          </text>
        </g>

        <g
          onMouseEnter={onEnter("technology")}
          onMouseLeave={onLeave}
          onFocus={onEnter("technology")}
          onBlur={onLeave}
          tabIndex={0}
          role="button"
          aria-label="Technology pillar – highlights technology-related initiatives"
          style={{ cursor: "pointer" }}
        >
          <circle
            cx={820}
            cy={600}
            r={260}
            fill="url(#circleFill)"
            stroke={PILLAR_COLOUR}
            strokeWidth={2}
            style={hi(["technology"])}
          />
          <text
            x={820}
            y={590}
            textAnchor="middle"
            fill={TEXT_MAIN}
            fontSize={40}
            letterSpacing="0.3em"
            fontWeight={700}
            style={hi(["technology"])}
          >
            TECHNOLOGY
          </text>
          <text
            x={820}
            y={620}
            textAnchor="middle"
            fill={TEXT_MUTED}
            fontSize={16}
            letterSpacing="0.22em"
            style={hi(["technology"])}
          >
            AI-INTEGRATED TECHNOLOGY
          </text>
        </g>

        {/* AI Sweet Spot */}
        <g>
          <circle
            cx={600}
            cy={450}
            r={90}
            fill="#ffffff"
            stroke="#ffffff"
            strokeWidth={2}
          />
          <text
            x={600}
            y={440}
            textAnchor="middle"
            fill="#000000"
            fontSize={20}
            fontWeight={700}
          >
            AI Sweet
          </text>
          <text
            x={600}
            y={465}
            textAnchor="middle"
            fill="#000000"
            fontSize={20}
            fontWeight={700}
          >
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
        {renderPill(230, 110, 170, 40, "Unstoppable Company Game", ["strategy"], hi, setActiveGroup)}
        {renderPill(400, 100, 260, 40, "AI Strategic & Execution Roadmap Workshop", ["strategy"], hi, setActiveGroup)}
        {renderPill(655, 100, 160, 40, "HTC Campaign", ["strategy"], hi, setActiveGroup)}
        {renderPill(820, 120, 220, 40, "End in Mind Process Mapping", ["strategy", "execution"], hi, setActiveGroup)}
        {renderPill(955, 140, 180, 40, "AI Command Room", ["execution"], hi, setActiveGroup)}

        {renderPill(990, 290, 120, 40, "OKRx", ["execution"], hi, setActiveGroup)}
        {renderPill(1010, 390, 190, 40, "DDDEEE Framework", ["execution", "technology"], hi, setActiveGroup)}
        {renderPill(1010, 520, 180, 40, "SaaS Audit Review", ["technology"], hi, setActiveGroup)}
        {renderPill(980, 625, 190, 40, "Data Audit Review", ["technology"], hi, setActiveGroup)}
        {renderPill(830, 685, 260, 40, "AI Agents + Automation Integration", ["technology"], hi, setActiveGroup)}
        {renderPill(550, 745, 170, 40, "Use Case Library", ["technology"], hi, setActiveGroup)}

        {renderPill(210, 390, 160, 40, "AI Agility Check", ["strategy", "people"], hi, setActiveGroup)}
        {renderPill(165, 505, 170, 40, "Innovators Culture", ["people"], hi, setActiveGroup)}
        {renderPill(165, 615, 150, 40, "Critical Thinking", ["people"], hi, setActiveGroup)}
        {renderPill(240, 730, 150, 40, "Upskilling", ["people"], hi, setActiveGroup)}
        {renderPill(345, 770, 160, 40, "Access to Talent", ["people"], hi, setActiveGroup)}

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
  );
};

function renderPill(
  x: number,
  y: number,
  width: number,
  height: number,
  label: string,
  groups: Group[],
  hi: (groups: Group[]) => React.CSSProperties,
  setActive: (g: Group | null) => void
) {
  const rx = height / 2;
  const cx = x + width / 2;
  const cy = y + height / 2;

  return (
    <g
      key={label}
      onMouseEnter={() => setActive(groups[0] ?? null)}
      onMouseLeave={() => setActive(null)}
      onFocus={() => setActive(groups[0] ?? null)}
      onBlur={() => setActive(null)}
      tabIndex={0}
      role="button"
      aria-label={`${label} (${groups.filter(Boolean).join(" & ")} initiative)`}
      style={{ ...hi(groups), cursor: "pointer" }}
    >
      <rect
        x={x}
        y={y}
        width={width}
        height={height}
        rx={rx}
        ry={rx}
        fill="rgba(5,5,5,0.8)"
        stroke="rgba(220,220,220,0.7)"
        strokeDasharray="4 4"
      />
      <text
        x={cx}
        y={cy + 4}
        textAnchor="middle"
        fill={TEXT_MUTED}
        fontSize={13}
      >
        {label}
      </text>
    </g>
  );
}
