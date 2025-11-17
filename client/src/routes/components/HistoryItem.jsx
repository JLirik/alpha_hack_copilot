import React, { useState, useRef, useEffect } from "react";
import "./history.css";

export default function HistoryItem({ item }) {
    const [open, setOpen] = useState(false);
    const contentRef = useRef(null);
    const [height, setHeight] = useState("0px");
    console.log(item);
    useEffect(() => {
        if (open) {
            setHeight(`${contentRef.current.scrollHeight}px`);
        } else {
            setHeight("0px");
        }
    }, [open]);

    return (
        <div 
            className={`history-item ${open ? "open" : ""}`}
            onClick={() => setOpen(!open)}
        >
            <div className="history-header">
                <div className="history-item-time">
                    {new Date(item.createdAt).toLocaleDateString()}
                </div>

                <div className="history-item-query">
                    {item.prompt}
                </div>

                <div className={`arrow ${open ? "rotated" : ""}`}>▸</div>
            </div>

            <div className="history-content-wrapper" style={{ maxHeight: height }}>
                <div ref={contentRef} className="history-content">
                    <div className="history-item-answer">
                        {item.answer}
                    </div>
                </div>
            </div>
        </div>
    );
}
