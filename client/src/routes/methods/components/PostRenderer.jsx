import React from "react";
import PostCard from "./PostCard";
import MarketingPostCard from "./MarketingPostCard";

export default function PostRenderer({ data }) {
  // HIRING CASE
  if (data.answer_type === "hire") {
    return (
      <>
        <PostCard title="Formal" body={data.formal} />
        <PostCard title="Friendly" body={data.friendly} />
        <PostCard title="Sales" body={data.sales} />
      </>
    );
  }

  // MARKETING
  if (data.answer_type === "marketing") {
    const styles = ["standard", "creative", "insane"];

    return (
      <>
        {styles.map((style) => (
          <MarketingPostCard
            key={style}
            styleType={style}
            body={data[style]}
          />
        ))}
      </>
    );
  }

  // FINANCE, LAW, GENERAL - simple card
  return (
    <PostCard
      title={data.answer_type.toUpperCase()}
      body={data.answer}
    />
  );
}
