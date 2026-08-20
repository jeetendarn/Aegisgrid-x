import { useEffect, useState } from "react";
import { api, endpoints } from "../services/api";
import type { HealthResponse } from "../types/api";

const modules = [
  ["Branches", endpoints.branches],
  ["Networks", endpoints.networks],
  ["Devices", endpoints.devices],
  ["Assets", endpoints.assets],
  ["Applications", endpoints.applications],
  ["Incidents", endpoints.incidents],
  ["MITRE ATT&CK", endpoints.mitre],
  ["Sigma Rules", endpoints.sigma],
  ["YARA Rules", endpoints.yara],
  ["Threat Intelligence", endpoints.threatIntelligence],
  ["Security Events", endpoints.events],
];

export default function Dashboard() {
  const [health, setHealth] = useState<HealthResponse | null>(null);
  const [counts, setCounts] = useState<Record<string, number>>({});

  useEffect(() => {
    api.get<HealthResponse>(endpoints.health)
      .then((res) => setHealth(res.data))
      .catch(() => setHealth(null));

    Promise.all(
      modules.map(async ([name, endpoint]) => {
        try {
          const response = await api.get(endpoint);
          const data = Array.isArray(response.data) ? response.data : [];
          return [name, data.length] as const;
        } catch {
          return [name, 0] as const;
        }
      })
    ).then((results) => {
      setCounts(Object.fromEntries(results));
    });
  }, []);

  return (
    <div className="dashboard">
      <header>
        <h1>AegisGrid X</h1>
        <p>Zero-Trust Cyber Range & Enterprise Security Fabric</p>
      </header>

      <section className="system-status">
        <strong>Backend:</strong>{" "}
        {health?.status === "ok" ? "ONLINE" : "OFFLINE"}
      </section>

      <section className="module-grid">
        {modules.map(([name]) => (
          <article className="module-card" key={name}>
            <h3>{name}</h3>
            <div className="module-count">
              {counts[name] ?? 0}
            </div>
            <span>Records</span>
          </article>
        ))}
      </section>
    </div>
  );
}
