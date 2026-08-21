import { BrowserRouter, Routes, Route } from "react-router-dom";

import AppLayout from "./layouts/AppLayout";
import Dashboard from "./pages/Dashboard";
import ModulePage from "./pages/ModulePage";
import { endpoints } from "./services/api";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>

          <Route path="/" element={<Dashboard />} />

          <Route
            path="/branches"
            element={
              <ModulePage
                title="Branches"
                description="Enterprise branch infrastructure and locations."
                endpoint={endpoints.branches}
              />
            }
          />

          <Route
            path="/networks"
            element={
              <ModulePage
                title="Networks"
                description="Network zones, segmentation and enterprise connectivity."
                endpoint={endpoints.networks}
              />
            }
          />

          <Route
            path="/devices"
            element={
              <ModulePage
                title="Devices"
                description="Managed endpoints, servers and connected infrastructure."
                endpoint={endpoints.devices}
              />
            }
          />

          <Route
            path="/assets"
            element={
              <ModulePage
                title="Assets"
                description="Enterprise assets monitored by AegisGrid X."
                endpoint={endpoints.assets}
              />
            }
          />

          <Route
            path="/applications"
            element={
              <ModulePage
                title="Applications"
                description="Applications and workloads protected by the security fabric."
                endpoint={endpoints.applications}
              />
            }
          />

          <Route
            path="/incidents"
            element={
              <ModulePage
                title="Incidents"
                description="Security incidents requiring investigation and response."
                endpoint={endpoints.incidents}
              />
            }
          />

          <Route
            path="/mitre"
            element={
              <ModulePage
                title="MITRE ATT&CK"
                description="Adversary tactics, techniques and detection coverage."
                endpoint={endpoints.mitre}
              />
            }
          />

          <Route
            path="/sigma"
            element={
              <ModulePage
                title="Sigma Rules"
                description="Detection rules for identifying suspicious activity."
                endpoint={endpoints.sigma}
              />
            }
          />

          <Route
            path="/yara"
            element={
              <ModulePage
                title="YARA Rules"
                description="Malware and threat detection signatures."
                endpoint={endpoints.yara}
              />
            }
          />

          <Route
            path="/threat-intelligence"
            element={
              <ModulePage
                title="Threat Intelligence"
                description="Threat indicators and intelligence records."
                endpoint={endpoints.threatIntelligence}
              />
            }
          />

          <Route
            path="/events"
            element={
              <ModulePage
                title="Security Events"
                description="Security telemetry collected by AegisGrid X."
                endpoint={endpoints.events}
              />
            }
          />

        </Route>
      </Routes>
    </BrowserRouter>
  );
}
