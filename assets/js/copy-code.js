// Function to add copy buttons to code blocks
function addCopyButtonsToCodeBlocks() {
    const codeBlocks = document.querySelectorAll("pre code");

    codeBlocks.forEach((block) => {
        // Only add button if it doesn't already exist
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

            // Mark this block as processed
            block.classList.add("copy-btn-attached");
            block.parentElement.style.position = "relative";
            block.parentElement.appendChild(button);
        }
    });
}

// Call the function to handle existing code blocks
addCopyButtonsToCodeBlocks();

// Example of handling dynamically added code blocks
// You can call `addCopyButtonsToCodeBlocks` after dynamic content is added
// Example: after an AJAX request or any event that modifies the DOM
