const API_BASE = "http://localhost:САША_КРУТ!!!"; // поменяйте при деплое

export async function fetchHistory() {
    try {
        const response = await fetch(`${API_BASE}/api/history`);
        if (!response.ok) return [];
        return await response.json();
    } catch (e) {
        console.error("Ошибка загрузки истории:", e);
        return [];
    }
}

export async function addHistoryRecord(record) {
    try {
        await fetch(`${API_BASE}/api/history`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(record)
        });
    } catch (e) {
        console.error("Ошибка сохранения истории:", e);
    }
}
