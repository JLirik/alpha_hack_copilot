import React, { useState } from "react";
import MarkdownBlock from "./MarkdownBlock";
import { motion } from "framer-motion";
import "./post.css";

export default function MarketingPostCard({ styleType, body }) {
  const [likes, setLikes] = useState(Math.floor(Math.random() * 100 + 15));

  const styleClass = {
    standard: "mkt-alpha-standard",
    creative: "mkt-alpha-creative",
    insane: "mkt-alpha-insane"
  }[styleType];

  return (
    <motion.div
      className={`post-card marketing ${styleClass}`}
      initial={{ opacity: 0, scale: 0.96 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.4, ease: "easeOut" }}
      whileHover={{ scale: 1.015 }}
    >
      <div className="alpha-header">
        <div className="alpha-icon red">A</div>
        <h2>Маркетинг • {styleType}</h2>
      </div>

      <div className="post-body">
        <MarkdownBlock text={body} />
      </div>

      <div className="alpha-footer">
        <button
          className="alpha-like"
          onClick={() => setLikes(likes + 1)}
        >
          ♥ {likes}
        </button>
      </div>
    </motion.div>
  );
}
