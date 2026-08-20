import { NavLink, Outlet } from "react-router-dom";

const navigation = [
  ["Dashboard", "/"],
  ["Branches", "/branches"],
  ["Networks", "/networks"],
  ["Devices", "/devices"],
  ["Assets", "/assets"],
  ["Applications", "/applications"],
  ["Incidents", "/incidents"],
  ["MITRE ATT&CK", "/mitre"],
  ["Sigma Rules", "/sigma"],
  ["YARA Rules", "/yara"],
  ["Threat Intelligence", "/threat-intelligence"],
  ["Events", "/events"],
];

export default function AppLayout() {
  return (
    <div className="app">
      <aside>
        <div className="logo">AEGISGRID X</div>

        <nav>
          {navigation.map(([label, path]) => (
            <NavLink
              key={path}
              to={path}
              className={({ isActive }) =>
                isActive ? "active" : ""
              }
            >
              {label}
            </NavLink>
          ))}
        </nav>
      </aside>

      <main>
        <Outlet />
      </main>
    </div>
  );
}
