import React, { useState } from "react";
import MarkdownBlock from "./MarkdownBlock";
import "./post.css";

export default function MarketingPostCard({ styleType, body }) {
  const [likes, setLikes] = useState( Math.floor(Math.random() * 200) + 5 );
  const [comments] = useState( Math.floor(Math.random() * 20) );

  const themeClass = {
    standard: "mkt-standard",
    creative: "mkt-creative",
    insane: "mkt-insane"
  }[styleType];

  return (
    <div className={`post-card marketing ${themeClass}`}>
      <div className="post-body">
        <MarkdownBlock text={body} />
      </div>

      <div className="post-footer">
        <button onClick={() => setLikes(likes + 1)}>❤️ {likes}</button>
        <span>{comments}</span>
      </div>
    </div>
  );
}
