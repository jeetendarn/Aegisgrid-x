import { BrowserRouter, Routes, Route } from "react-router-dom";
import AppLayout from "./layouts/AppLayout";
import Dashboard from "./pages/Dashboard";

function Placeholder({ title }: { title: string }) {
  return (
    <div>
      <h1>{title}</h1>
      <p>Module connected to the AegisGrid X backend.</p>
    </div>
  );
}

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route element={<AppLayout />}>
          <Route path="/" element={<Dashboard />} />

          <Route path="/branches" element={<Placeholder title="Branches" />} />
          <Route path="/networks" element={<Placeholder title="Networks" />} />
          <Route path="/devices" element={<Placeholder title="Devices" />} />
          <Route path="/assets" element={<Placeholder title="Assets" />} />
          <Route path="/applications" element={<Placeholder title="Applications" />} />
          <Route path="/incidents" element={<Placeholder title="Incidents" />} />
          <Route path="/mitre" element={<Placeholder title="MITRE ATT&CK" />} />
          <Route path="/sigma" element={<Placeholder title="Sigma Rules" />} />
          <Route path="/yara" element={<Placeholder title="YARA Rules" />} />
          <Route
            path="/threat-intelligence"
            element={<Placeholder title="Threat Intelligence" />}
          />
          <Route path="/events" element={<Placeholder title="Security Events" />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
