import React, { useEffect, useState } from "react";
import { fetchHistory } from "./historyApi";
import HistoryItem from "./HistoryItem";
import "./history.css";

export default function HistoryList({ data, loading }) {
    return (
        <div className="history-container">
            <h3 className="history-title">История запросов</h3>

            {data.length === 0 ? (
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
