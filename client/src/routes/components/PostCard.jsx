import React from "react";
import MarkdownBlock from "./MarkdownBlock";
import "./post.css";

export default function PostCard({ title, body }) {
  return (
    <div className="post-card alpha-card">
      <div className="alpha-header">
        <div className="alpha-icon">A</div>
        <h2>{title}</h2>
      </div>

      <MarkdownBlock text={body} />
    </div>
  );
}
