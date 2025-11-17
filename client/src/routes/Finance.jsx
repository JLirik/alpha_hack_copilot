import SearchBar from "./components/SearchBar"
import LatexRenderer from "./methods/LatexRenderer"
import { LatexExample } from "./methods/LatexExample"

function Finance() {
    return (
    <>
    <h1>Finance!</h1>
    <LatexRenderer content={LatexExample}> </LatexRenderer>
    <SearchBar apiEndpoint="finance"/>
    </>
    )
}

export default Finance