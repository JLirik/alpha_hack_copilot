import MarkdownBlock from "./MarkdownBlock";
import "./post.css";
import { useNavigate } from 'react-router';


export default function MarketingPostCard({ styleType, body, requestId }) {
  let navigate = useNavigate();
  const classMap = {
    standard: "mkt-standard",
    creative: "mkt-creative",
    insane: "mkt-insane"
  };

  return (
    <div className={`post-card marketing ${classMap[styleType]}`} onClick={() => navigate("/marketing/" + requestId)}>
      <div className="alpha-header">
        <div className="alpha-icon red">A</div>
        <h2>Маркетинг • {styleType}</h2>
      </div>

      <MarkdownBlock text={body} />
    </div>
  );
}
