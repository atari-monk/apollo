function addCopyButtonsToCodeBlocks() {
    const codeBlocks = document.querySelectorAll("pre code");

    codeBlocks.forEach((block) => {
        if (!block.parentElement.querySelector(".copy-btn")) {
            const button = document.createElement("button");
            button.className = "copy-btn";
            button.textContent = "📋";
            button.addEventListener("click", () => {
                navigator.clipboard.writeText(block.textContent).then(() => {
                    button.textContent = "✔️";
                    setTimeout(() => (button.textContent = "📋"), 2000);
                });
            });

            const container = document.createElement("div");
            container.className = "code-block-container";
            block.parentElement.insertAdjacentElement("beforebegin", container);
            container.appendChild(block.parentElement);
            container.appendChild(button);
        }
    });
}

addCopyButtonsToCodeBlocks();
