export interface HealthResponse {
  status: string;
  service: string;
}

export interface ApiItem {
  id?: string;
  name?: string;
  [key: string]: unknown;
}
