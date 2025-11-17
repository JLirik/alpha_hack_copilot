import React from "react";
import MarkdownBlock from "./MarkdownBlock";
import { motion } from "framer-motion";
import "./post.css";

export default function PostCard({ title, body }) {
  return (
    <motion.div
      className="post-card alpha-card"
      initial={{ opacity: 0, y: 12 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.35, ease: "easeOut" }}
    >
      <div className="alpha-header">
        <div className="alpha-icon">A</div>
        <h2>{title}</h2>
      </div>

      <div className="post-body">
        <MarkdownBlock text={body} />
      </div>
    </motion.div>
  );
}
