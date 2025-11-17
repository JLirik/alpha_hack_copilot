import { useMemo } from 'react';
import ReactMarkdown from 'react-markdown';
import rehypeRaw from 'rehype-raw';
import katex from 'katex';
import 'katex/dist/katex.min.css';

export default function LatexRenderer({ content }) {
    const parsedContent = useMemo(() => {
        if (!content) {
            return '';
        }

        let processedText = content;

        const renderKatex = (formula, displayMode) => {
            try {
                return katex.renderToString(formula, {
                    displayMode: displayMode,
                    throwOnError: false,
                    output: 'html',
                });
            } catch (error) {
                console.error('KaTeX rendering error:', error);
                return `<span>${formula}</span>`;
            }
        };

        processedText = processedText.replace(/\$\$(.*?)\$\$/gs, (match, formula) => {
            return renderKatex(formula, true);
        });

        processedText = processedText.replace(/\$(.*?)\$/g, (match, formula) => {
            // Avoid matching $$...$$ again
            if (match.startsWith('$$') && match.endsWith('$$')) {
                return match;
            }
            return renderKatex(formula, false);
        });

        return processedText;

    }, [content]);
    return (
        <ReactMarkdown rehypePlugins={[rehypeRaw]}>
            {parsedContent}
        </ReactMarkdown>
    );
};