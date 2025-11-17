import MarketingPostCard from "./components/MarketingPostCard";
import SearchBar from "./components/SearchBar";

function Marketing() {
    const returnAnswer = () => {
        const stored = localStorage.getItem("answer");
        if (!stored) return null;

        let data;
        try {
            data = JSON.parse(stored);
        } catch {
            return null; 
        }

        if (data.answerType !== "marketing") return null;

        const answer = data.answer;

        if (typeof answer === "object") {
            return Object.entries(answer).map(([key, item]) => (
                <MarketingPostCard
                    key={item.requestId || key}
                    styleType={key}
                    body={item.answer}
                    requestId={item.requestId}
                />
            ));
        }

        return (
            <MarketingPostCard
                body={answer}
                styleType={'creative'}
                requestId={data.requestId}
            />
        );
    };

    return (
        <>
            <h1>Маркетинг</h1>
            {returnAnswer()}
            <SearchBar apiEndpoint="query/marketing/generate" />
        </>
    );
}

export default Marketing;