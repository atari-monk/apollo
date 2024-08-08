document.addEventListener("DOMContentLoaded", () => {
    // Function to observe mutations
    function observeCodeBlocks() {
        const codeBlocks = document.querySelectorAll("pre code");
        codeBlocks.forEach((block) => {
            const button = document.createElement("button");
            button.className = "copy-btn";
            button.textContent = "Copy";
            button.addEventListener("click", () => {
                navigator.clipboard.writeText(block.textContent).then(() => {
                    button.textContent = "Copied!";
                    setTimeout(() => (button.textContent = "Copy"), 2000);
                });
            });
            block.parentElement.style.position = "relative";
            block.parentElement.appendChild(button);
        });
    }

    // Create a MutationObserver to watch for changes in the DOM
    const observer = new MutationObserver((mutationsList) => {
        for (const mutation of mutationsList) {
            if (mutation.type === "childList") {
                observeCodeBlocks(); // Re-run your function when DOM changes
            }
        }
    });

    // Start observing the document body for changes
    observer.observe(document.body, { childList: true, subtree: true });

    // Initial call to handle existing code blocks
    observeCodeBlocks();
});
