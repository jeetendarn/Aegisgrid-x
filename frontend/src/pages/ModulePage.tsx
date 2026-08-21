import { useEffect, useState } from "react";
import { api } from "../services/api";
import type { ApiItem } from "../types/api";

interface ModulePageProps {
  title: string;
  description: string;
  endpoint: string;
}

export default function ModulePage({
  title,
  description,
  endpoint,
}: ModulePageProps) {
  const [items, setItems] = useState<ApiItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  useEffect(() => {
    setLoading(true);
    setError(false);

    api
      .get(endpoint)
      .then((response) => {
        setItems(Array.isArray(response.data) ? response.data : []);
      })
      .catch(() => {
        setError(true);
        setItems([]);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [endpoint]);

  return (
    <section className="module-page">
      <header className="module-header">
        <div>
          <h1>{title}</h1>
          <p>{description}</p>
        </div>

        <div className="module-status">
          {loading ? "LOADING" : error ? "ERROR" : "ONLINE"}
        </div>
      </header>

      {error && (
        <div className="error-panel">
          Unable to retrieve data from the AegisGrid X backend.
        </div>
      )}

      {!loading && !error && items.length === 0 && (
        <div className="empty-panel">
          <strong>No records available</strong>
          <span>The backend currently contains no records for this module.</span>
        </div>
      )}

      {!loading && items.length > 0 && (
        <div className="data-grid">
          {items.map((item, index) => (
            <article className="data-card" key={String(item.id ?? index)}>
              <div className="data-card-header">
                <strong>
                  {String(item.name ?? item.title ?? item.id ?? `Record ${index + 1}`)}
                </strong>

                <span>#{index + 1}</span>
              </div>

              <div className="data-fields">
                {Object.entries(item)
                  .filter(([, value]) => value !== null && value !== undefined)
                  .slice(0, 6)
                  .map(([key, value]) => (
                    <div className="data-field" key={key}>
                      <span>{key.replaceAll("_", " ")}</span>
                      <strong>
                        {typeof value === "object"
                          ? JSON.stringify(value)
                          : String(value)}
                      </strong>
                    </div>
                  ))}
              </div>
            </article>
          ))}
        </div>
      )}
    </section>
  );
}
