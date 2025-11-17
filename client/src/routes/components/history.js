export function loadHistory() {
    const raw = localStorage.getItem("alpha_history");
    if (!raw) return [];
    try {
        return JSON.parse(raw);
    } catch {
        return [];
    }
}

export function saveHistory(history) {
    localStorage.setItem("alpha_history", JSON.stringify(history));
}

export function addToHistory(item) {
    const history = loadHistory();
    const updated = [item, ...history].slice(0, 10);
    saveHistory(updated);
}
