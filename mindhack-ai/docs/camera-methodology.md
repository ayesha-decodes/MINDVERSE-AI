# Camera methodology and current limitations

Camera access is optional and requested only after a user action. The current build shows a live preview and does not save or transmit frames. Media tracks are stopped when the game is exited or reset.

**Current implementation status:** MediaPipe is not integrated in this initial build. No face landmarks, iris landmarks, gaze estimates, or hand positions are produced. Gaze Quest and Motion Sync remain playable in click/mouse mode, and the UI explicitly identifies that mode. Do not interpret the preview as tracking.

A future gaze implementation should document calibration points, camera mirroring, viewport mapping, quality/confidence thresholds, smoothing, tracking-loss behavior and per-device validation. Head orientation must remain separate from eye-gaze estimation. Do not display a gaze dot when data is missing or below the reliability threshold.

Camera access generally requires HTTPS in production; localhost is usually considered a secure context for development. Camera hardware, lighting, glasses and browser support vary.
