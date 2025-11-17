import React, { useEffect, useState } from "react";
import { fetchHistory } from "../../api/historyApi";
import HistoryItem from "./HistoryItem";
import "./history.css";

export default function HistoryList() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    async function load() {
        setLoading(true);
        const items = await fetchHistory();
        setData(items);
        setLoading(false);
    }

    useEffect(() => {
        load();
    }, []);

    return (
        <div className="history-container">
            <h3 className="history-title">История запросов</h3>

            {loading ? (
                <p>Загрузка...</p>
            ) : data.length === 0 ? (
                <p>История пока пуста</p>
            ) : (
                <div className="history-list">
                    {data.map((item) => (
                        <HistoryItem item={item} key={item.id} />
                    ))}
                </div>
            )}
        </div>
    );
}
