import MarketingPostCard from "./methods/components/MarketingPostCard"


function Marketing() {
    return (
        <>
            <h1>Marketing!</h1>
            <MarketingPostCard 
                styleType="creative"
                body={"Для решения задачи определим ежемесячные платежи, при которых сумма долга уменьшается равномерно (линейно)."}
            />
        </>
    )
}

export default Marketing