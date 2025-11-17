import { Accordion } from "react-bootstrap";
import HistoryItem from "./HistoryItem";
import "./history.css";

export default function HistoryList({ data }) {
    return (
        <div className="history-container">
            <h3 className="history-title">История запросов</h3>

            {data.length === 0 ? (
                <p>История пока пуста</p>
            ) : (
                <Accordion className="history-list">
                    {data.map((item) => (
                        <HistoryItem item={item} key={item.id} />
                    ))}
                </Accordion>
            )}
        </div>
    );
}
