const chart = document.getElementById("chart");
const meta = document.getElementById("meta");

const btnPlay = document.getElementById("btnPlay");
const btnPause = document.getElementById("btnPause");
const btnReplay = document.getElementById("btnReplay");

const initial = DATA.initial;
const frames = DATA.frames;
const fps = Math.max(1, DATA.fps || 12);

let items = [];
let i = 0;

let playing = false;
let lastTick = 0;
let rafId = null;

const maxVal = Math.max(...initial);
const pxHeight = 440;

let slotW = 0;
let barW = 0;
let gap = 6;

function h(val){
  return Math.max(2, Math.round((val / maxVal) * pxHeight));
}

function layoutConstants(){
  const n = initial.length;

  const style = getComputedStyle(chart);
  const paddingL = parseFloat(style.paddingLeft) || 0;
  const paddingR = parseFloat(style.paddingRight) || 0;

  const usableW = chart.clientWidth - paddingL - paddingR;
  let g = 6;

  let bw = Math.floor((usableW - g * (n - 1)) / n);

  while (bw < 1 && g > 0){
    g--;
    bw = Math.floor((usableW - g * (n - 1)) / n);
  }

  bw = Math.max(1, bw);

  gap = g;
  barW = bw;
  slotW = barW + gap;

  chart.style.setProperty("--barW", barW + "px");

  chart.style.setProperty("--showLabels", barW < 10 ? "none" : "block");
}



function x(pos){ return pos * slotW; }

function renderInitial(){
  chart.innerHTML = "";
  layoutConstants();

  items = initial.map((v, id) => {
    const bar = document.createElement("div");
    bar.className = "bar";
    bar.dataset.id = String(id);

    const label = document.createElement("div");
    label.className = "val";
    label.textContent = String(v);

    bar.appendChild(label);

    bar.style.height = h(v) + "px";
    bar.style.transform = `translateX(${x(id)}px)`;

    chart.appendChild(bar);
    return { id, value: v, el: bar, label, pos: id };
  });

  meta.textContent = `0 / ${frames.length}`;
  i = 0;
}

function applyPositions(newPosById){
  const firstLeft = new Map();
  for (const it of items){
    firstLeft.set(it.id, it.el.getBoundingClientRect().left);
  }

  for (const it of items){
    const newPos = newPosById.get(it.id);
    it.pos = newPos;
    it.el.style.transform = `translateX(${x(newPos)}px)`;
  }

  for (const it of items){
    const last = it.el.getBoundingClientRect().left;
    const dx = firstLeft.get(it.id) - last;

    it.el.style.transition = "none";
    it.el.style.transform = `translateX(${x(it.pos) + dx}px)`;
  }

  requestAnimationFrame(() => {
    for (const it of items){
      it.el.style.transition = "transform .18s ease, height .18s ease, filter .22s ease, background-color .22s ease";
      it.el.style.transform = `translateX(${x(it.pos)}px)`;
    }
  });
}

function setFrame(idx){
  const f = frames[idx];

  const hot = new Set(f.hot || []);
  const pivot = f.pivot;
  for (const it of items){
    it.el.classList.toggle("hot", hot.has(it.pos));
    it.el.classList.toggle("pivot", pivot === it.pos);
  }

  const newPosById = new Map();
  for (let pos=0; pos<f.order.length; pos++){
    newPosById.set(f.order[pos], pos);
  }
  applyPositions(newPosById);

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

window.addEventListener("resize", () => {
  renderInitial();
});

renderInitial();
