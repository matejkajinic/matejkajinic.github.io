# Matej Kajinic

I'm an engineer, researcher, and venture partner. Former mountain and cave rescuer. My work is driven by a core thesis: the world's two most valuable currencies are FLOPS (Intelligence) and Watts (Energy).

I have an M.S. in Computer Science (neural networks for financial market forecasting) and a B.S. in Electrical Engineering (electromagnetic waves and real-world propagation models).

---

## Research & Writing

* **[ATLAS: Autonomous Task-Learning Agent System](https://matejkajinic.github.io/atlas/)** *(October 2024)*  
  ATLAS autonomously learns, plans, and executes tasks across business operations while maintaining compliance and security. [Source](https://github.com/matejkajinic/ATLAS).

* **[AI Architectures](https://matejkajinic.github.io/ai-architectures/)** *(October 2024)*  
  Comparison of AI architectures: Large Language Models (LLMs), Liquid Neural Networks (LNNs), and Neuromorphic AI. [Source](https://github.com/matejkajinic/AI-architectures).

* **GPU Cloud** *(Internal Paper, October 2024)*  
  Market overview and updated financial models for GPU cloud infrastructure.

* **[Nuclear Energy](https://matejkajinic.github.io/nuclear-energy/)** *(July 2024)*  
  Market overview of nuclear reactor technologies. [Source](https://github.com/matejkajinic/nuclear-energy).

* **[Energy Is All You Need](https://matejkajinic.github.io/energy-is-all-you-need/)** *(June 2024)*  
  Thesis on why we need more nuclear and solar + battery energy to power AI's growth, guiding infrastructure investments. [Source](https://github.com/matejkajinic/energy-is-all-you-need).

* **Economics of GPU** *(Internal Paper, April 2024)*  
  Financial models and analysis of GPU cloud economics and market dynamics.

* **The Economics of Intelligence** *(Internal Paper, March 2024)*  
  Detailed research on chip supply chain, bottlenecks, and predictions for GPU needs in the near and mid-term future.

* **Application of Neural Networks for Forecasting Financial Market Trends** *(Master's Thesis, July 2021)*  
  Built recurrent neural networks (RNN) with long short-term memory (LSTM) for predicting market trends.

* **[Educational Simulation Tools for Radio Wave Propagation Models](https://www.researchgate.net/publication/333340116_Educational_Simulation_Tools_for_Radio_Wave_Propagation_Models)**  
  *International Journal of Education and Information Technologies*, Volume 13, 2019.

* **[Simulation of Radio Wave Propagation Models on 800 MHz and 1.8 GHz in the City of Dubrovnik](https://ieeexplore.ieee.org/document/8910093)**  
  2018 2nd European Conference on Electrical Engineering and Computer Science (EECS), IEEE, 2018.

---

## Technical Projects

* **[ProntoPR](https://matejkajinic.github.io/prontopr/)**  
  A team of specialized autonomous agents that can safely ship incremental features to production using GitHub pull requests, code review, automated tests, and retrieval-augmented generation (RAG).  
  [Source](https://github.com/matejkajinic/prontopr).  
  *Tech: Python*

* **[AI for Historical Document Analysis](https://matejkajinic.github.io/3a-d20/)**  
  Natural language processing (NLP) system with long short-term memory (LSTM) to read and analyze handwritten documents from the Dubrovnik archives dating to the 13th century.  
  [Source](https://github.com/matejkajinic/3A-D20).  
  *Tech: Python, Tesseract OCR, OpenCV, Pandas*

* **[Drone Swarm Simulation](https://matejkajinic.github.io/ros-flocking/)**  
  Simulates group drone flights with ROS.  
  [Source](https://github.com/matejkajinic/ros-flocking).  
  *Tech: C++, ROS, Gazebo, Python*

* **[Predict Breast Cancer](https://matejkajinic.github.io/predict-breast-cancer/)**  
  Demo test for breast cancer prediction.  
  [Source](https://github.com/matejkajinic/predict-breast-cancer).  
  *Tech: Python, TensorFlow, Keras*

---

## Topographic Cartography Publications

Reviewed cartography publications, all available on the [Croatian Mountain Rescue Service website](https://www.hgss.hr/kartografija/):

* **(4) PP Lastovo** (2020) - ISBN 978-953-7527-88-4
* **(11) Korcula** (2019) - ISBN 978-953-7527-73-0
* **(20) Mljet** (2015, 2018) - ISBN 978-953-7527-43-3
* **(25) Dubrovnik** (2016) - ISBN 978-953-7527-50-1
* **(28) Konavle** (2017) - ISBN 978-953-7527-58-7
* **(30) Dubrovacko Primorje** (2018) - ISBN 978-953-7527-60-0
* **(31) Dolina Neretve** (2019) - ISBN 978-953-7527-67-9
* **(38) PP Ucka** (2019) - ISBN 978-953-7527-91-4

---

## Other

* **[The Manifestos](https://matejkajinic.github.io/the-manifestos/)**  
  List inspired by conversation between [David Perell](https://www.perell.com/) and [Marc Andreessen](https://a16z.com/author/marc-andreessen/). Marc concluded: *["It's amazing there aren't more manifestos."](https://youtu.be/tV6kDr1rwTs?si=KQhS31lfrs5vBOgr&t=4093)*
  [Source](https://github.com/matejkajinic/the-manifestos).

---

## Writing Sync

This site now renders selected GitHub repos as on-site reader pages under paths like `https://matejkajinic.github.io/nuclear-energy/`.

- Source config: `writing_sources.yml`
- Sync script: `scripts/sync_writing.py`
- Generated pages: `_writing/*.md`
- Optional automation: `.github/workflows/sync-writing.yml`

### Pages build mode

- Current setup is compatible with the default GitHub Pages Jekyll build because generated `_writing` pages are committed.
- If you ever switch Pages source to **GitHub Actions**, you can move to a fully CI-built deploy flow later.

### When a reader page “doesn’t match” the main site (e.g. The Manifestos)

GitHub also publishes **project** sites from individual repos at `https://<user>.github.io/<repo>/`, with that repo’s own theme. That path is **separate** from your user site build. If Pages is enabled on e.g. [`the-manifestos`](https://github.com/matejkajinic/the-manifestos), visitors to [`matejkajinic.github.io/the-manifestos/`](https://matejkajinic.github.io/the-manifestos/) see **that** deployment—not the styled page generated here from `_writing/the-manifestos.md`.

**To use this site’s layout for that URL:** in the project repo → **Settings → Pages → Build and deployment**, set the source to **None** (disable Pages), then deploy the `matejkajinic.github.io` repo so `_writing/the-manifestos.md` owns `/the-manifestos/`.

**Alternative:** keep the project’s standalone site and give the reader here a different slug in `writing_sources.yml` (e.g. `manifestos`) so it lives at `/manifestos/` without path overlap.

---

## Contact

[Email](mailto:matejkajinic@gmail.com) • [GitHub](https://github.com/matejkajinic/) • [X (Twitter)](https://x.com/matejkajinic/) • [LinkedIn](https://www.linkedin.com/in/matejkajinic/)
