import MarketingPostCard from "./components/MarketingPostCard"
import { useParams } from "react-router";
import { Spinner } from "react-bootstrap";
import { useState, useEffect } from "react";
import fetcher from "./methods/Fetcher";

function MarketingIdeas() {
    const { requestId } = useParams();
    const [posts, setPosts] = useState();

    useEffect(() => {
        async function loadPosts() {
            try {
                const response = await fetcher("query/marketing/regenerate", {"contentId": requestId}, 'POST');
                if (response) {
                    setPosts(response);
                }
            } catch (err) {
                console.error(err);
                alert('Неизвестная ошибка')
            }
        }

        loadPosts()
    }, [])

    const returnAnswer = () => {
        if (posts) {
            const answer = posts.answer;
            return JSON.parse(answer).map((key, item) => (
                    <MarketingPostCard styleType={key} body={item.answer} key={key} />
                ))
            } 
         else {
                return <Spinner animation="border" />;
            }
    }
    return (
        <>
            <h1>Маркетинг</h1>
            {returnAnswer()}
        </>
    )
}

export default MarketingIdeas;
