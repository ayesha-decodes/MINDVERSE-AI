export const median = (values: number[]) => { if (!values.length) return null; const s=[...values].sort((a,b)=>a-b); const m=Math.floor(s.length/2); return s.length%2?s[m]:(s[m-1]+s[m])/2; };
export const accuracy = (correct: number, total: number) => total > 0 ? Math.round((correct / total) * 100) : null;
export const csvEscape = (v: unknown) => `"${String(v ?? '').replaceAll('"','""')}"`;
