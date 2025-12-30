const chart = document.getElementById("chart");
const meta = document.getElementById("meta");

const btnPlay = document.getElementById("btnPlay");
const btnPause = document.getElementById("btnPause");
const btnReplay = document.getElementById("btnReplay");

const initial = DATA.initial;
const frames = DATA.frames;
const highlights = DATA.highlights;
const fps = Math.max(1, DATA.fps || 12);

let bars = [];
let values = [];
let i = 0;

let playing = false;
let lastTick = 0;
let rafId = null;

const maxVal = Math.max(...initial, ...frames.flat());
const pxHeight = 440;

function h(val){
  return Math.max(2, Math.round((val / maxVal) * pxHeight));
}

function renderInitial(){
  chart.innerHTML = "";
  bars = [];
  values = [];
  console.log("Dupa")
  const arr = initial;
  for (let k=0; k<arr.length; k++){
    const bar = document.createElement("div");
    bar.className = "bar";

    const label = document.createElement("div");
    label.className = "val";
    label.textContent = String(arr[k]);

    bar.appendChild(label);
    bar.style.height = h(arr[k]) + "px";

    chart.appendChild(bar);
    bars.push(bar);
    values.push(label);
  }

  meta.textContent = `0 / ${frames.length}`;
  i = 0;
}

function setFrame(idx){
  const arr = frames[idx];
  const hot = new Set(highlights[idx] || []);

  for (let k=0; k<arr.length; k++){
    bars[k].style.height = h(arr[k]) + "px";
    values[k].textContent = String(arr[k]);
  }

  for (let k=0; k<bars.length; k++){
    if (hot.has(k)) bars[k].classList.add("hot");
    else bars[k].classList.remove("hot");
  }

  meta.textContent = `${idx+1} / ${frames.length}`;
}

function tick(ts){
  if (!playing) return;

  const interval = 1000 / fps;
  if (ts - lastTick >= interval){
    lastTick = ts;

    if (i >= frames.length){
      playing = false;
      return;
    }
    setFrame(i);
    i++;
  }
  rafId = requestAnimationFrame(tick);
}

btnPlay.addEventListener("click", () => {
  if (playing) return;
  playing = true;
  lastTick = performance.now();
  rafId = requestAnimationFrame(tick);
});

btnPause.addEventListener("click", () => {
  playing = false;
  if (rafId) cancelAnimationFrame(rafId);
  rafId = null;
});

btnReplay.addEventListener("click", () => {
  playing = false;
  if (rafId) cancelAnimationFrame(rafId);
  rafId = null;

  renderInitial();
});

renderInitial();
