const API_BASE = import.meta.env.VITE_API_BASE_URL ?? 'http://127.0.0.1:8000';
export async function getApiHealth(): Promise<{status:string}> {
  const response = await fetch(`${API_BASE}/api/health`);
  if (!response.ok) throw new Error(`API health request failed (${response.status})`);
  return response.json();
}
export async function validateSessionSummary(summary: unknown) {
  const response = await fetch(`${API_BASE}/api/results/validate`, {method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(summary)});
  if (!response.ok) throw new Error(`Summary validation failed (${response.status})`);
  return response.json();
}
