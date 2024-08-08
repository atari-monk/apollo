function addCopyButtonsToCodeBlocks() {
    const codeBlocks = document.querySelectorAll("pre code");

    codeBlocks.forEach((block) => {
        if (!block.classList.contains("copy-btn-attached")) {
            const button = document.createElement("button");
            button.className = "copy-btn";
            button.textContent = "Copy";
            button.addEventListener("click", () => {
                navigator.clipboard.writeText(block.textContent).then(() => {
                    button.textContent = "Copied!";
                    setTimeout(() => (button.textContent = "Copy"), 2000);
                });
            });

            block.classList.add("copy-btn-attached");
            block.parentElement.style.position = "relative";
            block.parentElement.appendChild(button);
        }
    });
}

addCopyButtonsToCodeBlocks();
