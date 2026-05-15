# TP4 — Homografía

Real-time perspective correction using homography, built with OpenCV and Python.

A live camera feed is displayed in a window. The user selects four corner points
on a planar surface — either manually by clicking or automatically via QR code
detection — and the application computes a homography matrix that maps those
corners to a frontal square view. Two outputs are then rendered continuously:

- **Warp window**: a rectified, top-down view of the selected region.
- **Perspective window**: the live feed with a 3×3 grid overlaid on the detected
  plane, projected back via the inverse homography.

---

## Architecture

The project follows an Onion Architecture with three layers:

```
src/tp4_homografia/
├── domain/                  # Core logic, no framework dependencies
│   ├── homography.py        # Homography value object (wraps the 3×3 matrix)
│   ├── point.py             # 2D point value object
│   └── state_machine/       # Application state machine
│       ├── state_machine.py # Transitions between states
│       ├── state_event.py   # Typed events (discriminated union)
│       └── states/          # One class per state
│           ├── abstract.py
│           ├── visualization.py     # Idle / live preview
│           ├── manual_selection.py  # Collecting 4 clicks
│           ├── qr_selection.py      # Waiting for QR key press
│           └── final.py             # Terminal state
├── services/                # Stateless computation services
│   ├── homography/          # HomographyService (OpenCV implementation)
│   ├── qr/                  # QR detector (OpenCV implementation)
│   └── rendering/
│       ├── warp_renderer.py   # warpPerspective → "Warp" window
│       └── grid_renderer.py   # Inverse-project grid → live frame
├── infrastructure/
│   └── camera.py            # V4L2 camera abstraction (1280×720, MJPG)
├── interaction/
│   └── input_controller.py  # Mouse click queue + keyboard polling
└── application.py           # Wires all collaborators; main loop
```

### State Machine

```
VisualizationState  ──[StartManualSelectionEvent]──►  ManualSelectionState
                    ◄─[CancelSelectionEvent]──────────
                    ◄─[EndSelectionEvent (4 clicks)]──

VisualizationState  ──[StartQrPreDetectionEvent]──►  QrPreDetectionState
                    ◄─[CancelSelectionEvent / EndSelectionEvent]──

Any state          ──[StopEvent]──►  FinalState  (loop exits)
```

`ManualSelectionState` accumulates left-clicks; after the fourth click it emits
`EndSelectionEvent`. `QrPreDetectionState` triggers a QR scan on any key press;
the detector either returns `EndSelectionEvent` (with padded corners) or
`CancelSelectionEvent` on failure.

---

## Dependencies

| Package | Role |
|---|---|
| `opencv-python` | Camera capture, homography, QR detection, rendering |
| `numpy` | Matrix operations |

Python ≥ 3.11.9 required.

---

## Installation

```bash
uv sync
```

---

## Running

```bash
tp4-homografia
```

Or directly:

```bash
python -m tp4_homografia.main
```

Requires a V4L2-compatible camera on `/dev/video0`.

---

## Controls

| Input | State | Action |
|---|---|---|
| Any key | `VisualizationState` | Enter manual selection mode |
| Left click ×4 | `ManualSelectionState` | Select corners; compute homography |
| Any key | `ManualSelectionState` | Cancel selection |
| Any key | `QrPreDetectionState` | Trigger QR auto-detection |
| `q` / `Esc` | Any | Quit *(standard OpenCV window close)* |

> QR detection uses `cv2.QRCodeDetector` and expands the detected quad by a
> factor of 1.15 to provide padding around the code boundary.

---

## Output

Once a homography is computed:

- **Warp** window shows a 1000×1000 px rectified view of the frozen source frame.
- **Perspective** window shows the live feed with a green 3×3 grid projected onto
  the detected plane.
