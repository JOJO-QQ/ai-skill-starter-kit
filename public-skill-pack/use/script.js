document.querySelectorAll("[data-copy-target]").forEach((button) => {
  button.addEventListener("click", async () => {
    const targetId = button.getAttribute("data-copy-target");
    const target = document.getElementById(targetId);
    if (!target) return;

    const text = target.innerText;

    try {
      await navigator.clipboard.writeText(text);
      button.textContent = "コピーしました";
      button.classList.add("copied");
      setTimeout(() => {
        button.textContent = "全文コピー";
        button.classList.remove("copied");
      }, 1800);
    } catch (error) {
      const range = document.createRange();
      range.selectNodeContents(target);
      const selection = window.getSelection();
      selection.removeAllRanges();
      selection.addRange(range);
      button.textContent = "選択しました。コピーしてください";
    }
  });
});
