import axios from "axios";

export const api = axios.create({
  baseURL: "http://127.0.0.1:8000",
  headers: {
    "Content-Type": "application/json",
  },
});

export const endpoints = {
  health: "/health",
  branches: "/branches/",
  networks: "/networks/",
  devices: "/devices/",
  assets: "/assets/",
  applications: "/applications/",
  incidents: "/incidents/",
  mitre: "/mitre/",
  sigma: "/sigma/",
  yara: "/yara/",
  threatIntelligence: "/threat-intelligence/",
  events: "/events/",
};
