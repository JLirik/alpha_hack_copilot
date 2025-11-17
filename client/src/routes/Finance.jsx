import SearchBar from "./methods/SearchBar"
import LatexRenderer from "./methods/LatexRenderer"
import { LatexExample } from "./methods/LatexExample"

function Finance() {
    return (
    <>
    <h1>Finance!</h1>
    <LatexRenderer latex={LatexExample} />
    <SearchBar apiEndpoint="finance"/>
    </>
    )
}

export default Finance