let selected = 25 * 60;
let remaining = selected;
let interval: number | undefined;
const timer = document.querySelector<HTMLDivElement>("#timer")!;
const render = () => timer.textContent = `${String(Math.floor(remaining/60)).padStart(2,"0")}:${String(remaining%60).padStart(2,"0")}`;
document.querySelectorAll<HTMLButtonElement>("[data-min]").forEach(button => button.onclick = () => {
  selected = Number(button.dataset.min) * 60; remaining = selected; render();
});
document.querySelector<HTMLButtonElement>("#start")!.onclick = () => {
  if (interval) return;
  interval = window.setInterval(() => { if (remaining > 0) remaining--; else { clearInterval(interval); interval=undefined; } render(); }, 1000);
};
document.querySelector<HTMLButtonElement>("#reset")!.onclick = () => { clearInterval(interval); interval=undefined; remaining=selected; render(); };
render();
