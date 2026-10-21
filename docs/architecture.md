# Architecture

The Vite/React frontend owns game state and browser-only camera preview. `src/services/scoring.ts` contains pure scoring helpers. The FastAPI service exposes health, public game configuration, summary validation and a non-persistent summary endpoint. The frontend remains usable when the API is unavailable.

The session is currently held in React state. Export is an explicit user action and creates a local JSON or CSV download. Camera media tracks are stopped on game reset, navigation away from a camera game, and component unmount.

## Planned next steps
1. Extract the game session controller into a typed reducer/state machine.
2. Add automated component tests for each game loop and camera cleanup.
3. Integrate MediaPipe Face Landmarker and Hand Landmarker with pinned model assets and versioned APIs.
4. Add calibrated gaze estimation only after documenting and testing the model, coordinate transform, smoothing, and quality thresholds.
5. Add charts only for recorded trial data and include sample sizes.
