import React from "react";
import MarkdownBlock from "./MarkdownBlock";
import "./post.css";

export default function PostCard({ title, body }) {
  return (
    <div className="post-card">
      <div className="post-header">
        <h2>{title}</h2>
      </div>

      <div className="post-body">
        <MarkdownBlock text={body} />
      </div>
    </div>
  );
}
