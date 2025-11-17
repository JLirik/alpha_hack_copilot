import React, { useEffect, useState } from "react";
import { loadHistory } from "./history";
import "./history.css";

export default function HistoryList() {
    const [data, setData] = useState([]);

    useEffect(() => {
        setData(loadHistory());
    }, []);

    if (data.length === 0) {
        return (
            <div className="history-container">
                <h3 className="history-title">История запросов</h3>
                <p>Пока пусто. Попробуйте задать вопрос!</p>
            </div>
        );
    }

    return (
        <div className="history-container">
            <h3 className="history-title">История запросов</h3>
            <div className="history-list">
                {data.map((item, idx) => (
                    <div className="history-item" key={idx}>
                        <div className="history-item-time">
                            {new Date(item.timestamp).toLocaleString()}
                        </div>

                        <div className="history-item-query">
                            {item.query}
                        </div>

                        <div className="history-item-answer">
                            {item.answer}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    );
}
