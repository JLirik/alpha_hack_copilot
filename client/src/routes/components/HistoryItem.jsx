import React, { useState, useRef, useEffect } from "react";
import { Accordion } from "react-bootstrap";
import "./history.css";

export default function HistoryItem({ item }) {
    const contentRef = useRef(null);
    console.log(item);

    return (
            <Accordion.Item eventKey={item.requestId}>
                <Accordion.Header className="history-header">
                    <div className="history-item-time">
                        {new Date(item.createdAt).toLocaleDateString()}
                    </div>

                    <div className="history-item-query">
                        {item.prompt}
                    </div></Accordion.Header>
                <Accordion.Body>
                        {item.answer}
                </Accordion.Body>
            </Accordion.Item>
    );
}
