function addCopyButtonsToCodeBlocks() {
    const codeBlocks = document.querySelectorAll("pre code");

    codeBlocks.forEach((block) => {
        // Ensure button is only added once
        if (!block.parentElement.querySelector(".copy-btn")) {
            const button = document.createElement("button");
            button.className = "copy-btn";
            button.textContent = "Copy";
            button.addEventListener("click", () => {
                navigator.clipboard.writeText(block.textContent).then(() => {
                    button.textContent = "Copied!";
                    setTimeout(() => (button.textContent = "Copy"), 2000);
                });
            });

            // Add button next to the code block
            const container = document.createElement("div");
            container.className = "code-block-container";
            block.parentElement.insertAdjacentElement("beforebegin", container);
            container.appendChild(block.parentElement);
            container.appendChild(button);
        }
    });
}

addCopyButtonsToCodeBlocks();
