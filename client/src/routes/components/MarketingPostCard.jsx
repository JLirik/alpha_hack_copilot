import React from "react";
import MarkdownBlock from "./MarkdownBlock";
import "./post.css";

export default function MarketingPostCard({ styleType, body }) {
  const classMap = {
    standard: "mkt-standard",
    creative: "mkt-creative",
    insane: "mkt-insane"
  };

  return (
    <div className={`post-card marketing ${classMap[styleType]}`}>
      <div className="alpha-header">
        <div className="alpha-icon red">A</div>
        <h2>Маркетинг • {styleType}</h2>
      </div>

      <MarkdownBlock text={body} />
    </div>
  );
}
